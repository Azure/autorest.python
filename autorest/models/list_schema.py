from .base_schema import BaseSchema
from typing import Any, Dict


class ListSchema(BaseSchema):
    def __init__(self, yaml_data, element_type, **kwargs):
        super(ListSchema, self).__init__(yaml_data, **kwargs)
        self.element_type = element_type
        self.max_items = kwargs.pop('max_items', None)
        self.min_items = kwargs.pop('min_items', None)
        self.unique_items = kwargs.pop('unique_items', None)


    def get_serialization_type(self):
        return '[{}]'.format(self.element_type.get_serialization_type())

    def get_python_type(self, namespace):
        return 'list[{}]'.format(self.element_type.get_python_type(namespace))

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], **kwargs) -> "SequenceType":
        # TODO: for items, if the type is a primitive is it listed in type instead of $ref?
        element_schema = yaml_data['elementType']

        from . import build_schema
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