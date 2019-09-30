from .baseschema import BaseSchema
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
            yaml_data=yaml_data,
            required=kwargs.pop('required', None)
        )
        if yaml_data['elementType'].get('$ref'):
            # type of value in dict is another Class
            element_type = yaml_data['elementType']['$ref']
        else:
            # type of value in dict is a known type
            element_type = yaml_data['elementType']['type']

        return cls(
            name=name,
            description=common_parameters_dict['description'],
            element_type=element_type,
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant']
        )
