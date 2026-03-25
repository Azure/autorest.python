---
changeKind: fix
packages:
  - "@autorest/python"
  - "@azure-tools/typespec-python"
---

Remove `None` from "Known values" in `api_version` parameter docstring since the parameter is typed as `str` and `None` is not a valid API version value.
