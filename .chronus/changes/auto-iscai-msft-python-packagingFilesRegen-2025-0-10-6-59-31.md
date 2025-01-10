---
changeKind: fix
packages:
  - "@autorest/python"
  - "@azure-tools/typespec-python"
---

Don't automatically overwrite version in `_version.py` file and `setup.py` file if the existing version is newer