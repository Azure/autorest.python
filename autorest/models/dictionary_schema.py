from .base_schema import BaseSchema
from typing import Any, Dict

class DictionarySchema(BaseSchema):
    def __init__(self, name, description, element_type, **kwargs):
        super(DictionarySchema, self).__init__(name, description, **kwargs)
        self.element_type = element_type


    def get_attribute_map_type(self):
        return "{{{}}}".format(self.element_type)

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], **kwargs: Any) -> "DictionarySchema":
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data
        )
        return cls(
            name=name,
            description=common_parameters_dict['description'],
            element_type=yaml_data['schema']['elementType']['type'],
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant']
        )
