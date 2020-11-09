# Testing adding a custom poller and pager

### Settings

``` yaml
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/paging.json
namespace: custompollerpager
output-folder: $(python-sdks-folder)/azure/Expected/AcceptanceTests/CustomPollerPager
package-name: custompollerpager
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
    from: swagger-document
    where: '$.paths["/paging/single"].get'
    transform: >
        $["x-python-custom-pager-sync"] = "azure.search.documents.SearchItemPaged";
        $["x-python-custom-pager-async"] = "azure.search.documents.aio.AsyncSearchItemPaged"
```
