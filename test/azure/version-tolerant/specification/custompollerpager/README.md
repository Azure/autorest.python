# Testing adding a custom poller and pager

### Settings

``` yaml
input-file: ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/paging.json
namespace: custompollerpagerversiontolerant
output-folder: $(python-sdks-folder)/azure/version-tolerant/Expected/AcceptanceTests/CustomPollerPagerVersionTolerant
package-name: custompollerpagerversiontolerant
license-header: MICROSOFT_MIT_NO_VERSION
azure-arm: true
add-credentials: true
package-version: 0.1.0
basic-setup-py: true
output-artifact: code-model-v4-no-tags
payload-flattening-threshold: 1
clear-output-folder: true
```

### Override ItemPaged to custom Pager
``` yaml
directive:
    - from: swagger-document
      where: '$.paths["/paging/single"].get'
      transform: >
        $["x-python-custom-pager-sync"] = "custompollerpagerdefinitions.CustomPager";
        $["x-python-custom-pager-async"] = "custompollerpagerdefinitions.aio.AsyncCustomPager"
```

### Override LROPoller to custom Poller
``` yaml
directive:
    - from: swagger-document
      where: '$.paths["/paging/multiple/lro"].post'
      transform: >
        $["x-python-custom-poller-sync"] = "custompollerpagerdefinitions.CustomPoller";
        $["x-python-custom-poller-async"] = "custompollerpagerdefinitions.aio.AsyncCustomPoller"
```
