# `Http.File` Compatibility for Python

## Overview

TypeSpec `Http.File` is emitted differently depending on whether it appears as a request body or a response body:

- **Request body**: emits `IO | bytes` (widens legacy `bytes`-only signature)
- **Response body**: emits `bytes` (identical to legacy signature)

Both cases preserve full backward compatibility with Swagger `type: file`.

## Request Body

### TypeSpec Definition

```typespec
import "@typespec/http";

using TypeSpec.Http;

@route("/files")
namespace Files;

@post
op upload(@body body: Http.File): void;
```

### Generated Python SDK

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

### Backward Compatibility

Swagger `type: file`(e.g. [`operationId: "WebApps_GetWebSiteContainerLogs"`](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/web/resource-manager/Microsoft.Web/AppService/stable/2024-11-01/WebApps.json#L2675)) generated `bytes`-only input (e.g. [`WebAppsOperations.get_web_site_container_logs(...)`](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/appservice/azure-mgmt-web/azure/mgmt/web/operations/_web_apps_operations.py#L22070)). After migrating to TypeSpec, the input type widens to `IO | bytes`. Since `bytes` is still accepted, existing callers require **no code changes**, making this migration **non-breaking**.

## Response Body

### TypeSpec Definition

```typespec
@route("/files")
namespace Files;

@get
op download(): Http.File;
```

### Generated Python SDK

```python
def download(self, **kwargs) -> bytes:
    ...
```

### Backward Compatibility

Swagger `type: file` responses also generated `bytes`. The TypeSpec `Http.File` response emits the same `bytes` return type, so existing callers are **completely unaffected**.

