from .modeltype import ModelType
from typing import Dict

class SequenceType(ModelType):
    def __init__(self, name, description, element_type, **kwargs):
        super(SequenceType, self).__init__(name, description, **kwargs)
        self.element_type = element_type
    def get_attribute_map_type(self):
        return '[{}]'.format(self.element_type)

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], name: str) -> "SequenceType":
        required = yaml_data.get('required')
        readonly = yaml_data.get('readOnly')
        constant = yaml_data.get('constant')
        element_type = yaml_data['schema']['elementType']['type']
        description = yaml_data['schema']['description'].strip()
        return cls(
            name=name,
            description=description,
            element_type=element_type,
            required=required,
            readonly=readonly,
            constant=constant
        )