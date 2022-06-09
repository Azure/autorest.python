# Testing multiapi custom base url

``` yaml $(tag) == 'v1'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v1-custom-base-url.json
namespace: multiapicustombaseurl.v1
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiCustomBaseUrl/multiapicustombaseurl/v1
```

``` yaml $(tag) == 'v2'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/multiapi-v2-custom-base-url.json
namespace: multiapicustombaseurl.v2
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiCustomBaseUrl/multiapicustombaseurl/v2
```

### Settings
``` yaml
package-name: multiapicustombaseurl
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
add-credentials: true
python3-only: true
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
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiCustomBaseUrl/multiapicustombaseurl/
clear-output-folder: false
perform-load: false
```
