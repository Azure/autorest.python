# Testing adding a custom poller and pager

### Settings

``` yaml
input-file:
- ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/head.json
- ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/azure-special-properties.json
title: MixedApiVersionClient
namespace: mixedapiversion
output-folder: $(python-sdks-folder)/azure/legacy/Expected/AcceptanceTests/MixedApiVersion
package-name: mixedapiversion
license-header: MICROSOFT_MIT_NO_VERSION
add-credentials: true
package-version: 1.0.0b1
basic-setup-py: true
output-artifact: code-model-v4-no-tags
clear-output-folder: true
version-tolerant: false
```
