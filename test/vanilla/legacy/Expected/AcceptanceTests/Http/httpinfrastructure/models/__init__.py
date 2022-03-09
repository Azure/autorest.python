# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import B
    from ._models_py3 import C
    from ._models_py3 import D
    from ._models_py3 import Error
    from ._models_py3 import MyException
except (SyntaxError, ImportError):
    from ._models import B  # type: ignore
    from ._models import C  # type: ignore
    from ._models import D  # type: ignore
    from ._models import Error  # type: ignore
    from ._models import MyException  # type: ignore
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "B",
    "C",
    "D",
    "Error",
    "MyException",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
