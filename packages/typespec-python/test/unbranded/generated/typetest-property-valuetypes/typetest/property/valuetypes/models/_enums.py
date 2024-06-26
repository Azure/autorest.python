# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from corehttp.utils import CaseInsensitiveEnumMeta


class ExtendedEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of ExtendedEnum."""

    ENUM_VALUE2 = "value2"


class FixedInnerEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum that will be used as a property for model EnumProperty. Non-extensible."""

    VALUE_ONE = "ValueOne"
    """First value."""
    VALUE_TWO = "ValueTwo"
    """Second value."""


class InnerEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum that will be used as a property for model EnumProperty. Extensible."""

    VALUE_ONE = "ValueOne"
    """First value."""
    VALUE_TWO = "ValueTwo"
    """Second value."""
