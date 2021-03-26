# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._request_builders_py3 import build_bool_get_true_request
    from ._request_builders_py3 import build_bool_put_true_request
    from ._request_builders_py3 import build_bool_get_false_request
    from ._request_builders_py3 import build_bool_put_false_request
    from ._request_builders_py3 import build_bool_get_null_request
    from ._request_builders_py3 import build_bool_get_invalid_request
except (SyntaxError, ImportError):
    from ._request_builders import build_bool_get_true_request  # type: ignore
    from ._request_builders import build_bool_put_true_request  # type: ignore
    from ._request_builders import build_bool_get_false_request  # type: ignore
    from ._request_builders import build_bool_put_false_request  # type: ignore
    from ._request_builders import build_bool_get_null_request  # type: ignore
    from ._request_builders import build_bool_get_invalid_request  # type: ignore

__all__ = [
    "build_bool_get_true_request",
    "build_bool_put_true_request",
    "build_bool_get_false_request",
    "build_bool_put_false_request",
    "build_bool_get_null_request",
    "build_bool_get_invalid_request",
]
