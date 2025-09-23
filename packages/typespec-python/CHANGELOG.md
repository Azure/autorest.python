# Release

## 0.51.1

### Bump dependencies

- [#3220](https://github.com/Azure/autorest.python/pull/3220) Fix dependency bump from `@azure-tools/typespec` libraries


## 0.51.0

### Features

- [#3209](https://github.com/Azure/autorest.python/pull/3209) Support nested nextLink for paging operation

### Bug Fixes

- [#3216](https://github.com/Azure/autorest.python/pull/3216) Add overload for operation when body type is array of model


## 0.50.0

### Features

- [#3169](https://github.com/Azure/autorest.python/pull/3169) DPG model supports multi-layer discriminator.

### Bump dependencies

- [#3190](https://github.com/Azure/autorest.python/pull/3190) Bump dependencies on `http-client-python`
- [#3192](https://github.com/Azure/autorest.python/pull/3192) Bump dependency on `http-client-python` which optimizes exception handling logic when Python and package managers are available but installation fails

### Bug Fixes

- [#3194](https://github.com/Azure/autorest.python/pull/3194) Fix dependencies of pyproject.toml for ARM SDK


## 0.49.0

### Features

- [#3176](https://github.com/Azure/autorest.python/pull/3176) Add keyword only signature `cloud_setting` into ARM client

### Bump dependencies

- [#3188](https://github.com/Azure/autorest.python/pull/3188) Bump dep on `http-client-python`
- [#3177](https://github.com/Azure/autorest.python/pull/3177) Upgrade azure-http-specs version.

### Bug Fixes

- [#3166](https://github.com/Azure/autorest.python/pull/3166) Fix typing to take advantage of `3.9` being the min python version
- [#3174](https://github.com/Azure/autorest.python/pull/3174) fix to keep some existing parts of pyproject.toml
- [#3181](https://github.com/Azure/autorest.python/pull/3181) don't send content-type when no request body


## 0.48.2

### Bug Fixes

- [#3173](https://github.com/Azure/autorest.python/pull/3173) fix generated output folder for packaging files
- [#3173](https://github.com/Azure/autorest.python/pull/3173) keep declaration of pyproject.toml same with existing setup.py of ARM SDK


## 0.48.1

### Bump dependencies

- [#3168](https://github.com/Azure/autorest.python/pull/3168) Bump tsp 1.3.0 and 0.59.0

### Bug Fixes

- [#3168](https://github.com/Azure/autorest.python/pull/3168) Don't include folder suffixes in documentation generated with `generation-subdir`
- [#3168](https://github.com/Azure/autorest.python/pull/3168) Exclude doc folder in pyproject.toml and update license as per PEP 639
- [#3163](https://github.com/Azure/autorest.python/pull/3163) Don't throw when deserializing error model responses


## 0.48.0

### Features

- [#3131](https://github.com/Azure/autorest.python/pull/3131) Add pyproject.toml generation by default
- [#3156](https://github.com/Azure/autorest.python/pull/3156) Add support for `generation-subdir`

### Bug Fixes

- [#3157](https://github.com/Azure/autorest.python/pull/3157) Don't hardcode `emit-cross-language-definition-file` as `true` for azure generations


## 0.47.2

### Bug Fixes

- [#3154](https://github.com/Azure/autorest.python/pull/3154) fix outputfolder of packaging files for arm sdk
- [#3154](https://github.com/Azure/autorest.python/pull/3154) Ensure necessary typing imports for internal models


## 0.47.1

### Bug Fixes

- [#3135](https://github.com/Azure/autorest.python/pull/3135) Import mixins from operations init file to get patch changes
- [#3135](https://github.com/Azure/autorest.python/pull/3135) Don't hardcode client in sample to first client in list
- [#3134](https://github.com/Azure/autorest.python/pull/3134) Fix regression that ignored patches to mixin operation groups when patched in the `operations` folder


## 0.47.0

### Features

- [#3128](https://github.com/Azure/autorest.python/pull/3128) Support @override to reorder operation parameters

### Bump dependencies

- [#3128](https://github.com/Azure/autorest.python/pull/3128) Bump typespec


## 0.46.0

### Features

- Make mixin operations classes private to remove from documentation


## 0.45.5

### Features

- [#3116](https://github.com/Azure/autorest.python/pull/3116) [typespec-python] Add support for uv package manager alongside pip


## 0.45.4

### Bump dependencies

- [#3108](https://github.com/Azure/autorest.python/pull/3108) Bump dependency TCGC 0.57.2


## 0.45.3

### Bump dependencies

- [#3103](https://github.com/Azure/autorest.python/pull/3103) Add support for `validate-versioning` flag, so users can toggle whether they get api versioning validation
- [#3103](https://github.com/Azure/autorest.python/pull/3103) Validate api versions by looking at ordering of api versions from spec


## 0.45.2

No changes, version bump only.

## 0.45.1

### Bump dependencies

- Bump typespec


## 0.45.0

### Features

- [#3089](https://github.com/Azure/autorest.python/pull/3089) generate `_metadata.json` to store info from TCGC

### Bug Fixes

- [#3088](https://github.com/Azure/autorest.python/pull/3088) Fix response type of paging operations from `Iterable` to `ItemPaged`


## 0.44.2

### Bug Fixes

- [#3081](https://github.com/Azure/autorest.python/pull/3081) Fix typing for generic `PipelineClient`
- [#3085](https://github.com/Azure/autorest.python/pull/3085) Add support for legacy parameterized next links

### Bump dependencies

- [#3085](https://github.com/Azure/autorest.python/pull/3085) Bump typespec 1.0.0


## 0.44.1

### Bump dependencies

- Bump to latest typespec version


## 0.44.0

### Bug Fixes

- [#3077](https://github.com/Azure/autorest.python/pull/3077) Move all utils code into a `_utils` folder
- [#3070](https://github.com/Azure/autorest.python/pull/3070) Improve emitter performance by updating black plugin implementation.

### Bump dependencies

- [#3078](https://github.com/Azure/autorest.python/pull/3078) Bump to http-client-python 0.11.0.


## 0.43.0

### Features

- [#3076](https://github.com/Azure/autorest.python/pull/3076) Improve user experience in multi clouds scenario
- [#3073](https://github.com/Azure/autorest.python/pull/3073) add more hooks into setup.py template for users with custom templates


## 0.42.3

### Bug Fixes

- [#3071](https://github.com/Azure/autorest.python/pull/3071) Allow `_` in namespaces

### Other Changes

- [#3065](https://github.com/Azure/autorest.python/pull/3065) Drop support for python3.8

## 0.42.2

No changes, version bump only.

## 0.42.1

### Bug Fixes

- [#3067](https://github.com/Azure/autorest.python/pull/3067) Fix crash when configure `license` in tspconfig.yaml`
- [#3067](https://github.com/Azure/autorest.python/pull/3067) Keep license header for legacy SDK


## 0.42.0

### Features

- [#3062](https://github.com/Azure/autorest.python/pull/3062) Pass authentication flows info into credential policy for unbranded
- [#3061](https://github.com/Azure/autorest.python/pull/3061) support typespec license config


## 0.41.0

### Features

- [#3057](https://github.com/Azure/autorest.python/pull/3057) Always respect namespace from TCGC
- [#3060](https://github.com/Azure/autorest.python/pull/3060) Refine emitter options


## 0.40.0

### Bump dependencies

- [#3058](https://github.com/Azure/autorest.python/pull/3058) Bump `@typespec/*` 0.67

### Features

- [#3050](https://github.com/Azure/autorest.python/pull/3050) Support continuation token for paging


## 0.39.1

### Bug Fixes

- [#3047](https://github.com/Azure/autorest.python/pull/3047) Pass combined types to python generator
- [#3047](https://github.com/Azure/autorest.python/pull/3047) Remove m2r dependency in favor of internally converting md to rst.

## 0.39.0

### Bug Fixes

- [#3051](https://github.com/Azure/autorest.python/pull/3051) Fix sphinx syntax for raising `DeserializationError` in serialization file
- [#3051](https://github.com/Azure/autorest.python/pull/3051) remove useless docstring for models
- [#3051](https://github.com/Azure/autorest.python/pull/3051) Don't throw error directly when emitter crash

### Features

- [#3051](https://github.com/Azure/autorest.python/pull/3051) Report TCGC diagnostics after create SDK context.


## 0.38.4

No changes, version bump only.

## 0.38.3

- [#3038](https://github.com/Azure/autorest.python/pull/3038) Fix crash when value of `--package-pprint-name` contains space

## 0.38.2

### Bug Fixes

- [#3011](https://github.com/Azure/autorest.python/pull/3011) Fix spelling mistakes by running cspell in pipelines
- [#3029](https://github.com/Azure/autorest.python/pull/3029) Fix for scenario that output folder is different with namespace
- [#3029](https://github.com/Azure/autorest.python/pull/3029) Improve XML serialization information in generated models
- [#3025](https://github.com/Azure/autorest.python/pull/3025) Fix sphinx typing for raising documentation
- [#3025](https://github.com/Azure/autorest.python/pull/3025) fix typing for class methods in _serialization.py
- [#3015](https://github.com/Azure/autorest.python/pull/3015) Order keyword-only args overload first in generated operations
- [#3030](https://github.com/Azure/autorest.python/pull/3030) Fix output folder of models when output folder is different with namespace in configuration


## 0.38.1

### Bug Fixes

- [#3007](https://github.com/Azure/autorest.python/pull/3007) Fix import issues for typespec namespace
- [#3007](https://github.com/Azure/autorest.python/pull/3007) Only import helpers for serialization if input body is not binary
- [#3007](https://github.com/Azure/autorest.python/pull/3007) Unify descriptions for credentials in documentation
- [#3007](https://github.com/Azure/autorest.python/pull/3007) Add type annotations for initialized properties in msrest model inits
- [#3007](https://github.com/Azure/autorest.python/pull/3007) Add mypy typing to operation group inits
- [#3007](https://github.com/Azure/autorest.python/pull/3007) Remove Python2 specific datetime logic from internal serialization.


## 0.38.0

### Bug Fixes

- [#3000](https://github.com/Azure/autorest.python/pull/3000) Only add linting disables for a file with too many lines if the file doesn't already disable this linter rule
- [#3000](https://github.com/Azure/autorest.python/pull/3000) Don't automatically overwrite version in `_version.py` file and `setup.py` file if the existing version is newer
- [#3000](https://github.com/Azure/autorest.python/pull/3000) Generate __init__ for internal models to allow for discriminator needs

### Features

- [#2968](https://github.com/Azure/autorest.python/pull/2968) Support typespec namespace


## 0.37.3

### Bug Fixes

- [#2993](https://github.com/Azure/autorest.python/pull/2993) Do not do exception sort if there is no operation groups

### Features

- [#2988](https://github.com/Azure/autorest.python/pull/2988) set flavor to azure if not set


## 0.37.2

### Bug Fixes

- [#2973](https://github.com/Azure/autorest.python/pull/2973) `:code:` in docstring should always be preceded by `\`


## 0.37.1

### Bump dependencies

- [#2965](https://github.com/Azure/autorest.python/pull/2965) Bump `@typespec/*` 0.63.0 and `@azure-tools/*` 0.49.0


## 0.37.0

### Bug Fixes

- [#2959](https://github.com/Azure/autorest.python/pull/2959) Filter out credential that python does not support for now
- [#2959](https://github.com/Azure/autorest.python/pull/2959) Ignore models only used as LRO envelope results because we don't do anything with them

### Features

- [#2959](https://github.com/Azure/autorest.python/pull/2959) Refine exception handling logic and support exception with ranged status code


## 0.36.7

### Bug Fixes

- [#2943](https://github.com/Azure/autorest.python/pull/2943) Fix pylint `useless-object-inheritance` in generated code


## 0.36.6

### Bug Fixes

- [#2935](https://github.com/Azure/autorest.python/pull/2935) Fix crash if no valid client define in typespec file
- [#2935](https://github.com/Azure/autorest.python/pull/2935) Pad special property name in model to avoid conflict


## 0.36.5

### Bump dependencies

- [#2928](https://github.com/Azure/autorest.python/pull/2928) bump `@typespec/http-client-python` to `0.3.10`


## 0.36.4

### Bug Fixes

- [#2918](https://github.com/Azure/autorest.python/pull/2918) Fix quote for string type


## 0.36.3

### Bug Fixes

- [#2908](https://github.com/Azure/autorest.python/pull/2908) Bump http-client-python to fix access for paging operation and lro

### Bump dependencies

- [#2906](https://github.com/Azure/autorest.python/pull/2906) Bump http-client-python 0.3.7


## 0.36.2

### Bump dependencies

- [#2902](https://github.com/Azure/autorest.python/pull/2902) Bump typespec 0.62.0 and http-client-python 0.3.6
- [#2896](https://github.com/Azure/autorest.python/pull/2896) Add devDependency `@azure-tools/cadl-ranch`
- [#2901](https://github.com/Azure/autorest.python/pull/2901) Bump http-client-python to 0.3.5 and tcgc to 0.47.4


## 0.36.1

### Bug Fixes

- [#2876](https://github.com/Azure/autorest.python/pull/2876) - Fix pylint issue for useless suppressions
- [#2870](https://github.com/Azure/autorest.python/pull/2870) Update generated code so there is no need to run the `postprocess` script when customizations are made
- [#2877](https://github.com/Azure/autorest.python/pull/2877) Added ignore comment in `__init__.py` to avoid mypy error
- [#2430](https://github.com/Azure/autorest.python/pull/2430) Avoid change original data when deserialize for polymorphic model


## 0.36.0

### Bump dependencies

- [#2867](https://github.com/Azure/autorest.python/pull/2867) Bump to typespec 0.61.0


## 0.35.1

### Bug Fixes

- [#2864](https://github.com/Azure/autorest.python/pull/2864) Await call to http-client-python onEmit


## 0.35.0

### Bug Fixes

- [#2861](https://github.com/Azure/autorest.python/pull/2861) Fix install issue


## 0.34.0

### Bump dependencies

- [#2851](https://github.com/Azure/autorest.python/pull/2851) bump cadl-ranch
- [#2854](https://github.com/Azure/autorest.python/pull/2854) bump tcgc 0.46.2

### Features

- [#2856](https://github.com/Azure/autorest.python/pull/2856) Depend completely on `@typespec/http-client-python`


## 0.33.0

### Bump dependencies

- [#2845](https://github.com/Azure/autorest.python/pull/2845) bump dependencies
- [#2847](https://github.com/Azure/autorest.python/pull/2847) bump to tcgc 0.46.1


## 0.32.1

### Bug Fixes

- [#2842](https://github.com/Azure/autorest.python/pull/2842) Map `Foundations.Error` -> `core.OdataV4Format`
- [#2839](https://github.com/Azure/autorest.python/pull/2839) Fix wrong word in generated test


## 0.32.0

### Bug Fixes

- [#2835](https://github.com/Azure/autorest.python/pull/2835) Fix lint issue "line-too-long" for docstring in operation
- [#2837](https://github.com/Azure/autorest.python/pull/2837) Fix "line-too-long" for property of model

### Bump dependencies

- [#2834](https://github.com/Azure/autorest.python/pull/2834) Bump typespec 0.60.0


## 0.31.1

### Bug Fixes

- [#2830](https://github.com/Azure/autorest.python/pull/2830) Add pylint disable for "line-too-long" and "too-many-locals"
- [#2831](https://github.com/Azure/autorest.python/pull/2831) Add pylint disable for "unsubscriptable-object"
- [#2829](https://github.com/Azure/autorest.python/pull/2829) Fix bandit error in serialization


## 0.31.0

### Bug Fixes

- [#2814](https://github.com/Azure/autorest.python/pull/2814) Fix pylint errors in serialization.py
- [#2823](https://github.com/Azure/autorest.python/pull/2823) Include link to core models for `HttpResponseError` when it's included as a property in a model

### Features

- [#2815](https://github.com/Azure/autorest.python/pull/2815) Add support for `HttpPart<{@body body: XXX}>` of multipart
- [#2810](https://github.com/Azure/autorest.python/pull/2810) Optimize snake-case naming rule
- [#2806](https://github.com/Azure/autorest.python/pull/2806) dpg model support xml


## 0.30.0

### Features

- [#2775](https://github.com/Azure/autorest.python/pull/2775) support query `explode` and path `allowReserved`, also change the logic of generating spread body parameter
- [#2771](https://github.com/Azure/autorest.python/pull/2771) Support encode int as string
- [#2805](https://github.com/Azure/autorest.python/pull/2805) Add `x-ms-original-file` in generated sample to declare original sample file of typespec


## 0.29.0

### Bug Fixes

- [#2756](https://github.com/Azure/autorest.python/pull/2756) Fix to get right response and exception
- [#2763](https://github.com/Azure/autorest.python/pull/2763) Fix import for "json" and bump cadl-ranch dependency
- [#2784](https://github.com/Azure/autorest.python/pull/2784) Fix sample generation for keyword-only parameters

### Bump dependencies

- [#2773](https://github.com/Azure/autorest.python/pull/2773) Use `@typespec/compiler` `0.59.1` to absorb fix for compiler

### Features

- [#2740](https://github.com/Azure/autorest.python/pull/2740) Support advanced multipart for `@multipartBody`
- [#2750](https://github.com/Azure/autorest.python/pull/2750) optimize performance of dpg model
- [#2774](https://github.com/Azure/autorest.python/pull/2774) Remove samples from docstring of operation


## 0.28.0

### Bug Fixes

- [#2759](https://github.com/Azure/autorest.python/pull/2759) Fix sample generation for lro and paging operation
- [#2758](https://github.com/Azure/autorest.python/pull/2758) Revert client signature `endpoint` to `base_url` to avoid breaking for Mgmt SDK

### Features

- [#2731](https://github.com/Azure/autorest.python/pull/2731) Support generate samples from Typespec


## 0.27.1

### Bug Fixes

- [#2737](https://github.com/Azure/autorest.python/pull/2737) Fix initialize for model which only has discriminator property
- [#2727](https://github.com/Azure/autorest.python/pull/2727) Fix vendor import for mixin operation group when there are multi sub-clients
- [#2729](https://github.com/Azure/autorest.python/pull/2729) Fix import for multipart

### Bump dependencies

- [#2723](https://github.com/Azure/autorest.python/pull/2723) upgrade to tcgc 0.44.2


## 0.27.0

### Bug Fixes

- [#2716](https://github.com/Azure/autorest.python/pull/2716) Fix the logic to judge whether model is output or not

### Features

- [#2706](https://github.com/Azure/autorest.python/pull/2706) Generate API for multi content types of internal operation


## 0.26.0

### Bug Fixes

- [#2684](https://github.com/Azure/autorest.python/pull/2684) don't throw if stream is already read or consumed when we load in the error body
- [#2681](https://github.com/Azure/autorest.python/pull/2681) Fix for construct headers and queries when build request
- [#2695](https://github.com/Azure/autorest.python/pull/2695) always interpret `package-version` as a string
- [#2690](https://github.com/Azure/autorest.python/pull/2690) Fix import error when method name is reserved word in Pyhton

### Bump dependencies

- [#2704](https://github.com/Azure/autorest.python/pull/2704) Bump typespec 0.58.0

### Features

- [#2680](https://github.com/Azure/autorest.python/pull/2680) Expose kwargs `decompress` for API whose response type is binary
- [#2692](https://github.com/Azure/autorest.python/pull/2692) Optimize test generation for multiapi package
- [#2676](https://github.com/Azure/autorest.python/pull/2676) spread object when it is spread in TypeSpec


## 0.25.0

### Bug Fixes

- [#2663](https://github.com/Azure/autorest.python/pull/2663) Support SdkType "uri"

### Features

- [#2588](https://github.com/Azure/autorest.python/pull/2588) add package pygen that both autorest.python and typespec-python will rely on
- [#2677](https://github.com/Azure/autorest.python/pull/2677) Enable test generation for ARM SDK


## 0.24.3

### Bug Fixes

- [#2649](https://github.com/Azure/autorest.python/pull/2649) fix deserialization from vendored msrest code for text plain responses


## 0.24.2

### Bug Fixes

- [#2650](https://github.com/Azure/autorest.python/pull/2650) fix sphinx rendering of json docs by removing comments


## 0.24.1

### Bug Fixes

- [#2645](https://github.com/Azure/autorest.python/pull/2645) add visibility support to discriminator rest field


## 0.24.0

### Bug Fixes

- [#2628](https://github.com/Azure/autorest.python/pull/2628) Fix deserialization error for lro when return type has discriminator and succeed in initial response

### Bump dependencies

- [#2640](https://github.com/Azure/autorest.python/pull/2640) bump typespec version to 0.57


## 0.23.14

No changes, version bump only.

## 0.23.13

### Bug Fixes

- [#2607](https://github.com/Azure/autorest.python/pull/2607) Fix serialization error when setting model property with `azure.core.serialization.NULL`.
- [#2608](https://github.com/Azure/autorest.python/pull/2608) don't lowercase serialized names when building a body from splatted arguments


## 0.23.12

### Bug Fixes

- [#2601](https://github.com/Azure/autorest.python/pull/2601) Remove unused model for paging operation


## 0.23.11

### Bump dependencies

- [#2590](https://github.com/Azure/autorest.python/pull/2590) bump tcgc to 0.41.3


## 2023-05-11 - 0.23.10

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.56.0`      |
| `@typespec/http`                                                        | `0.56.0`      |
| `@typespec/rest`                                                        | `0.56.0`      |
| `@typespec/versioning`                                                  | `0.56.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.42.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.42.2`      |
| `azure-core` dep of generated code                                      | `1.30.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b3`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code                               | `4.6.0`       |

### Bump dependencies

- [#2581](https://github.com/Azure/autorest.python/pull/2581) bump tcgc to 0.42.2


## 2023-04-30 - 0.23.9

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.55.0`      |
| `@typespec/http`                                                        | `0.55.0`      |
| `@typespec/rest`                                                        | `0.55.0`      |
| `@typespec/versioning`                                                  | `0.55.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.41.8`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.41.2`      |
| `azure-core` dep of generated code                                      | `1.30.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b3`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code                               | `4.6.0`       |

**Bug Fixes**

- Escape backslashes in docstrings. Thanks @onlined for this contribution, you rock! #2560

- **Other Changes**

- Bump `@azure-tools/typespec-client-generator-core` version to `0.41.8` #2562

## 2023-04-26 - 0.23.8

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.55.0`      |
| `@typespec/http`                                                        | `0.55.0`      |
| `@typespec/rest`                                                        | `0.55.0`      |
| `@typespec/versioning`                                                  | `0.55.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.41.7`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.41.2`      |
| `azure-core` dep of generated code                                      | `1.30.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b3`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code                               | `4.6.0`       |

**Bug Fixes**

- Use fully qualified name for operation `crossLanguageDefinitionId`s in `api_view_mapping_python.json` #2548

## 2023-04-25 - 0.23.7

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.55.0`      |
| `@typespec/http`                                                        | `0.55.0`      |
| `@typespec/rest`                                                        | `0.55.0`      |
| `@typespec/versioning`                                                  | `0.55.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.41.6`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.41.2`      |
| `azure-core` dep of generated code                                      | `1.30.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b3`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code                               | `4.6.0`       |

**Other Changes**

- Bump `@azure-tools/typespec-client-generator-core` version to `0.41.6` #2545

## 2023-04-25 - 0.23.6

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.55.0`      |
| `@typespec/http`                                                        | `0.55.0`      |
| `@typespec/rest`                                                        | `0.55.0`      |
| `@typespec/versioning`                                                  | `0.55.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.41.5`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.41.2`      |
| `azure-core` dep of generated code                                      | `1.30.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b3`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code                               | `4.6.0`       |

**Other Changes**

- Bump `@azure-tools/typespec-client-generator-core` version to `0.41.5` #2544

## 2023-04-23 - 0.23.5

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.55.0`      |
| `@typespec/http`                                                        | `0.55.0`      |
| `@typespec/rest`                                                        | `0.55.0`      |
| `@typespec/versioning`                                                  | `0.55.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.41.4`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.41.2`      |
| `azure-core` dep of generated code                                      | `1.30.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b3`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code                               | `4.6.0`       |

**Bug Fixes**

- Json serialize input bodies whose default content type is a JSON type with a charset encoding section #2542

## 2023-04-22 - 0.23.4

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.55.0`      |
| `@typespec/http`                                                        | `0.55.0`      |
| `@typespec/rest`                                                        | `0.55.0`      |
| `@typespec/versioning`                                                  | `0.55.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.41.4`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.41.2`      |
| `azure-core` dep of generated code                                      | `1.30.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b3`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code                               | `4.6.0`       |

**Other Changes**

- Bump `@azure-tools/typespec-client-generator-core` to `0.41.4`. By default, we just generate the api surface for the latest API version #2540
- Generate apiview mapping for all azure generations #2504

## 2023-04-12 - 0.23.3

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.55.0`    |
| `@typespec/http`                                                        | `0.55.0`    |
| `@typespec/rest`                                                        | `0.55.0`    |
| `@typespec/versioning`                                                  | `0.55.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.41.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.41.1`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `corehttp` dep of generated code                                        | `1.0.0b3`   |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code                               | `4.6.0`     |

**Other Changes**

- Reformat deserialization files for generated models to allow more insight into deserialization #2512

## 2023-04-09 - 0.23.2

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.55.0`    |
| `@typespec/http`                                                        | `0.55.0`    |
| `@typespec/rest`                                                        | `0.55.0`    |
| `@typespec/versioning`                                                  | `0.55.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.41.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.41.1`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `corehttp` dep of generated code                                        | `1.0.0b3`   |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code                               | `4.6.0`     |

**Other Changes**

- Bump `setuptools` dep to `69.2.0` to deal with issue with Python 12. Thanks @chaen for contributing! #2455

## 2023-04-09 - 0.23.1

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.55.0`    |
| `@typespec/http`                                                        | `0.55.0`    |
| `@typespec/rest`                                                        | `0.55.0`    |
| `@typespec/versioning`                                                  | `0.55.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.41.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.41.1`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `corehttp` dep of generated code                                        | `1.0.0b3`   |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code                               | `4.6.0`     |

**Other Changes**

- Emitter doc changes, thanks @catalinaperalta #2475

## 2023-04-05 - 0.23.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.55.0`    |
| `@typespec/http`                                                        | `0.55.0`    |
| `@typespec/rest`                                                        | `0.55.0`    |
| `@typespec/versioning`                                                  | `0.55.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.41.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.41.1`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `corehttp` dep of generated code                                        | `1.0.0b3`   |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code                               | `4.6.0`     |

**Other Changes**

- Refactor code to use the type ecosystem from "@azure-tools/typespec-client-generator-core" #2476

## 2023-03-22 - 0.22.5

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.54.0`    |
| `@typespec/http`                                                        | `0.54.0`    |
| `@typespec/rest`                                                        | `0.54.0`    |
| `@typespec/versioning`                                                  | `0.54.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.40.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.40.0`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `corehttp` dep of generated code                                        | `1.0.0b3`   |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code                               | `4.6.0`     |

**Other Changes**

- Generate new DPG model instead of msrest model for Mgmt SDK generated from TSP #2461
- `msrest` is not available anymore for `--models-mode` #2464
- Add support for apiview flag `emit-cross-language-definition-file` #2468

## 2023-03-14 - 0.22.4

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.54.0`    |
| `@typespec/http`                                                        | `0.54.0`    |
| `@typespec/rest`                                                        | `0.54.0`    |
| `@typespec/versioning`                                                  | `0.54.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.40.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.40.0`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `corehttp` dep of generated code                                        | `1.0.0b3`   |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code                               | `4.6.0`     |

**Bug Fixes**

- Fix generation failure when payload body is empty #2439

## 2023-03-12 - 0.22.3

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.54.0`    |
| `@typespec/http`                                                        | `0.54.0`    |
| `@typespec/rest`                                                        | `0.54.0`    |
| `@typespec/versioning`                                                  | `0.54.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.40.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.40.0`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `corehttp` dep of generated code                                        | `1.0.0b3`   |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code                               | `4.6.0`     |

**Bug Fixes**

- Upgrade pip when creating venv #2447

## 2023-03-12 - 0.22.2

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.54.0`    |
| `@typespec/http`                                                        | `0.54.0`    |
| `@typespec/rest`                                                        | `0.54.0`    |
| `@typespec/versioning`                                                  | `0.54.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.39.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.40.0`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `corehttp` dep of generated code                                        | `1.0.0b3`   |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code                               | `4.6.0`     |

**Bug Fixes**

- Automatically set `--flavor` to `azure` if we detect `"azure"`in the output directory #2446

## 2023-03-11 - 0.22.1

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.54.0`    |
| `@typespec/http`                                                        | `0.54.0`    |
| `@typespec/rest`                                                        | `0.54.0`    |
| `@typespec/versioning`                                                  | `0.54.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.39.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.40.0`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `corehttp` dep of generated code                                        | `1.0.0b3`   |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code                               | `4.6.0`     |

**Other Changes**

- Change typing annotation and document type of binary response from `bytes` to `Iterator[bytes]` #2427

## 2023-03-06 - 0.22.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.54.0`    |
| `@typespec/http`                                                        | `0.54.0`    |
| `@typespec/rest`                                                        | `0.54.0`    |
| `@typespec/versioning`                                                  | `0.54.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.39.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.40.0`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `corehttp` dep of generated code                                        | `1.0.0b3`   |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code                               | `4.6.0`     |

**New Features**

- Add support for `--flavor` flag. Only special value right now is the `"azure"` flag. When `--flavor=azure` is passed in, we generate an SDK following Microsoft Azure guidelines #2440

**Bug Fixes**

- Fix unused code in `_vendor.py` for multipart #2434

**Other Changes**

- Bump `typespec` dependencies to `0.54.0` and `0.40.0` #2441
- Remove support for `--unbranded` flag #2440

## 2023-03-01 - 0.21.2

| Library                                                                 | Min Version     |
| ----------------------------------------------------------------------- | --------------- |
| `@typespec/compiler`                                                    | `0.53.0`        |
| `@typespec/http`                                                        | `0.53.0`        |
| `@typespec/rest`                                                        | `0.53.0`        |
| `@typespec/versioning`                                                  | `0.53.0`        |
| `@azure-tools/typespec-azure-core`                                      | `0.39.0`        |
| `@azure-tools/typespec-client-generator-core`                           | `0.40.0-dev.21` |
| `azure-core` dep of generated code                                      | `1.30.0`        |
| `corehttp` dep of generated code                                        | `1.0.0b3`       |
| `isodate` dep of generated code                                         | `0.6.1`         |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`         |
| `typing-extensions` dep of generated code                               | `4.6.0`         |

**Bug Fixes**

- Fix empty enum name generation issue #2426

## 2023-02-27 - 0.21.1

| Library                                                                 | Min Version     |
| ----------------------------------------------------------------------- | --------------- |
| `@typespec/compiler`                                                    | `0.53.0`        |
| `@typespec/http`                                                        | `0.53.0`        |
| `@typespec/rest`                                                        | `0.53.0`        |
| `@typespec/versioning`                                                  | `0.53.0`        |
| `@azure-tools/typespec-azure-core`                                      | `0.39.0`        |
| `@azure-tools/typespec-client-generator-core`                           | `0.40.0-dev.14` |
| `azure-core` dep of generated code                                      | `1.30.0`        |
| `corehttp` dep of generated code                                        | `1.0.0b3`       |
| `isodate` dep of generated code                                         | `0.6.1`         |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`         |
| `typing-extensions` dep of generated code                               | `4.6.0`         |

**Bug Fixes**

- Fix reading of some stream responses #2416

## 2023-02-12 - 0.21.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.53.0`    |
| `@typespec/http`                                                        | `0.53.0`    |
| `@typespec/rest`                                                        | `0.53.0`    |
| `@typespec/versioning`                                                  | `0.53.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.39.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.39.0`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `corehttp` dep of generated code                                        | `1.0.0b3`   |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code                               | `4.6.0`     |

**New Features**

- Add support for legacy @flattened decorator #2362
- Generate operations that have multiple binary content types #2401

## 2023-02-09 - 0.20.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.53.0`    |
| `@typespec/http`                                                        | `0.53.0`    |
| `@typespec/rest`                                                        | `0.53.0`    |
| `@typespec/versioning`                                                  | `0.53.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.39.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.39.0`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `corehttp` dep of generated code                                        | `1.0.0b3`   |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code                               | `4.6.0`     |

**New Features**

- Add support for `next-pyright` in the `azure-sdk-for-python` repo (thank you @kristapratico!) #2351
- Improve polymorphic kind detection in returned polymorphic models (thank you @kristapratico!) #2351

**Bug Fixes**

- Fix serialization and deserialization of enum types in models #2399

**Other Changes**

- Update `typespec` dependencies to `0.53.0` and `typespec-azure` depedencies to `0.39.0` #2397

## 2023-02-01 - 0.19.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.52.0`    |
| `@typespec/http`                                                         | `0.52.0`    |
| `@typespec/rest`                                                         | `0.52.0`    |
| `@typespec/versioning`                                                   | `0.52.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.38.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.38.0`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `corehttp` dep of generated code                                         | `1.0.0b3`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Add support for complete tuple input for file types #2380

**Other Changes**

- Bump min dep of `azure-core` to `1.30.0` #2380
- Bump min dep of `corehttp` to `1.0.0b3` #2380

## 2023-01-24 - 0.18.3

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.52.0`    |
| `@typespec/http`                                                         | `0.52.0`    |
| `@typespec/rest`                                                         | `0.52.0`    |
| `@typespec/versioning`                                                   | `0.52.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.38.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.38.0`    |
| `azure-core` dep of generated code                                       | `1.29.5`    |
| `corehttp` dep of generated code                                         | `1.0.0b2`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Update typespec dependencies to `0.52.0` #2382

## 2023-01-19 - 0.18.2

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.51.0`    |
| `@typespec/http`                                                         | `0.51.0`    |
| `@typespec/rest`                                                         | `0.51.0`    |
| `@typespec/versioning`                                                   | `0.51.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.37.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.37.0`    |
| `azure-core` dep of generated code                                       | `1.29.5`    |
| `corehttp` dep of generated code                                         | `1.0.0b2`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix missing tzinfo for `Repeatability-First-Sent` setting #2373

## 2023-01-11 - 0.18.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.51.0`    |
| `@typespec/http`                                                         | `0.51.0`    |
| `@typespec/rest`                                                         | `0.51.0`    |
| `@typespec/versioning`                                                   | `0.51.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.37.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.37.0`    |
| `azure-core` dep of generated code                                       | `1.29.5`    |
| `corehttp` dep of generated code                                         | `1.0.0b2`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix enum value wrap comments #2359

## 2023-01-04 - 0.18.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.51.0`    |
| `@typespec/http`                                                         | `0.51.0`    |
| `@typespec/rest`                                                         | `0.51.0`    |
| `@typespec/versioning`                                                   | `0.51.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.37.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.37.0`    |
| `azure-core` dep of generated code                                       | `1.29.5`    |
| `corehttp` dep of generated code                                         | `1.0.0b2`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Upgrade minimum version of Python from `3.7` to `3.8` #2338

## 2023-12-22 - 0.17.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.51.0`    |
| `@typespec/http`                                                         | `0.51.0`    |
| `@typespec/rest`                                                         | `0.51.0`    |
| `@typespec/versioning`                                                   | `0.51.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.37.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.37.0`    |
| `azure-core` dep of generated code                                       | `1.29.5`    |
| `corehttp` dep of generated code                                         | `1.0.0b2`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Support `multipart/form-data` #2314

**Other Changes**

- import deserialization logic with content type #2320

## 2023-12-11 - 0.16.4

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.50.0`    |
| `@typespec/http`                                                         | `0.50.0`    |
| `@typespec/rest`                                                         | `0.50.0`    |
| `@typespec/versioning`                                                   | `0.50.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.36.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.1`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `corehttp` dep of generated code                                         | `1.0.0b1`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix deserialization error for Lro operation #2302

## 2023-12-07 - 0.16.3

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.50.0`    |
| `@typespec/http`                                                         | `0.50.0`    |
| `@typespec/rest`                                                         | `0.50.0`    |
| `@typespec/versioning`                                                   | `0.50.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.36.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.1`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `corehttp` dep of generated code                                         | `1.0.0b1`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- upgrade dependency about typespec #2299

## 2023-12-06 - 0.16.2

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.50.0`    |
| `@typespec/http`                                                         | `0.50.0`    |
| `@typespec/rest`                                                         | `0.50.0`    |
| `@typespec/versioning`                                                   | `0.50.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.36.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.1`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `corehttp` dep of generated code                                         | `1.0.0b1`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Pin `setuptools` dependency to avoid generation error #2296

## 2023-11-30 - 0.16.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.50.0`    |
| `@typespec/http`                                                         | `0.50.0`    |
| `@typespec/rest`                                                         | `0.50.0`    |
| `@typespec/versioning`                                                   | `0.50.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.36.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.1`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `corehttp` dep of generated code                                         | `1.0.0b1`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix typehints for IO, changing generation from IO -> IO[bytes] #2142

## 2023-11-29 - 0.16.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.50.0`    |
| `@typespec/http`                                                         | `0.50.0`    |
| `@typespec/rest`                                                         | `0.50.0`    |
| `@typespec/versioning`                                                   | `0.50.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.36.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.1`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `corehttp` dep of generated code                                         | `1.0.0b1`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Add decimal type support #2269

**Bug Fixes**

- Fix body parameter type when it is wrapped by template #2275

## 2023-11-20 - 0.15.14

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.50.0`    |
| `@typespec/http`                                                         | `0.50.0`    |
| `@typespec/rest`                                                         | `0.50.0`    |
| `@typespec/versioning`                                                   | `0.50.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.36.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.0`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `corehttp` dep of generated code                                         | `1.0.0b1`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix model when discriminator is enum #2274

## 2023-11-13 - 0.15.13

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.50.0`    |
| `@typespec/http`                                                         | `0.50.0`    |
| `@typespec/rest`                                                         | `0.50.0`    |
| `@typespec/versioning`                                                   | `0.50.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.36.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.0`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `corehttp` dep of generated code                                         | `1.0.0b1`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Hide `stream` in docstring if return type is None #2257

## 2023-11-08 - 0.15.12

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.50.0`    |
| `@typespec/http`                                                         | `0.50.0`    |
| `@typespec/rest`                                                         | `0.50.0`    |
| `@typespec/versioning`                                                   | `0.50.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.36.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.0`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `corehttp` dep of generated code                                         | `1.0.0b1`   |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Bump `tsp` versions to `0.50.0` #2253

## 2023-11-07 - 0.15.11

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.49.0`       |
| `@typespec/http`                                                         | `0.49.0`       |
| `@typespec/rest`                                                         | `0.49.0`       |
| `@typespec/versioning`                                                   | `0.49.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.35.1`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.0-dev.8` |
| `azure-core` dep of generated code                                       | `1.28.0`       |
| `corehttp` dep of generated code                                         | `1.0.0b1`      |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**Bug Fixes**

- HTTP auth prefix case sensitive. #2250
- Remove base model flag of JSON for anonymous model. #2250

**Other Changes**

- Allow users to pass in a folder of template files and arguments to these templates with emitter configs `packaging-files-dir` and `packaging-files-config` #2248

## 2023-11-06 - 0.15.10

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.49.0`       |
| `@typespec/http`                                                         | `0.49.0`       |
| `@typespec/rest`                                                         | `0.49.0`       |
| `@typespec/versioning`                                                   | `0.49.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.35.1`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.0-dev.8` |
| `azure-core` dep of generated code                                       | `1.28.0`       |
| `corehttp` dep of generated code                                         | `1.0.0b1`      |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**Bug Fixes**

- Correctly apply routes when defined on the resource. Fix was to bump min `@azure-tools/typespec-azure-core` version. #2243
- Add dependency on `requests` when using `corehttp`. #2247

## 2023-11-03 - 0.15.9

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.49.0`       |
| `@typespec/http`                                                         | `0.49.0`       |
| `@typespec/rest`                                                         | `0.49.0`       |
| `@typespec/versioning`                                                   | `0.49.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.35.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.0-dev.8` |
| `azure-core` dep of generated code                                       | `1.28.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**Bug Fixes**

- Fix orphan enum usage override #2227

**Other Changes**

- Do not expose `stream` when no response #2234
- Fix docstring for `match_condition` #2232
- Bump min `@azure-tools/typespec-client-generator-core` dep to `0.36.0-dev.8` #2236

## 2023-10-27 - 0.15.8

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.49.0`       |
| `@typespec/http`                                                         | `0.49.0`       |
| `@typespec/rest`                                                         | `0.49.0`       |
| `@typespec/versioning`                                                   | `0.49.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.35.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.0-dev.5` |
| `azure-core` dep of generated code                                       | `1.28.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**Bug Fixes**

- Allow tsp generation to support `models-mode: none` #2220
- Fix duplicate JSON overloads when generating without models #2221
- Fix pytyped in setup.py #2222

## 2023-10-26 - 0.15.7

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.49.0`       |
| `@typespec/http`                                                         | `0.49.0`       |
| `@typespec/rest`                                                         | `0.49.0`       |
| `@typespec/versioning`                                                   | `0.49.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.35.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.0-dev.5` |
| `azure-core` dep of generated code                                       | `1.28.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**Bug Fixes**

- Correctly return response content when response type is bytes #2217

## 2023-10-25 - 0.15.6

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.49.0`       |
| `@typespec/http`                                                         | `0.49.0`       |
| `@typespec/rest`                                                         | `0.49.0`       |
| `@typespec/versioning`                                                   | `0.49.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.35.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.36.0-dev.5` |
| `azure-core` dep of generated code                                       | `1.28.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**Bug Fixes**

- Fix model access regression by bumping `@azure-tools/typespec-client-generator-core` min version #2210

## 2023-10-23 - 0.15.5

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.49.0`    |
| `@typespec/http`                                                         | `0.49.0`    |
| `@typespec/rest`                                                         | `0.49.0`    |
| `@typespec/versioning`                                                   | `0.49.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.35.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.35.0`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Make generated code `pyright-next` compatible. Thanks @kristapratico for the contribution! #2149

**Other Changes**

- Code changes to internal `FileImport` model. Should have no impact on generated code #2204

## 2023-10-18 - 0.15.4

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.49.0`    |
| `@typespec/http`                                                         | `0.49.0`    |
| `@typespec/rest`                                                         | `0.49.0`    |
| `@typespec/versioning`                                                   | `0.49.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.35.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.35.0`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Make generated code mypy-next compliant #2181

## 2023-10-16 - 0.15.3

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.49.0`    |
| `@typespec/http`                                                         | `0.49.0`    |
| `@typespec/rest`                                                         | `0.49.0`    |
| `@typespec/versioning`                                                   | `0.49.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.35.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.35.0`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix list query param serialization. Thank you @tothandras for your contribution! #2156

## 2023-10-12 - 0.15.2

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.49.0`    |
| `@typespec/http`                                                         | `0.49.0`    |
| `@typespec/rest`                                                         | `0.49.0`    |
| `@typespec/versioning`                                                   | `0.49.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.35.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.35.0`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Do not duplicate `begin_` in an LRO operation's name if the service definition already starts with `begin` #2169
- Correctly internalize LRO operation's if their access is listed as internal #2169
- Correctly internalize enums if their access is listed as internal #2171

## 2023-10-07 - 0.15.1

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.48.0`       |
| `@typespec/http`                                                         | `0.48.0`       |
| `@typespec/rest`                                                         | `0.48.0`       |
| `@typespec/versioning`                                                   | `0.48.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.34.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.35.0-dev.2` |
| `azure-core` dep of generated code                                       | `1.28.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**Other Changes**

- United DPG ordering for mgmt plane client parameters #2161

## 2023-10-05 - 0.15.0

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.48.0`       |
| `@typespec/http`                                                         | `0.48.0`       |
| `@typespec/rest`                                                         | `0.48.0`       |
| `@typespec/versioning`                                                   | `0.48.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.34.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.35.0-dev.2` |
| `azure-core` dep of generated code                                       | `1.28.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**New Features**

- Add flag `generate-packaging-files` flag to tspconfig.yaml. On by default. Also no longer able to specify `package-mode` #2157

## 2023-09-27 - 0.14.0

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.48.0`       |
| `@typespec/http`                                                         | `0.48.0`       |
| `@typespec/rest`                                                         | `0.48.0`       |
| `@typespec/versioning`                                                   | `0.48.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.34.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.35.0-dev.2` |
| `azure-core` dep of generated code                                       | `1.28.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**New Features**

- Support `maxpagesize` for DPG # 2140

## 2023-09-26 - 0.13.7

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.48.0`       |
| `@typespec/http`                                                         | `0.48.0`       |
| `@typespec/rest`                                                         | `0.48.0`       |
| `@typespec/versioning`                                                   | `0.48.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.34.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.35.0-dev.2` |
| `azure-core` dep of generated code                                       | `1.28.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**Bug Fixes**

- Fix problem of getting body parameter encode info # 2137

## 2023-09-22 - 0.13.6

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.48.0`       |
| `@typespec/http`                                                         | `0.48.0`       |
| `@typespec/rest`                                                         | `0.48.0`       |
| `@typespec/versioning`                                                   | `0.48.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.34.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.35.0-dev.2` |
| `azure-core` dep of generated code                                       | `1.28.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**Other Changes**

- Adjust signature order of client to make sure no breaking for legacy mgmt code # 2123

## 2023-09-15 - 0.13.5

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.48.0`       |
| `@typespec/http`                                                         | `0.48.0`       |
| `@typespec/rest`                                                         | `0.48.0`       |
| `@typespec/versioning`                                                   | `0.48.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.34.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.35.0-dev.2` |
| `azure-core` dep of generated code                                       | `1.28.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**Other Changes**

- Bump tsp dependencies to 0.48.0

## 2023-09-12 - 0.13.4

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.47.0`    |
| `@typespec/http`                                                         | `0.47.0`    |
| `@typespec/rest`                                                         | `0.47.0`    |
| `@typespec/versioning`                                                   | `0.47.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.33.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.33.0`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Continue adding support for mgmt plane generation by introducing `models-mode` to tsp config #2085

## 2023-08-31 - 0.13.3

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.47.0`    |
| `@typespec/http`                                                         | `0.47.0`    |
| `@typespec/rest`                                                         | `0.47.0`    |
| `@typespec/versioning`                                                   | `0.47.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.33.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.33.0`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other changes**

- Refactoring in preparation of mgmt and TSP #2078

**Bug Fixes**

- Fix datetime in response headers #2083

## 2023-08-21 - 0.13.2

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.46.0`    |
| `@typespec/http`                                                         | `0.46.0`    |
| `@typespec/rest`                                                         | `0.46.0`    |
| `@typespec/versioning`                                                   | `0.46.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.32.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.32.0`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix `_vendor.py` when only `etag` exists #2056
- Fix generation error when `next_link` in undefined #2055

## 2023-08-09 - 0.13.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.46.0`    |
| `@typespec/http`                                                         | `0.46.0`    |
| `@typespec/rest`                                                         | `0.46.0`    |
| `@typespec/versioning`                                                   | `0.46.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.32.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.32.0`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix duplicated discriminator of model #2037

**Other Changes**

- Optimize log for `black` when error happens #2041

## 2023-07-20 - 0.13.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.46.0`    |
| `@typespec/http`                                                         | `0.46.0`    |
| `@typespec/rest`                                                         | `0.46.0`    |
| `@typespec/versioning`                                                   | `0.46.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.32.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.32.0`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Convert method signature `if_match/if_none_match` to `etag/match_condition` #2013

**Bug Fixes**

- Read error into disk to correctly deserialize #2020

## 2023-07-11 - 0.12.0

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.44.0`       |
| `@typespec/http`                                                         | `0.44.0`       |
| `@typespec/rest`                                                         | `0.44.0`       |
| `@typespec/versioning`                                                   | `0.44.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.30.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.31.0-dev.3` |
| `azure-core` dep of generated code                                       | `1.27.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**New Features**

- Change readonly to visibility #1968
- Support global config for `head-as-boolean` #1949

**Bug Fixes**

- Ensure that LRO final results are the final result returned by our generated LRO pollers #1992
- Support `@projectedName` in typespec for query parameter #2006

## 2023-06-12 - 0.11.0

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.44.0`       |
| `@typespec/http`                                                         | `0.44.0`       |
| `@typespec/rest`                                                         | `0.44.0`       |
| `@typespec/versioning`                                                   | `0.44.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.30.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.31.0-dev.3` |
| `azure-core` dep of generated code                                       | `1.27.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**New Features**

- Support repeatable headers #1958

## 2023-06-08 - 0.10.0

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.44.0`       |
| `@typespec/http`                                                         | `0.44.0`       |
| `@typespec/rest`                                                         | `0.44.0`       |
| `@typespec/versioning`                                                   | `0.44.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.30.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.31.0-dev.3` |
| `azure-core` dep of generated code                                       | `1.27.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**New Features**

- Support Http auth #1860

## 2023-06-02 - 0.9.3

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.44.0`       |
| `@typespec/http`                                                         | `0.44.0`       |
| `@typespec/rest`                                                         | `0.44.0`       |
| `@typespec/versioning`                                                   | `0.44.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.30.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.31.0-dev.3` |
| `azure-core` dep of generated code                                       | `1.24.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**Bug Fixes**

- Fix encode on duration scalar #1927

## 2023-05-19 - 0.9.2

| Library                                                                  | Min Version    |
| ------------------------------------------------------------------------ | -------------- |
| `@typespec/compiler`                                                     | `0.44.0`       |
| `@typespec/http`                                                         | `0.44.0`       |
| `@typespec/rest`                                                         | `0.44.0`       |
| `@typespec/versioning`                                                   | `0.44.0`       |
| `@azure-tools/typespec-azure-core`                                       | `0.30.0`       |
| `@azure-tools/typespec-client-generator-core`                            | `0.31.0-dev.3` |
| `azure-core` dep of generated code                                       | `1.24.0`       |
| `isodate` dep of generated code                                          | `0.6.1`        |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`        |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`        |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`        |

**Other Changes**

- Expose the scoped `@internal` decorator in TCGC #1926

## 2023-05-17 - 0.9.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.44.0`    |
| `@typespec/http`                                                         | `0.44.0`    |
| `@typespec/rest`                                                         | `0.44.0`    |
| `@typespec/versioning`                                                   | `0.44.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.30.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.30.0`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Do generate user defined empty model #1921

## 2023-05-16 - 0.9.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.44.0`    |
| `@typespec/http`                                                         | `0.44.0`    |
| `@typespec/rest`                                                         | `0.44.0`    |
| `@typespec/versioning`                                                   | `0.44.0`    |
| `@azure-tools/typespec-azure-core`                                       | `0.30.0`    |
| `@azure-tools/typespec-client-generator-core`                            | `0.30.0`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Add support for `@encode` for durations #1886

**Bug Fixes**

- Optimize logic about camel to snake case in case of the name contains "/" #1907

## 2023-05-15 - 0.8.6

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@typespec/compiler`                                                     | `0.44.0`    |
| `@typespec/http`                                                         | `0.44.0`    |
| `@typespec/rest`                                                         | `0.44.0`    |
| `@typespec/versioning`                                                   | `0.44.0`    |
| `@azure-tools/typespec-azure-core                                        | `0.30.0`    |
| `@azure-tools/typespec-client-generator-core                             | `0.30.0`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix linting errors in vendored model base class #1915

## 2023-05-12 - 0.8.5

**Bug Fixes**

- Add support for ssv, tsv, pipes collection format

**Other Changes**

- Bump TSP dependency to `0.44`

## 2023-04-20 - 0.8.4

**Bug Fixes**

- Do not generate page result model for DPG #1825

## 2023-04-19 - 0.8.3

**Other Changes**

- Bump python generator dependency

## 2023-04-10 - 0.8.2

**Other Changes**

- Bump python generator dependency

## 2023-04-10 - 0.8.1

**Bug Fixes**

- Do not generate model for object, {} and empty model, type them as any

## 2023-03-30 - 0.8.0

**New Features**

- Support typespec @internal for models and operations #1798

**Bug Fixes**

- Don't update dictionary representation of a model if you pass in `None` for a field through keyword #1825

## 2023-03-28 - 0.7.4

**Other Changes**

- Bump `@azure-tools/typespec-azure-core` to `0.28.1` to generate LROs through polling location #1818

## 2023-03-27 - 0.7.3

**Other Changes**

- Bump python generator dependency

## 2023-03-23 - 0.7.2

**Other Changes**

- Switch from `@typespec/versioning`'s `getAddedOnVersion` to `getAddedOnVersions` because it's getting deprecated #1808

## 2023-03-23 - 0.7.1

**Bug Fixes**

- Generate operations with multiple input content types as abstract instead of crashing #1806

## 2023-03-20 - 0.7.0

- Rename package to `@azure-tools/typespec-python` #1800

## 2023-03-06 - 0.6.1

**Bug Fixes**

- Fix vendored xml serialization code #1795

## 2023-03-06 - 0.6.0

**Other Changes**

- Switch to typespec packages from cadl packages #1786

## 2023-03-06 - 0.5.2

**Other Changes**

- Expose `stream` kwarg. Defaults to `False`, when passed in as `True` we stream the response back to users #1777

## 2023-03-06 - 0.5.1

**Other Changes**

- Bump dependency on python generator

## 2023-03-01 - 0.5.0

**New Features**

- Support nullable type generation. #1758
- Generate named union type in \_types.py #1733

## 2023-02-15 - 0.4.25

**Other Changes**

- Support `@collectionFormat` for queries and headers. #1748

## 2023-02-14 - 0.4.24

**Other Changes**

- Support cadl @projectedName on operation/model/property. #1687

## 2023-02-08 - 0.4.23

**Other Changes**

- Bump Cadl dependency to `0.40.0` #1736

## 2023-02-01 - 0.4.22

**Other Changes**

- Update codegen dependency

## 2023-01-27 - 0.4.21

**Other Changes**

- Update codegen dependency

## 2023-01-23 - 0.4.20

**Other Changes**

- Make DPG models type complete #1689

## 2023-01-19 - 0.4.19

**Other Changes**

- Bump CADL dependencies to 0.39.0 #1691

## 2023-01-18 - 0.4.18

**Bug Fixes**

- Fix generation for overloads with splatted out body arguments #1684, #1685

## 2023-01-11 - 0.4.17

**Other Changes**

- Hide header properties in DPG models #1668

## 2023-01-09 - 0.4.16

**Bug Fixes**

- Fix body type for spread model. #1659

## 2023-01-06 - 0.4.15

**Other Changes**

- Support multiple authentication #1626
- Flatten JSONModelType body properties as operation parameters #1623

**Bug Fixes**

- Fix requirement on presence of `cadl-output` folder #1622
- Fix import and \_vendor for subnamespace #1649

## 2022-12-15 - 0.4.14

**Bug Fixes**

- Generate anonymous models and aliases as JSON objects #1619

## 2022-12-08 - 0.4.13

**Other Changes**

- Bump cadl library dependencies #1608

## 2022-12-07 - 0.4.12

**Other Changes**

- Update python generator dependency

## 2022-12-05 - 0.4.11

**Bug Fixes**

- Fix submodel deserialization #1594

**Other Changes**

- Add additional overload for model input #1589

## 2022-11-17 - 0.4.10

**Bug Fixes**

- Fix support for client path parameters #1584
- Remove unnecessary warning logging when deserializing models #1585

## 2022-11-16 - 0.4.9

**Other Changes**

- Support `package-mode` to add package files #1574

## 2022-11-15 - 0.4.8

**Bug Fixes**

- Fix import of enums in client for CADL #1573
- Fix api version property on client #1577
- Skip URL encoding for client path parameters #1578

**Other Changes**

- Do not generate Azure.Core.Foundations Error models #1567

## 2022-11-08 - 0.4.7

**Other Changes**

- Make @key properties readonly #1554
- Do not generate operations with the `@convenienceAPI` decorator as hidden operations #1564

## 2022-11-04 - 0.4.6

**Bug Fixes**

- Bump python generator to 6.2.5

## 2022-11-04 - 0.4.5

**Bug Fixes**

- Don't continue paging empty next links #1557

## 2022-10-31 - 0.4.4

**Bug Fixes**

- Don't force users to manually install `@azure-tools/cadl-dpg` #1549

## 2022-10-26 - 0.4.3

**Bug Fixes**

- Make special `api-version` logic more generic to allow for path parameters #1537

## 2022-10-25 - 0.4.2

**Bug Fixes**

- Add defaults for some config flags #1524
- Allow users to specify a subnamespace for their client in the client name #1529

**Other Changes**

- Generate operations with the `@convenienceAPI` decorator as hidden operations so users can customize them #1533

## 2022-10-19 - 0.4.1

**Bug Fixes**

- Generate names for anonymous models #1519

## 2022-10-19 - 0.4.0

**New Features**

- Add support for multiple clients #1518

## 2022-10-13 - 0.3.1

**Bug Fixes**

- Only generate operation groups from cadl if a group is tagged with `@operationGroup` from `cadl-dpg` #1516

## 2022-10-13 - 0.3.0

**New Features**

- Basic support for LRO #1442

**Other Changes**

- Bump Cadl Dependencies #1509

## 2022-09-26 - 0.2.5

**Bug Fixes**

- Do not `output.yaml` if `noEmit` is specified #1471

## 2022-09-26 - 0.2.4

**Bug Fixes**

- Do not emit SDK if `noEmit` is specified #1470

## 2022-09-23 - 0.2.3

**Other Changes**

- Accept parameters passed in `cadl-project.yaml` #1467

## 2022-09-23 - 0.2.2

**New Features**

- Correctly filter out duplicate models #1466

## 2022-09-22 - 0.2.1

**New Features**

- Bump dependency to ensure DPG models are generated #1463
- Do not fail on description key errors for non-model anonymous body parameters #1463

## 2022-09-21 - 0.2.0

**New Features**

- Generate DPG models as default #1345

## 2022-09-15 - 0.1.0

- Initial Release
