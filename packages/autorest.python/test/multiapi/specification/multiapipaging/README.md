# Testing multiapi

``` yaml $(tag) == 'v0'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/paging.json
namespace: multiapipaging.v0
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiPaging/multiapipaging/v0
directive:
  - from: swagger-document
    where: $.info
    transform: >
        $['version'] = '0.0.0';
```

``` yaml $(tag) == 'v1'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/paging.json
namespace: multiapipaging.v1
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiPaging/multiapipaging/v1
```

### Settings
``` yaml
package-name: multiapipaging
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
version-tolerant: false
```

``` yaml $(multiapi)
clear-output-folder: true
batch:
    - tag: v0
    - tag: v1
    - multiapiscript: true
```

### Multi-api script

``` yaml $(multiapiscript)
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiPaging/multiapipaging/
clear-output-folder: false
perform-load: false
```
