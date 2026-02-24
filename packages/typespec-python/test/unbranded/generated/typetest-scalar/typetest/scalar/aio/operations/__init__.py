# coding=utf-8
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._operations import ScalarClientStringOperations  # type: ignore
from ._operations import ScalarClientBooleanOperations  # type: ignore
from ._operations import ScalarClientUnknownOperations  # type: ignore
from ._operations import ScalarClientDecimalTypeOperations  # type: ignore
from ._operations import ScalarClientDecimal128TypeOperations  # type: ignore
from ._operations import ScalarClientDecimalVerifyOperations  # type: ignore
from ._operations import ScalarClientDecimal128VerifyOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ScalarClientStringOperations",
    "ScalarClientBooleanOperations",
    "ScalarClientUnknownOperations",
    "ScalarClientDecimalTypeOperations",
    "ScalarClientDecimal128TypeOperations",
    "ScalarClientDecimalVerifyOperations",
    "ScalarClientDecimal128VerifyOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
