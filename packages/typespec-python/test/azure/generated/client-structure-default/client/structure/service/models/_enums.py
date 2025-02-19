# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ClientType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of ClientType."""

    DEFAULT = "default"
    MULTI_CLIENT = "multi-client"
    RENAMED_OPERATION = "renamed-operation"
    TWO_OPERATION_GROUP = "two-operation-group"
    CLIENT_OPERATION_GROUP = "client-operation-group"
