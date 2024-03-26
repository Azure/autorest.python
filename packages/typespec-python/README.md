# TypeSpec Python Client Emitter

## Getting started

### Initialize TypeSpec Project

Follow [TypeSpec Getting Started](https://typespec.io/docs) to initialize your TypeSpec project.

Make sure `npx tsp compile .` runs correctly.

### Add typespec-python to your project

Include @azure-tools/typespec-python dependencies in `package.json`:

```diff
 "dependencies": {
+      "@azure-tools/typespec-python": "latest"
  },
```

Run `npm install` to install the dependency.

### Generate a Python client library

You can either specify typespec-python on the commandline or through tspconfig.yaml.

#### Generate with `--emit` command

Run command `npx tsp compile --emit @azure-tools/typespec-python <path-to-typespec-file>`

e.g.

```cmd
npx tsp compile main.tsp --emit @azure-tools/typespec-python
```

or

```cmd
npx tsp compile client.tsp --emit @azure-tools/typespec-python
```

#### Generate with tspconfig.yaml

Add the following configuration in tspconfig.yaml:

```diff
emit:
  - "@azure-tools/typespec-csharp"
options:
  "@azure-tools/typespec-csharp":
+    namespace: Azure.Template.MyTypeSpecProject
```

Run the command to generate your library:

```cmd
npx tsp compile main.tsp
```

or

```cmd
npx tsp compile client.tsp
```

## Configure the generated library

You can further configure the generated client library using the emitter options on @azure-tools/typespec-python.

You can set options in the command line directly via `--option @azure-tools/typespec-python.<optionName>=XXX`, e.g. `--option @azure-tools/typespec-python.package-name=azure-contoso`

or

Modify `tspconfig.yaml` in the TypeSpec project to add emitter options under options/@azure-tools/typespec-python.

```diff
emit:
  - "@azure-tools/typespec-python"
options:
  "@azure-tools/typespec-python":
+    package-dir: azure-contoso
+    package-name: {package-dir}
```

### Supported Emitter options

Common emitter configuration example:
```yaml
emit:
  - "@azure-tools/typespec-python"
options:
  "@azure-tools/typespec-python":
    package-dir: "azure-contoso"
    package-name: "{package-dir}"
```

|Option|Type|Description|
|-|-|-|
|`package-version`|string|Specify the package version. Default version: `1.0.0b1`|
|`package-name`|string|The client library name, this will be the package name on PyPi.|
|`output-dir`|string|optionally specify an output directory.|
|`generate-packaging-files`|boolean|indicate if packaging files should be generated. For example: setup.py.|
|`package-pprint-name`|string|specify the package name to be used on PyPi.|
|`models-mode`|string|indicate if models should be generated. Default: `true`.|
|`flavor`||"azure"|
|`emit-cross-language-definition-file`|boolean|
|`head-as-boolean`|boolean|
|`packaging-files-dir`|string|
|`packaging-files-config`|object|
|`tracing`|boolean|
|`company-name`|string|
|`debug`|boolean|