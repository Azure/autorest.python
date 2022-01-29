# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._request_builders_py3 import build_get_null_request
    from ._request_builders_py3 import build_put_null_request
    from ._request_builders_py3 import build_get_empty_request
    from ._request_builders_py3 import build_put_empty_request
    from ._request_builders_py3 import build_get_mbcs_request
    from ._request_builders_py3 import build_put_mbcs_request
    from ._request_builders_py3 import build_get_whitespace_request
    from ._request_builders_py3 import build_put_whitespace_request
    from ._request_builders_py3 import build_get_not_provided_request
    from ._request_builders_py3 import build_get_base64_encoded_request
    from ._request_builders_py3 import build_get_base64_url_encoded_request
    from ._request_builders_py3 import build_put_base64_url_encoded_request
    from ._request_builders_py3 import build_get_null_base64_url_encoded_request
except (SyntaxError, ImportError):
    from ._request_builders import build_get_null_request  # type: ignore
    from ._request_builders import build_put_null_request  # type: ignore
    from ._request_builders import build_get_empty_request  # type: ignore
    from ._request_builders import build_put_empty_request  # type: ignore
    from ._request_builders import build_get_mbcs_request  # type: ignore
    from ._request_builders import build_put_mbcs_request  # type: ignore
    from ._request_builders import build_get_whitespace_request  # type: ignore
    from ._request_builders import build_put_whitespace_request  # type: ignore
    from ._request_builders import build_get_not_provided_request  # type: ignore
    from ._request_builders import build_get_base64_encoded_request  # type: ignore
    from ._request_builders import build_get_base64_url_encoded_request  # type: ignore
    from ._request_builders import build_put_base64_url_encoded_request  # type: ignore
    from ._request_builders import build_get_null_base64_url_encoded_request  # type: ignore

__all__ = [
    'build_get_null_request',
    'build_put_null_request',
    'build_get_empty_request',
    'build_put_empty_request',
    'build_get_mbcs_request',
    'build_put_mbcs_request',
    'build_get_whitespace_request',
    'build_put_whitespace_request',
    'build_get_not_provided_request',
    'build_get_base64_encoded_request',
    'build_get_base64_url_encoded_request',
    'build_put_base64_url_encoded_request',
    'build_get_null_base64_url_encoded_request',
]
