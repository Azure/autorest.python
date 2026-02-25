# `Http.File` request body compatibility for Python

## Problem

When a TypeSpec operation uses `Http.File` as the request body type, the Python emitter generates an SDK method input type of `IO[bytes] | bytes`.

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
from typing import IO, Union

def upload(self, body: Union[IO[bytes], bytes], **kwargs) -> None:
    ...
```

## Compatibility statement

- Swagger `type: file` callers pass `bytes`.
- `bytes` is still accepted by `Union[IO[bytes], bytes]`.
- Existing `bytes`-based callsites continue to work without code changes.

Therefore, migrating this shape from Swagger to TypeSpec is **non-breaking** for existing Python SDK consumers.
