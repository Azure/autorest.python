---
changeKind: fix
packages:
  - "@autorest/python"
  - "@azure-tools/typespec-python"
---

Fix TypeSpec `numeric` scalar type being emitted as `int` in Python; it is now emitted as `float`.
