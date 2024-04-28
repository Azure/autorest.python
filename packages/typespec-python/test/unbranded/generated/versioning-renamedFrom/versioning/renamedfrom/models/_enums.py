# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from corehttp.utils import CaseInsensitiveEnumMeta


class NewEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of NewEnum."""

    NEW_ENUM_MEMBER = "newEnumMember"


class Versions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The version of the API."""

    V1 = "v1"
    """The version v1."""
    V2 = "v2"
    """The version v2."""
