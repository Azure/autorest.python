from .base_schema import BaseSchema
from ..common.utils import get_property_name
from typing import Any, Dict

class DictionarySchema(BaseSchema):
    def __init__(self, name, description, element_type, id, **kwargs):
        super(DictionarySchema, self).__init__(name, description, id, **kwargs)
        self.element_type = element_type
        self.additional_properties = kwargs.pop('additional_properties', False)


    def get_attribute_map_type(self):
        if self.additional_properties:
            return '{{str}}'
        return "{{{}}}".format(self.element_type.get_attribute_map_type())

    def get_doc_string_type(self, namespace):
        # in this case, it's an additional_properties property for unmatched properties
        if self.additional_properties:
            return 'dict[str, str]'
        return 'dict[str, {}]'.format(self.element_type.get_doc_string_type(namespace))

    @classmethod
    def create_additional_properties_dict(cls):
        return cls(
            name='additional_properties',
            description='Unmatched properties from the message are deserialized to this collection.',
            id='additional_properties',
            element_type='object',
            additional_properties=True
        )

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], serialize_name="") -> "DictionarySchema":
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data
        )

        element_schema = yaml_data['schema']['elementType']

        from . import build_schema
        element_type = build_schema(
            name='_',
            yaml_data=element_schema,
            serialize_name='_'
        )

        return cls(
            name=name,
            description=common_parameters_dict['description'],
            id=common_parameters_dict['id'],
            element_type=element_type,
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant'],
            default_value = (yaml_data['schema'].get('defaultValue')
                            if yaml_data.get('schema')
                            else yaml_data.get('defaultValue')),
            serialize_name=serialize_name
        )
