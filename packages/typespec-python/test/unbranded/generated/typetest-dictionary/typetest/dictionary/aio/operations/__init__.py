# coding=utf-8
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._operations import DictionaryClientInt32ValueOperations  # type: ignore
from ._operations import DictionaryClientInt64ValueOperations  # type: ignore
from ._operations import DictionaryClientBooleanValueOperations  # type: ignore
from ._operations import DictionaryClientStringValueOperations  # type: ignore
from ._operations import DictionaryClientFloat32ValueOperations  # type: ignore
from ._operations import DictionaryClientDatetimeValueOperations  # type: ignore
from ._operations import DictionaryClientDurationValueOperations  # type: ignore
from ._operations import DictionaryClientUnknownValueOperations  # type: ignore
from ._operations import DictionaryClientModelValueOperations  # type: ignore
from ._operations import DictionaryClientRecursiveModelValueOperations  # type: ignore
from ._operations import DictionaryClientNullableFloatValueOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "DictionaryClientInt32ValueOperations",
    "DictionaryClientInt64ValueOperations",
    "DictionaryClientBooleanValueOperations",
    "DictionaryClientStringValueOperations",
    "DictionaryClientFloat32ValueOperations",
    "DictionaryClientDatetimeValueOperations",
    "DictionaryClientDurationValueOperations",
    "DictionaryClientUnknownValueOperations",
    "DictionaryClientModelValueOperations",
    "DictionaryClientRecursiveModelValueOperations",
    "DictionaryClientNullableFloatValueOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
