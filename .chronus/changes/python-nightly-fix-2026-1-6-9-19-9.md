---
changeKind: fix
packages:
  - "@autorest/python"
  - "@azure-tools/typespec-python"
---

Fall back "Http.File" to "bytes" to avoid generation failure