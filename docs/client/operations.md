# <img align="center" src="../images/logo.png">  Calling Operations with Your Python Client

AutoRest provides both synchronous and asynchronous method overloads for each service operation.
Depending on your swagger definition, operations can be accessed through operation groups (TODO: link to swagger docs) on the client,
or directly on the client.

## Operation Group vs No Operation Group

If your swagger defines an operation group for your operation (for example, in [this][operation_group_example] swagger, the operation `list`
is part of operation group `application`), you would access the operation through `client.application.list()`.

If there's no operation group, as in [this][mixin_example] case, you would access the operation directly from the client
itself, i.e. `client.get_dog()`.

## Regular Operations

### Sync Operations

We will be using the [example swagger][pets_swagger] in our main docs repo. After [initializing][initializing] our client, we
call our operation like this:

```python
from azure.identity import DefaultAzureCredential
from azure.pets import PetsClient

client = PetsClient(credential=DefaultAzureCredential())
dog = client.get_dog()
```

### Async Operations

When calling our async operations, we use our async client, which is in a different module. Following the [example above](#sync-operations "Sync Operations"),
our call to `get_dog` looks like this:

```python
import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.pets.aio import PetsClient

async def get_my_dog():
    async with DefaultAzureCredential() as credential:
        async with PetsClient(credential=credential) as client:
            dog = await client.get_dog()

loop = asyncio.get_event_loop()
loop.run_until_complete(get_my_dog())
loop.close()
```

## Long Running Operations

Long-running operations are operations which consist of an initial request sent to the service to start an operation, followed by polling the service at intervals to determine whether the operation has completed or failed, and if it has succeeded, to get the result.

In concurrence with our [python guidelines][poller_guidelines], all of our long running operations are prefixed with `begin_`, to signify the starting of the long running operation.

For our example, we will use the long running operation generated from [this][example_swagger] swagger. Let's say we generated this swagger with namespace `azure.lro`.

### Sync Long Running Operations

By default, our sync long running operations return an [`LROPoller`][lro_poller] polling object, though there [are ways][custom_poller] of changing this. Calling `.wait()` on this poller
waits for the operation to finish, while calling `.result()` both waits on the operation and returns the final response.

```python
from azure.identity import DefaultAzureCredential
from azure.lro import PollingPagingExampleClient
from azure.lro.models import Product

client = PollingPagingExampleClient(credential=DefaultAzureCredential())
input_product = Product(id=1, name="My Polling Example")
poller = client.begin_basic_polling(product=input_product)
output_product = poller.result()
```

### Async Long Running Operations

By default, our async long running operations return an [`AsyncLROPoller`][async_lro_poller] polling object, though there [are ways][custom_poller] of changing this. Same as the sync version,
calling `.wait()` on this poller waits for the operation to finish, while calling `.result()` both waits on the operation and returns the final response.

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.lro.aio import PollingPagingExampleClient
from azure.lro.models import Product

async def basic_polling():
    async with PollingPagingExampleClient(credential=DefaultAzureCredential()) as client:
        input_product = Product(id=1, name="My Polling Example")
        poller = await client.begin_basic_polling(product=input_product)
        output_product = await poller.result()

loop = asyncio.get_event_loop()
loop.run_until_complete(basic_polling())
loop.close()
```

## Paging Operations

A paging operation pages through lists of data, returning an iterator for the items. Network calls get made when users start iterating through the output, not when the operation
is initially called.

For our example, we will use the long running operation generated from [this][example_swagger] swagger. Let's say we generated this swagger with namespace `azure.paging`.

### Sync Paging Operations

By default, our sync paging operations return an [`ItemPaged`][item_paged] pager, though there [are ways][custom_pager] of changing this. The initial call to the function returns
the pager, but doesn't make any network calls. Instead, calls are made when users start iterating, with each network call returning a page of data.

```python
from azure.identity import DefaultAzureCredential
from azure.paging import PollingPagingExampleClient

client = PollingPagingExampleClient(credential=DefaultAzureCredential())
pages = client.basic_paging()
[print(page) for page in pages]
```

### Async Paging Operations

By default, our async paging operations return an [`AsyncItemPaged`][async_item_paged] pager, though there [are ways][custom_pager] of changing this. Since network calls aren't
made until starting to page, our generated operation is synchronous, and there's no need to wait the initial call to the function. Since network calls are made when iterating,
we have to do async looping.

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.paging.aio import PollingPagingExampleClient

async def basic_paging():
    async with PollingPagingExampleClient(credential=DefaultAzureCredential()) as client:
        pages = client.basic_paging()  #  note how there's no awaiting here
        async for page in pages:  # since network calls are only made during iteration, we await the network calls when iterating
            print(page)

loop = asyncio.get_event_loop()
loop.run_until_complete(basic_paging())
loop.close()
```


## Advanced: LRO + paging

We also support generating a long running paging operation. In this case, we return a poller from the operation, and the final result from the poller is
a pager that pages through the final lists of data.


<!-- LINKS -->
[operation_group_example]: https://github.com/Azure/azure-rest-api-specs/blob/master/specification/batch/data-plane/Microsoft.Batch/stable/2020-09-01.12.0/BatchService.json#L64
[mixin_example]: https://github.com/Azure/autorest/blob/master/docs/openapi/examples/pets.json#L20
[pets_swagger]: https://github.com/Azure/autorest/blob/master/docs/openapi/examples/pets.json
[initializing]: https://github.com/Azure/autorest.python/blob/main/docs/client/initializing.md
[lro_poller]:  https://docs.microsoft.com/python/api/azure-core/azure.core.polling.lropoller?view=azure-python
[custom_poller]: https://github.com/Azure/autorest.python/blob/main/docs/generate/directives.md#generate-with-a-custom-poller
[example_swagger]: https://github.com/Azure/autorest/blob/master/docs/openapi/examples/pollingPaging.json
[poller_guidelines]: https://azure.github.io/azure-sdk/python_design.html#service-operations
[async_lro_poller]: https://docs.microsoft.com/python/api/azure-core/azure.core.polling.asynclropoller?view=azure-python
[item_paged]: https://docs.microsoft.com/python/api/azure-core/azure.core.paging.itempaged?view=azure-python
[custom_pager]: https://github.com/Azure/autorest.python/blob/main/docs/generate/directives.md#generate-with-a-custom-pager
[async_item_paged]: https://docs.microsoft.com/python/api/azure-core/azure.core.async_paging.asyncitempaged?view=azure-python
