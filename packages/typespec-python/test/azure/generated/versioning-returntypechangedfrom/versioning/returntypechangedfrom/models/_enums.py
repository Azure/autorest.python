# coding=utf-8
None

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class Versions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The version of the API."""

    V1 = "v1"
    """The version v1."""
    V2 = "v2"
    """The version v2."""
