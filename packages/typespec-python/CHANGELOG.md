# Release

## 2023-06-XX - 0.12.0

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
- Support global config for `skip-special-headers` #1973

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
