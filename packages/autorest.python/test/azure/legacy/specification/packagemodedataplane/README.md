# Testing package-mode

### Settings

``` yaml
input-file: ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/head.json
output-folder: $(python-sdks-folder)/azure/legacy/Expected/AcceptanceTests/PackageModeDataPlane
namespace: azure.packagemode.dataplane
package-name: azure-packagemode-dataplane
package-pprint-name: Azure Package Mode Data Plane
license-header: MICROSOFT_MIT_NO_VERSION
azure-arm: true
add-credentials: true
package-version: 1.0.0
output-artifact: code-model-v4-no-tags
payload-flattening-threshold: 1
black: true
package-mode: azure-dataplane
version-tolerant: false
```
