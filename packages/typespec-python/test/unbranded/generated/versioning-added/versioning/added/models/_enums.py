# coding=utf-8

from enum import Enum
from corehttp.utils import CaseInsensitiveEnumMeta


class EnumV1(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of EnumV1."""

    ENUM_MEMBER_V1 = "enumMemberV1"
    ENUM_MEMBER_V2 = "enumMemberV2"


class EnumV2(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of EnumV2."""

    ENUM_MEMBER = "enumMember"


class Versions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The version of the API."""

    V1 = "v1"
    """The version v1."""
    V2 = "v2"
    """The version v2."""
