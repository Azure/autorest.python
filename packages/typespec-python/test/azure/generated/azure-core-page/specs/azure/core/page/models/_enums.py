# coding=utf-8
None

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ListItemInputExtensibleEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """An extensible enum input parameter."""

    FIRST = "First"
    """The first enum value."""
    SECOND = "Second"
    """The second enum value."""
