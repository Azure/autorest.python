# Azure Text Analytics for Python

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
input-file: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/cognitiveservices/data-plane/TextAnalytics/stable/v2.1/TextAnalytics.json
output-folder: _generated
package-name: azure-ai-textanalytics
namespace: azure.ai.textanalytics
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
enable-xml: true
vanilla: true
clear-output-folder: true
python: true
add-credentials: true
payload-flattening-threshold: 2
credential-scopes: https://cognitiveservices.azure.com/.default
```