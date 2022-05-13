# Python DPG Client

--------------------------------- Isabella ---------------------------------

## Intro

### Goals of DPG Clients

1. Be version tolerant: if it's not breaking in the service, end users are not broken
2. Be more Pythonic: use more keyword only arguments, which solves our breaking issue
3. Clean grow up story with easy to use customizations

### Main changes from current generation

1. Now only path and body parameters are positional, all other parameters are keyword only. Path parameters are always required, path are ordered by their position in the template. Body is always the last positional parameter. Query and header params are always keyword-only, even if they are required. Keyword only is just like an options bag.
2. We've gotten rid of models for now and are just using raw JSON objects. Python people are happy with this, and have been asking for this for a long time. So we are able to better fulfill end user goals while being more version tolerant. We may provide compatible models later based on customer feedback, and we may never do it if we don't have user asks.
be able to accessed as dicts and as models as well
3. We've added glass breaker `send_request` to all of our clients. Clients can now send an `HttpRequest` directly to the server leveraging our client pipelines.
4. We've also added easy-to-use for SDK writers customizations, and this the foundation of our grow up story. We are no longer wrapping all of generated code, customizing in place.

### Things Staying the Same

1. Client and Operation group structure stays the same. Client looks exactly regular, has endpoint, has credential.

The rest of the archboard is split into two large chunks. In the first half, Yuchao and Changlong are going to take us through the differences between legacy generated code and DPG generated code, and in the second half I'm going to go over the customization story with Metrics Advisor as my service.


--------------------------------------------------------------------------
--------------------------------- Yuchao ---------------------------------

## Developer Experience

### Creating a client

The end-users experience of creating a client is the same as it was before. We are not compromising on any user input here, this behavior is consistent with Python guidelines and existing user behavior.

```python
from azure.purview.catalog import PurviewCatalogClient
from azure.identity import DefaultAzureCredential

client = PurviewCatalogClient(endpoint="http://myendpoint.com", credential=DefaultAzureCredential())
```

### Simple GET request

The overall flow of all operation calls are largely the same as before. Users must still initialize their client, then either call operations directly on the client, or on operation group attributes.

There are two main things I want to talk about with these basic REST calls.

1. You can see here that we've moved all query and header parameters to keyword-only. This really solves all of our potential versioning issues with parameter ordering. Since path parameters are always required, we are comfortable including them as positional arguments, and we are positioning them based off of their location in the url. The body parameter will always be the last positional argument. Finally, all query and header parameters are keyword-only, they're kind of in Python's options bag. Here ordering doesn't matter.
2. GET requests will also be the main place where we see the differences with us going from models to just returning raw JSON. We want to be very clear here: Python believes its DPG story is complete without models and just returning raw JSON. Python users are very comfortable with JSON bodies, and in fact we have gotten numerous issues over the years from customers just asking for raw JSON. Additionally, we have also invested a lot of effort in making sure the structure of the model inputs and outputs are documented for users.


### Creating a POST request

POST requests are another area where we're going to see JSON bodies pop up.

We have invested a lot of effort into good docs even though we are removing models. We have input templates for JSON inputs, like the one here: https://azuresdkdocs.blob.core.windows.net/$web/python/azure-purview-catalog/1.0.0b3/azure.purview.catalog.operations.html#azure.purview.catalog.operations.DiscoveryOperations.browse

Now, it's even easier for users to input their bodies, because they can directly copy the template, fill in the information,
and pass that to the service. This also removes a lot of the imports and lines they'd have to dedicate to importing and initializing these models before passing them to the server.

We've also additionally added overloads for post methods where the input is a JSON type. These overloads will be helpful to people who don't want to read large models into memory just to pass them as a JSON input. Instead, they are now able to stream serialized JSON straight to the service. None of our SDKs do this yet, and it's not in the Python guidelines, but this is an issue that Johan has been wanting to solve for a long time, and now we have a well-typed solution for users.

I also want to be clear that these overloads DO NOT mean C# overloads, these don't add time or space complexity. These are for intellisense purposes only.

### Break the glass scenario

Our DPG clients all come with a `send_request` function on a client. Here, you can create your own request and use our client to send that request to the service through our client pipeline. This way you can use the existing client pipeline set up to send requests that we maybe haven't added to our SDK yet. These requests can be done to relative or full URLs.

In the first example, we are making a request with a relative URL. This url will be formatted relative to the endpoint we initialized the client with.

In the second example, we are making a request to a whole new URL. Both of these scenarios are possible.

One file note is the `raise_for_status()`. This method on the response is common across all Python stack libraries, and it raises an `HttpResponseError` if the status code is 400 and up.

--------------------------------------------------------------------------
--------------------------------- Changlong ---------------------------------

### Streams

#### Inputs

The way users stream inputs to services stays the same. The only change here is we've opened up streamed inputs to include more cases. This is the scenario that Yuchao talked about, so users with large input bodies aren't forced to read their bodies into memory before passing them to the service. Otherwise, streamed inputs are the same as our current generation.

#### Outputs

With streamed outputs, we have changed end user behavior. Users used to iterate over `.stream_download()` on the response object. We've changed this method to `.iter_bytes()`. This is the syntax that `httpx` uses, which is the HTTP stack that Python is migrating to. So basically we are making our behavior here consistent with the main Python HTTP stack packages.

### Multiple Content and Body Types

We have improved the way we deal with multiple content and body types. We now do some body type sniffing on input bodies, and based off of the inputted body type, we default to a content type.

Here, the service accepts either a stream body or a JSON body. They've listed their content types as `"application/octet-stream"` and `"application/json"`. If Python sees `"application/octet-stream"`, we default IO bodies to this behavior. For other possible IO content types, like `"application/pdf"`, we make users be clear and input their content type, `"application/octet-stream"` is the only value we default to if listed in the swagger, because a lot of transports end up defaulting to this content type for streamed inputs. For JSON inputs, we default to `"application/json"` if it is included in the swagger.

This also is probably one of the more controversial parts of our design, and that's because as a huge edge case, we have a potential for breaking changes in immediate generation, and here's the edge case we're talking about:

Say a service team starts out by just accepting a JSON input to an endpoint. Then our initial generation of this SDK with our DPG code generator will add an overload so users can pass in streamed body with default content type `"application/json"`. Then, if the service team says "now I accept a streamed body and content type `"application/octet-stream"`", the default content type or streamed input bodies will change from `"application/json"` to `"application/octet-stream"`.

The reasons why we're ok with breaking in this scenario are because

1. This is very much an edge case
2. Our tooling can catch this breaking change, so we can either do a quick customization to make it unbreaking, or use `x-ms-paths`
to add a new operation. Basically we can easily fix this manually if we don't want to break customers

Overall we weighed the pros and cons here, and we feel that the benefit of helping users stream large inputs is bigger than the con
of a technically breaking change we can easily catch and make non-breaking before getting to end users.

### LROs

LROs are like what we have right now, with the exception of us dealing with raw JSON instead of models.

Here is another input template we have for users: https://azuresdkdocs.blob.core.windows.net/$web/python/azure-iot-deviceupdate/1.0.0b2/azure.iot.deviceupdate.operations.html#azure.iot.deviceupdate.operations.DeviceUpdateOperations.begin_import_update

We also accept overloads here for streamed inputs in all cases with JSON model inputs as well.


### Paging

Paging is also the same as right now, with the exception of raw JSON instead of models

```python
pages = client.list_pages()
for page in pages:
    print(page["id"])
```

--------------------------------------------------------------------------
--------------------------------- Isabella ---------------------------------

## Customization

### What are customizations like right now?

https://github.com/Azure/autorest.python/blob/autorestv3/docs/customizations.md

### Metrics Advisor Customizations

How did we tackle the two clients?

--------------------------------------------------------------------------
