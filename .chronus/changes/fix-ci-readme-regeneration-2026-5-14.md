---
changeKind: internal
packages:
  - "@autorest/python"
  - "@azure-tools/typespec-python"
---

Fix CI on main by deleting README.md files during baseline reset so regeneration recreates them; extend unit test to assert README.md exists for every generated SDK package (azure & unbranded).
