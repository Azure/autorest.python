# Testing multiapi

### Tag: v1

These settings apply only when `--tag=v1` is specified on the command line.

``` yaml $(tag) == 'v1'
input-file: swaggers/swagger1.json
namespace: autorest.multiapi.v1
output-folder: $(python-sdks-folder)/multiapi/azure-mulitapi/azure/multiapi/v1
```

### Settings
``` yaml
package-name: autorest-multiapi
namespace: autorest.multiapi
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
vanilla: true
add-credentials: true
payload-flattening-threshold: 2
```

``` yaml $(multiapi)
clear-output-folder: true
batch:
    - tag: v1
    - multiapiscript: true
```

### Multi-api script

``` yaml $(multiapiscript)
output-folder: $(python-sdks-folder)/multiapi/azure-mulitapi/azure/multiapi/
clear-output-folder: false
perform-load: false
```
