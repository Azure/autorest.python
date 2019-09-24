from .modeltype import ModelType
from typing import Dict

class EnumType(ModelType):
    def __init__(self, name, description, enum_type, **kwargs):
        super(EnumType, self).__init__(name, description, **kwargs)
        self._enum_type = enum_type
        self._type_documentation = None

    def type_documentation(self):
        self._type_documentation = "str or {}".format(self._enum_type)
        return self._type_documentation

    def get_attribute_map_type(self):
        return 'str'

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], name: str) -> "EnumType":
        description = yaml_data['description'].strip()
        required = yaml_data.get('required')
        readonly = yaml_data.get('readOnly')
        constant = yaml_data.get('constant')
        enum_type = yaml_data['$key']

        return cls(
            name=name,
            description=description,
            enum_type=enum_type,
            required=required,
            readonly=readonly,
            constant=constant
        )