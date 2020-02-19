# Azure Mgmt Resources (Features) for Python

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
azure-arm: true
license-header: MICROSOFT_MIT_NO_VERSION
package-name: azure-mgmt-resource
payload-flattening-threshold: 2
clear-output-folder: true
no-namespace-folders: true
verbose: true
debug: true
multiapi: true
```

```yaml $(multiapi)
batch:
  - tag: package-features-2015-12
```
### Tag: package-features-2015-12
``` yaml $(tag) == 'package-features-2015-12'
input-file:
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/resources/resource-manager/Microsoft.Features/stable/2015-12-01/features.json
namespace: azure.mgmt.resource.features.v2015_12_01
output-folder: F:/azure-sdk-for-python/sdk/resources/azure-mgmt-resource/azure/mgmt/resource/features/v2015_12_01
package-version: '2015-12-01'
```