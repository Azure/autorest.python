# coding=utf-8
None

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class EnumV2(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of EnumV2."""

    ENUM_MEMBER_V2 = "enumMemberV2"


class EnumV3(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of EnumV3."""

    ENUM_MEMBER_V1 = "enumMemberV1"
    ENUM_MEMBER_V2_PREVIEW = "enumMemberV2Preview"


class Versions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The version of the API."""

    V1 = "v1"
    """The version v1."""
    V2_PREVIEW = "v2preview"
    """The V2 Preview version."""
    V2 = "v2"
    """The version v2."""
