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


class BlobPrefix(Model):
    """BlobPrefix.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
    }
    _xml_map = {
        'name': 'BlobPrefix'
    }
    _xml_attribute_map = {
        'name': {'name': 'Name'},
    }

    def __init__(self, *, name: str, **kwargs) -> None:
        super(BlobPrefix, self).__init__(**kwargs)
        self.name = name
