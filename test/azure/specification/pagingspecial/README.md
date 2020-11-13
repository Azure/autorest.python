# Special paging

### Settings

``` yaml
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/paging-special.json
namespace: pagingspecial
output-folder: $(python-sdks-folder)/azure/Expected/AcceptanceTests/PagingSpecial
package-name: pagingspecial
license-header: MICROSOFT_MIT_NO_VERSION
azure-arm: true
add-credentials: true
package-version: 0.1.0
basic-setup-py: true
output-artifact: code-model-v4-no-tags
payload-flattening-threshold: 1
clear-output-folder: true
trace: true
```

### Override ItemPaged to custom Pager
``` yaml
directive:
    from: swagger-document
    where: '$.paths["/pagingSpecial/tokenWithMetadata"].get'
    transform: >
        $["x-python-custom-pager-sync"] = "customdefinitions.PagerWithMetadata";
        $["x-python-custom-pager-async"] = "customdefinitions.aio.AsyncPagerWithMetadata"
```
