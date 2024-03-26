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
  - "@azure-tools/typespec-python"
options:
  "@azure-tools/typespec-python":
+    package-dir: "azure-contoso"
+    package-name: "azure-contoso"
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

You can further configure the generated client library using the emitter options provided through @azure-tools/typespec-python.

You can set options in the command line directly via `--option @azure-tools/typespec-python.<optionName>=XXX`, e.g. `--option @azure-tools/typespec-python.package-name="azure-contoso"`

or

Modify `tspconfig.yaml` in the TypeSpec project to add emitter options under options/@azure-tools/typespec-python.

```diff
emit:
  - "@azure-tools/typespec-python"
options:
  "@azure-tools/typespec-python":
+    package-dir: "azure-contoso"
+    package-name: "{package-dir}"
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
|`package-name`|string|Specify the package name.|
|`output-dir`|string|Specify an output directory.|
|`generate-packaging-files`|boolean|Indicate if packaging files, such as setup.py, should be generated.|
|`package-pprint-name`|string|Specify the pretty print name for the package.|
|`models-mode`|string|Indicate if models should be generated. Default: `true`.|
|`flavor`|"azure"|"azure"|
|`emit-cross-language-definition-file`|boolean|
|`head-as-boolean`|boolean|
|`packaging-files-dir`|string|
|`packaging-files-config`|object|
|`tracing`|boolean|Enable tracing.|
|`company-name`|string|
|`debug`|boolean|Enable debugging.|