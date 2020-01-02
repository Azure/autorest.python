# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict
from .base_schema import BaseSchema


class ListSchema(BaseSchema):
    def __init__(self, yaml_data, element_type, **kwargs):
        super(ListSchema, self).__init__(yaml_data)
        self.element_type = element_type
        self.max_items = kwargs.pop('max_items', None)
        self.min_items = kwargs.pop('min_items', None)
        self.unique_items = kwargs.pop('unique_items', None)


    def get_serialization_type(self):
        return '[{}]'.format(self.element_type.get_serialization_type())

    def get_python_type_annotation(self):
        return f'List[{self.element_type.get_python_type_annotation()}]'

    def get_python_type(self, namespace):
        return f'list[{self.element_type.get_python_type(namespace)}]'

    def get_validation_map(self):
        validation_map = {}
        if self.max_items:
            validation_map['max_items'] = self.max_items
            validation_map['min_items'] = self.min_items or 0
        if self.min_items:
            validation_map['min_items'] = self.min_items
        if self.unique_items:
            validation_map['unique'] = True
        return validation_map or None

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], **kwargs) -> "SequenceType":  # pylint: disable=arguments-differ
        # TODO: for items, if the type is a primitive is it listed in type instead of $ref?
        element_schema = yaml_data['elementType']

        from . import build_schema  # pylint: disable=import-outside-toplevel
        element_type = build_schema(
            yaml_data=element_schema,
            **kwargs
        )

        return cls(
            yaml_data=yaml_data,
            element_type=element_type,
            max_items=yaml_data.get('maxItems'),
            min_items=yaml_data.get('minItems'),
            unique_items=yaml_data.get('uniqueItems'),
        )
