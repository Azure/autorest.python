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


class RootWithRefAndMeta(Model):
    """I am root, and I ref a model WITH meta.

    :param ref_to_model: XML will use XMLComplexTypeWithMeta
    :type ref_to_model: ~xmlservice.models.ComplexTypeWithMeta
    :param something: Something else (just to avoid flattening)
    :type something: str
    """

    _attribute_map = {
        'ref_to_model': {'key': 'RefToModel', 'type': 'ComplexTypeWithMeta', 'xml': {'name': 'RefToModel'}},
        'something': {'key': 'Something', 'type': 'str', 'xml': {'name': 'Something'}},
    }
    _xml_map = {
    }

    def __init__(self, *, ref_to_model=None, something: str=None, **kwargs) -> None:
        super(RootWithRefAndMeta, self).__init__(**kwargs)
        self.ref_to_model = ref_to_model
        self.something = something
