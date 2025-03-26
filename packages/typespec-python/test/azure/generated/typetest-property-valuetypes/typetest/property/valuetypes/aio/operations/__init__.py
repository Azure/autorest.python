# coding=utf-8
None
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._operations import BooleanOperations  # type: ignore
from ._operations import StringOperations  # type: ignore
from ._operations import BytesOperations  # type: ignore
from ._operations import IntOperations  # type: ignore
from ._operations import FloatOperations  # type: ignore
from ._operations import DecimalOperations  # type: ignore
from ._operations import Decimal128Operations  # type: ignore
from ._operations import DatetimeOperations  # type: ignore
from ._operations import DurationOperations  # type: ignore
from ._operations import EnumOperations  # type: ignore
from ._operations import ExtensibleEnumOperations  # type: ignore
from ._operations import ModelOperations  # type: ignore
from ._operations import CollectionsStringOperations  # type: ignore
from ._operations import CollectionsIntOperations  # type: ignore
from ._operations import CollectionsModelOperations  # type: ignore
from ._operations import DictionaryStringOperations  # type: ignore
from ._operations import NeverOperations  # type: ignore
from ._operations import UnknownStringOperations  # type: ignore
from ._operations import UnknownIntOperations  # type: ignore
from ._operations import UnknownDictOperations  # type: ignore
from ._operations import UnknownArrayOperations  # type: ignore
from ._operations import StringLiteralOperations  # type: ignore
from ._operations import IntLiteralOperations  # type: ignore
from ._operations import FloatLiteralOperations  # type: ignore
from ._operations import BooleanLiteralOperations  # type: ignore
from ._operations import UnionStringLiteralOperations  # type: ignore
from ._operations import UnionIntLiteralOperations  # type: ignore
from ._operations import UnionFloatLiteralOperations  # type: ignore
from ._operations import UnionEnumValueOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "BooleanOperations",
    "StringOperations",
    "BytesOperations",
    "IntOperations",
    "FloatOperations",
    "DecimalOperations",
    "Decimal128Operations",
    "DatetimeOperations",
    "DurationOperations",
    "EnumOperations",
    "ExtensibleEnumOperations",
    "ModelOperations",
    "CollectionsStringOperations",
    "CollectionsIntOperations",
    "CollectionsModelOperations",
    "DictionaryStringOperations",
    "NeverOperations",
    "UnknownStringOperations",
    "UnknownIntOperations",
    "UnknownDictOperations",
    "UnknownArrayOperations",
    "StringLiteralOperations",
    "IntLiteralOperations",
    "FloatLiteralOperations",
    "BooleanLiteralOperations",
    "UnionStringLiteralOperations",
    "UnionIntLiteralOperations",
    "UnionFloatLiteralOperations",
    "UnionEnumValueOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
