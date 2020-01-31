# SearchServiceClient

> see https://aka.ms/autorest

This is the AutoRest configuration file for SearchServiceClient.


---
## Getting Started

To build the SDK for SearchServiceClient, simply [Install AutoRest](https://aka.ms/autorest/install) and in this folder, run:

> `autorest`

To see additional help and options, run:

> `autorest --help`
---

## Configuration
### Basic Information
These are the global settings for SearchServiceClient.

``` yaml
opt-in-extensible-enums: true
openapi-type: data-plane
tag: package-2019-05
```
---
# Code Generation

!!! READ THIS !!!
This swagger is ready for C# and Java.
!!! READ THIS !!!

https://github.com/Azure/autorest.csharp/blob/6398c8a58af4aaac10e1680ccb58aeb11a86c825/samples/CognitiveSearch/readme.md

### Settings
``` yaml
title: AzureSearch
input-file:
#- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/search/data-plane/Microsoft.Azure.Search.Service/stable/2019-05-06/searchservice.json
- https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/search/data-plane/Microsoft.Azure.Search.Data/stable/2019-05-06/searchindex.json
output-folder: _generated
package-name: azure-search
namespace: azure.search
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
enable-xml: true
clear-output-folder: true
python: true
payload-flattening-threshold: 2
```