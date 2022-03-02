# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Error
    from ._models_py3 import ErrorResponse
    from ._models_py3 import InnerError
    from ._models_py3 import SecretResponse
except (SyntaxError, ImportError):
    from ._models import Error  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import InnerError  # type: ignore
    from ._models import SecretResponse  # type: ignore

from ._errorwith_secrets_enums import (
    ErrorCode,
    InnerErrorCode,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Error",
    "ErrorResponse",
    "InnerError",
    "SecretResponse",
    "ErrorCode",
    "InnerErrorCode",
]
__all__.extend(_patch_all)
_patch_sdk()
