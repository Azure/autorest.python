from typing import Dict
from .modeltype import ModelType

class DictionaryType(ModelType):
    def __init__(self, name, description, element_type, **kwargs):
        super(DictionaryType, self).__init__(name, description, **kwargs)
        self.element_type = element_type


    def get_attribute_map_type(self):
        return "{{{}}}".format(self.element_type)

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], name: str) -> "DictionaryType":
        required = yaml_data.get('required')
        readonly = yaml_data.get('readOnly')
        constant = yaml_data.get('constant')
        description = yaml_data['schema']['description'].strip()
        element_type = yaml_data['schema']['elementType']['type']

        return cls(
            name=name,
            description=description,
            element_type=element_type,
            required=required,
            readonly=readonly,
            constant=constant
        )