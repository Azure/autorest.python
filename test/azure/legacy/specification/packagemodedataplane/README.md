# Testing package-mode

### Settings

``` yaml
input-file: ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/paging.json
output-folder: $(python-sdks-folder)/azure/legacy/Expected/AcceptanceTests/PackageModeDataPlane
namespace: packagemode
package-name: packagemode
add-credentials: true
credential-default-policy-type: AzureKeyCredentialPolicy
license-header: MICROSOFT_MIT_NO_VERSION
package-version: 1.0.0b1
output-artifact: code-model-v4-no-tags
payload-flattening-threshold: 1
clear-output-folder: true
version-tolerant: true
black: true
```
