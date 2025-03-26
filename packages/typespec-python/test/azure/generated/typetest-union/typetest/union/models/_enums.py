# coding=utf-8
None

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class StringExtensibleNamedUnion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of StringExtensibleNamedUnion."""

    OPTION_B = "b"
    C = "c"
