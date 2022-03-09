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

``` yaml $(tag) == 'v2'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v2.json
namespace: multiapisecurity.v2
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiSecurity/multiapisecurity/v2
```

``` yaml $(tag) == 'v3'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v3.json
namespace: multiapisecurity.v3
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiSecurity/multiapisecurity/v3
```

### Settings
``` yaml
package-name: multiapisecurity
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
security: [AADToken, AzureKey]
```

``` yaml $(multiapi)
clear-output-folder: true
batch:
    - tag: v0
    - tag: v1
    - tag: v2
    - tag: v3
    - multiapiscript: true
```

### Multi-api script

``` yaml $(multiapiscript)
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiSecurity/multiapisecurity/
perform-load: false
```
