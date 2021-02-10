# Generating with Autorest for Python v5.0.0

See [here](https://github.com/Azure/autorest.python/wiki/Generating-with-autorest-for-python-v5.0.0) for Python-specific docs, and [here] for general docs

# Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

### Autorest plugin configuration

- Please don't edit this section unless you're re-configuring how the powershell extension plugs in to AutoRest
  AutoRest needs the below config to pick this up as a plug-in - see https://github.com/Azure/autorest/blob/master/docs/developer/architecture/AutoRest-extension.md

#### Python code gen

```yaml !$(multiapiscript)
pass-thru:
  - model-deduplicator
  - subset-reducer
version: ^3.0.6372
use-extension:
  "@autorest/modelerfour": ^4.15.456

modelerfour:
  group-parameters: true
  flatten-models: true
  flatten-payloads: true
  resolve-schema-name-collisons: true
  always-create-content-type-parameter: true
  multiple-request-parameter-flattening: false
  naming:
    parameter: snakecase
    property: snakecase
    operation: snakecase
    operationGroup: pascalcase
    choice: pascalcase
    choiceValue: uppercase
    constant: snakecase
    constantParameter: snakecase
    type: pascalcase
    local: _ + snakecase
    global: snakecase
    preserve-uppercase-max-length: 6
    override:
      $host: $host
      base64: base64
      IncludeAPIs: include_apis

pipeline:
  python:
    # doesn't process anything, just makes it so that the 'python:' config section loads early.
    pass-thru: true
    input: openapi-document/multi-api/identity

  modelerfour:
    # in order that the modelerfour/flattener/grouper/etc picks up
    # configuration nested under python: in the user's config,
    # we have to make modeler four pull from the 'python' task.
    input: python

  python/m2r:
    input: modelerfour/identity

  python/namer:
    input: python/m2r

  python/codegen:
    input: python/namer
    output-artifact: python-files

  python/codegen/emitter:
    input: codegen
    scope: scope-codegen/emitter

scope-codegen/emitter:
  input-artifact: python-files
  output-uri-expr: $key

output-artifact: python-files
```

# Multiapi script pipeline

```yaml $(multiapiscript)
pipeline:
  python/multiapiscript:
    scope: multiapiscript
    output-artifact: python-files

  python/multiapiscript/emitter:
    input: multiapiscript
    scope: scope-multiapiscript/emitter

scope-multiapiscript/emitter:
  input-artifact: python-files
  output-uri-expr: $key

output-artifact: python-files
```

# Black script pipeline

```yaml $(black)
pipeline:
  python/black:
    scope: black
    input: python/codegen
    output-artifact: python-files

  python/black/emitter:
    input: black
    scope: scope-black/emitter

scope-black/emitter:
  input-artifact: python-files
  output-uri-expr: $key

output-artifact: python-files
```

<!-- LINKS -->

[python_docs]: https://github.com/Azure/autorest.python/tree/autorestv3/docs/readme.md
[main_docs]: https://github.com/Azure/autorest/tree/master/docs
