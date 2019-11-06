from .base_schema import BaseSchema
from typing import Any, Dict
from ..common.utils import get_enum_name


class EnumValue:
    def __init__(self, name, value, **kwargs):
        self.name = name
        self.value = value
        self.description = kwargs.pop('description', None)

    @classmethod
    def from_yaml(cls, yaml_data):
        name = get_enum_name(yaml_data['language']['default']['name'])
        return cls(
            name=name,
            value=yaml_data['value'],
            description=yaml_data['language']['default'].get('description')
        )

class EnumSchema(BaseSchema):
    def __init__(self, name, description, enum_type, values, **kwargs):
        super(EnumSchema, self).__init__(name, description, **kwargs)
        self.enum_type = enum_type
        self.values = values

    def get_attribute_map_type(self):
        return 'str'

    def get_doc_string_type(self, namespace):
        return "str or ~{}.models.{}".format(namespace, self.enum_type)

    @classmethod
    def _get_enum_values(cls, yaml_data):
        values = []
        for enum in yaml_data:
            values.append(EnumValue.from_yaml(enum))
        return values

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], **kwargs: Any) -> "EnumType":
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data
        )
        enum_type = yaml_data['language']['default']['name']
        schema_data = yaml_data['schema'] if yaml_data.get('schema') else yaml_data
        values = cls._get_enum_values(schema_data['choices'])

        return cls(
            name=name,
            description=common_parameters_dict['description'],
            enum_type=enum_type,
            values=values,
            default_value=schema_data.get('defaultValue'),
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant'],
            serialize_name=kwargs.pop('serialize_name', None)
        )
