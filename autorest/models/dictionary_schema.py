from .base_schema import BaseSchema
from ..common.utils import get_property_name
from typing import Any, Dict

class DictionarySchema(BaseSchema):
    def __init__(self, yaml_data, name, description, element_type, **kwargs):
        super(DictionarySchema, self).__init__(yaml_data, name, description, **kwargs)
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
            yaml_data=None,
            name='additional_properties',
            description='Unmatched properties from the message are deserialized to this collection.',
            element_type='object',
            additional_properties=True
        )

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], **kwargs) -> "DictionarySchema":
        original_swagger_name = kwargs.pop("original_swagger_name", "")
        for_additional_properties = kwargs.pop('for_additional_properties', False)

        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data
        )

        description = ('Unmatched properties from the message are deserialized to this collection.'
                    if for_additional_properties else common_parameters_dict['description'])

        element_schema = yaml_data['schema']['elementType'] if yaml_data.get('schema') else yaml_data['elementType']

        from . import build_schema
        element_type = build_schema(
            name='_',
            yaml_data=element_schema,
            original_swagger_name='_',
            for_additional_properties=for_additional_properties
        )

        return cls(
            yaml_data=yaml_data,
            name=name,
            description=description,
            element_type=element_type,
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant'],
            is_discriminator=common_parameters_dict['is_discriminator'],
            discriminator_value = common_parameters_dict['discriminator_value'],
            default_value = (yaml_data['schema'].get('defaultValue')
                            if yaml_data.get('schema')
                            else yaml_data.get('defaultValue')),
            original_swagger_name=original_swagger_name
        )