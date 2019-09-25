from .modeltype import ModelType
from typing import Dict

class EnumType(ModelType):
    def __init__(self, name, description, enum_type, **kwargs):
        super(EnumType, self).__init__(name, description, **kwargs)
        self.enum_type = enum_type


    def get_attribute_map_type(self):
        return 'str'

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], name: str) -> "EnumType":
        required = yaml_data.get('required')
        readonly = yaml_data.get('readOnly')
        constant = yaml_data.get('constant')
        enum_type = yaml_data['schema']['$key']
        description = yaml_data['schema']['description'].strip()

        return cls(
            name=name,
            description=description,
            enum_type=enum_type,
            required=required,
            readonly=readonly,
            constant=constant
        )