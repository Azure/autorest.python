# Azure GraphRBAC for Python

> see https://aka.ms/autorest

## Suppression

``` yaml
directive:
  - suppress: D5001
    reason: this spec never has examples. It is owned by the SDK group and we already have CLI commands testing it
  - suppress: R2058
    reason: existing since the spec started
  - suppress: R3016
    reason: existing since the spec started
```

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
input-file: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/96e30c6e5713b364c17c154a99131ebf14a3083a/specification/graphrbac/data-plane/Microsoft.GraphRbac/stable/1.6/graphrbac.json
output-folder: _generated
package-name: azure-graphrbac
namespace: azure.graphrbac
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
payload-flattening-threshold: 2
package-version: 0.61.1
```