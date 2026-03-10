---
changeKind: fix
packages:
  - "@autorest/python"
  - "@azure-tools/typespec-python"
---

Remove includeRootSlash client option logic, which should be handled at the TypeSpec core level
