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


class SampleResourceGroup(Model):
    """SampleResourceGroup.

    :param name: resource group name 'testgroup101'
    :type name: str
    :param location: resource group location 'West US'
    :type location: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, name=None, location=None):
        super(SampleResourceGroup, self).__init__()
        self.name = name
        self.location = location
