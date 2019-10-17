from .base_schema import BaseSchema
from typing import Any, Dict
from ..common.utils import get_property_name


class ListSchema(BaseSchema):
    def __init__(self, name, description, element_type, id, **kwargs):
        super(ListSchema, self).__init__(get_property_name(name), description, id, **kwargs)
        self.element_type = element_type
        self.max_items = kwargs.pop('max_items', None)
        self.min_items = kwargs.pop('min_items', None)
        self.unique_items = kwargs.pop('unique_items', None)


    def get_attribute_map_type(self):
        return '[{}]'.format(self.element_type.get_attribute_map_type())

    def get_doc_string_type(self, namespace):
        return 'list[{}]'.format(self.element_type.get_doc_string_type(namespace))

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], serialize_name) -> "SequenceType":
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data
        )
        # TODO: for items, if the type is a primitive is it listed in type instead of $ref?
        schema_data = yaml_data['schema'] if yaml_data.get('schema') else yaml_data
        element_schema = schema_data['elementType']

        from . import build_schema
        element_type = build_schema(
            name='_',
            yaml_data=element_schema,
            serialize_name='_',
            for_element_type=True
        )

        return cls(
            name=name,
            description=common_parameters_dict['description'],
            id=common_parameters_dict['id'],
            element_type=element_type,
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant'],
            max_items=schema_data.get('maxItems'),
            min_items=schema_data.get('minItems'),
            unique_items=schema_data.get('uniqueItems'),
            default_value = schema_data.get('defaultValue'),
            serialize_name=serialize_name
        )