# `Http.File` request body compatibility for Python

## Overview

When a TypeSpec operation uses `Http.File` as the request body type, the Python emitter generates an SDK method input type of `IO | bytes`.

For migrated Swagger APIs, this must remain compatible with previous SDKs where Swagger `type: file` was represented as `bytes`.

## Compact example

TypeSpec:

```typespec
import "@typespec/http";

using TypeSpec.Http;

@route("/files")
namespace Files;

@post
op upload(@body body: Http.File): void;
```

Python SDK (generated shape):

```python
from typing import IO, overload

@overload
def upload(self, body: IO, **kwargs) -> None:
    ...

@overload
def upload(self, body: bytes, **kwargs) -> None:
    ...

def upload(self, body: IO | bytes, **kwargs) -> None:
    ...
```

## Compatibility statement

- Swagger `type: file` callers pass `bytes`.
- `bytes` is still accepted by `IO | bytes`.
- Existing `bytes`-based callsites continue to work without code changes.

Therefore, migrating this shape from Swagger to TypeSpec is **non-breaking** for existing Python SDK consumers.
