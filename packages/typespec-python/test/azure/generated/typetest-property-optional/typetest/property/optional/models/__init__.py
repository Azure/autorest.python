# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import BooleanLiteralProperty
from ._models import BytesProperty
from ._models import CollectionsByteProperty
from ._models import CollectionsModelProperty
from ._models import DatetimeProperty
from ._models import DurationProperty
from ._models import FloatLiteralProperty
from ._models import IntLiteralProperty
from ._models import PlainDateProperty
from ._models import PlainTimeProperty
from ._models import RequiredAndOptionalProperty
from ._models import StringLiteralProperty
from ._models import StringProperty
from ._models import UnionFloatLiteralProperty
from ._models import UnionIntLiteralProperty
from ._models import UnionStringLiteralProperty
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "BooleanLiteralProperty",
    "BytesProperty",
    "CollectionsByteProperty",
    "CollectionsModelProperty",
    "DatetimeProperty",
    "DurationProperty",
    "FloatLiteralProperty",
    "IntLiteralProperty",
    "PlainDateProperty",
    "PlainTimeProperty",
    "RequiredAndOptionalProperty",
    "StringLiteralProperty",
    "StringProperty",
    "UnionFloatLiteralProperty",
    "UnionIntLiteralProperty",
    "UnionStringLiteralProperty",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
