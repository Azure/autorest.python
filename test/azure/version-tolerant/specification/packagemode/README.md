# Testing adding a custom poller and pager

### Settings

``` yaml
input-file: ../../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/paging.json
namespace: custompollerpagerversiontolerant
package-name: custompollerpagerversiontolerant
license-header: MICROSOFT_MIT_NO_VERSION
azure-arm: true
add-credentials: true
package-version: 0.1.0
basic-setup-py: true
output-artifact: code-model-v4-no-tags
payload-flattening-threshold: 1
clear-output-folder: true
version-tolerant: true
black: true
```

```yaml $(package-mode)
package-configuration:
    test_parameters: hello_world
```