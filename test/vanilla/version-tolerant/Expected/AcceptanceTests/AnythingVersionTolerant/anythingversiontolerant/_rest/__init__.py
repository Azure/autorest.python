# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._request_builders_py3 import build_get_object_request
    from ._request_builders_py3 import build_put_object_request
    from ._request_builders_py3 import build_get_string_request
    from ._request_builders_py3 import build_put_string_request
    from ._request_builders_py3 import build_get_array_request
    from ._request_builders_py3 import build_put_array_request
except (SyntaxError, ImportError):
    from ._request_builders import build_get_object_request  # type: ignore
    from ._request_builders import build_put_object_request  # type: ignore
    from ._request_builders import build_get_string_request  # type: ignore
    from ._request_builders import build_put_string_request  # type: ignore
    from ._request_builders import build_get_array_request  # type: ignore
    from ._request_builders import build_put_array_request  # type: ignore

__all__ = [
    "build_get_object_request",
    "build_put_object_request",
    "build_get_string_request",
    "build_put_string_request",
    "build_get_array_request",
    "build_put_array_request",
]
