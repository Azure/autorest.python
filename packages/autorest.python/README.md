# Generating with Autorest for Python

**This emitter is deprecated and will no longer receive support**

#### Python code gen

```yaml !$(multiclientscript)
# default values for version tolerant and black
black: true
```

```yaml !$(low-level-client)
version-tolerant: true
```

```yaml !$(low-level-client) && !$(version-tolerant)
modelerfour:
  group-parameters: true
  flatten-models: true
  flatten-payloads: true
```

```yaml !$(multiclientscript)
pass-thru:
  - model-deduplicator
  - subset-reducer
version: ~3.8.1
use-extension:
  "@autorest/modelerfour": ~4.23.5

modelerfour:
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
    # Doesn't process anything, just makes it so that the 'python:' config section is loaded and available for the next plugins.
    pass-thru: true
    input: modelerfour/identity

  python/m2r:
    input: python

  python/m4reformatter:
    input: python/m2r

  python/preprocess:
    input: python/m4reformatter

  python/codegen:
    input: python/preprocess
    output-artifact: python-files

  python/codegen/emitter:
    input: codegen
    scope: scope-codegen/emitter

scope-codegen/emitter:
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

# Multi Client pipeline

```yaml $(multiclientscript)
pipeline:
  python/multiclientscript:
    scope: multiclientscript
    output-artifact: python-files

  python/multiclientscript/emitter:
    input: multiclientscript
    scope: scope-multiclientscript/emitter

scope-multiclientscript/emitter:
  input-artifact: python-files
  output-uri-expr: $key

output-artifact: python-files
```

<!-- LINKS -->

[python_docs]: https://github.com/Azure/autorest.python/tree/main/docs/readme.md
[main_docs]: https://github.com/Azure/autorest/tree/master/docs
