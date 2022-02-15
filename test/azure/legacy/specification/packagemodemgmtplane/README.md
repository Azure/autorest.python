# Testing package-mode

### Settings

``` yaml
input-file: ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/paging.json
output-folder: $(python-sdks-folder)/azure/legacy/Expected/AcceptanceTests/PackageModeMgmtPlane
namespace: azure.package.mode
package-name: azure-package-mode
license-header: MICROSOFT_MIT_NO_VERSION
azure-arm: true
add-credentials: true
package-version: 1.0.0b1
output-artifact: code-model-v4-no-tags
payload-flattening-threshold: 1
clear-output-folder: true
black: true
```
