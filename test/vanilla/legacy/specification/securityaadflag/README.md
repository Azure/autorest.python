# Testing package-mode

### Settings

``` yaml
input-file: ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/any-type.json
output-folder: $(python-sdks-folder)/vanilla/legacy/Expected/AcceptanceTests/SecurityAadFlag
title: SecurityAadFlagClient
namespace: securityaadflag
package-name: securityaadflag
license-header: MICROSOFT_MIT_NO_VERSION
basic-setup-py: true
package-version: 1.0.0b1
output-artifact: code-model-v4-no-tags
payload-flattening-threshold: 1
security: AADToken
```
