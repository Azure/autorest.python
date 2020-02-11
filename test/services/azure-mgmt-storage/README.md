# Azure Mgmt Storage for Python

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
package-name: azure-mgmt-storage
license-header: MICROSOFT_MIT_NO_VERSION
azure-arm: true
clear-output-folder: true
no-namespace-folders: true
python: true
payload-flattening-threshold: 2
multiapi: true
```

```yaml $(multiapi)
batch:
  - tag: package-2019-06
  - tag: package-2019-04
  - tag: package-2018-11
  - tag: package-2018-07
  - tag: package-2018-03
  - tag: package-2018-02
  - tag: package-2017-10
  - tag: package-2017-06
  - tag: package-2016-12
  - tag: package-2016-01
  - tag: package-2015-06
```
### Tag: package-2019-06
``` yaml $(tag) == 'package-2019-06'
input-file:
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2019-06-01/storage.json
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2019-06-01/blob.json
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2019-06-01/file.json
namespace: azure.mgmt.storage.v2019_06_01
output-folder: F:/azure-sdk-for-python/sdk/storage/azure-mgmt-storage/azure/mgmt/storage/v2019_06_01
package-version: '2019-06-01'
```

### Tag: package-2019-04
``` yaml $(tag) == 'package-2019-04'
input-file:
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2019-04-01/storage.json
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2019-04-01/blob.json
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2019-04-01/file.json
namespace: azure.mgmt.storage.v2019_04_01
output-folder: F:/azure-sdk-for-python/sdk/storage/azure-mgmt-storage/azure/mgmt/storage/v2019_04_01
package-version: '2019-04-01'
```

### Tag: package-2018-11

``` yaml $(tag) == 'package-2018-11'
input-file:
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2018-11-01/storage.json
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2018-11-01/blob.json
namespace: azure.mgmt.storage.v2018_11_01
output-folder: F:/azure-sdk-for-python/sdk/storage/azure-mgmt-storage/azure/mgmt/storage/v2018_11_01
package-version: '2018-11-01'
```

### Tag: package-2018-07

``` yaml $(tag) == 'package-2018-07'
input-file:
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2018-07-01/storage.json
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2018-07-01/blob.json
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/preview/2018-03-01-preview/managementpolicy.json
namespace: azure.mgmt.storage.v2018_07_01
output-folder: F:/azure-sdk-for-python/sdk/storage/azure-mgmt-storage/azure/mgmt/storage/v2018_07_01
package-version: '2018-07-01'
```

### Tag: package-2018-03

``` yaml $(tag) == 'package-2018-03'
input-file:
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/preview/2018-03-01-preview/storage.json
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/preview/2018-03-01-preview/blob.json
namespace: azure.mgmt.storage.v2018_03_01_preview
output-folder: F:/azure-sdk-for-python/sdk/storage/azure-mgmt-storage/azure/mgmt/storage/v2018_03_01_preview
package-version: '2018-03-01-preview'
```

### Tag: package-2018-02

``` yaml $(tag) == 'package-2018-02'
input-file:
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2018-02-01/storage.json
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2018-02-01/blob.json
namespace: azure.mgmt.storage.v2018_02_01
output-folder: F:/azure-sdk-for-python/sdk/storage/azure-mgmt-storage/azure/mgmt/storage/v2018_02_01
package-version: '2018-02-01'
```

### Tag: package-2017-10

``` yaml $(tag) == 'package-2017-10'
input-file:
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2017-10-01/storage.json
namespace: azure.mgmt.storage.v2017_10_01
output-folder: F:/azure-sdk-for-python/sdk/storage/azure-mgmt-storage/azure/mgmt/storage/v2017_10_01
package-version: '2017-10-01'
```

### Tag: package-2017-06

``` yaml $(tag) == 'package-2017-06'
input-file:
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2017-06-01/storage.json
namespace: azure.mgmt.storage.v2017_06_01
output-folder: F:/azure-sdk-for-python/sdk/storage/azure-mgmt-storage/azure/mgmt/storage/v2017_06_01
package-version: '2017-06-01'
```

### Tag: package-2016-12

``` yaml $(tag) == 'package-2016-12'
input-file:
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2016-12-01/storage.json
namespace: azure.mgmt.storage.v2016_12_01
output-folder: F:/azure-sdk-for-python/sdk/storage/azure-mgmt-storage/azure/mgmt/storage/v2016_12_01
package-version: '2016-12-01'
```

### Tag: package-2016-01

``` yaml $(tag) == 'package-2016-01'
input-file:
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2016-01-01/storage.json
namespace: azure.mgmt.storage.v2016_01_01
output-folder: F:/azure-sdk-for-python/sdk/storage/azure-mgmt-storage/azure/mgmt/storage/v2016_01_01
package-version: '2016-01-01'
```

### Tag: package-2015-06

``` yaml $(tag) == 'package-2015-06'
input-file:
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2015-06-15/storage.json
namespace: azure.mgmt.storage.v2015_06_15
output-folder: F:/azure-sdk-for-python/sdk/storage/azure-mgmt-storage/azure/mgmt/storage/v2015_06_15
package-version: '2015-06-15'
```