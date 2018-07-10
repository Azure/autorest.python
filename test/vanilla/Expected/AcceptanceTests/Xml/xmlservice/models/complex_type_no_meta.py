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


class ComplexTypeNoMeta(Model):
    """I am a complex type with no XML node.

    :param id: The id of the res
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'ID', 'type': 'str', 'xml': {'name': 'ID'}},
    }
    _xml_map = {
    }

    def __init__(self, **kwargs):
        super(ComplexTypeNoMeta, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
