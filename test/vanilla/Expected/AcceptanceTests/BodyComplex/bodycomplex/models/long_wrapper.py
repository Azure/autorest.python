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


class LongWrapper(Model):
    """LongWrapper.

    :param field1:
    :type field1: long
    :param field2:
    :type field2: long
    """

    _attribute_map = {
        'field1': {'key': 'field1', 'type': 'long'},
        'field2': {'key': 'field2', 'type': 'long'},
    }

    def __init__(self, **kwargs):
        super(LongWrapper, self).__init__(**kwargs)
        self.field1 = kwargs.get('field1', None)
        self.field2 = kwargs.get('field2', None)
