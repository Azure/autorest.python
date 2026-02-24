# coding=utf-8
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._operations import ArrayClientInt32ValueOperations  # type: ignore
from ._operations import ArrayClientInt64ValueOperations  # type: ignore
from ._operations import ArrayClientBooleanValueOperations  # type: ignore
from ._operations import ArrayClientStringValueOperations  # type: ignore
from ._operations import ArrayClientFloat32ValueOperations  # type: ignore
from ._operations import ArrayClientDatetimeValueOperations  # type: ignore
from ._operations import ArrayClientDurationValueOperations  # type: ignore
from ._operations import ArrayClientUnknownValueOperations  # type: ignore
from ._operations import ArrayClientModelValueOperations  # type: ignore
from ._operations import ArrayClientNullableFloatValueOperations  # type: ignore
from ._operations import ArrayClientNullableInt32ValueOperations  # type: ignore
from ._operations import ArrayClientNullableBooleanValueOperations  # type: ignore
from ._operations import ArrayClientNullableStringValueOperations  # type: ignore
from ._operations import ArrayClientNullableModelValueOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ArrayClientInt32ValueOperations",
    "ArrayClientInt64ValueOperations",
    "ArrayClientBooleanValueOperations",
    "ArrayClientStringValueOperations",
    "ArrayClientFloat32ValueOperations",
    "ArrayClientDatetimeValueOperations",
    "ArrayClientDurationValueOperations",
    "ArrayClientUnknownValueOperations",
    "ArrayClientModelValueOperations",
    "ArrayClientNullableFloatValueOperations",
    "ArrayClientNullableInt32ValueOperations",
    "ArrayClientNullableBooleanValueOperations",
    "ArrayClientNullableStringValueOperations",
    "ArrayClientNullableModelValueOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
