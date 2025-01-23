# Azure Communication Configuration for Python

Make sure the configuration of data-plane SDK (e.g. [here](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/communication/azure-communication-callautomation/swagger/SWAGGER.md)) could work

### Settings

```yaml
input-file: ../../../node_modules/@microsoft.azure/autorest.testserver/swagger/head.json
output-folder: $(python-sdks-folder)/test/azure-test/azure/test/_generated
namespace: azure.test
package-name: azure-test
license-header: MICROSOFT_MIT_NO_VERSION
clear-output-folder: true
no-namespace-folders: true
```
