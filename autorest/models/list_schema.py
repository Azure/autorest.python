from .base_schema import BaseSchema
from typing import Any, Dict
from ..common.utils import get_property_name


class ListSchema(BaseSchema):
    def __init__(self, yaml_data, name, element_type, **kwargs):
        super(ListSchema, self).__init__(yaml_data, get_property_name(name), **kwargs)
        self.element_type = element_type
        self.max_items = kwargs.pop('max_items', None)
        self.min_items = kwargs.pop('min_items', None)
        self.unique_items = kwargs.pop('unique_items', None)


    def get_serialization_type(self):
        return '[{}]'.format(self.element_type.get_serialization_type())

    def get_doc_string_type(self, namespace):
        return 'list[{}]'.format(self.element_type.get_doc_string_type(namespace))

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], **kwargs) -> "SequenceType":
        # TODO: for items, if the type is a primitive is it listed in type instead of $ref?
        original_swagger_name = kwargs.pop("original_swagger_name", None)
        element_schema = yaml_data['elementType']

        from . import build_schema
        element_type = build_schema(
            name='_',
            yaml_data=element_schema,
            original_swagger_name='_',
            **kwargs
        )

        return cls(
            yaml_data=yaml_data,
            name=name,
            element_type=element_type,
            max_items=yaml_data.get('maxItems'),
            min_items=yaml_data.get('minItems'),
            unique_items=yaml_data.get('uniqueItems'),
            original_swagger_name=original_swagger_name
        )