# Testing adding a custom poller and pager

### Settings

``` yaml
title: LroPagingClient
input-file: lropaging.json
namespace: lropagingversiontolerant
package-name: lropagingversiontolerant
output-folder: $(python-sdks-folder)/azure/version-tolerant/Expected/AcceptanceTests/LroPagingVersionTolerant
license-header: MICROSOFT_MIT_NO_VERSION
clear-output-folder: true
python: true
package-version: 1.0.0b1
basic-setup-py: true
```

```yaml
directive:
- where-operation: QuestionAnsweringProjects_UpdateQnas
  transform: |
    $["x-ms-pageable"] = {
      "nextLinkName": "nextLink",
      "itemName": "value"
    };
    $.responses["200"] = {
      description: "All the QnAs of a project.",
      schema: {
        "$ref": "#/definitions/QnaAssets"
      }
    };
```
