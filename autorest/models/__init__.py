from .code_model import CodeModel
from .object_schema import ObjectSchema
from .dictionary_schema import DictionarySchema
from .list_schema import ListSchema
from .primitive_schemas import get_primitive_schema, PrimitiveSchema
from .enum_schema import EnumSchema
from .base_schema import BaseSchema
from ..common.utils import to_python_case

__all__ = [
    "BaseSchema",
    "CodeModel",
    "ObjectSchema",
    "DictionarySchema",
    "ListSchema",
    "EnumSchema",
    "PrimitiveSchema"
]

# TODO: should this be in models.__init__ or CodeModel
def build_schema(name, yaml_data, required=None):
    schema_type = yaml_data.get('type')
    if schema_type == 'array':
        return ListSchema.from_yaml(
            name=name,
            yaml_data=yaml_data,
            required=required
        )
    if schema_type == 'dictionary':
        return DictionarySchema.from_yaml(
            name=name,
            yaml_data=yaml_data,
            required=required
        )
    if schema_type in ('sealed-choice', 'choice'):
        return EnumSchema.from_yaml(
            name=name,
            yaml_data=yaml_data,
            required=required
        )
    if schema_type == 'object':
        return ObjectSchema.from_yaml(
            name=name,
            yaml_data=yaml_data,
            required=required
        )
    return get_primitive_schema(
        name=name,
        yaml_data=yaml_data,
        required=required,
        schema_type=schema_type
    )