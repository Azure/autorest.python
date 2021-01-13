# Sample Directives Generation

### Settings

``` yaml
input-file: https://raw.githubusercontent.com/Azure/autorest/master/docs/openapi/examples/pollingPaging.json
namespace: azure.directives.sample
package-name: azure-directives-sample
license-header: MICROSOFT_MIT_NO_VERSION
package-version: 0.1.0
basic-setup-py: true
clear-output-folder: true
```

### Override LROPoller to custom Poller

```yaml
directive:
    from: swagger-document
    where: '$.paths["/basic/polling"].put'
    transform: >
        $["x-python-custom-poller-sync"] = "my.library.CustomPoller";
        $["x-python-custom-poller-async"] = "my.library.aio.AsyncCustomPoller"
```

### Override Default Polling Method to Custom Polling Method

```yaml
directive:
    from: swagger-document
    where: '$.paths["/basic/polling"].put'
    transform: >
        $["x-python-custom-default-polling-method-sync"] = "my.library.CustomDefaultPollingMethod";
        $["x-python-custom-default-polling-method-async"] = "my.library.aio.AsyncCustomDefaultPollingMethod"
```


### Override ItemPaged to Custom Pager

```yaml
directive:
    from: swagger-document
    where: '$.paths["/basic/paging"].get'
    transform: >
        $["x-python-custom-pager-sync"] = "my.library.CustomPager";
        $["x-python-custom-pager-async"] = "my.library.aio.AsyncCustomPager"
```

### Override Default Paging Method to Custom Paging Method

```yaml
directive:
    from: swagger-document
    where: '$.paths["/basic/paging"].get'
    transform: >
        $["x-python-custom-default-paging-method"] = "my.library.CustomDefaultPagingMethod";
```
