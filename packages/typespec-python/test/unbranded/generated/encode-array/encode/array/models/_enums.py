# coding=utf-8

from enum import Enum
from corehttp.utils import CaseInsensitiveEnumMeta


class Colors(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of Colors."""

    BLUE = "blue"
    RED = "red"
    GREEN = "green"


class ColorsExtensibleEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of ColorsExtensibleEnum."""

    BLUE = "blue"
    RED = "red"
    GREEN = "green"
