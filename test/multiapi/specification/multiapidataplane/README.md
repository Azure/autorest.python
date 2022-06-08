# Testing multiapi data plane

### Tag: v1

These settings apply only when `--tag=v1` is specified on the command line.

``` yaml $(tag) == 'v1'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v1.json
namespace: multiapidataplane.v1
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiDataPlane/multiapidataplane/v1
```

``` yaml $(tag) == 'v2'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v2.json
namespace: multiapidataplane.v2
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiDataPlane/multiapidataplane/v2
```

``` yaml $(tag) == 'v3'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v3.json
namespace: multiapidataplane.v3
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiDataPlane/multiapidataplane/v3
```

### Settings
``` yaml
package-name: multiapidataplane
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
add-credentials: true
python3-only: true
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
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiDataPlane/multiapidataplane/
clear-output-folder: false
perform-load: false
```
