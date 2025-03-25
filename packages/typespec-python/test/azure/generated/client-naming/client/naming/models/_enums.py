# coding=utf-8

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ClientExtensibleEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of ClientExtensibleEnum."""

    ENUM_VALUE1 = "value1"


class ExtensibleEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of ExtensibleEnum."""

    CLIENT_ENUM_VALUE1 = "value1"
    CLIENT_ENUM_VALUE2 = "value2"
