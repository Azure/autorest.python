# Release History

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
