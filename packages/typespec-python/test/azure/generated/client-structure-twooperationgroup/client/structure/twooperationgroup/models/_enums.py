# coding=utf-8

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ClientType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of ClientType."""

    DEFAULT = "default"
    MULTI_CLIENT = "multi-client"
    RENAMED_OPERATION = "renamed-operation"
    TWO_OPERATION_GROUP = "two-operation-group"
    CLIENT_OPERATION_GROUP = "client-operation-group"
