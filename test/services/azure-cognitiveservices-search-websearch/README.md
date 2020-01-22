# Azure Cognitive Services Web Search for Python

> see https://aka.ms/autorest

### Setup
```ps
cd C:\work
git clone --recursive https://github.com/Azure/autorest.python.git
cd autorest.python
git checkout azure-core
npm install
```

### Generation
```ps
cd <swagger-folder>
autorest --use=C:/work/autorest.python --version=2.0.4280
```

### Settings
``` yaml
input-file: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/cognitiveservices/data-plane/WebSearch/stable/v1.0/WebSearch.json
output-folder: _generated
package-name: azure-cognitiveservices-search-websearch
namespace: azure.cognitiveservices.search.websearch
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
clear-output-folder: true
add-credentials: true
payload-flattening-threshold: 2
```