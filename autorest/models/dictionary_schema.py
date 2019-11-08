from .base_schema import BaseSchema
from ..common.utils import get_property_name
from typing import Any, Dict

class DictionarySchema(BaseSchema):
    def __init__(self, yaml_data, name, element_type, **kwargs):
        super(DictionarySchema, self).__init__(yaml_data, name, **kwargs)
        self.element_type = element_type
        self.additional_properties = kwargs.pop('additional_properties', False)


    def get_serialization_type(self, namespace=None):
        # if self.additional_properties:
        #     return '{object}'
        return "{{{}}}".format(self.element_type.get_serialization_type())

    def get_doc_string_type(self, namespace):
        # in this case, it's an additional_properties property for unmatched properties
        # if self.additional_properties:
        #     return 'dict[str, object]'
        return 'dict[str, {}]'.format(self.element_type.get_doc_string_type(namespace))

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], **kwargs) -> "DictionarySchema":
        for_additional_properties = kwargs.pop('for_additional_properties', False)

        element_schema = yaml_data['elementType']

        from . import build_schema
        element_type = build_schema(
            name='_',
            yaml_data=element_schema,
            for_additional_properties=for_additional_properties,
            **kwargs
        )

        return cls(
            yaml_data=yaml_data,
            name=name,
            element_type=element_type,
            additional_properties=for_additional_properties
        )