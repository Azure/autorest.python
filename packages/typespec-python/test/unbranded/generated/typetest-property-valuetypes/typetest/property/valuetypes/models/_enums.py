# coding=utf-8


from enum import Enum
from corehttp.utils import CaseInsensitiveEnumMeta


class FixedInnerEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum that will be used as a property for model EnumProperty. Non-extensible."""

    VALUE_ONE = "ValueOne"
    """First value."""
    VALUE_TWO = "ValueTwo"
    """Second value."""


class InnerEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum that will be used as a property for model EnumProperty. Non-extensible."""

    VALUE_ONE = "ValueOne"
    """First value."""
    VALUE_TWO = "ValueTwo"
    """Second value."""
