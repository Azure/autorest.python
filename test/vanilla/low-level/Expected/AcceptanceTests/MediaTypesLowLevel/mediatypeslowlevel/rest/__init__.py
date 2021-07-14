# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._request_builders_py3 import build_analyze_body_request
    from ._request_builders_py3 import build_content_type_with_encoding_request
except (SyntaxError, ImportError):
    from ._request_builders import build_analyze_body_request  # type: ignore
    from ._request_builders import build_content_type_with_encoding_request  # type: ignore

__all__ = [
    "build_analyze_body_request",
    "build_content_type_with_encoding_request",
]
