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


class StorageAccountKeys(Model):
    """The access keys for the storage account.

    :param key1: Gets the value of key 1.
    :type key1: str
    :param key2: Gets the value of key 2.
    :type key2: str
    """

    _attribute_map = {
        'key1': {'key': 'key1', 'type': 'str'},
        'key2': {'key': 'key2', 'type': 'str'},
    }

    def __init__(self, key1=None, key2=None):
        super(Model, self).__init__()
        self.key1 = key1
        self.key2 = key2
