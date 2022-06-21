# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class OperationResultStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the request."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "canceled"
    ACCEPTED = "Accepted"
    CREATING = "Creating"
    CREATED = "Created"
    UPDATING = "Updating"
    UPDATED = "Updated"
    DELETING = "Deleting"
    DELETED = "Deleted"
    OK = "OK"
