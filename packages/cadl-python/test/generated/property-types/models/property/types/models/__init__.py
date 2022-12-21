﻿# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import BooleanProperty
from ._models import BytesProperty
from ._models import CollectionsIntProperty
from ._models import CollectionsModelProperty
from ._models import CollectionsStringProperty
from ._models import DatetimeProperty
from ._models import DictionaryStringProperty
from ._models import DurationProperty
from ._models import EnumProperty
from ._models import ExtensibleEnumProperty
from ._models import FloatProperty
from ._models import InnerModel
from ._models import IntProperty
from ._models import ModelProperty
from ._models import NeverProperty
from ._models import StringProperty

from ._enums import FixedInnerEnum
from ._enums import InnerEnum
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "BooleanProperty",
    "BytesProperty",
    "CollectionsIntProperty",
    "CollectionsModelProperty",
    "CollectionsStringProperty",
    "DatetimeProperty",
    "DictionaryStringProperty",
    "DurationProperty",
    "EnumProperty",
    "ExtensibleEnumProperty",
    "FloatProperty",
    "InnerModel",
    "IntProperty",
    "ModelProperty",
    "NeverProperty",
    "StringProperty",
    "FixedInnerEnum",
    "InnerEnum",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
