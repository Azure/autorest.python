# Azure Text Analytics for Python

> see https://aka.ms/autorest

### Setup
```ps
cd C:\work
git clone --recursive https://github.com/Azure/autorest.python.git
cd autorest.python
git checkout azure-core
npm install
```

### Generation
```ps
cd <swagger-folder>
autorest --use=C:/work/autorest.python --version=2.0.4280
```

---
# Code Generation

### Settings
``` yaml
input-file: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2019-06-01/blob.json
output-folder: _generated
package-name: azure-mgmt-storage
namespace: azure.mgmt.storage
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
azure-arm: true
clear-output-folder: true
python: true
payload-flattening-threshold: 2
```