# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class UnionFloatLiteralPropertyProperty(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of UnionFloatLiteralPropertyProperty."""

    1.2 = "1.2"
    2.3 = "2.3"


class UnionIntLiteralPropertyProperty(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of UnionIntLiteralPropertyProperty."""

    1 = "1"
    2 = "2"


class UnionStringLiteralPropertyProperty(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of UnionStringLiteralPropertyProperty."""

    HELLO = "hello"
    WORLD = "world"
