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


class RetentionPolicy(Model):
    """the retention policy.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. Indicates whether a retention policy is enabled
     for the storage service
    :type enabled: bool
    :param days: Indicates the number of days that metrics or logging or
     soft-deleted data should be retained. All data older than this value will
     be deleted
    :type days: int
    """

    _validation = {
        'enabled': {'required': True},
        'days': {'minimum': 1},
    }

    _attribute_map = {
        'enabled': {'key': 'Enabled', 'type': 'bool'},
        'days': {'key': 'Days', 'type': 'int'},
    }
    _xml_map = {
        'name': 'RetentionPolicy'
    }
    _xml_attribute_map = {
        'enabled': {'name': 'Enabled'},
        'days': {'name': 'Days'},
    }

    def __init__(self, *, enabled: bool, days: int=None, **kwargs) -> None:
        super(RetentionPolicy, self).__init__(**kwargs)
        self.enabled = enabled
        self.days = days
