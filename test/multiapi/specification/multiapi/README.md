# Testing multiapi

### Tag: v1

These settings apply only when `--tag=v1` is specified on the command line.

``` yaml $(tag) == 'v1'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v1.json
namespace: multiapi.v1
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/Multiapi/multiapi/v1
```

``` yaml $(tag) == 'v2'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v2.json
namespace: multiapi.v2
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/Multiapi/multiapi/v2
```

``` yaml $(tag) == 'v3'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v3.json
namespace: multiapi.v3
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/Multiapi/multiapi/v3
```

### Settings
``` yaml
package-name: multiapi
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
azure-arm: true
add-credentials: true
```

``` yaml $(multiapi)
clear-output-folder: true
batch:
    - tag: v1
    - tag: v2
    - tag: v3
    - multiapiscript: true
```

### Multi-api script

``` yaml $(multiapiscript)
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/Multiapi/multiapi/
clear-output-folder: false
perform-load: false
```
