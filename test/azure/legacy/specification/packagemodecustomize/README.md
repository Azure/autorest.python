# Testing package-mode

### Settings

``` yaml
input-file: ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/paging.json
output-folder: $(python-sdks-folder)/azure/legacy/Expected/AcceptanceTests/PackageModeCustomize
namespace: azure.packagemode.customize
package-name: azure-packagemode-customize
license-header: MICROSOFT_MIT_NO_VERSION
azure-arm: true
add-credentials: true
package-version: 0.1.0
output-artifact: code-model-v4-no-tags
payload-flattening-threshold: 1
clear-output-folder: true
black: true
```

```yaml $(package-mode)
package-configuration:
    min_python_version: 3.6
    package_name: azure-packagemode-customize
```
