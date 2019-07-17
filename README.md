
# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# AutoRest extension configuration

``` yaml
use-extension:
  "@microsoft.azure/autorest.modeler": "2.3.44"

pipeline:
  python/imodeler1:
    input: openapi-document/identity
    output-artifact: code-model-v1
    scope: python
  python/commonmarker:
    input: imodeler1
    output-artifact: code-model-v1
  python/cm/transform:
    input: commonmarker
    output-artifact: code-model-v1
  python/cm/emitter:
    input: transform
    scope: scope-cm/emitter
  python/generate:
    plugin: python
    input: cm/transform
    output-artifact: source-file-python
  python/transform:
    input: generate
    output-artifact: source-file-python
    scope: scope-transform-string
  python/emitter:
    input: transform
    scope: scope-python/emitter

scope-python/emitter:
  input-artifact: source-file-python
  output-uri-expr: $key

output-artifact:
- source-file-python
```

## Help

``` yaml
help-content:
  python: # type: Help as defined in autorest-core/help.ts
    activationScope: python
    categoryFriendlyName: Python Generator
    settings:
    - key: azure-arm
      description: generate code in Azure flavor
    - key: namespace
      description: determines the namespace to be used in generated code. impacts folder structure.
      type: string
    - key: license-header
      description: 'text to include as a header comment in generated files (magic strings: MICROSOFT_MIT, MICROSOFT_APACHE, MICROSOFT_MIT_NO_VERSION, MICROSOFT_APACHE_NO_VERSION, MICROSOFT_MIT_NO_CODEGEN). Should be MICROSOFT_MIT_NO_VERSION.'
      type: string
    - key: payload-flattening-threshold
      description: max. number of properties in a request body. If the number of properties in the request body is less than or equal to this value, these properties will be represented as individual method arguments instead. Should be 2.
      type: number
    - key: add-credentials
      description: include a credential property and constructor parameter supporting different authentication behaviors. This value is frozen to true if azure-arm=true.
    - key: override-client-name
      description: overrides the name of the client class (usually derived from $.info.title)
      type: string
    - key: client-side-validation
      description: 'whether to validate parameters at the client side (according to OpenAPI definition) before making a request; default: true'
      type: boolean
    - key: package-name
      description: Distribution package name (i.e. PyPI). Impact base folder and UserAgent
      type: string
    - key: package-version
      description: Distribution package version (i.e. PyPI). Impact __version__ and UserAgent
      type: string
    - key: basic-setup-py
      description: If used, generate a basic setup.py to build a wheel package.
      type: bool
    - key: no-namespace-folders
      description: If used, does not generate the namespace folder hierarchy, but directly the client. Useful for update.
      type: bool
    - key: keep-version-file
      description: If used, do not replace the version.py if it already exists.
      type: bool
    - key: no-async
      description: If used, do not generate async code
      type: bool
```