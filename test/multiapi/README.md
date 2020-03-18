# Testing multiapi

### Tag: v1

These settings apply only when `--tag=v1` is specified on the command line.

``` yaml $(tag) == 'v1'
input-file: swaggers/swagger1.json
namespace: multiapi.v1
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/Multiapi/multiapi/v1
```

``` yaml $(tag) == 'v2'
input-file: swaggers/swagger2.json
namespace: multiapi.v2
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/Multiapi/multiapi/v2
```

``` yaml $(tag) == 'v3'
input-file: swaggers/swagger3.json
namespace: multiapi.v3
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/Multiapi/multiapi/v3
```

### Settings
``` yaml
package-name: multiapi
namespace: multiapi
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
azure: true
add-credentials: true
payload-flattening-threshold: 2
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
