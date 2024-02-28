# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from corehttp.utils import CaseInsensitiveEnumMeta


class EnumsOnlyCasesLr(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of EnumsOnlyCasesLr."""

    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"


class EnumsOnlyCasesUd(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of EnumsOnlyCasesUd."""

    UP = "up"
    DOWN = "down"


class GetResponseProp2(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of GetResponseProp2."""

    1.1 = "1.1"
    2.2 = "2.2"
    3.3 = "3.3"


class GetResponseProp3(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of GetResponseProp3."""

    1 = "1"
    2 = "2"
    3 = "3"


class GetResponseProp4(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of GetResponseProp4."""

    B = "b"
    C = "c"


class GetResponseProp5(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of GetResponseProp5."""

    A = "a"
    B = "b"
    C = "c"


class StringExtensibleNamedUnion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of StringExtensibleNamedUnion."""

    OPTION_B = "b"
    C = "c"
