# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class FlattenedProductPropertiesProvisioningStateValues(str, Enum):
    
    succeeded = "Succeeded"  #: The value 'Succeeded'.
    failed = "Failed"  #: The value 'Failed'.
    canceled = "canceled"  #: The value 'canceled'.
    accepted = "Accepted"  #: The value 'Accepted'.
    creating = "Creating"  #: The value 'Creating'.
    created = "Created"  #: The value 'Created'.
    updating = "Updating"  #: The value 'Updating'.
    updated = "Updated"  #: The value 'Updated'.
    deleting = "Deleting"  #: The value 'Deleting'.
    deleted = "Deleted"  #: The value 'Deleted'.
    ok = "OK"  #: The value 'OK'.
