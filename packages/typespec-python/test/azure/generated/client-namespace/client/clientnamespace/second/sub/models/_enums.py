# coding=utf-8
None

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class SecondClientEnumType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of SecondClientEnumType."""

    SECOND = "second"
