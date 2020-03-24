# Testing multiapi

### Tag: v1

These settings apply only when `--tag=v1` is specified on the command line.

``` yaml $(tag) == 'v1'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v1.json
namespace: multiapiwithsubmodule.submodule.v1
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiWithSubmodule/multiapiwithsubmodule/submodule/v1
```

``` yaml $(tag) == 'v2'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v2.json
namespace: multiapiwithsubmodule.submodule.v2
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiWithSubmodule/multiapiwithsubmodule/submodule/v2
```

``` yaml $(tag) == 'v3'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v3.json
namespace: multiapiwithsubmodule.submodule.v3
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiWithSubmodule/multiapiwithsubmodule/submodule/v3
```

### Settings
``` yaml
license-header: MICROSOFT_MIT_NO_VERSION
azure: true
add-credentials: true
```

``` yaml $(multiapi)
package-name: multiapiwithsubmodule
clear-output-folder: true
batch:
    - tag: v1
    - tag: v2
    - tag: v3
```

### Multi-api script

``` yaml $(multiapiscript)
package-name: multiapiwithsubmodule#submodule
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiWithSubmodule/multiapiwithsubmodule/submodule
clear-output-folder: false
perform-load: false
```
