# coding=utf-8

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class DogKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """extensible enum type for discriminator."""

    GOLDEN = "golden"
    """Species golden"""


class SnakeKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """fixed enum type for discriminator."""

    COBRA = "cobra"
    """Species cobra"""
