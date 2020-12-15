# Python-Specific Directives

### Settings

``` yaml
input-file: pollingPaging.json
namespace: python.directives
package-name: python-directives
output-folder: $(python-sdks-folder)/directives/python-directives
license-header: MICROSOFT_MIT_NO_VERSION
package-version: 0.1.0
basic-setup-py: true
output-artifact: code-model-v4-no-tags
clear-output-folder: true
```

### Override LROPoller to custom Poller

```yaml
directive:
    from: swagger-document
    where: '$.paths["/directives/polling"].put'
    transform: >
        $["x-python-custom-poller-sync"] = "my.library.CustomPoller";
        $["x-python-custom-poller-async"] = "my.library.aio.AsyncCustomPoller"
```

### Override Default Polling Method to Custom Polling Method

```yaml
directive:
    from: swagger-document
    where: '$.paths["/directives/polling"].put'
    transform: >
        $["x-python-custom-default-polling-method-sync"] = "my.library.CustomDefaultPollingMethod";
        $["x-python-custom-default-polling-method-async"] = "my.library.aio.AsyncCustomDefaultPollingMethod"
```


### Override ItemPaged to Custom Pager

```yaml
directive:
    from: swagger-document
    where: '$.paths["/directives/paging"].get'
    transform: >
        $["x-python-custom-pager-sync"] = "my.library.CustomPager";
        $["x-python-custom-pager-async"] = "my.library.aio.AsyncCustomPager"
```

### Override Default Paging Method to Custom Paging Method

```yaml
directive:
    from: swagger-document
    where: '$.paths["/directives/paging"].get'
    transform: >
        $["x-python-custom-default-paging-method"] = "my.library.CustomDefaultPagingMethod";
```
