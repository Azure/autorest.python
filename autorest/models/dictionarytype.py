from typing import Dict
from .modeltype import ModelType

class DictionaryType(ModelType):
    def __init__(self, name, description, element_type, **kwargs):
        super(DictionaryType, self).__init__(name, description, **kwargs)
        self.element_type = element_type
        self._type_documentation = None

    def type_documentation(self):
        self._type_documentation = "dict[str, {}]".format(self.element_type)
        return self._type_documentation

    def get_attribute_map_type(self):
        return "{{{}}}".format(self.element_type)

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], name:str) -> "DictionaryType":
        description = yaml_data['description'].strip()
        required = yaml_data.get('required')
        readonly = yaml_data.get('readOnly')
        constant = yaml_data.get('constant')
        element_type = yaml_data['elementType']['type']

        return cls(
            name=name,
            description=description,
            element_type=element_type,
            required=required,
            readonly=readonly,
            constant=constant
        )