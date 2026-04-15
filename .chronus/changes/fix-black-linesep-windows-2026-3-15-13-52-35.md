---
changeKind: fix
packages:
  - "@autorest/python"
  - "@azure-tools/typespec-python"
---

Fix mixed line endings in black plugin on Windows by using literal newlines instead of os.linesep