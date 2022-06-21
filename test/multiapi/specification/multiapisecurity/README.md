# Testing MultiapiSecurity

### Tag: v1

These settings apply only when `--tag=v1` is specified on the command line.

``` yaml $(tag) == 'v0'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v0.json
namespace: multiapisecurity.v0
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiSecurity/multiapisecurity/v0
```

``` yaml $(tag) == 'v1'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v1.json
namespace: multiapisecurity.v1
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiSecurity/multiapisecurity/v1
```

### Settings
``` yaml
package-name: multiapisecurity
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
security: AADToken
python3-only: true
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
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiSecurity/multiapisecurity/
perform-load: false
```
