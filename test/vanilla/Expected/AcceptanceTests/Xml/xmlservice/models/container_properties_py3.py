# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ContainerProperties(Model):
    """Properties of a container.

    All required parameters must be populated in order to send to Azure.

    :param last_modified: Required.
    :type last_modified: datetime
    :param etag: Required.
    :type etag: str
    :param lease_status: Possible values include: 'locked', 'unlocked'
    :type lease_status: str or ~xmlservice.models.LeaseStatusType
    :param lease_state: Possible values include: 'available', 'leased',
     'expired', 'breaking', 'broken'
    :type lease_state: str or ~xmlservice.models.LeaseStateType
    :param lease_duration: Possible values include: 'infinite', 'fixed'
    :type lease_duration: str or ~xmlservice.models.LeaseDurationType
    :param public_access: Possible values include: 'container', 'blob'
    :type public_access: str or ~xmlservice.models.PublicAccessType
    """

    _validation = {
        'last_modified': {'required': True},
        'etag': {'required': True},
    }

    _attribute_map = {
        'last_modified': {'key': 'Last-Modified', 'type': 'rfc-1123'},
        'etag': {'key': 'Etag', 'type': 'str'},
        'lease_status': {'key': 'LeaseStatus', 'type': 'LeaseStatusType'},
        'lease_state': {'key': 'LeaseState', 'type': 'LeaseStateType'},
        'lease_duration': {'key': 'LeaseDuration', 'type': 'LeaseDurationType'},
        'public_access': {'key': 'PublicAccess', 'type': 'str'},
    }
    _xml_map = {
        'name': 'ContainerProperties'
    }
    _xml_attribute_map = {
        'last_modified': {'name': 'Last-Modified'},
        'etag': {'name': 'Etag'},
        'lease_status': {'name': 'LeaseStatus'},
        'lease_state': {'name': 'LeaseState'},
        'lease_duration': {'name': 'LeaseDuration'},
        'public_access': {'name': 'PublicAccess'},
    }

    def __init__(self, *, last_modified, etag: str, lease_status=None, lease_state=None, lease_duration=None, public_access=None, **kwargs) -> None:
        super(ContainerProperties, self).__init__(**kwargs)
        self.last_modified = last_modified
        self.etag = etag
        self.lease_status = lease_status
        self.lease_state = lease_state
        self.lease_duration = lease_duration
        self.public_access = public_access
