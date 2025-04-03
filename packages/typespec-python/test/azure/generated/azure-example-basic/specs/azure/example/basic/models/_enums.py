# coding=utf-8

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class EnumEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of Enum."""

    ENUM_VALUE1 = "EnumValue1"
