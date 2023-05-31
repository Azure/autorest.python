# Testing multiapicombiner


``` yaml $(tag) == 'v1'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v1.json
namespace: multiapicombiner.v1
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/multiapicombiner/multiapicombiner/v1
```

``` yaml $(tag) == 'v2'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v2.json
namespace: multiapicombiner.v2
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/multiapicombiner/multiapicombiner/v2
```

``` yaml $(tag) == 'v3'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v3.json
namespace: multiapicombiner.v3
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/multiapicombiner/multiapicombiner/v3
```

### Settings
``` yaml
package-name: multiapicombiner
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
azure-arm: true
add-credentials: true
python3-only: true
version-tolerant: false
combine-operation-files: true
only-path-and-body-params-positional: true
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
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/multiapicombiner/multiapicombiner/
clear-output-folder: false
perform-load: false
```
