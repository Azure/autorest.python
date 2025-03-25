# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models_py3 import (  # type: ignore
    ArrayWrapper,
    Basic,
    BooleanWrapper,
    ByteWrapper,
    Cat,
    Cookiecuttershark,
    DateWrapper,
    DatetimeWrapper,
    Datetimerfc1123Wrapper,
    DictionaryWrapper,
    Dog,
    DotFish,
    DotFishMarket,
    DotSalmon,
    DoubleWrapper,
    DurationWrapper,
    Error,
    Fish,
    FloatWrapper,
    Goblinshark,
    IntWrapper,
    LongWrapper,
    MyBaseType,
    MyDerivedType,
    Pet,
    ReadonlyObj,
    Salmon,
    Sawshark,
    Shark,
    Siamese,
    SmartSalmon,
    StringWrapper,
)

from ._auto_rest_complex_test_service_enums import (  # type: ignore
    CMYKColors,
    GoblinSharkColor,
    MyKind,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ArrayWrapper",
    "Basic",
    "BooleanWrapper",
    "ByteWrapper",
    "Cat",
    "Cookiecuttershark",
    "DateWrapper",
    "DatetimeWrapper",
    "Datetimerfc1123Wrapper",
    "DictionaryWrapper",
    "Dog",
    "DotFish",
    "DotFishMarket",
    "DotSalmon",
    "DoubleWrapper",
    "DurationWrapper",
    "Error",
    "Fish",
    "FloatWrapper",
    "Goblinshark",
    "IntWrapper",
    "LongWrapper",
    "MyBaseType",
    "MyDerivedType",
    "Pet",
    "ReadonlyObj",
    "Salmon",
    "Sawshark",
    "Shark",
    "Siamese",
    "SmartSalmon",
    "StringWrapper",
    "CMYKColors",
    "GoblinSharkColor",
    "MyKind",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
