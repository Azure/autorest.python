from .basetype import BaseType
from typing import Any, Dict

class EnumType(BaseType):
    def __init__(self, name, description, enum_type, **kwargs):
        super(EnumType, self).__init__(name, description, **kwargs)
        self.enum_type = enum_type


    def get_attribute_map_type(self):
        return 'str'

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], **kwargs: Any) -> "EnumType":
        parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data,
            required_list=kwargs.pop('required_list', None)
        )
        enum_type = ""

        return cls(
            name=name,
            description=parameters_dict['description'],
            enum_type=enum_type,
            required=parameters_dict['required'],
            readonly=parameters_dict['readonly'],
            constant=parameters_dict['constant']
        )