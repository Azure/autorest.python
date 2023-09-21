# Testing package-mode

### Settings

``` yaml
input-file: ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/media_types.json
output-folder: $(python-sdks-folder)/vanilla/legacy/Expected/AcceptanceTests/InternalOperation
namespace: internaloperation
package-name: internaloperation
package-pprint-name: Internal Operation
add-credentials: false
license-header: MICROSOFT_MIT_NO_VERSION
package-version: 1.0.0b1
output-artifact: code-model-v4-no-tags
payload-flattening-threshold: 1
black: true
vanilla: true
package-mode: azure-dataplane
version-tolerant: false
```

### Add x-ms-internal
``` yaml
directive:
    - from: swagger-document
      where: '$.paths["/mediatypes/bodyThreeTypes"]'
      transform: >
        $.post["x-ms-internal"] = true
```
