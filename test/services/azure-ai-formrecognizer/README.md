# Azure Form Recognizer for Python

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
input-file: https://raw.githubusercontent.com/iscai-msft/azure-rest-api-specs/working_form_recognizer/specification/cognitiveservices/data-plane/FormRecognizer/preview/v2.0/FormRecognizer.json
output-folder: _generated
package-name: azure-ai-formrecognizer
namespace: azure.ai.formrecognizer
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
enable-xml: true
vanilla: true
clear-output-folder: true
python: true
add-credentials: true
payload-flattening-threshold: 2
basic-setup-py: true
package-version: 2.0.0
credential-scopes: https://cognitiveservices.azure.com/.default
```