from .code_model import CodeModel
from .object_schema import ObjectSchema
from .dictionary_schema import DictionarySchema
from .list_schema import ListSchema
from .primitive_schemas import get_primitive_schema, PrimitiveSchema
from .enum_schema import EnumSchema
from .base_schema import BaseSchema
from .constant_schema import ConstantSchema

__all__ = [
    "BaseSchema",
    "CodeModel",
    "ConstantSchema",
    "ObjectSchema",
    "DictionarySchema",
    "ListSchema",
    "EnumSchema",
    "PrimitiveSchema"
]

# TODO: should this be in models.__init__ or CodeModel
def build_schema(yaml_data, **kwargs):
    code_model = kwargs.get('code_model')
    yaml_id = id(yaml_data)
    try:
        return code_model.lookup_schema(yaml_id)
    except Exception:
        # Not created yet, let's create it and add it to the index
        pass

    schema_type = yaml_data['type']
    if schema_type == 'constant':
        schema = ConstantSchema.from_yaml(yaml_data=yaml_data)
        code_model.primitives[yaml_id] = schema

    elif schema_type in ['choice', 'sealed-choice']:
        schema = EnumSchema.from_yaml(yaml_data=yaml_data)
        code_model.enums[yaml_id] = schema

    elif schema_type == 'array':
        schema = ListSchema.from_yaml(yaml_data=yaml_data, **kwargs)
        code_model.primitives[yaml_id] = schema

    elif schema_type == 'dictionary':
        schema = DictionarySchema.from_yaml(yaml_data=yaml_data, **kwargs)
        code_model.primitives[yaml_id] = schema

    elif schema_type == 'object' or schema_type == 'and':
        # To avoid infinite loop, create the right instance in memory,
        # put it in the index, and then parse the object.
        schema = ObjectSchema(yaml_data, None, None)
        code_model.schemas[yaml_id] = schema
        schema.fill_instance_from_yaml(yaml_data, **kwargs)

    else:
        schema = get_primitive_schema(yaml_data=yaml_data)
        code_model.primitives[yaml_id] = schema

    return schema
