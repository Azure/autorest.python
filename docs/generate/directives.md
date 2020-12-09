# <img align="center" src="../images/logo.png">  Python-Specific Directives

If you want to see how to generally use a directive to change AutoRest behavior, check out the [main docs](https://github.com/Azure/autorest/tree/master/docs/generate/directives.md). This section will go into the Python-specific directives.


* [Generate with a custom poller](#generate-with-a-custom-poller "Generate with a custom poller")
* [Generate with a custom polling method](#generate-with-a-custom-polling-method "Generate with a custom polling method")
* [Generate with a custom pager](#generate-with-a-custom-pager "Generate with a custom pager")
* [Generate with a custom paging method](#generate-with-a-custom-paging-method "Generate with a custom paging method")

## Generate with a custom poller

By default, a long running operation will generate with poller [`LROPoller`][lro_poller_docs] from [azure-core][azure_core_pypi]'s polling library (the async version being [`AsyncLROPoller`][async_lro_poller_docs]). With this directive, you can change the generated code to generate with your custom poller. For this example, we will be using our example [directives.json][directives_swagger] swagger. We start off with the general skeleton of a directive.

>Note: There are a couple of requirements your custom poller must fulfil.
>1. It must take in a `Generic` of the final response object type, i.e. its definition should look like `class CustomPoller(Generic[PollingReturnType]):`
>2. The initialization parameters must be the same as [`LROPoller`][lro_poller_docs]'s
>3. If you want continuation token support on your poller, you need to implement class method `from_continuation_token` with the same method signature as [`LROPoller`][lro_poller_docs]'s

````
```yaml
directive:
    from: swagger-document
    where: ...
    transform: ...
```
````

To do so, you need to first tell the directive which operation you would like to change the poller for. You refer to operation using it's path in the swagger, and the HTTP verb it's listed under.
This gives us `where: '$.paths["/directives/polling"].post'`.

We use `$["x-python-custom-poller-sync"]` and `$["x-python-custom-poller-async"]` to specify our sync and async custom pollers. You have to use the full import path of the custom poller you're specifying, i.e. `my.library.CustomPoller`. Putting this altogether, we get the following directive, which we will insert in our config file.

```yaml
directive:
    from: swagger-document
    where: '$.paths["/directives/polling"].put'
    transform: >
        $["x-python-custom-poller-sync"] = "my.library.CustomPoller";
        $["x-python-custom-poller-async"] = "my.library.aio.AsyncCustomPoller"
```

To illustrate the generated code difference, here are before and afters of the typing and docstrings. Not including the full code for the sake of room.

Without directive:
# <img align="center" src="../images/before_polling_directive.png">

With directive:
# <img align="center" src="../images/after_polling_directive.png">


## Generate with a custom polling method

pass


## Generate with a custom pager

By default, a paging operation will generate with pager [`ItemPaged`][item_paged_docs] from [azure-core][azure_core_pypi]'s polling library (the async version being [`AsyncItemPaged`][async_item_paged_docs]). With this directive, you can change the generated code to generate with your custom pager. For this example, we will be using our example [directives.json][directives_swagger] swagger. We start off with the general skeleton of a directive.

>Note: Your custom pager must have the same initialization parameters as [`ItemPaged`][item_paged_docs]

````
```yaml
directive:
    from: swagger-document
    where: ...
    transform: ...
```
````

To do so, you need to first tell the directive which operation you would like to change the pager for. You refer to operation using it's path in the swagger, and the HTTP verb it's listed under.
This gives us `where: '$.paths["/directives/paging"].get'`.

We use `$["x-python-custom-pager-sync"]` and `$["x-python-custom-pager-async"]` to specify our sync and async custom pagers. You have to use the full import path of the custom pager you're specifying, i.e. `my.library.CustomPager`. Putting this altogether, we get the following directive, which we will insert in our config file.

```yaml
directive:
    from: swagger-document
    where: '$.paths["/directives/paging"].get'
    transform: >
        $["x-python-custom-pager-sync"] = "my.library.CustomPager";
        $["x-python-custom-pager-async"] = "my.library.aio.AsyncCustomPager"
```

To illustrate the generated code difference, here are before and afters of the typing and docstrings. Not including the full code for the sake of room.

Without directive:
# <img align="center" src="../images/before_paging_directive.png">

With directive:
# <img align="center" src="../images/after_paging_directive.png">

<!-- LINKS -->

[lro_poller_docs]: https://azuresdkdocs.blob.core.windows.net/$web/python/azure-core/latest/azure.core.polling.html#azure.core.polling.LROPoller
[azure_core_pypi]: https://pypi.org/project/azure-core/
[async_lro_poller_docs]: https://azuresdkdocs.blob.core.windows.net/$web/python/azure-core/latest/azure.core.polling.html#azure.core.polling.AsyncLROPoller
[directives_swagger]: ./examples/directives.json

[item_paged_docs]: https://azuresdkdocs.blob.core.windows.net/$web/python/azure-core/latest/azure.core.html#azure.core.paging.ItemPaged
[async_item_paged_docs]: https://azuresdkdocs.blob.core.windows.net/$web/python/azure-core/latest/azure.core.html#azure.core.async_paging.AsyncItemPaged

## Generate with a custom paging method

pass
