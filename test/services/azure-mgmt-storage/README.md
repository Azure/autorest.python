# Azure Management Storage for Python

> see https://aka.ms/autorest

## Configuration



### Basic Information
These are the global settings for the Storage API.

``` yaml
openapi-type: arm
tag: package-2019-06
```

### Tag: package-2019-06

These settings apply only when `--tag=package-2019-06` is specified on the command line.

``` yaml $(tag) == 'package-2019-06'
input-file:
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2019-06-01/storage.json
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2019-06-01/blob.json
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/storage/resource-manager/Microsoft.Storage/stable/2019-06-01/file.json

directive:
  - suppress: R3018
    reason: Existing boolean properties
    approved-by: "@fearthecowboy"

  - where:
    - $.paths["/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/setLegalHold"].post.operationId
    - $.paths["/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/clearLegalHold"].post.operationId
    - $.paths["/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/regenerateKey"].post.operationId
    suppress: R1003
    reason: APIs return array of values, is not actually a 'list' operation
    approved-by: "@fearthecowboy"

```

### Generation
```ps
cd <swagger-folder>
autorest --use=C:/work/autorest.python --version=2.0.4280
```

### Settings
``` yaml
output-folder: _generated
package-name: azure-mgmt-storage
no-namespace-folders: true
clear-output-folder: true
license-header: MICROSOFT_MIT_NO_VERSION
azure-arm: true
clear-output-folder: true
python: true
payload-flattening-threshold: 2
```