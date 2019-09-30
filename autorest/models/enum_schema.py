from .base_schema import BaseSchema
from typing import Any, Dict
from ..common.utils import to_python_type


class EnumValue:
    def __init__(self, name, value, enum_type, description, **kwargs):
        self.name = name
        self.value = value
        self.enum_type = enum_type
        self.description = description

        if enum_type not in ('str', 'bool', 'int'):
            raise ValueError('The type of the enum can not be {}.'
                            'It must be either a str, bool, or int.'.format(enum_type))

    # @classmethod
    # def from_yaml(cls, name, yaml_data):
    #     return cls(
    #         name=name,
    #         value=yaml_data['value'],
    #         enum_type=to_python_type(yaml_data['type'])
    #     )

class EnumSchema(BaseSchema):
    def __init__(self, name, description, enum_type, **kwargs):
        super(EnumSchema, self).__init__(name, description, **kwargs)
        self.enum_type = enum_type
        self.enum_values = kwargs.pop('enum_values', None)

    def get_attribute_map_type(self):
        return 'str'

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], **kwargs: Any) -> "EnumType":
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data
        )
        enum_type = yaml_data['choiceType']

        # this is to check whether this instance of EnumSchema is a property or an enum class itself
        is_class = kwargs.pop('is_class', None)
        if is_class:
            enum_values = yaml_data['items']

        return cls(
            name=name,
            description=common_parameters_dict['description'],
            enum_type=enum_type,
            enum_values=enum_values,
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant']
        )
