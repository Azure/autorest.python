# Testing package-mode

### Settings

``` yaml
package-version: 1.0.0
license-header: MICROSOFT_MIT_NO_VERSION
output-artifact: code-model-v4-no-tags
payload-flattening-threshold: 1
package-mode: dataplane
package-name: azure-packagemode-batch
package-pprint-name: Azure Package Mode Batch Data Plane
output-folder: $(python-sdks-folder)/azure/legacy/Expected/AcceptanceTests/PackageModeBatch
```

### Python multi-client

``` yaml
batch:
    - tag: v0
    - tag: v1
    - multiclient: true
```

``` yaml $(tag) == 'v0'
title: BatchV0Client
input-file: ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/head.json
namespace: azure.packagemode.batch.v0
```

``` yaml $(tag) == 'v1'
title: BatchV1Client
input-file: ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/head.json
namespace: azure.packagemode.batch.v1
```

``` yaml $(multiclient)
output-folder: $(python-sdks-folder)/azure/legacy/Expected/AcceptanceTests/PackageModeBatch/azure/packagemode/batch
```
