# Testing multiapi keyword only

``` yaml $(tag) == 'v1'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v1-custom-base-url.json
namespace: multiapikeywordonly.v1
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiKeywordOnly/multiapikeywordonly/v1
```

``` yaml $(tag) == 'v2'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v2-custom-base-url.json
namespace: multiapikeywordonly.v2
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiKeywordOnly/multiapikeywordonly/v2
```

### Settings
``` yaml
package-name: multiapikeywordonly
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
add-credentials: true
python3-only: true
version-tolerant: false
only-path-and-body-params-positional: true
```

``` yaml $(multiapi)
clear-output-folder: true
batch:
    - tag: v1
    - tag: v2
    - multiapiscript: true
```

### Multi-api script

``` yaml $(multiapiscript)
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiKeywordOnly/multiapikeywordonly/
clear-output-folder: false
perform-load: false
```
