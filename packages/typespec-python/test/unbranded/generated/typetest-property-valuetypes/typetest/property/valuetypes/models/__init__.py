# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models import (  # type: ignore
    BooleanLiteralProperty,
    BooleanProperty,
    BytesProperty,
    CollectionsIntProperty,
    CollectionsModelProperty,
    CollectionsStringProperty,
    DatetimeProperty,
    Decimal128Property,
    DecimalProperty,
    DictionaryStringProperty,
    DurationProperty,
    EnumProperty,
    ExtensibleEnumProperty,
    FloatLiteralProperty,
    FloatProperty,
    InnerModel,
    IntLiteralProperty,
    IntProperty,
    ModelProperty,
    NeverProperty,
    StringLiteralProperty,
    StringProperty,
    UnionEnumValueProperty,
    UnionFloatLiteralProperty,
    UnionIntLiteralProperty,
    UnionStringLiteralProperty,
    UnknownArrayProperty,
    UnknownDictProperty,
    UnknownIntProperty,
    UnknownStringProperty,
)

from ._enums import (  # type: ignore
    ExtendedEnum,
    FixedInnerEnum,
    InnerEnum,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "BooleanLiteralProperty",
    "BooleanProperty",
    "BytesProperty",
    "CollectionsIntProperty",
    "CollectionsModelProperty",
    "CollectionsStringProperty",
    "DatetimeProperty",
    "Decimal128Property",
    "DecimalProperty",
    "DictionaryStringProperty",
    "DurationProperty",
    "EnumProperty",
    "ExtensibleEnumProperty",
    "FloatLiteralProperty",
    "FloatProperty",
    "InnerModel",
    "IntLiteralProperty",
    "IntProperty",
    "ModelProperty",
    "NeverProperty",
    "StringLiteralProperty",
    "StringProperty",
    "UnionEnumValueProperty",
    "UnionFloatLiteralProperty",
    "UnionIntLiteralProperty",
    "UnionStringLiteralProperty",
    "UnknownArrayProperty",
    "UnknownDictProperty",
    "UnknownIntProperty",
    "UnknownStringProperty",
    "ExtendedEnum",
    "FixedInnerEnum",
    "InnerEnum",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
