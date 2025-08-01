# Release

## 6.37.2

### Bug Fixes

- [#3154](https://github.com/Azure/autorest.python/pull/3154) fix outputfolder of packaging files for arm sdk
- [#3154](https://github.com/Azure/autorest.python/pull/3154) Ensure necessary typing imports for internal models


## 6.37.1

### Bug Fixes

- [#3135](https://github.com/Azure/autorest.python/pull/3135) Import mixins from operations init file to get patch changes
- [#3135](https://github.com/Azure/autorest.python/pull/3135) Don't hardcode client in sample to first client in list
- [#3134](https://github.com/Azure/autorest.python/pull/3134) Fix regression that ignored patches to mixin operation groups when patched in the `operations` folder


## 6.37.0

### Bump dependencies

- [#3128](https://github.com/Azure/autorest.python/pull/3128) Bump typespec


## 6.36.0

### Features

- Make mixin operations classes private to remove from documentation


## 6.35.5

No changes, version bump only.

## 6.35.4

### Bump dependencies

- [#3108](https://github.com/Azure/autorest.python/pull/3108) Bump dependency TCGC 0.57.2


## 6.35.3

### Bump dependencies

- Regular release

## 6.35.2

No changes, version bump only.

## 6.35.1

### Bump dependencies

- Bump typespec


## 6.35.0

### Features

- [#3089](https://github.com/Azure/autorest.python/pull/3089) generate `_metadata.json` to store info from TCGC

### Bug Fixes

- [#3088](https://github.com/Azure/autorest.python/pull/3088) Fix response type of paging operations from `Iterable` to `ItemPaged`
- [#3090](https://github.com/Azure/autorest.python/pull/3090) Revert for `_utils` only for multiapi


## 6.34.2

### Bug Fixes

- [#3081](https://github.com/Azure/autorest.python/pull/3081) Fix typing for generic `PipelineClient`
- [#3085](https://github.com/Azure/autorest.python/pull/3085) Add support for legacy parameterized next links


## 6.34.1

### Bump dependencies

- Bump to latest typespec version


## 6.34.0

### Bug Fixes

- [#3077](https://github.com/Azure/autorest.python/pull/3077) Move all utils code into a `_utils` folder

### Bump dependencies

- [#3078](https://github.com/Azure/autorest.python/pull/3078) Bump to http-client-python 0.11.0.


## 6.33.0

### Features

- [#3076](https://github.com/Azure/autorest.python/pull/3076) Improve user experience in multi clouds scenario
- [#3073](https://github.com/Azure/autorest.python/pull/3073) add more hooks into setup.py template for users with custom templates


## 6.32.3

### Bug Fixes

- [#3071](https://github.com/Azure/autorest.python/pull/3071) Allow `_` in namespaces

### Other Changes

- [#3065](https://github.com/Azure/autorest.python/pull/3065) Drop support for python3.8

## 6.32.2

No changes, version bump only.

## 6.32.1

### Bug Fixes

- [#3067](https://github.com/Azure/autorest.python/pull/3067) Fix crash when configure `license` in tspconfig.yaml`
- [#3067](https://github.com/Azure/autorest.python/pull/3067) Keep license header for legacy SDK


## 6.32.0

### Features

- [#3062](https://github.com/Azure/autorest.python/pull/3062) Pass authentication flows info into credential policy for unbranded
- [#3061](https://github.com/Azure/autorest.python/pull/3061) support typespec license config


## 6.31.0

### Features

- [#3057](https://github.com/Azure/autorest.python/pull/3057) Always respect namespace from TCGC
- [#3060](https://github.com/Azure/autorest.python/pull/3060) Refine emitter options


## 6.30.0

### Bump dependencies

- [#3058](https://github.com/Azure/autorest.python/pull/3058) Bump `@typespec/*` 0.67

### Features

- [#3050](https://github.com/Azure/autorest.python/pull/3050) Support continuation token for paging


## 6.29.1

No changes, version bump only.

## 6.29.0

### Bug Fixes

- [#3051](https://github.com/Azure/autorest.python/pull/3051) Fix sphinx syntax for raising `DeserializationError` in serialization file
- [#3051](https://github.com/Azure/autorest.python/pull/3051) remove useless docstring for models
- [#3051](https://github.com/Azure/autorest.python/pull/3051) Don't throw error directly when emitter crash

### Features

- [#3051](https://github.com/Azure/autorest.python/pull/3051) Report TCGC diagnostics after create SDK context.


## 6.28.4

No changes, version bump only.

## 6.28.3

No changes, version bump only.


## 6.28.2

### Bug Fixes

- [#3011](https://github.com/Azure/autorest.python/pull/3011) Fix spelling mistakes by running cspell in pipelines
- [#3029](https://github.com/Azure/autorest.python/pull/3029) Fix for scenario that output folder is different with namespace
- [#3029](https://github.com/Azure/autorest.python/pull/3029) Improve XML serialization information in generated models
- [#3025](https://github.com/Azure/autorest.python/pull/3025) Fix sphinx typing for raising documentation
- [#3025](https://github.com/Azure/autorest.python/pull/3025) fix typing for class methods in _serialization.py
- [#3015](https://github.com/Azure/autorest.python/pull/3015) Order keyword-only args overload first in generated operations
- [#3030](https://github.com/Azure/autorest.python/pull/3030) Fix output folder of models when output folder is different with namespace in configuration


## 6.28.1

### Bug Fixes

- [#3007](https://github.com/Azure/autorest.python/pull/3007) Fix import issues for typespec namespace
- [#3007](https://github.com/Azure/autorest.python/pull/3007) Only import helpers for serialization if input body is not binary
- [#3007](https://github.com/Azure/autorest.python/pull/3007) Unify descriptions for credentials in documentation
- [#3007](https://github.com/Azure/autorest.python/pull/3007) Add type annotations for initialized properties in msrest model inits
- [#3007](https://github.com/Azure/autorest.python/pull/3007) Add mypy typing to operation group inits
- [#3007](https://github.com/Azure/autorest.python/pull/3007) Remove Python2 specific datetime logic from internal serialization.


## 6.28.0

### Bug Fixes

- [#3000](https://github.com/Azure/autorest.python/pull/3000) Only add linting disables for a file with too many lines if the file doesn't already disable this linter rule
- [#3000](https://github.com/Azure/autorest.python/pull/3000) Don't automatically overwrite version in `_version.py` file and `setup.py` file if the existing version is newer
- [#3000](https://github.com/Azure/autorest.python/pull/3000) Generate __init__ for internal models to allow for discriminator needs

### Features

- [#2968](https://github.com/Azure/autorest.python/pull/2968) Support typespec namespace


## 6.27.4

### Bug Fixes

- [771c357](https://github.com/Azure/autorest.python/commit/771c35756afc5c69928835aa01576200d43172b0) Fix install for autorest.python


## 6.27.3

### Bug Fixes

- [#2993](https://github.com/Azure/autorest.python/pull/2993) Do not do exception sort if there is no operation groups
- [#2990](https://github.com/Azure/autorest.python/pull/2990) Improve mypy typing for pipeline clients in deprecated multiapi package


## 6.27.2

### Bug Fixes

- [#2973](https://github.com/Azure/autorest.python/pull/2973) `:code:` in docstring should always be preceded by `\`


## 6.27.1

### Bump dependencies

- [#2965](https://github.com/Azure/autorest.python/pull/2965) Bump `@typespec/*` 0.63.0 and `@azure-tools/*` 0.49.0


## 6.27.0

### Features

- [#2959](https://github.com/Azure/autorest.python/pull/2959) Refine exception handling logic and support exception with ranged status code


## 6.26.7

### Bug Fixes

- [#2943](https://github.com/Azure/autorest.python/pull/2943) Fix pylint `useless-object-inheritance` in generated code


## 6.26.6

### Bug Fixes

- [#2935](https://github.com/Azure/autorest.python/pull/2935) Fix crash if no valid client define in typespec file
- [#2935](https://github.com/Azure/autorest.python/pull/2935) Pad special property name in model to avoid conflict


## 6.26.5

### Bump dependencies

- [#2928](https://github.com/Azure/autorest.python/pull/2928) bump `@typespec/http-client-python` to `0.3.10`


## 6.26.4

### Bug Fixes

- [#2918](https://github.com/Azure/autorest.python/pull/2918) Fix quote for string type


## 6.26.3

### Bug Fixes

- [#2908](https://github.com/Azure/autorest.python/pull/2908) Bump http-client-python to fix access for paging operation and lro

### Bump dependencies

- [#2906](https://github.com/Azure/autorest.python/pull/2906) Bump http-client-python 0.3.7


## 6.26.2

### Bug Fixes

- [#2891](https://github.com/Azure/autorest.python/pull/2891) Float dependency for `@typespec/http-client-python`

### Bump dependencies

- [#2902](https://github.com/Azure/autorest.python/pull/2902) Bump typespec 0.62.0 and http-client-python 0.3.6
- [#2901](https://github.com/Azure/autorest.python/pull/2901) Bump http-client-python to 0.3.5 and tcgc to 0.47.4


## 6.26.1

### Bug Fixes

- [#2876](https://github.com/Azure/autorest.python/pull/2876) - Fix pylint issue for useless suppressions
- [#2870](https://github.com/Azure/autorest.python/pull/2870) Update generated code so there is no need to run the `postprocess` script when customizations are made
- [#2877](https://github.com/Azure/autorest.python/pull/2877) Added ignore comment in `__init__.py` to avoid mypy error
- [#2430](https://github.com/Azure/autorest.python/pull/2430) Avoid change original data when deserialize for polymorphic model


## 6.26.0

### Bump dependencies

- [#2867](https://github.com/Azure/autorest.python/pull/2867) Bump http-client-python 0.3.0


## 6.25.0

No changes, version bump only.

## 6.24.0

### Features

- [#2856](https://github.com/Azure/autorest.python/pull/2856) Depend completely on `@typespec/http-client-python`


## 6.23.0

No changes, version bump only.

## 6.22.0

### Bug Fixes

- [#2835](https://github.com/Azure/autorest.python/pull/2835) Fix lint issue "line-too-long" for docstring in operation


## 6.21.1

### Bug Fixes

- [#2831](https://github.com/Azure/autorest.python/pull/2831) Add pylint disable for "unsubscriptable-object"


## 6.21.0

### Bug Fixes

- [#2814](https://github.com/Azure/autorest.python/pull/2814) Fix pylint errors in serialization.py


## 6.20.0

No changes, version bump only.

## 6.19.0

### Bug Fixes

- [#2766](https://github.com/Azure/autorest.python/pull/2766) Fix crash when paging operation return type has parent type

### Features

- [#2774](https://github.com/Azure/autorest.python/pull/2774) Remove samples from docstring of operation


## 6.18.0

### Features

- [#2731](https://github.com/Azure/autorest.python/pull/2731) Support generate samples from Typespec


## 6.17.1

### Bug Fixes

- [#2727](https://github.com/Azure/autorest.python/pull/2727) Fix vendor import for mixin operation group when there are multi sub-clients


## 6.17.0

No changes, version bump only.

## 6.16.0

### Bug Fixes

- [#2684](https://github.com/Azure/autorest.python/pull/2684) don't throw if stream is already read or consumed when we load in the error body
- [#2681](https://github.com/Azure/autorest.python/pull/2681) Fix for construct headers and queries when build request

### Features

- [#2680](https://github.com/Azure/autorest.python/pull/2680) Expose kwargs `decompress` for API whose response type is binary


## 6.15.0

### Features

- [#2588](https://github.com/Azure/autorest.python/pull/2588) add package pygen that both autorest.python and typespec-python will rely on
- [#2677](https://github.com/Azure/autorest.python/pull/2677) Enable test generation for ARM SDK


## 6.14.3

### Bug Fixes

- [#2649](https://github.com/Azure/autorest.python/pull/2649) fix deserialization from vendored msrest code for text plain responses


## 6.14.2

### Bug Fixes

- [#2650](https://github.com/Azure/autorest.python/pull/2650) fix sphinx rendering of json docs by removing comments


## 6.14.1

### Bug Fixes

- [#2645](https://github.com/Azure/autorest.python/pull/2645) add visibility support to discriminator rest field


## 6.14.0

### Bug Fixes

- [#2634](https://github.com/Azure/autorest.python/pull/2634) do not add api version validation decorator to overload function
- [#2628](https://github.com/Azure/autorest.python/pull/2628) Fix deserialization error for lro when return type has discriminator and succeed in initial response
- [#2638](https://github.com/Azure/autorest.python/pull/2638) Do not pad name for enum when generate SDK from Typespec
- [#2633](https://github.com/Azure/autorest.python/pull/2633) generate sdks without operations

### Features

- [#2621](https://github.com/Azure/autorest.python/pull/2621) remove support for deprecated azure.core.pipeline.transport requests and responses


## 6.13.19

### Bug Fixes

- [#2615](https://github.com/Azure/autorest.python/pull/2615) fix casing of multipart legacy properties


## 6.13.18

### Bug Fixes

- [#2607](https://github.com/Azure/autorest.python/pull/2607) Fix serialization error when setting model property with `azure.core.serialization.NULL`.
- [#2608](https://github.com/Azure/autorest.python/pull/2608) don't lowercase serialized names when building a body from splatted arguments


## 2024-05-11 - 6.13.17

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.9.2`     |
| `@autorest/modelerfour`                                                 | `4.24.3`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`     |

### Bug Fixes

- [#2567](https://github.com/Azure/autorest.python/pull/2567) Fix import for multipart/form-data in _vendor.py

## 2024-04-30 - 6.13.16

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.9.2`     |
| `@autorest/modelerfour`                                                 | `4.24.3`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`     |

**Bug Fixes**

- Escape backslashes in docstrings. Thanks @onlined for this contribution, you rock! #2560

## 2024-04-29 - 6.13.15

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.9.2`     |
| `@autorest/modelerfour`                                                 | `4.24.3`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`     |

**Bug Fixes**

- Fix internal model typing  #2517

## 2024-04-23 - 6.13.14

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.9.2`     |
| `@autorest/modelerfour`                                                 | `4.24.3`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`     |

**Bug Fixes**

- Json serialize input bodies whose default content type is a JSON type with a charset encoding section #2542

## 2024-04-22 - 6.13.13

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.9.2`     |
| `@autorest/modelerfour`                                                 | `4.24.3`    |
| `azure-core` dep of generated code                                      | `1.30.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`     |

**Other Changes**

- Generate apiview mapping for all azure generations #2504

## 2024-04-12 - 6.13.12

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Reformat deserialization files for generated models to allow more insight into deserialization #2512

## 2024-04-09 - 6.13.11

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Bump `setuptools` dep to `69.2.0` to deal with issue with Python 12. Thanks @chaen for contributing! #2455

## 2024-04-09 - 6.13.10

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Emitter doc changes, thanks @catalinaperalta #2475

## 2024-04-05 - 6.13.9

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Refactor code to use the type ecosystem from "@azure-tools/typespec-client-generator-core" #2476

## 2024-03-22 - 6.13.8

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix misspelled word in README template #2456

**Other Changes**

- Add support for `emit-cross-language-definition-file` in tsp emitter #2468

## 2024-03-14 - 6.13.7

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix api-vesrion in next link for mgmt multiapi package #2452

## 2024-03-13 - 6.13.6

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Upgrade pip when creating venv #2447

## 2024-03-12 - 6.13.5

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Change typing annotation and document type of binary response from `bytes` to `Iterator[bytes]` #2427

## 2024-03-06 - 6.13.4

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix unused code in `_vendor.py` for multipart #2434

**Other Changes**

- Add support for `--flavor` flag for tsp #2440

## 2024-03-01 - 6.13.3

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix empty enum name generation issue #2426

## 2024-02-27 - 6.13.2

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix reading of some stream responses #2416

## 2024-02-12 - 6.13.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Add support for legacy @flattened decorator in tsp #2362
- Generate operations that have multiple binary content types in tsp #2401

## 2024-02-09 - 6.13.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Add support for `next-pyright` in the `azure-sdk-for-python` repo (thank you @kristapratico!) #2351
- Improve polymorphic kind detection in returned polymorphic models (thank you @kristapratico!) #2351

## 2024-02-01 - 6.12.4

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.30.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Add support for multipart generation from typespec #2380
- Bump minimum dependency of `azure-core` to 1.30.0

## 2023-01-19 - 6.12.3

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.29.5`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix missing tzinfo for `Repeatability-First-Sent` setting #2373

## 2023-01-11 - 6.12.2

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.29.5`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix enum value wrap comments #2359

## 2023-01-09 - 6.12.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.29.5`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- fix logic for judging whether there is non-abstract operations #2340
- fix multipart for sub operation groups #2347

## 2023-01-04 - 6.12.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.29.5`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Upgrade minimum version of Python from `3.7` to `3.8` #2338

## 2023-12-22 - 6.11.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.29.5`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Upgrade dependency of `azure-core` #2314

## 2023-12-11 - 6.11.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Support sub operation groups #2294

## 2023-12-06 - 6.10.2

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Pin `setuptools` dependency to avoid generation error #2296

## 2023-11-30 - 6.10.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix typehints for IO input #2142

## 2023-11-29 - 6.10.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Add decimal type support #2269

## 2023-11-13 - 6.9.9

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Hide `stream` in docstring if return type is `None` #2257

## 2023-11-06 - 6.9.8

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Allow tsp to pass in templating folder #2248

## 2023-11-03 - 6.9.7

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Do not expose `stream` when no response #2234

## 2023-10-27 - 6.9.6

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix duplicate JSON overloads when generating without models #2221
- Fix pytyped in setup.py #2222

## 2023-10-26 - 6.9.5

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Correctly return response content when response type is bytes #2217

## 2023-10-23 - 6.9.4

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Make generated code `pyright-next` compatible. Thanks @kristapratico for the contribution! #2149

**Other Changes**

- Code changes to internal `FileImport` model. Should have no impact on generated code #2204

## 2023-10-18 - 6.9.3

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Make generated code mypy-next compliant #2181

## 2023-10-16 - 6.9.2

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix list query param serialization. Thank you @tothandras for your contribution! #2156

### 2023-10-12 - 6.9.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Do not duplicate `begin_` in an LRO operation's name if the service definition already starts with `begin` #2169

### 2023-10-07 - 6.9.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Maintain old credential and subscription id ordering for azure arm generations for dpg #2161

### 2023-10-05 - 6.8.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Support tsp flags

### 2023-09-27 - 6.8.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Support `maxpagesize` for DPG # 2140

### 2023-09-26 - 6.7.8

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix bytes body with/without encode issue # 2137

### 2023-09-22 - 6.7.7

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Skip quote for etag when it starts with `/W` # 2133
- Remove operation metadata for Mgmt # 2134

### 2023-09-15 - 6.7.6

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix overload for lro paging operation #2114

### 2023-09-12 - 6.7.5

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.28.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Add missing signature `match_condition` when only `if-match` is defined swagger or typespec #2084

### 2023-08-31 - 6.7.4

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.27.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Fix base model generation and add support for `as_dict` on DPG models #2027

### 2023-08-21 - 6.7.3

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.27.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- encode `{}` of url even if skip_quoto is `True` # 2063

### 2023-08-09 - 6.7.2

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.27.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Do not delete `models` and `operations` folder by default for multiapi package #2024
- Optimize log for `black` when error happens #2041

### 2023-07-20 - 6.7.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.27.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Read error into disk to correctly deserialize #2020

### 2023-07-10 - 6.7.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.27.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Support visibility for dpg #1968

**Bug Fixes**

- Fix LRO init operation mypy issue #1992

### 2023-06-12 - 6.6.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.27.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Support repeatable headers #1958

**Bug Fixes**

- Optimize default value for `api_version` for better compatibility of multiapi package #1934

### 2023-06-08 - 6.5.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.27.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Support Http auth #1860

### 2023-06-02 - 6.5.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Support `x-ms-internal` for swagger #1947

**Bug Fixes**

- Fix `x-ms-client-default` for model property #1937
- Added sub-namespace folder when generating samples #1920
- Optimize logic to find related params in example files #1916

### 2023-05-19 - 6.4.15

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix pylint and mypy bugs for internal models #1922

### 2023-05-16 - 6.4.14

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Add support for encode in typespec

### 2023-05-15 - 6.4.13

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix linting errors in vendored model base code #1915

### 2023-05-12 - 6.4.12

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- optimize output folder to avoid sample files are overwritten #1875

### 2023-04-20 - 6.4.11

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Do not generate page result model for DPG #1825

### 2023-04-19 - 6.4.10

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Correctly handle `azure.core.serialization.NULL` #1857

### 2023-04-11 - 6.4.9

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix IO input support for legacy generated code #1842

### 2023-04-10 - 6.4.8

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- set default vaule from `package-name` if `package-pprint-name` is not configured #1841
- Optimize logic about `is_xml` when serialization #1835

### 2023-03-30 - 6.4.7

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Add padded enums for legacy generated code #1820

**Other Changes**

- Add support for generating internal models and operations #1798

### 2023-03-27 - 6.4.6

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Switch typing for `api-version` parameters from a literal to a string #1796
- Fix cases of lro paging where generation was failing on `itemType` #1817
- Fix generation of `version-tolerant: false` with `only-path-and-body-params-positional: true` so client signature is not impacted #1809

### 2023-03-14 - 6.4.5

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix vendored xml serialization code #1795

### 2023-03-14 - 6.4.4

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Code refactoring #1786

### 2023-03-07 - 6.4.3

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Expose `stream` keyword for TypeSpec generations #1777

### 2023-03-06 - 6.4.2

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix import for `by_version` for multiapi package #1774

**Other Changes**

- Modify how we deal with LRO initial operations. No longer clone one past serialization from defined LRO operation #1775

### 2023-03-01 - 6.4.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Make internal pipeline client typing compatible with latest-in-main azure-core #1765

### 2023-02-01 - 6.4.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Add support for `--generate-sample` with multiapi packages #1681

**Bug Fixes**

- Don't fail on generation if `black` can not read a file #1716

### 2023-01-23 - 6.3.2

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- fix casing when generating code to handle parameter grouping #1707

### 2023-01-23 - 6.3.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Make DPG models type complete #1689

### 2023-01-18 - 6.3.0

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Generate M4 externalDocs in Sphinx operation doc #1676

**Bug Fixes**

- Fix JSON template description #1679

### 2023-01-11 - 6.2.16

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**New Features**

- Support `azure.core.serialization.NULL` in msrest model #1669
- Support `azure.core.serialization.NULL` in dpg model serialization #1669

### 2023-01-069 - 6.2.15

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Bump Pyright #1653

### 2023-01-06 - 6.2.14

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Document Enum items with """ pair #1655

**New Features**

- Flatten JSONModelType body properties as operation parameters #1623

### 2022-12-16 - 6.2.13

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix support for multiapi with `--only-path-and-body-params-positional` #1606

### 2022-12-15 - 6.2.12

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Make vendored msrest models type-complete #1618

### 2022-12-07 - 6.2.11

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix LRO response in case the polling and final responses are different body models #1600

### 2022-12-05 - 6.2.10

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix deserialization for model type property #1594

### 2022-11-17 - 6.2.9

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix list type for xml generation with models #1583

### 2022-11-16 - 6.2.8

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Add support for CADL `package-mode` #1574

### 2022-11-15 - 6.2.7

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Clean pyright issues #1547
- Optimize rule about name of generated sample files to avoid too long path #1540

### 2022-11-07 - 6.2.6

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fix clients with enum params #1558

### 2022-11-04 - 6.2.5

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Don't continue paging empty next links #1557
- Fix deserialization of msrest models containing private models #1556

### 2022-11-03 - 6.2.4

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Handle complex string for generated sample #1546
- Allow `api-version` to be a path parameter #1551

### 2022-10-31 - 6.2.3

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Other Changes**

- Install `typing-extensions` instead of `typing_extensions` #1538
- Pad special characters in names #1535

### 2022-10-26 - 6.2.2

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Make special `api-version` logic more generic to allow for path parameters #1537

### 2022-10-25 - 6.2.1

| Library                                                                  | Min Version |
| ------------------------------------------------------------------------ | ----------- |
| `@autorest/core`                                                         | `3.9.2`     |
| `@autorest/modelerfour`                                                  | `4.24.3`    |
| `azure-core` dep of generated code                                       | `1.24.0`    |
| `isodate` dep of generated code                                          | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)               | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code)  | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants) | `4.0.1`     |

**Bug Fixes**

- Fixed lro operation name in auto-generated sample #1521

**Other Changes**

- Type constant properties as Literals #1464
- Deserialize complex schema response for cadl generated operation #1520

### 2022-10-19 - 6.2.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.9.2`     |
| `@autorest/modelerfour`                                                 | `4.24.3`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |

**New Features**

- Add new flag `--generate-sample` to generate samples automatically #1505

### 2022-10-11 - 6.1.11

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.9.2`     |
| `@autorest/modelerfour`                                                 | `4.24.3`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |

**New Features**

- Handle all unrecognized types as "string" #1483
- Make sure to urlencode next link when paging with multiple pages #1504

### 2022-10-10 - 6.1.10

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.4`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |

**Bug Fixes**

- Fix `--postprocess` for windows and embeded packages #1491
- Be able to detect bodies with JSON content types with charsets as JSON requests #1490

### 2022-09-29 - 6.1.9

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.4`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |

**Bug Fixes**

- Can now handle multiple pages when paging in a multiapi SDK #1486
- Fix bug for paging with a DPG SDK with `msrest` models #1487

### 2022-09-23 - 6.1.8

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.4`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |

**Other Changes**

- Cadl configuraiton support #1467

### 2022-09-21 - 6.1.7

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.4`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |

**Bug Fixes**

- Add models for cadl generation

### 2022-09-15 - 6.1.6

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.4`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |

**Bug Fixes**

- Fix `--clear-output-folder` when `--black=true` #1410

### 2022-09-06 - 6.1.5

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.4`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |

**Bug Fixes**

- Fix `api_version` error when there are multi different `api-version`(not multiapi) #1429
- Fix generator raising `KeyError` in corner case when generating an LRO-paging operation #1425

**Other Changes**

- Default `304` errors to throw `azure.core.exception.ResourceNotFoundError`s #1415

### 2022-08-31 - 6.1.4

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.4`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |

**Bug Fixes**

- Fix generation failure for `format: password` #1404
- Fix `content_type` error when paging with body #1407
- Fix excessive warning level logging in vendored `failsafe_deserialize` #1419

**Other Changes**

- Upgrade min dependency for `azure-mgmt-core` to `1.3.2` #1404

### 2022-08-22 - 6.1.3

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.4`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |

**Bug Fixes**

- Fix circular recursion for lropaging #1400

### 2022-08-16 - 6.1.2

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.1`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Bug Fixes**

- Correctly document polymorphic page responses #1389
- Add `__version__` to `__init__.py` for multiapi #1393

### 2022-07-20 - 6.1.1

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.1`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Other Changes**

- Get skeleton for cadl generation released #1358

### 2022-07-20 - 6.1.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.1`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**New Features**

- Add new plugin `MultiClient` and new flag `--multiclientscript` to handle package structure of multi client #1328

**Bug Fixes**

- Fallback unrecognized type as string to avoid a fatal error. #1341
- Fix regression in default namespace for SDKs generated without `--namespace` flag #1354

**Other Changes**

- Generated code no longer supports Python 3.6 #1353
- Order json input and response template entries by whether they are required or not #1335
- Reduce extreme amount of `black` logs when running in `--debug` mode to just log errors

### 2022-06-29 - 6.0.1

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.1`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Bug Fixes**

- Ignore linting error for clients with no credentials #1333

### 2022-06-24 - 6.0.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.1`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Breaking Changes**

- Don't generate paging variables `maxpagesize` for DPG generations. Users should pass in `maxpagesize` to the `by_page` method of their
  pager #1320

### 2022-06-17 - 6.0.0-rc.1

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.1`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Breaking Changes**

- Default to generating DPG SDKs with `--version-tolerant` now defaulting to `true`. For a list of flag default changes, please
  see [here](https://github.com/Azure/autorest.python/issues/1186) #1304
- Only generate Python3 SDKs #1297
- Don't reformat initial query parameters into the next link. However, we do append `api-version` parameters if they are not present in the next link #1297 #1309
- Don't generate operations with more than two body types. SDK authors need to implement this operation themselves #1300

**New Features**

- Automatically format generated code with `black`. To not format, pass in `--black=false` #1304

**Other**

- Remove testing support for `--low-level-client` SDKs #1303

### 2022-06-13 - 5.19.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.1`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `msrest` dep of generated code                                          | `0.7.0`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**New Features**

- Add \_serialization.py for `--client-side-validation=false` generation, and migrate serilization from msrest to \_serialization.py #1236

### 2022-06-09 - 5.18.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.1`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `msrest` dep of generated code                                          | `0.7.0`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Breaking Changes in Version Tolerant**

- No longer allow users to specify `api_version` on the method level #1281
- Make `content_type` param required with no default if streaming with no `application/octet-stream` #1288

**Bug Fixes**

- Fix duplicate params in signature with `--payload-flattening-threshold` #1289
- Fix overloaded request builder signatures #1289
- Improve docstring templates, specifically for polymorphic bodies #1279

### 2022-06-02 - 5.17.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.8.1`     |
| `@autorest/modelerfour`                                                 | `4.23.5`    |
| `azure-core` dep of generated code                                      | `1.23.0`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**New Features**

- Hide `api_version` in doc string for singleapi SDK even if contains multi api versions #1239
- Add overloads for operations with different body types. We now sniff bodies and assign content type based off of body type. #1230
- Add flag `--postprocess`. Run this after doing customizations for full mypy support

**Breaking Changes in Version Tolerant**

- Have stream responses directly return an iterator of bytes, so you don't need to call `.iter_bytes()` on the response object. #1254
- If generating with `--models-mode=msrest` in version tolerant, we hide paging models #1259

**Breaking Changes in Request Builders**

- Request builders for LRO operations have the `_initial` suffix removed from their name #1241
- Request builders from groups with reserved words will now be padded with the word "Operations" instead of "Builders" #1243

**Bug Fixes**

- Make sure `any-object` schemas from swagger are typed with `MutableMapping`s #1243
- Make typing for parameters `Optional` only if `None` is a valid input, not only if it is specified as `optional` in swagger #1244
- Fix for render failure of `README.md` when `--package-mode==dataplane` #1247
- Fix typing for stream responses to iterators of bytes. #1254
- Additional linting support #1265
- Fix Sphinx documentation for raised exception #1264
- Use `api_version` in `_config` as default value for operation function #1268

**Other Changes**

- Update template files for `--package-mode` # 1248

### 2022-04-18 - 5.16.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.23.0`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Breaking Changes in Version Tolerant Generation**

- We no longer generate operations for operations with multipart or urlencoded bodies. SDK writers must implement these operations in their customized patch file. See https://aka.ms/azsdk/python/dpcodegen/python/customize for how to customize generated code #1223

**Bug Fixes**

- Drop package dependency on "@azure-tools/extension", switch to "@autorest/system-requirements" #1229
- Fix `content_type` generation in multiapi SDKs with multiple content types for bodies #1232

### 2022-04-07 - 5.15.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.23.0`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**New Features**

- Add support for security configurations in the swagger. For more information, see https://github.com/Azure/autorest/blob/main/docs/generate/authentication.md #1161
- Add support for handwritten customizations of generated code. For more information, see https://aka.ms/azsdk/python/dpcodegen/python/customize #1153
- Allow `header` and `params` as kwargs in operation and request-build function to hand over REST Header and Query parameters case insensitively #1183
- Typing operation parameters as JSON, Primitives or Any for `--version-tolerant` #1210

**Bug Fixes**

- Make `--version-tolerant` generated code mypy compatible in the `azure-sdk-for-python` repo. Tested only with the `--black` flag #1185
- Remove unnecessary vendored code in the `_vendor` file if the SDK has no operations #1196
- Fix the generation of the root `__init__` files for packages with only models #1195
- Add pylint and mypy support for `--version-tolerant` generations with `--models-mode=msrest` #1202

**Breaking Changes in Version Tolerant Generation**

- Change client filenames to `_client.py` #1206
- Change the models filename from `_models_py3.py` to `_models.py` #1204
- Change the enums filename to `_enums.py` #1204

### 2022-03-08 - 5.14.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.20.1`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**New Features**

- Add flag `--package-mode=mgmtplane|dataplane|<custom package template folder>` to generate necessary files for package #1154

**Bug Fixes**

- Improve operation group documentation to prevent users from initializing operation groups themselves #1179

### 2022-03-03 - 5.13.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.20.1`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Breaking Changes in Version Tolerant Generation**

- We now generate with optional constant parameters as None by defaulting `--default-optional-constants-to-none` to True #1171
- Version tolerant paging does not reformat initial query parameters into the next link #1168

**New Features**

- Add flag `--default-optional-constants-to-none` with which optional constant parameters is default to None #1171
- Add flag `--reformat-next-link`, determines whether we reformat initial query parameters into the next link. Defaults to `True` for the GA generator, forced to `False` for `--version-tolerant`.

**Bug Fixes**

- Add default value consistently for parameters #1164
- Make `content_type` param keyword-only if there are multiple content types #1167

**Other Changes**

- Drop testing support for 2.7 packages #1175

### 2022-02-09 - 5.12.6

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.20.1`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Bug Fixes**

- Remove unused `metadata` value for paging and long running operations with `version-tolerant` generations #1131
- Remove name conflicts with parameters called `url`, `header_parameters`, and `query_parameters` #1143
- Make `--version-tolerant` generated code pylint compatible in the `azure-sdk-for-python` repo when generated with the `--black` flag #1147, #1144, #1130

### 2022-01-26 - 5.12.5

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.20.1`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Bug Fixes**

- Fix usage of `--black` flag outside of repo #1126
- Remove unused `metadata` value for `version-tolerant` generations #1127

### 2022-01-14 - 5.12.4

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.20.1`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Bug Fixes**

- Remove duplicate generation of properties in classes that inherit from multiple classes #1120

### 2022-01-13 - 5.12.3

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.20.1`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Bug Fixes**

- Unify multiapi constant behavior with single API version #1119
- Clean up docstrings by removing descriptions for client constants on methods and request builders #1119

### 2022-01-11 - 5.12.2

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.20.1`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Bug Fixes**

- Fix installation of autorest python package #1118

### 2022-01-10 - 5.12.1

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.20.1`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Bug Fixes**

- Fix support for json merge patch #1117

### 2021-12-06 - 5.12.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.20.1`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Breaking Changes in Version Tolerant Generation**

- Remove metadata property for version tolerant and low level client generations #1090
- Generate SDKs with `--python3-only` defaulting to `True` for version tolerant and low level client #1087

**New Features**

- Generate a `_patch.py` file if one does not exist. These files are used to customize the generated code #1092

**Bug Fixes**

- Can now handle body params with names `json`, `content`, `data`, and `files` #1081
- Improve generated templates for `data` and `files` input body params by adding quotes around the keys #1082
- Using flag `--python3-only` will get you typed sync client and config files #1085
- Pin `mistune` dependency to less than `2.x.x` so autorest can be successfully installed #1106

### 2021-11-05 - 5.11.2

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.20.0`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Bug Fixes**

- Respect no client side validation for low level client generations #1080

### 2021-11-05 - 5.11.1

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.20.0`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Bug Fixes**

- Hide mixin operations for version tolerant generation #1071

### 2021-11-04 - 5.11.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.20.0`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**New Features**

- Add `_patch.py` support for `aio` folder #1070

**Bug Fixes**

- Fix documentation for HEAD calls that perform boolean checks on returned status codes in version tolerant code #1072
- Fix body grouping by content types for binary bodies #1076
- Fix default content type determination #1078

### 2021-11-01 - 5.10.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.19.1`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**New Features**

- Allow users to override constant swagger params with kwarg input #1060

### 2021-10-15 - 5.9.3

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.19.0`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**Bug Fixes**

- Fix generation of form-data inputs #1061

### 2021-10-05 - 5.9.2

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.19.0`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**New Features**

- Updating generated code for `azure-core` release `1.19.0`.

### 2021-09-27 - 5.9.1

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@autorest/core`                                                        | `3.6.2`     |
| `@autorest/modelerfour`                                                 | `4.19.1`    |
| `azure-core` dep of generated code                                      | `1.18.0`    |
| `msrest` dep of generated code                                          | `0.6.21`    |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`     |

**New Features**

- We have added a **provisional** `rest` layer to our generated code. We have also added the following **provisional** flags listed [here](https://github.com/Azure/autorest.python/wiki/Generating-Low-Level-Client#generate-a-low-level-client). #875
- With this new release, we are also dropping support for Python 3.5 + async. #875
- For mgmt plan SDK, default policy changes from `BearerTokenCredentialPolicy` to `ARMChallengeAuthenticationPolicy`.
- We now add tracing by default, the flag `--trace` now defaults to `True` if you have operations.
- Added flag `--python3-only` for users looking to generate SDKs that only support Python 3 #1044

**Bug Fixes**

- Correctly pad operation groups with reserved names with `Operations` #1005
- Fix the generated docstrings for input kwargs of models #1026
- Pass pipeline context to `msrest` in `failsafe_deserialize` so `msrest` has access to the context #1030

### 2021-09-27 - 5.9.0

YANKED

### 2021-07-13 - 5.8.4

min Autorest core version: 3.4.5

min Modelerfour version: 4.19.1

**Bug Fixes**

- Fix case where we have a grouped parameter whose name is a reserved property name #970
- Remove all hosts from global parameters, regardless of how many m4 sends us #972

### 2021-07-06 - 5.8.3

min Autorest core version: 3.3.0

min Modelerfour version: 4.19.1

**Bug Fixes**

- Fix LRO path parameterization when we have a constant path parameter #968

### 2021-06-22 - 5.8.2

min Autorest core version: 3.3.0

min Modelerfour version: 4.19.1

**Bug Fixes**

- We are now more lenient with our checks for the content type parameter #956

### 2021-06-16 - 5.8.1

min Autorest core version: 3.3.0

min Modelerfour version: 4.19.1

**Bug Fixes**

- Fix optional properties with constant schemas. Now, properties that have constant schemas but are optional will not have the hardcoded constant value,
  but will default to its `x-ms-client-default` or `None` #952

### 2021-05-17 - 5.8.0

min Autorest core version: 3.3.0

min Modelerfour version: 4.19.1

**New Features**

- Add support for parameters and properties that can be of type "Anything". #946

### 2021-04-20 - 5.7.0

min Autorest core version: 3.1.0

min Modelerfour version: 4.15.456

**Bug Fixes**

- Fix data plane LRO operations so they poll by default. Bumping minor version because this bug fix will change some default behavior. #936

### 2021-04-07 - 5.6.6

min Autorest core version: 3.1.0

min Modelerfour version: 4.15.456

**Bug Fixes**

- Fix docstrings so they don't get split on hyphens #931

### 2021-04-07 - 5.6.5

min Autorest core version: 3.1.0

min Modelerfour version: 4.15.456

**Bug Fixes**

- Fix regression in multiapi generation for multiapi versions without mixin operations #928

### 2021-03-01 - 5.6.4

min Autorest core version: 3.1.0

min Modelerfour version: 4.15.456

**Bug Fixes**

- Bump `Autorest core` minimum version to be able to deal with indented `python` blocks in config files

### 2021-02-10 - 5.6.3

min Autorest core version: 3.0.6372

min Modelerfour version: 4.15.456

**Bug Fixes**

- Bump `Autorest core` minimum version to [correctly deal with](https://github.com/Azure/autorest/pull/3860) overriding configs. Fixes submodule-specific code in our multiapi client #880

### 2021-02-04 - 5.6.2

Autorest core version: 3.0.6318

Modelerfour version: 4.15.456

**Bug Fixes**

- Bump `Modelerfour` minimum version to [correctly deal with](https://github.com/Azure/autorest.modelerfour/pull/385) parameters specified as `'required': false` in swagger #877

### 2021-01-27 - 5.6.1

Autorest core version: 3.0.6318

Modelerfour version: 4.15.442

**Bug Fixes**

- Instead of throwing a `DeserializationError` in the case of failed error model deserialization, we swallow the error and return the `HttpResponseError` to users.
  WARNING: You need to make sure your `msrest` version is `0.6.21` or above, or a lot of your calls will fail with an `AttributeError` message #870

### 2021-01-15 - 5.6.0

Autorest core version: 3.0.6318

Modelerfour version: 4.15.442

**New Features**

- Add support for [`black`](https://pypi.org/project/black/) formatting of your generated files. Pass flag `--black` when generating to get this behavior. #836

**Bug Fixes**

- Wrap individual enum descriptions #844
- Bump `Modelerfour` minimum version to `4.15.442` to fix [circular reference error](https://github.com/Azure/autorest/issues/3630). Special thanks to @amrElroumy for this PR. #866

### 2020-11-12 - 5.5.0

Autorest core version: 3.0.6318

Modelerfour version: 4.15.421

**New Features**

- Can now take in custom pollers and pagers through directives. This will override the defaults (`LROPoller` and `ItemPaged`, respectively). See [this readme](https://github.com/Azure/autorest.python/tree/main/test/azure/specification/custompollerpager) for the directive to use to override. #821

### 2020-11-11 - 5.4.3

Autorest core version: 3.0.6320

Modelerfour version: 4.15.421

**Bug Fixes**

- Correctly choose schema from response with 200 status code in the case of LRO operations with multiple responses #814
- Fix conflict for model deserialization when operation has input param with name `models` #819

### 2020-11-09 - 5.4.2

Autorest core version: 3.0.6320

Modelerfour version: 4.15.421

**Bug Fixes**

- Set discriminator value in cases where discriminator is readonly #815

### 2020-11-03 - 5.4.1

Autorest core version: 3.0.6318

Modelerfour version: 4.15.421

**Bug Fixes**

- Honor default value for properties if `x-ms-client-default` value is passed #798
- Can now generate services with no operations #801

### 2020-10-19 - 5.4.0

Autorest core version: 3.0.6318

Modelerfour version: 4.15.421

**New Features**

- Add support for `--python.debugger`. With this flag, you can start debugging using VS Code. Make sure to still set up your [debugging configuration](https://github.com/Azure/autorest.python/wiki/Autorest-v3-based-generator-cheatsheet#vscode-debug) #790

**Bug Fixes**

- Correctly handling inheritance of class properties for inheritance chains > 3 levels #795

### 2020-10-06 - 5.3.5

Autorest core version: 3.0.6318

Modelerfour version: 4.15.421

**Bug Fixes**

- Can now correctly poll in the case of parameterized endpoints with relative polling urls #784

### 2020-09-24 - 5.3.4

Autorest core version: 3.0.6318

Modelerfour version: 4.15.421

**Bug Fixes**

- Include `content_type` docstrings for LRO and paging operations in the case of multiple media types #778
- Return response body if its content type is `text/plain` (taken from m4 update - m4 PR #353)

### 2020-09-17 - 5.3.3

Autorest core version: 3.0.6318

Modelerfour version: 4.15.419

**Bug fixes**

- Fix trailing comma issues in metadata.json (unblocks resource multiapi generation) #777

### 2020-09-14 - 5.3.2

Autorest core version: 3.0.6318

Modelerfour version: 4.15.419

**Bug fixes**

- Allow client side validation to be turned off for multiapi mixin operations #775

### 2020-09-14 - 5.3.1

Autorest core version: 3.0.6318

Modelerfour version: 4.15.419

**Bug fixes**

- Min autorest core is now 3.0.6318 to ensure client-side-validation is disabled by default (per track2 guidelines) #772

### 2020-09-11 - 5.3.0

Autorest Core version: 3.0.6306

Modelerfour version: 4.15.419

GA of autorest V5!

**Breaking Changes**

- Raise `ValueError` instead of `NotImplementedError` if API version code doesn't exist #764

### 2020-08-31 - 5.2.0-preview.1

Autorest Core version: 3.0.6306

Modelerfour version: 4.15.410

**Breaking Changes**

- Removed the `_async` suffix from async files #759

**New Features**

- Add mapping of 401 to `ClientAuthenticationError` for default error map #763
- Updated minimum `azure-core` version to 1.8.0 #747
- Updated minimum `msrest` version to 0.6.18 #747
- Support for `multipart/form-data` #746

**Bug fixes**

- Fix "multi" in Swagger (will generate correctly multiple query param now)

### 2020-08-07 - 5.1.0-preview.7

Autorest Core version: 3.0.6302
Modelerfour version: 4.15.400

**New Features**

- Add `azure-mgmt-core` as a dependency in the generated setup.py file #738
- Correct typing for `credential` when default credential policy type is `AzureKeyCredentialPolicy` #744
- Replace instead of extending `credential_scopes` if user has inputted their own #745

### 2020-08-04 - 5.1.0-preview.6

Autorest Core version: 3.0.6287
Modelerfour version: 4.15.378

**New Features**

- Add support for `x-ms-text` XML extension #722
- Allow users to pass the name of the key header for `AzureKeyCredentialPolicy` during generation. To use, pass in
  `AzureKeyCredentialPolicy` with the `--credential-default-policy-type` flag, and pass in the key header name using
  the `--credential-key-header-name` flag #736

**Bug Fixes**

- Fix duplicate type signatures in multiapi async config file #727
- Allowing single quote in regexp #726

### 2020-06-23 - 5.1.0-preview.5

Autorest Core version: 3.0.6287
Modelerfour version: 4.15.378

**Bug Fixes**

- Correctly have default behavior of csv for array query parameters when collection format is not specified in the swagger
  (taken from m4 update - perks PR #118)
- Fix bug when generating parameters with client default value and constant schema #707
- Make operation mixin signatures for multiapi default to default api version #715
- Fix name in setup.py to default to `package-name` if set #721
- Allow different custom base url host templates across API versions #719

### 2020-07-07 - 5.1.0-preview.4

Modelerfour version: 4.15.378

**New Features**

- Enum values are uppercase (with an alias from the lowercase version) #692
- Add `http_logging_policy` setting for config, and users can override the default by passing in the kwarg `http_logging_policy` #698

### 2020-06-24 - 5.1.0-preview.3

Modelerfour version: 4.13.351

**New Features**

- Supports a function that is both LRO and paging #689
- We have added a `--credential-default-policy-type` flag. Its default value is `BearerTokenCredentialPolicy`, but it can also accept
  `AzureKeyCredentialPolicy`. The value passed in will be the default authentication policy in the client's config, so users using the
  generated library will use that auth policy unless they pass in a separate one through kwargs #686
- Added support for a data plane multiapi client #693

**Bug Fixes**

- Fix typing for discriminator values in models, so Python 3.5 can import py3 file for models #691

**Bug Fixes**

- Make enum names all upper case. This fixes issues that arise if the name of an enum is also a method that can be applied to, say, a string.
  For example, if an enum's name is count. Made sure this fix will not break users currently accessing with lower case enum names #692

### 2020-06-08 - 5.1.0-preview.2

Modelerfour version: 4.13.351

**Bug Fixes**

- Fixed "Failed to install or start extension" issue arising when invoking autorest from a tar file, by correcctly calling Python 3. #678
- Generating correct formatting for LRO and paging operation docstrings #652
- Generating correct content and formatting for LRO and paging operations in multiapi mixin #652

### 2020-06-03 - 5.1.0-preview.1

Modelerfour version: 4.13.351

**Disclaimer**

This version requires azure-core 1.6.0 and contains features and bugfixes 5.0.0-preview.8

**Features**

- Refactor async LRO poller with a AsyncLROPoller class + "begin\_" prefix
- Add continuation_token kwargs to LRO methods

**Bug Fixes**

- Corrected generation of the item name of paging response when extracting data #648
- Corrected return type typing annotation for operations that return an optional body #656
- Fixed mypy issue by only setting the generated `deserialized` variable to None if the operation has an optional return type #656
- Fixed generation of pkgutil init files #661
- Have the next operation in a paging call use the HTTP verb GET if the next operation is not defined #664

### 2020-05-22 - 5.0.0-preview.8

Modelerfour version: 4.13.351

**Bug Fixes**

- Corrected ordering of summary and description in generated methods #640
- Have `IOSchema` call super init to get all of the properties shared in `BaseType` #642

### 2020-05-15 - 5.0.0-preview.7

Modelerfour version: 4.13.351

**Bug Fixes**

- Adding `self` as a reserved key word for parameters to avoid "duplicate argument 'self' in function definition" error #630
- Removed `self` as a reserved key word for method and model names #630

### 2020-05-13 - 5.0.0-preview.6

Modelerfour version: 4.13.351

**Bug Fixes**

- No longer assuming that response with body from an LRO call is an ObjectSchema #623
- Checking whether "protocol" entry exists in yaml in name converter to remove erroneous "KeyError: 'protocol'" #628

### 2020-05-08 - 5.0.0-preview.5

Modelerfour version: 4.13.351

**Bug Fixes**

- Users can pass in content types with ';' inside (such as 'text/plain; encoding=UTF-8') #619
- Allowing parameters to be of type `IO` as well #618
- Can now generate without FATAL: bad indentation error (taken from m4 update - perks PR #105)

### 2020-05-06 - 5.0.0-preview.4

Modelerfour version: 4.13.346

**New Features**

- Displaying the default and possible values for content type in the docstring for operations with multiple requests #615

**Bug Fixes**

- Fixing `AsyncTokenCredential` typing import and adding to service client #591
- Can now pass `content_type` and `error_map` kwargs to LRO functions without error #597
- Now making sure to include the content type of exceptions when passing content types to 'Accept' header #602
- `include_apis` in `Metrics` for tables swagger now cased correctly #603
- Corrected spacing after `if cls:` block in operations #606

### 2020-04-23 - 5.0.0-preview.3

Modelerfour version: 4.12.301

**Bug Fixes**

- Fixed sync lro method naming in MultiAPI operation mixins #572

### 2020-04-22 - 5.0.0-preview.2

Modelerfour version: 4.12.301

**New Features**

- User can now pass in credential scopes through kwargs #575
- Default error map always contains a mapping of 404 to `ResourceNotFoundError` and 409 to `ResourceExistsError` #580

**Bug Fixes**

- Not generating async multiapi client if `--no-async` flag is specified #586
- Fixes query parameter handling in paging operations #172
- Fixes losing 404/409 default is user pass a user_map #580

### 2020-04-16 - 5.0.0-preview.1

Modelerfour version: 4.12.301

**Breaking Changes**

- If the user would like to add a patch file, they now must name the file `_patch.py` #573

**New features**

- Support non-ARM polling by default (azure-core 1.4.0)
- Adding multiple inheritance #567
- Accept polling_interval keyword passed to LRO operations #571

**Bug Fixes**

- Fixed some generated typing hints (such as LROPoller) #507

### 2020-04-09 - 5.0.0-dev.20200409.1

Modelerfour version: 4.12.301

**Bug Fixes**

- Separating out typing imports in TYPE_CHECKING block #538
- Overriding a property inherited from a parent if they both have the same name #563

**New Features**

- Client side validation is now disabled by default #558
- We now also generate an async multiapi client when running multiapiscript # 480

### 2020-04-06 - 5.0.0-dev.20200406.1

Modelerfour version: 4.12.294

**New Features**

- Can now directly patch a client by defining a `patch.py` file in the top-level of the module with a `patch_sdk` function #548
- Can now handle `time` formats #551

### 2020-04-03 - 5.0.0-dev.20200403.1

Modelerfour version: 4.12.276

**Bug Fixes**

- Fixes parameter ordering so parameters with default values are all ordered at the end #545
- Fixes `TokenCredential` and `AsyncTokenCredential` sphinx docstring #546

### 2020-04-01 - 5.0.0-dev.20200401.1

Modelerfour version: 4.12.276

**Bug Fixes**

- Now the generic models file and python3 models file have the same behavior in regards to required properties and their default values #532
- Can now specify non-string enums #534
- Fixes `TokenCredential` typing #535

### 2020-03-30 - 5.0.0-dev.20200330.1

Modelerfour version: 4.12.276

**Bug Fixes**

- Fix enum default and required default #532

### 2020-03-26 - 5.0.0-dev.20200326.1

Modelerfour version: 4.12.276

**Bug Fixes**

- Will no longer permit generated enums and models to have the same name #504
- No longer exposing models from operation groups without importing them #486
- Now correctly deserializes error's that have an empty object (AnyType) as a model #516
- Added a list of parameter names to reserved parameter words, so there won't be clashes #525
- If a property's schema is readonly, we will show that property as being readonly (taken from m4 update #234)
- Remove `"azure-"` prefix from user agent name #523
- Correcting issue in generating multiapi with submodule, where generated user agent name included the `#` #505

### 2020-01-17 - 4.0.74

- Declare "self" as reserved keyword

### 2019-06-12 - 4.0.71

- no-async flag to skip async code generation

### 2019-05-21 - 4.0.70

- Beta version of --keep-version-file for ARM generator

### 2019-02-13 - 4.0.67

- All models will now be generated in two files `_models` and `_models_py3`, and paging in a page file
- Breaking changes: Import of models and enums from package must be done from package.models

### 2019-02-11 - 4.0.66

- Fix async cross-link documentation

### 2019-02-08 - 4.0.65

- New version of async generation. Requires msrest 0.6.3 and msrestazure 0.6.0.

  - namespace.XXXXClientAsync is now namespace.aio.XXXClient

- Support now MICROSOFT_MIT_SMALL and MICROSOFT_MIT_SMALL_NO_CODEGEN headers options

### 2019-01-08 - 4.0.64

- New version of async generation. Requires msrest 0.6.3 and msrestazure 0.6.0.

### 2018-12-17 - 4.0.63

- Autorest now generates async code.

**This version requires EXACTLY msrest 0.6.0 to 0.6.2 and is considered deprecated. Do NOT generate with it.**

### 2018-07-09 - 3.0.58

- Fix some complex XML parsing issues. Requires msrest 0.5.2

### 2018-07-05 - 3.0.56

- Differentiate Default and AzureAsyncOperation LRO options
- Fix bug with operation flattenning if operation has a parameter called "foo" and model too disambiguiated as "foo1"

### 2018-06-13 - 3.0.54

This version requires msrestazure 0.4.32

- Add support for LRO options

### 2018-06-13 - 3.0.53

This version requires msrest 0.5.0

- XML support
- Big fix on headers (Accept/Content-Type) to better reflect consumes/produces of Swagger
- Refactoring of "send" to better separate request creation and request sending

### 2018-06-08 - 3.0.52

- Beta version of --keep-version-file

### 2018-05-08 - 3.0.51

- Py3 model files must inherit from Py3 files

### 2018-04-18 - 3.0.50

- Add context manager to SDK client that keeps the same sessions across requests.

### 2018-04-17 - 3.0.49

- Fix some valid discriminator + flatten scenarios #2889

### 2018-04-16 - 3.0.48

- Fix bad comma on py3 models if super class has no attributes

### 2018-03-27 - 3.0.43

- Add documentation to enum #49

### 2018-03-07 - 3.0.41

**Breaking changes**

- Model signatures are now using only keywords-arguments syntax. Every positional arguments are required to be rewritten as keywords-arguments.
  To keep auto-completion in most cases, models are now generated for Python 2 and Python 3. Python 3 uses the "\*" syntax for keyword-only arguments.
- Enum type are now using the "str" mixin (`class AzureEnum(str, Enum)`) to improve experiences when unkown enum are met. This is not a breaking change,
  but documentation about mixin enum and some recommendations should be known:
  https://docs.python.org/3/library/enum.html#others
  At a glance:

  - "is" should not be used at all.
  - "format" will return the string value, where "%s" string formatting will return `NameOfEnum.stringvalue`. Format syntax should be used always.

- New Long Running Operation:

  - Return type changes from msrestazure.azure_operation.AzureOperationPoller to msrest.polling.LROPoller. External API is the same.
  - Return type is now **always** a msrest.polling.LROPoller, whatever the optional parameters.
  - raw=True changes behavior. Instead of not polling and returning the initial call as ClientRawResponse, now we return a LROPoller as well and the final
    resource is returned as a ClientRawResponse.
  - Adding "polling" parameters. Polling=True is the default and poll using ARM algorithm. Polling=False does not poll and return the initial call reponse.
  - Polling accept instances of subclasses of msrest.polling.PollingMethod.
  - `add_done_callback` now does not fail if poller is done, but execute the callback right away.

### 2018-02-16 - 2.1.38

- Externalize Url as a metadata property on operation

### 2018-02-06 - 2.1.35

- Allow "baseUrl" as a custom parameter at the client level.

### 2018-01-04 - 2.1.34

- Fix inheritance and additionalProperties used together

### 2017-12-28 - 2.1.32

- Refactor LRO operations with an external \_XXX_initial call

### 2017-12-22 - 2.1.30

- Add "async", "await" and "mro" as Python reserved keywords.

### 2017-12-13 - 2.1.28

- All Model call super(XX, self).**init**()

### 2017-11-27 - 2.0.25

- Add no-namespace-folders option
- Add basic-setup-py. Change the default behavior to do NOT generate the setup.py.

### 2017-11-22 - 2.0.23

- Add "models" link inside operation groups
- Add help for Python

### 2017-10-19 - 2.0.18

- Fix namespace folders in Vanilla generator

### 2017-10-10 - 2.0.17

- Fix paging description

### 2017-10-10 - 2.0.16

- Improve polymorphic discriminator documentation (#17)
- Add deprecated support (#16)
- Fix invalid headers test (#15)
- Fix invalid python code in some scenario (#14)
- Stop checking str type for client parameter (#12)
- Add client-side-validation to Autorest.Python (#11)

### 2017-09-27 - 2.0.14

- Improve documentation cross-reference (#9)

### 2017-09-26 - 2.0.13

- Remove constraint on array type, if array is used in the URL (#8)
