# Release

## 2023-03-06 - 0.22.0

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.54.0`      |
| `@typespec/http`                                                        | `0.54.0`      |
| `@typespec/rest`                                                        | `0.54.0`      |
| `@typespec/versioning`                                                  | `0.54.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.39.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.40.0`      |
| `azure-core` dep of generated code                                      | `1.30.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b3`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**New Features**

- Add support for `--flavor` flag. Only valid value right now is the `"azure"` flag. When `--flavor=azure` is passed in, we generate an SDK following Microsoft Azure guidelines #2440

**Bug Fixes**

- Fix unused code in `_vendor.py` for multipart #2434

**Other Changes**

- Bump `typespec` dependencies to `0.54.0` and `0.40.0` #2441


## 2023-03-01 - 0.21.2

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.53.0`      |
| `@typespec/http`                                                        | `0.53.0`      |
| `@typespec/rest`                                                        | `0.53.0`      |
| `@typespec/versioning`                                                  | `0.53.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.39.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.40.0-dev.21`|
| `azure-core` dep of generated code                                      | `1.30.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b3`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix empty enum name generation issue #2426

## 2023-02-27 - 0.21.1

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.53.0`      |
| `@typespec/http`                                                        | `0.53.0`      |
| `@typespec/rest`                                                        | `0.53.0`      |
| `@typespec/versioning`                                                  | `0.53.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.39.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.40.0-dev.14`|
| `azure-core` dep of generated code                                      | `1.30.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b3`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix reading of some stream responses #2416

## 2023-02-12 - 0.21.0

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.53.0`      |
| `@typespec/http`                                                        | `0.53.0`      |
| `@typespec/rest`                                                        | `0.53.0`      |
| `@typespec/versioning`                                                  | `0.53.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.39.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.39.0`      |
| `azure-core` dep of generated code                                      | `1.30.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b3`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**New Features**

- Add support for legacy @flattened decorator #2362
- Generate operations that have multiple binary content types  #2401

## 2023-02-09 - 0.20.0

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.53.0`      |
| `@typespec/http`                                                        | `0.53.0`      |
| `@typespec/rest`                                                        | `0.53.0`      |
| `@typespec/versioning`                                                  | `0.53.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.39.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.39.0`      |
| `azure-core` dep of generated code                                      | `1.30.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b3`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**New Features**

- Add support for `next-pyright` in the `azure-sdk-for-python` repo (thank you @kristapratico!)  #2351
- Improve polymorphic kind detection in returned polymorphic models (thank you @kristapratico!)  #2351

**Bug Fixes**

- Fix serialization and deserialization of enum types in models #2399

**Other Changes**

- Update `typespec` dependencies to `0.53.0` and `typespec-azure` depedencies to `0.39.0` #2397

## 2023-02-01 - 0.19.0

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.52.0`      |
| `@typespec/http`                                                        | `0.52.0`      |
| `@typespec/rest`                                                        | `0.52.0`      |
| `@typespec/versioning`                                                  | `0.52.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.38.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.38.0`      |
| `azure-core` dep of generated code                                      | `1.30.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b3`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**New Features**

- Add support for complete tuple input for file types #2380

**Other Changes**

- Bump min dep of `azure-core` to `1.30.0` #2380
- Bump min dep of `corehttp` to `1.0.0b3` #2380

## 2023-01-24 - 0.18.3

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.52.0`      |
| `@typespec/http`                                                        | `0.52.0`      |
| `@typespec/rest`                                                        | `0.52.0`      |
| `@typespec/versioning`                                                  | `0.52.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.38.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.38.0`      |
| `azure-core` dep of generated code                                      | `1.29.5`      |
| `corehttp` dep of generated code                                        | `1.0.0b2`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Other Changes**

- Update typespec dependencies to `0.52.0` #2382

## 2023-01-19 - 0.18.2

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.51.0`      |
| `@typespec/http`                                                        | `0.51.0`      |
| `@typespec/rest`                                                        | `0.51.0`      |
| `@typespec/versioning`                                                  | `0.51.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.37.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.37.0`      |
| `azure-core` dep of generated code                                      | `1.29.5`      |
| `corehttp` dep of generated code                                        | `1.0.0b2`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix missing tzinfo for `Repeatability-First-Sent` setting #2373

## 2023-01-11 - 0.18.1

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.51.0`      |
| `@typespec/http`                                                        | `0.51.0`      |
| `@typespec/rest`                                                        | `0.51.0`      |
| `@typespec/versioning`                                                  | `0.51.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.37.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.37.0`      |
| `azure-core` dep of generated code                                      | `1.29.5`      |
| `corehttp` dep of generated code                                        | `1.0.0b2`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix enum value wrap comments #2359

## 2023-01-04 - 0.18.0

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.51.0`      |
| `@typespec/http`                                                        | `0.51.0`      |
| `@typespec/rest`                                                        | `0.51.0`      |
| `@typespec/versioning`                                                  | `0.51.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.37.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.37.0`      |
| `azure-core` dep of generated code                                      | `1.29.5`      |
| `corehttp` dep of generated code                                        | `1.0.0b2`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Other Changes**

- Upgrade minimum version of Python from `3.7` to `3.8` #2338

## 2023-12-22 - 0.17.0

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.51.0`      |
| `@typespec/http`                                                        | `0.51.0`      |
| `@typespec/rest`                                                        | `0.51.0`      |
| `@typespec/versioning`                                                  | `0.51.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.37.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.37.0`      |
| `azure-core` dep of generated code                                      | `1.29.5`      |
| `corehttp` dep of generated code                                        | `1.0.0b2`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**New Features**

- Support `multipart/form-data` #2314

**Other Changes**

- import deserialization logic with content type #2320

## 2023-12-11 - 0.16.4

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.50.0`      |
| `@typespec/http`                                                        | `0.50.0`      |
| `@typespec/rest`                                                        | `0.50.0`      |
| `@typespec/versioning`                                                  | `0.50.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.36.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.1`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b1`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix deserialization error for Lro operation #2302

## 2023-12-07 - 0.16.3

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.50.0`      |
| `@typespec/http`                                                        | `0.50.0`      |
| `@typespec/rest`                                                        | `0.50.0`      |
| `@typespec/versioning`                                                  | `0.50.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.36.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.1`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b1`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Other Changes**

- upgrade dependency about typespec #2299

## 2023-12-06 - 0.16.2

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.50.0`      |
| `@typespec/http`                                                        | `0.50.0`      |
| `@typespec/rest`                                                        | `0.50.0`      |
| `@typespec/versioning`                                                  | `0.50.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.36.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.1`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b1`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Pin `setuptools` dependency to avoid generation error #2296

## 2023-11-30 - 0.16.1

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.50.0`      |
| `@typespec/http`                                                        | `0.50.0`      |
| `@typespec/rest`                                                        | `0.50.0`      |
| `@typespec/versioning`                                                  | `0.50.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.36.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.1`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b1`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix typehints for IO, changing generation from IO -> IO[bytes] #2142

## 2023-11-29 - 0.16.0

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.50.0`      |
| `@typespec/http`                                                        | `0.50.0`      |
| `@typespec/rest`                                                        | `0.50.0`      |
| `@typespec/versioning`                                                  | `0.50.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.36.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.1`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b1`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**New Features**

- Add decimal type support  #2269

**Bug Fixes**

- Fix body parameter type when it is wrapped by template #2275

## 2023-11-20 - 0.15.14

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.50.0`      |
| `@typespec/http`                                                        | `0.50.0`      |
| `@typespec/rest`                                                        | `0.50.0`      |
| `@typespec/versioning`                                                  | `0.50.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.36.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.0`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b1`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix model when discriminator is enum #2274

## 2023-11-13 - 0.15.13

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.50.0`      |
| `@typespec/http`                                                        | `0.50.0`      |
| `@typespec/rest`                                                        | `0.50.0`      |
| `@typespec/versioning`                                                  | `0.50.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.36.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.0`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b1`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Other Changes**

- Hide `stream` in docstring if return type is None #2257

## 2023-11-08 - 0.15.12

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.50.0`      |
| `@typespec/http`                                                        | `0.50.0`      |
| `@typespec/rest`                                                        | `0.50.0`      |
| `@typespec/versioning`                                                  | `0.50.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.36.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.0`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b1`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Bump `tsp` versions to `0.50.0` #2253

## 2023-11-07 - 0.15.11

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.49.0`      |
| `@typespec/http`                                                        | `0.49.0`      |
| `@typespec/rest`                                                        | `0.49.0`      |
| `@typespec/versioning`                                                  | `0.49.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.35.1`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.0-dev.8`|
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b1`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- HTTP auth prefix case sensitive. #2250
- Remove base model flag of JSON for anonymous model. #2250

**Other Changes**

- Allow users to pass in a folder of template files and arguments to these templates with emitter configs `packaging-files-dir` and `packaging-files-config` #2248

## 2023-11-06 - 0.15.10

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.49.0`      |
| `@typespec/http`                                                        | `0.49.0`      |
| `@typespec/rest`                                                        | `0.49.0`      |
| `@typespec/versioning`                                                  | `0.49.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.35.1`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.0-dev.8`|
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `corehttp` dep of generated code                                        | `1.0.0b1`     |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Correctly apply routes when defined on the resource. Fix was to bump min `@azure-tools/typespec-azure-core` version. #2243
- Add dependency on `requests` when using `corehttp`. #2247

## 2023-11-03 - 0.15.9

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.49.0`      |
| `@typespec/http`                                                        | `0.49.0`      |
| `@typespec/rest`                                                        | `0.49.0`      |
| `@typespec/versioning`                                                  | `0.49.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.35.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.0-dev.8`|
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix orphan enum usage override #2227

**Other Changes**

- Do not expose `stream` when no response #2234
- Fix docstring for `match_condition` #2232
- Bump min `@azure-tools/typespec-client-generator-core` dep to `0.36.0-dev.8` #2236

## 2023-10-27 - 0.15.8

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.49.0`      |
| `@typespec/http`                                                        | `0.49.0`      |
| `@typespec/rest`                                                        | `0.49.0`      |
| `@typespec/versioning`                                                  | `0.49.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.35.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.0-dev.5`|
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Allow tsp generation to support `models-mode: none` #2220
- Fix duplicate JSON overloads when generating without models #2221
- Fix pytyped in setup.py #2222

## 2023-10-26 - 0.15.7

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.49.0`      |
| `@typespec/http`                                                        | `0.49.0`      |
| `@typespec/rest`                                                        | `0.49.0`      |
| `@typespec/versioning`                                                  | `0.49.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.35.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.0-dev.5`|
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Correctly return response content when response type is bytes #2217

## 2023-10-25 - 0.15.6

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.49.0`      |
| `@typespec/http`                                                        | `0.49.0`      |
| `@typespec/rest`                                                        | `0.49.0`      |
| `@typespec/versioning`                                                  | `0.49.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.35.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.36.0-dev.5`|
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix model access regression by bumping `@azure-tools/typespec-client-generator-core` min version #2210

## 2023-10-23 - 0.15.5

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.49.0`      |
| `@typespec/http`                                                        | `0.49.0`      |
| `@typespec/rest`                                                        | `0.49.0`      |
| `@typespec/versioning`                                                  | `0.49.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.35.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.35.0`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Make generated code `pyright-next` compatible. Thanks @kristapratico for the contribution! #2149

**Other Changes**

- Code changes to internal `FileImport` model. Should have no impact on generated code #2204

## 2023-10-18 - 0.15.4

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.49.0`      |
| `@typespec/http`                                                        | `0.49.0`      |
| `@typespec/rest`                                                        | `0.49.0`      |
| `@typespec/versioning`                                                  | `0.49.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.35.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.35.0`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Make generated code mypy-next compliant #2181

## 2023-10-16 - 0.15.3

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.49.0`      |
| `@typespec/http`                                                        | `0.49.0`      |
| `@typespec/rest`                                                        | `0.49.0`      |
| `@typespec/versioning`                                                  | `0.49.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.35.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.35.0`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix list query param serialization. Thank you @tothandras for your contribution! #2156

## 2023-10-12 - 0.15.2

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.49.0`      |
| `@typespec/http`                                                        | `0.49.0`      |
| `@typespec/rest`                                                        | `0.49.0`      |
| `@typespec/versioning`                                                  | `0.49.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.35.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.35.0`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Do not duplicate `begin_` in an LRO operation's name if the service definition already starts with `begin` #2169
- Correctly internalize LRO operation's if their access is listed as internal #2169
- Correctly internalize enums if their access is listed as internal #2171

## 2023-10-07 - 0.15.1

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.48.0`      |
| `@typespec/http`                                                        | `0.48.0`      |
| `@typespec/rest`                                                        | `0.48.0`      |
| `@typespec/versioning`                                                  | `0.48.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.34.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.35.0-dev.2`|
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Other Changes**

- United DPG ordering for mgmt plane client parameters #2161

## 2023-10-05 - 0.15.0

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.48.0`      |
| `@typespec/http`                                                        | `0.48.0`      |
| `@typespec/rest`                                                        | `0.48.0`      |
| `@typespec/versioning`                                                  | `0.48.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.34.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.35.0-dev.2`|
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**New Features**

- Add flag `generate-packaging-files` flag to tspconfig.yaml. On by default. Also no longer able to specify `package-mode`  #2157

## 2023-09-27 - 0.14.0

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.48.0`      |
| `@typespec/http`                                                        | `0.48.0`      |
| `@typespec/rest`                                                        | `0.48.0`      |
| `@typespec/versioning`                                                  | `0.48.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.34.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.35.0-dev.2`|
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**New Features**

- Support `maxpagesize` for DPG # 2140

## 2023-09-26 - 0.13.7

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.48.0`      |
| `@typespec/http`                                                        | `0.48.0`      |
| `@typespec/rest`                                                        | `0.48.0`      |
| `@typespec/versioning`                                                  | `0.48.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.34.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.35.0-dev.2`|
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix problem of getting body parameter encode info # 2137

## 2023-09-22 - 0.13.6

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.48.0`      |
| `@typespec/http`                                                        | `0.48.0`      |
| `@typespec/rest`                                                        | `0.48.0`      |
| `@typespec/versioning`                                                  | `0.48.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.34.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.35.0-dev.2`|
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Other Changes**

- Adjust signature order of client to make sure no breaking for legacy mgmt code # 2123

## 2023-09-15 - 0.13.5

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.48.0`      |
| `@typespec/http`                                                        | `0.48.0`      |
| `@typespec/rest`                                                        | `0.48.0`      |
| `@typespec/versioning`                                                  | `0.48.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.34.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.35.0-dev.2`|
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Other Changes**

- Bump tsp dependencies to 0.48.0

## 2023-09-12 - 0.13.4

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.47.0`      |
| `@typespec/http`                                                        | `0.47.0`      |
| `@typespec/rest`                                                        | `0.47.0`      |
| `@typespec/versioning`                                                  | `0.47.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.33.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.33.0`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Other Changes**

- Continue adding support for mgmt plane generation by introducing `models-mode` to tsp config #2085

## 2023-08-31 - 0.13.3

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.47.0`      |
| `@typespec/http`                                                        | `0.47.0`      |
| `@typespec/rest`                                                        | `0.47.0`      |
| `@typespec/versioning`                                                  | `0.47.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.33.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.33.0`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Other changes**

- Refactoring in preparation of mgmt and TSP #2078

**Bug Fixes**

- Fix datetime in response headers  #2083

## 2023-08-21 - 0.13.2

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.46.0`      |
| `@typespec/http`                                                        | `0.46.0`      |
| `@typespec/rest`                                                        | `0.46.0`      |
| `@typespec/versioning`                                                  | `0.46.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.32.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.32.0`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix `_vendor.py` when only `etag` exists  #2056
- Fix generation error when `next_link` in undefined  #2055

## 2023-08-09 - 0.13.1

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.46.0`      |
| `@typespec/http`                                                        | `0.46.0`      |
| `@typespec/rest`                                                        | `0.46.0`      |
| `@typespec/versioning`                                                  | `0.46.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.32.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.32.0`      |
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix duplicated discriminator of model #2037

**Other Changes**

- Optimize log for `black` when error happens  #2041

## 2023-07-20 - 0.13.0

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.46.0`      |
| `@typespec/http`                                                        | `0.46.0`      |
| `@typespec/rest`                                                        | `0.46.0`      |
| `@typespec/versioning`                                                  | `0.46.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.32.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.32.0`|
| `azure-core` dep of generated code                                      | `1.28.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**New Features**

- Convert method signature `if_match/if_none_match` to `etag/match_condition` #2013

**Bug Fixes**

- Read error into disk to correctly deserialize #2020

## 2023-07-11 - 0.12.0

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.44.0`      |
| `@typespec/http`                                                        | `0.44.0`      |
| `@typespec/rest`                                                        | `0.44.0`      |
| `@typespec/versioning`                                                  | `0.44.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.30.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.31.0-dev.3`|
| `azure-core` dep of generated code                                      | `1.27.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**New Features**

- Change readonly to visibility #1968
- Support global config for `head-as-boolean` #1949

**Bug Fixes**

- Ensure that LRO final results are the final result returned by our generated LRO pollers #1992
- Support `@projectedName` in typespec for query parameter #2006

## 2023-06-12 - 0.11.0

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.44.0`      |
| `@typespec/http`                                                        | `0.44.0`      |
| `@typespec/rest`                                                        | `0.44.0`      |
| `@typespec/versioning`                                                  | `0.44.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.30.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.31.0-dev.3`|
| `azure-core` dep of generated code                                      | `1.27.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**New Features**

- Support repeatable headers #1958

## 2023-06-08 - 0.10.0

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.44.0`      |
| `@typespec/http`                                                        | `0.44.0`      |
| `@typespec/rest`                                                        | `0.44.0`      |
| `@typespec/versioning`                                                  | `0.44.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.30.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.31.0-dev.3`|
| `azure-core` dep of generated code                                      | `1.27.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**New Features**

- Support Http auth #1860

## 2023-06-02 - 0.9.3

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.44.0`      |
| `@typespec/http`                                                        | `0.44.0`      |
| `@typespec/rest`                                                        | `0.44.0`      |
| `@typespec/versioning`                                                  | `0.44.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.30.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.31.0-dev.3`|
| `azure-core` dep of generated code                                      | `1.24.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Bug Fixes**

- Fix encode on duration scalar #1927

## 2023-05-19 - 0.9.2

| Library                                                                 | Min Version   |
| ----------------------------------------------------------------------- | ------------- |
| `@typespec/compiler`                                                    | `0.44.0`      |
| `@typespec/http`                                                        | `0.44.0`      |
| `@typespec/rest`                                                        | `0.44.0`      |
| `@typespec/versioning`                                                  | `0.44.0`      |
| `@azure-tools/typespec-azure-core`                                      | `0.30.0`      |
| `@azure-tools/typespec-client-generator-core`                           | `0.31.0-dev.3`|
| `azure-core` dep of generated code                                      | `1.24.0`      |
| `isodate` dep of generated code                                         | `0.6.1`       |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`       |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`       |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`       |

**Other Changes**

- Expose the scoped `@internal` decorator in TCGC #1926

## 2023-05-17 - 0.9.1

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.44.0`    |
| `@typespec/http`                                                        | `0.44.0`    |
| `@typespec/rest`                                                        | `0.44.0`    |
| `@typespec/versioning`                                                  | `0.44.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.30.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.30.0`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`     |


**Bug Fixes**

- Do generate user defined empty model #1921


## 2023-05-16 - 0.9.0

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.44.0`    |
| `@typespec/http`                                                        | `0.44.0`    |
| `@typespec/rest`                                                        | `0.44.0`    |
| `@typespec/versioning`                                                  | `0.44.0`    |
| `@azure-tools/typespec-azure-core`                                      | `0.30.0`    |
| `@azure-tools/typespec-client-generator-core`                           | `0.30.0`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`     |

**New Features**

- Add support for `@encode` for durations #1886

**Bug Fixes**

- Optimize logic about camel to snake case in case of the name contains "/"  #1907


## 2023-05-15 - 0.8.6

| Library                                                                 | Min Version |
| ----------------------------------------------------------------------- | ----------- |
| `@typespec/compiler`                                                    | `0.44.0`    |
| `@typespec/http`                                                        | `0.44.0`    |
| `@typespec/rest`                                                        | `0.44.0`    |
| `@typespec/versioning`                                                  | `0.44.0`    |
| `@azure-tools/typespec-azure-core                                       | `0.30.0`    |
| `@azure-tools/typespec-client-generator-core                            | `0.30.0`    |
| `azure-core` dep of generated code                                      | `1.24.0`    |
| `isodate` dep of generated code                                         | `0.6.1`     |
| `msrest` dep of generated code (If generating legacy code)              | `0.7.1`     |
| `azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.2`     |
| `typing-extensions` dep of generated code (If generating with constants)| `4.0.1`     |

**Bug Fixes**

- Fix linting errors in vendored model base class  #1915

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

- Support typespec @internal for models and operations  #1798

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

- Support nullable type generation.  #1758
- Generate named union type in _types.py  #1733

## 2023-02-15 - 0.4.25

**Other Changes**

- Support `@collectionFormat` for queries and headers.  #1748

## 2023-02-14 - 0.4.24

**Other Changes**

- Support cadl @projectedName on operation/model/property.  #1687

## 2023-02-08 - 0.4.23

**Other Changes**

- Bump Cadl dependency to `0.40.0`  #1736

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

- Support multiple authentication  #1626
- Flatten JSONModelType body properties as operation parameters #1623

**Bug Fixes**

- Fix requirement on presence of `cadl-output` folder #1622
- Fix import and _vendor for subnamespace  #1649

## 2022-12-15 - 0.4.14

**Bug Fixes**

- Generate anonymous models and aliases as JSON objects  #1619

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

- Support `package-mode` to add package files  #1574

## 2022-11-15 - 0.4.8

**Bug Fixes**

- Fix import of enums in client for CADL #1573
- Fix api version property on client #1577
- Skip URL encoding for client path parameters #1578

**Other Changes**

- Do not generate Azure.Core.Foundations Error models #1567

## 2022-11-08 - 0.4.7

**Other Changes**

- Make @key properties readonly  #1554
- Do not generate operations with the `@convenienceAPI` decorator as hidden operations #1564

## 2022-11-04 - 0.4.6

**Bug Fixes**

- Bump python generator to 6.2.5

## 2022-11-04 - 0.4.5

**Bug Fixes**

- Don't continue paging empty next links  #1557

## 2022-10-31 - 0.4.4

**Bug Fixes**

- Don't force users to manually install `@azure-tools/cadl-dpg`  #1549

## 2022-10-26 - 0.4.3

**Bug Fixes**

- Make special `api-version` logic more generic to allow for path parameters  #1537


## 2022-10-25 - 0.4.2

**Bug Fixes**

- Add defaults for some config flags  #1524
- Allow users to specify a subnamespace for their client in the client name  #1529

**Other Changes**

- Generate operations with the `@convenienceAPI` decorator as hidden operations so users can customize them #1533

## 2022-10-19 - 0.4.1

**Bug Fixes**

- Generate names for anonymous models  #1519

## 2022-10-19 - 0.4.0

**New Features**

- Add support for multiple clients  #1518

## 2022-10-13 - 0.3.1

**Bug Fixes**

- Only generate operation groups from cadl if a group is tagged with `@operationGroup` from `cadl-dpg`  #1516

## 2022-10-13 - 0.3.0

**New Features**

- Basic support for LRO  #1442

**Other Changes**

- Bump Cadl Dependencies  #1509

## 2022-09-26 - 0.2.5

**Bug Fixes**

- Do not `output.yaml` if `noEmit` is specified  #1471

## 2022-09-26 - 0.2.4

**Bug Fixes**

- Do not emit SDK if `noEmit` is specified  #1470

## 2022-09-23 - 0.2.3

**Other Changes**

- Accept parameters passed in `cadl-project.yaml`  #1467

## 2022-09-23 - 0.2.2

**New Features**

- Correctly filter out duplicate models  #1466

## 2022-09-22 - 0.2.1

**New Features**

- Bump dependency to ensure DPG models are generated  #1463
- Do not fail on description key errors for non-model anonymous body parameters  #1463

## 2022-09-21 - 0.2.0

**New Features**

- Generate DPG models as default  #1345

## 2022-09-15 - 0.1.0

- Initial Release
