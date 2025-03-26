# coding=utf-8
None

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class Versions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Service versions."""

    V1_0 = "v1.0"
    """Version 1.0"""
