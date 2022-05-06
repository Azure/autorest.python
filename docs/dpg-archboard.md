# Python DPG Client

## Intro

## Breaking Changes

* If the service doesn't break, the client shouldn't break.
* The main steps we've taken to mitigate this is using
    * For now, we're generating without models, and are going to be dealing with raw JSON. The feedback is actually positive for Python, Python users are very
    comfortable dealing with raw JSON, and in many cases prefer it. We are looking into our DPG models, which will be non-breaking, and provide additional
    documentation sticking points for people to look at
    * Make header and query parameters keyword only.

## Developer Experience

### Creating a client

```python
from azure.purview.catalog import PurviewCatalogClient
from azure.identity import DefaultAzureCredential

client = PurviewCatalogClient(endpoint="http://myendpoint.com", credential=DefaultAzureCredential())
```

### Simple GET request

```python
response = client.my_get_call()
```

### Creating a POST request

For model / dictionary / list input JSON types, we've added an overload for users to use. We don't want to force users to read in large models into memory
if the model is big, so we give users the option to pass in a file descriptor of serialized json as well.

```python

client.put_object({"hello": "world"})

with open("myLargeJsonFile", "rb") as fd:
    client.put_object(fd)
```

### Working with the response

#### JSON responses

We return JSON responses back to users

```python
response = client.get_object()
assert response["hello"] == "world!"
```

#### Stream responses

```python
response = client.get_streamed_response()
for data in response.iter_bytes():
    print(data)
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

request = HttpRequest("GET", "htt[://new-endpoint.com")
response = client.send_request(request)
response.raise_for_status()
json_response = response.json()
```

### Multiple Media types

```python
client.put_object({"hello": "world"})

with open("myLargeJsonFile", "rb") as fd:
    client.put_object(fd)
```

### LROs

```python
poller = client.begin_lro()
response = poller.result()
assert response["hello"] == "world!"
```

### Paging

```python
pages = client.list_pages()
for page in pages:
    print(page["id"])
```
## Customization

https://github.com/Azure/autorest.python/blob/autorestv3/docs/customizations.md
