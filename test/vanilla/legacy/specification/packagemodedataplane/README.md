# Testing package-mode

### Settings

``` yaml
input-file: ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/any-type.json
output-folder: $(python-sdks-folder)/vanilla/legacy/Expected/AcceptanceTests/PackageModeDataPlane
namespace: packagemode
package-name: packagemode
package-pprint-name: Azure Package Mode
add-credentials: false
license-header: MICROSOFT_MIT_NO_VERSION
package-version: 1.0.0b1
output-artifact: code-model-v4-no-tags
payload-flattening-threshold: 1
clear-output-folder: true
black: true
vanilla: true
package-mode: dataplane
```
