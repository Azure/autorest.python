# Sample Multi API Generation

This sample generates 3 API version: `v1`, `v2`, and `v3`. We first generate each API version individually in
a batch execution, then generate a multi API client on top of these generated API versions

### Settings

``` yaml
namespace: azure.multiapi.sample
package-name: azure-multiapi-sample
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
azure-arm: true
add-credential: true
version-tolerant: false
```

### Multi API Generation

These settings apply only when `--multiapi` is specified on the command line.

``` yaml $(multiapi)
clear-output-folder: true
batch:
    - tag: v1
    - tag: v2
    - tag: v3
    - multiapiscript: true
```

### Multi API script

``` yaml $(multiapiscript)
output-folder: $(python-sdks-folder)/generated/azure/multiapi/sample
clear-output-folder: false
perform-load: false
```

### Tag: v1

These settings apply only when `--tag=v1` is specified on the command line.

``` yaml $(tag) == 'v1'
input-file: ../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v1.json
namespace: azure.multiapi.sample.v1
output-folder: $(python-sdks-folder)/generated/azure/multiapi/sample/v1
```

### Tag: v2

These settings apply only when `--tag=v2` is specified on the command line.

``` yaml $(tag) == 'v2'
input-file: ../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v2.json
namespace: azure.multiapi.sample.v2
output-folder: $(python-sdks-folder)/generated/azure/multiapi/sample/v2
```

### Tag: v3

These settings apply only when `--tag=v2` is specified on the command line.

``` yaml $(tag) == 'v3'
input-file: ../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v3.json
namespace: azure.multiapi.sample.v3
output-folder: $(python-sdks-folder)/generated/azure/multiapi/sample/v3
```
