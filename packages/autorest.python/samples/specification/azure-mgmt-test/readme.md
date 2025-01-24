# Sample Management Generation

This file is to check whether standard [readme.python.md](https://github.com/Azure/azure-rest-api-specs/blob/main/documentation/samplefiles/readme.python.md) template could work.

### Settings

``` yaml $(python)
input-file: ../../../node_modules/@microsoft.azure/autorest.testserver/swagger/body-array.json
azure-arm: true
license-header: MICROSOFT_MIT_NO_VERSION
package-name: azure-mgmt-test
namespace: azure.mgmt.test
package-version: 1.0.0b1
clear-output-folder: true
version-tolerant: false
```

``` yaml $(python)
no-namespace-folders: true
output-folder: $(python-sdks-folder)/test/azure-mgmt-test/azure/mgmt/test
```

``` yaml $(python)
modelerfour:
  flatten-models: false
```
