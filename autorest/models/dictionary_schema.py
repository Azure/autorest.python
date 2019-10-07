from .base_schema import BaseSchema
from ..common.utils import to_python_type
from typing import Any, Dict

class DictionarySchema(BaseSchema):
    def __init__(self, name, description, element_type, id, **kwargs):
        super(DictionarySchema, self).__init__(name, description, id, **kwargs)
        try:
            self.element_type = to_python_type(element_type)
        except:
            self.element_type = element_type


    def get_attribute_map_type(self):
        return "{{{}}}".format(self.element_type)

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], serialize_name="") -> "DictionarySchema":
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data
        )
        return cls(
            name=name,
            description=common_parameters_dict['description'],
            id=common_parameters_dict['id'],
            element_type=(yaml_data['schema']['elementType']['type']
                          if yaml_data.get('schema')
                          else yaml_data['elementType']['type']),
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant'],
            default_value = (yaml_data['schema'].get('defaultValue')
                            if yaml_data.get('schema')
                            else yaml_data.get('defaultValue')),
            serialize_name=serialize_name
        )
