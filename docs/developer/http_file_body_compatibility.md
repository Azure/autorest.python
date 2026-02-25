# Python SDK design for `Http.File` when it appears in non-multipart request body and response body

## Overview

TypeSpec `Http.File` is emitted differently depending on whether it appears as a non-multipart request body or a response body:

- **Request body**: emits `IO | bytes` (new pattern; Swagger `type: file` was never used in non-multipart request bodies)
- **Response body**: emits `bytes` (identical to legacy Swagger `type: file` signature)

Since `type: file` was not used in non-multipart request bodies, the request body change is purely additive. The response body remains fully backward compatible.

## Request Body

### TypeSpec Definition

```typespec
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

## Response Body

### TypeSpec Definition

```typespec
@get
op download(): Http.File;
```

### Generated Python SDK

```python
def download(self, **kwargs) -> bytes:
    ...
```

### Backward Compatibility

Swagger `type: file` (e.g. [`operationId: "WebApps_GetWebSiteContainerLogs"`](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/web/resource-manager/Microsoft.Web/AppService/stable/2024-11-01/WebApps.json#L2675)) responses also generated `bytes` (e.g. [`WebAppsOperations.get_web_site_container_logs(...)`](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/appservice/azure-mgmt-web/azure/mgmt/web/operations/_web_apps_operations.py#L22070)). The TypeSpec `Http.File` response emits the same `bytes` return type, so existing callers are **completely unaffected**.

## References

- [TypeSpec `Http.File` documentation](https://typespec.io/docs/libraries/http/files/#using-httpfile-in-operations) — explains how `Http.File` works in operations (uploading, downloading, multipart payloads, custom file models, and when a model is effectively a `File`).
- [Spector test cases for `Http.File`](https://github.com/microsoft/typespec/blob/main/packages/http-specs/specs/type/file/main.tsp) — conformance tests covering file upload/download with specific, JSON, multiple, and default content types.

