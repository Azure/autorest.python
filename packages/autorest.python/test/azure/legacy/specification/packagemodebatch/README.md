# Testing package-mode

### Settings

``` yaml
azure-arm: true
package-version: 1.0.0
license-header: MICROSOFT_MIT_NO_VERSION
output-artifact: code-model-v4-no-tags
payload-flattening-threshold: 1
package-mode: mgmtplane
package-name: azure-packagemode-batch
package-pprint-name: Azure Package Mode Batch Mgmt Plane
output-folder: $(python-sdks-folder)/azure/legacy/Expected/AcceptanceTests/PackageModeBatch
version-tolerant: false
```

### Python multi-client

``` yaml
batch:
    - tag: head
    - tag: paging
    - multiclientscript: true
```

``` yaml $(tag) == 'head'
title: HeadClient
input-file: ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/head.json
namespace: azure.packagemode.batch.head
```

``` yaml $(tag) == 'paging'
title: PagingClient
input-file: ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/paging.json
namespace: azure.packagemode.batch.paging
```

``` yaml $(multiclientscript)
perform-load: false
output-folder: $(python-sdks-folder)/azure/legacy/Expected/AcceptanceTests/PackageModeBatch/azure/packagemode/batch
```
