from .code_model import CodeModel
from .object_schema import ObjectSchema
from .dictionary_schema import DictionarySchema
from .list_schema import ListSchema
from .primitive_schemas import get_primitive_schema, PrimitiveSchema
from .enum_schema import EnumSchema
from .base_schema import BaseSchema
from ..common.utils import get_property_name

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
def build_schema(name, yaml_data, **kwargs):
    code_model = kwargs.get('code_model')
    schema_type = yaml_data['type']
    if schema_type == 'array':
        return ListSchema.from_yaml(name=name, yaml_data=yaml_data, **kwargs)
    if schema_type == 'dictionary':
        return DictionarySchema.from_yaml(name=name, yaml_data=yaml_data, **kwargs)
    if schema_type == 'object' or schema_type == 'and' or schema_type == 'any':
        return ObjectSchema.from_yaml(
            name=name,
            yaml_data=yaml_data,
            **kwargs
        )
    # since we've already built all enums and primitives, we just need to look them up
    return code_model.lookup_schema(id(yaml_data))