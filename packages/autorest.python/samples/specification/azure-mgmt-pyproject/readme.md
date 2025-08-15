# Sample Management Generation

This file is to check whether standard [readme.python.md](https://github.com/Azure/azure-rest-api-specs/blob/main/documentation/samplefiles/readme.python.md) template could work.

### Settings

``` yaml $(python)
input-file: ../../../node_modules/@microsoft.azure/autorest.testserver/swagger/head.json
title: PyprojectMgmtClient
azure-arm: true
license-header: MICROSOFT_MIT_NO_VERSION
package-name: azure-mgmt-pyproject
namespace: azure.mgmt.pyproject
package-version: 1.0.0b1
clear-output-folder: true
version-tolerant: false
package-mode: azure-mgmt
```

``` yaml $(python)
no-namespace-folders: true
output-folder: $(python-sdks-folder)/test/azure-mgmt-pyproject/azure/mgmt/pyproject
```

``` yaml $(python)
modelerfour:
  flatten-models: false
```
