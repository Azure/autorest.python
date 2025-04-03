# coding=utf-8

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class SecondClientEnumType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of SecondClientEnumType."""

    SECOND = "second"
