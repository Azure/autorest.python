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
            return '{object}'
        return "{{{}}}".format(self.element_type.get_attribute_map_type())

    def get_doc_string_type(self, namespace):
        # in this case, it's an additional_properties property for unmatched properties
        if self.additional_properties:
            return 'dict[str, object]'
        return 'dict[str, {}]'.format(self.element_type.get_doc_string_type(namespace))

    @classmethod
    def create_additional_properties_dict(cls, element_type):
        if element_type == 'and':
            element_type = 'object'
        return cls(
            name='additional_properties',
            description='Unmatched properties from the message are deserialized to this collection.',
            id='additional_properties',
            element_type='object',
            additional_properties=True
        )

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], **kwargs) -> "DictionarySchema":
        serialize_name = kwargs.pop("serialize_name", "")
        for_additional_properties = kwargs.pop('for_additional_properties', False)

        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data
        )

        if for_additional_properties:
            description = 'Unmatched properties from the message are deserialized to this collection.'
            id = 'additional_properties'
        else:
            description = common_parameters_dict['description']
            id = common_parameters_dict['id']

        element_schema = yaml_data['schema']['elementType'] if yaml_data.get('schema') else yaml_data['elementType']

        from . import build_schema
        element_type = build_schema(
            name='_',
            yaml_data=element_schema,
            serialize_name='_',
            for_element_type=not for_additional_properties,
            for_additional_properties=for_additional_properties
        )

        return cls(
            name=name,
            description=description,
            id=id,
            element_type=element_type,
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant'],
            default_value = (yaml_data['schema'].get('defaultValue')
                            if yaml_data.get('schema')
                            else yaml_data.get('defaultValue')),
            serialize_name=serialize_name
        )
