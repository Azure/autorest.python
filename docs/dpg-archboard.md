# Python DPG Client

--------------------------------- Isabella ---------------------------------
## Intro

### Goals of DPG Clients

1. Be version tolerant: if it's not breaking in the service, end users should not be broken
2. Be more pythonic: use more keyword only arguments, which also helps with breaking
3. Clean grow up story, so service teams can grow up initial releases

### Main changes from current generation

1. Now only path and body parameters are positional, all other parameters are keyword only
2. We've gotten rid of models for now and are just using raw JSON objects. When we add our DPG models, this won't be breaking, because our models will
be able to accessed as dicts and as models as well
3. We've added glass breaker `send_request` to all of our clients. Clients can now send an `HttpRequest` directly to the server leveraging our client pipelines.
4. We've also added easy-to-use customizations, and are going to be pushing these customizations for SDK authors.


--------------------------------------------------------------------------
--------------------------------- Yuchao ---------------------------------

## Developer Experience

### Creating a client

Creating a client is largely the same as it was before. We have made the client arguments align with the Python guidelines,
generating an `endpoint` and `credential` parameter.

```python
from azure.purview.catalog import PurviewCatalogClient
from azure.identity import DefaultAzureCredential

client = PurviewCatalogClient(endpoint="http://myendpoint.com", credential=DefaultAzureCredential())
```

### Simple GET request

GET requests are largely the same as before. Since a lot of Azure services are JSON based and return JSON payloads, here is a main
place where we will see differences between GET requests with current generated code, because we no longer return models in this case.
We return raw JSON, so in most cases this means users access them like a dict. Python users have been very receptive to just accessing these
models as JSON, since Python users are already very comfortable with JSON. In fact, we've been getting issues over the years asking for our models
to really be dicts, so this change has actually been quite welcomed.

We still see the importance of adding DPG models, in large part because of the documentation benefits they give us, they serve
as a landing place for documentation. But when we add them, they will be non-breaking because you can still access them as a dict.

```python
response = client.get_object()
assert response["hello"] == "world"
```

### Creating a POST request

POST requests are another area where we're going to see JSON bodies pop up.

We've also additionally added overloads for post methods where the input is a JSON type, for example a model. These overloads will be helpful to people
who don't want to read large models into memory just to pass them as a JSON input. Instead, they are now able to stream serialized JSON straight to the
service.

```python

client.put_object({"hello": "world"})

with open("myLargeJsonFile", "rb") as fd:
    client.put_object(fd)
```

### Break the glass scenario

Our DPG clients all come with a `send_request` function on a client. Here, you can create your own request
and use our client to send it to the service. This way you get all of the existing pipeline setup for free,
and can send your request

```python
from azure.core.rest import HttpRequest
from azure.purview.catalog import PurviewCatalogClient
from azure.identity import DefaultAzureCredential

client = PurviewCatalogClient(endpoint="endpoint", credential=DefaultAzureCredential())

request = HttpRequest("GET", "http://new-endpoint.com")
response = client.send_request(request)
response.raise_for_status()
json_response = response.json()
```

--------------------------------------------------------------------------
--------------------------------- Changlong ---------------------------------

### Streams
Streams can be used to transfer large ammounts of data without using too big memory.
#### Inputs

As mentioned above, we've opened up streamed inputs to include more cases, so users with large input bodies aren't forced
to read their bodies into memory before passing them to the service. Otherwise, streamed inputs are largely the same
as they are in our current generation

```python
# in RP WebPubSub
with open("temp/blob.txt", "rb") as fd:
    client.send_to_all(fd)
```

One thing for Stream special is we don't support retry for stream sendings since the IO handler is in one way reading mode.
- Ask about what other languages are doing for retry streams
> Synced with Java that it don't have retry on streams too.

#### Outputs

With streamed outputs, users used to iterate over `.stream_download()` on the response object. We've changed this method to
`iter_bytes()`. This is the syntax that [`httpx`](https://www.python-httpx.org/) uses, which is the HTTP stack that Python is migrating to.
More aligned with `httpx`.


Generation changes:
```python
# Legacy
class FileOperations:
    def get_file(self, **kwargs):
        ...
        response = pipeline_response.http_response
        ...
        deserialized = response.stream_download(self._client._pipeline)
        return deserialized

# DPG:
class FileOperations:
    def get_file(self, **kwargs: Any) -> IO:
        ...
        response = pipeline_response.http_response
        ...
        deserialized = response
        return deserialized
```

Usage in DPG:
```python
# in testserver bodyfile

with io.BytesIO() as file_handle:
    stream = client.files.get_file()
    assert not stream._internal_response._content_consumed

    for data in stream.iter_bytes():
        assert 0 < len(data) <= stream.block_size
        file_handle.write(data)
```

### Multiple Media Types

We support multiple media types in both legacy and version-tolerant codegen. In version tolerant codegen, the main improvement is that the end user no need to provide content_type for the majority of cases.
Generation changes:
```python
# Legacy, content_type is delivered in kwargs, and no default value.
    @overload
    def analyze_body(self, input=None, **kwargs):
       pass

    @overload
    def analyze_body(self, input=None, **kwargs):
        pass

    def analyze_body(self, input=None, **kwargs):
       ...

# DPG, there is default value for content type
    @overload
    def analyze_body(
        self, input: Optional[JSON] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> str:
        pass

    @overload
    def analyze_body(self, input: Optional[IO] = None, *, content_type: Optional[str] = "application/octet-stream", **kwargs: Any) -> str:
        pass

    def analyze_body(self, input: Optional[Union[JSON, IO]] = None, **kwargs: Any) -> str:
        ...
```

Usage in DPG:
```
client.analyze_body({"hello": "world"})

with open('C:\\ZZ\\foo.txt', 'rb') as fd:
    client.analyze_body(fd)
```

### argues on breaking 
One cons of the above designing is that it will bring us breaking change in an edge case.

Say a service team starts out by just accepting a JSON input to an endpoint. Then our initial generation of this SDK
will also allow users to pass a streamed body with default content type "application/json". If the service team
then adds a streamed body that they accept and add content type `"application/octet-stream"`, then the default content type
for streamed input bodies will change from `"application/json"` to `"application/octet-stream"`.

The reasons why we're ok with breaking in this scenario are because

1. This is very much an edge case
2. Our tooling can catch this breaking change, so we can either do a quick customization to make it unbreaking, or use `x-ms-paths`
to add a new operation

Overall we weighed the pros and cons here, and we feel that the benefit of helping users stream large inputs is bigger than the con
of a technically breaking change we can easily catch and make non-breaking before getting to end users.


# DPG code: https://github.com/Azure/autorest.python/blob/archboard_docs/test/vanilla/version-tolerant/Expected/AcceptanceTests/MediaTypesVersionTolerant/mediatypesversiontolerant/_operations/_operations.py#L180
# Legacy code: https://github.com/Azure/autorest.python/blob/archboard_docs/test/vanilla/legacy/Expected/AcceptanceTests/MediaTypes/mediatypes/operations/_media_types_client_operations.py#L229

### LROs

LROs are like what we have right now, with the exception of us dealing with raw JSON instead of models

```python
poller = client.begin_lro()
response = poller.result()
assert response["hello"] == "world!"        # Be response.hello in legacy
```

### Paging

Paging is also the same as right now, with the exception of raw JSON instead of models

```python
pages = client.list_pages()
for page in pages:
    print(page["id"])                       # Be page.id in legacy
```

--------------------------------------------------------------------------
--------------------------------- Isabella ---------------------------------

## Customization

### What are customizations like right now?

https://github.com/Azure/autorest.python/blob/autorestv3/docs/customizations.md

### Metrics Advisor Customizations

How did we tackle the two clients?

--------------------------------------------------------------------------
