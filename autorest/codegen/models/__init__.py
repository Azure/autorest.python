# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict
from .base_model import BaseModel
from .code_model import CodeModel
from .credential_schema import AzureKeyCredentialSchema, TokenCredentialSchema
from .object_schema import ObjectSchema, get_object_schema, HiddenModelObjectSchema
from .dictionary_schema import DictionarySchema
from .list_schema import ListSchema
from .primitive_schemas import get_primitive_schema, AnySchema, PrimitiveSchema, IOSchema
from .enum_schema import EnumSchema, HiddenModelEnumSchema, get_enum_schema
from .base_schema import BaseSchema
from .constant_schema import ConstantSchema
from .imports import FileImport, ImportType, TypingSection
from .lro_operation import LROOperation
from .paging_operation import PagingOperation
from .parameter import Parameter, ParameterStyle, ParameterLocation
from .operation import Operation
from .property import Property
from .operation_group import OperationGroup
from .schema_response import SchemaResponse
from .parameter_list import ParameterList, GlobalParameterList
from .request_builder import RequestBuilder
from .base_builder import BaseBuilder, ContentTypesContainer, BodyKwargNames
from .lro_paging_operation import LROPagingOperation
from .request_builder_parameter import RequestBuilderParameter
from .schema_request import SchemaRequest

__all__ = [
    "AzureKeyCredentialSchema",
    "AnySchema",
    "BaseModel",
    "BaseSchema",
    "BodyKwargNames",
    "CodeModel",
    "ConstantSchema",
    "ContentTypesContainer",
    "ObjectSchema",
    "DictionarySchema",
    "ListSchema",
    "EnumSchema",
    "HiddenModelEnumSchema",
    "FileImport",
    "ImportType",
    "TypingSection",
    "PrimitiveSchema",
    "LROOperation",
    "Operation",
    "PagingOperation",
    "Parameter",
    "ParameterList",
    "ParameterLocation",
    "OperationGroup",
    "Property",
    "RequestBuilder",
    "SchemaResponse",
    "TokenCredentialSchema",
    "LROPagingOperation",
    "BaseBuilder",
    "SchemaRequest",
    "RequestBuilderParameter",
    "HiddenModelObjectSchema",
    "ParameterStyle",
    "IOSchema",
    "GlobalParameterList",
]

def _generate_as_object_schema(yaml_data: Dict[str, Any]) -> bool:
    if (
        yaml_data.get('properties') or
        yaml_data.get('discriminator') or
        yaml_data.get('parents') and yaml_data['parents'].get('immediate')
    ):
        return True
    return False


def build_schema(yaml_data: Dict[str, Any], **kwargs) -> BaseSchema:
    code_model = kwargs.get("code_model", None)
    if not code_model:
        raise ValueError("CodeModel not passed through kwargs")
    yaml_id = id(yaml_data)
    namespace = code_model.namespace
    try:
        return code_model.lookup_schema(yaml_id)
    except KeyError:
        # Not created yet, let's create it and add it to the index
        pass
    schema: BaseSchema
    schema_type = yaml_data["type"]
    if schema_type == "constant":
        schema = ConstantSchema.from_yaml(namespace=namespace, yaml_data=yaml_data)
        code_model.primitives[yaml_id] = schema

    elif schema_type in ["choice", "sealed-choice"]:
        schema = get_enum_schema(code_model).from_yaml(namespace=namespace, yaml_data=yaml_data, **kwargs)
        code_model.enums[yaml_id] = schema

    elif schema_type == "array":
        schema = ListSchema.from_yaml(namespace=namespace, yaml_data=yaml_data, **kwargs)
        code_model.primitives[yaml_id] = schema

    elif schema_type == "dictionary":
        schema = DictionarySchema.from_yaml(namespace=namespace, yaml_data=yaml_data, **kwargs)
        code_model.primitives[yaml_id] = schema

    elif schema_type in ["object", "and", "group", "any-object"]:
        if _generate_as_object_schema(yaml_data):
            # To avoid infinite loop, create the right instance in memory,
            # put it in the index, and then parse the object.
            schema = get_object_schema(code_model)(namespace, yaml_data, "_", "")
            code_model.schemas[yaml_id] = schema
            schema.fill_instance_from_yaml(namespace=namespace, yaml_data=yaml_data, **kwargs)
        else:
            schema = AnySchema.from_yaml(namespace=namespace, yaml_data=yaml_data)
            code_model.primitives[yaml_id] = schema
    else:
        schema = get_primitive_schema(namespace=namespace, yaml_data=yaml_data)
        code_model.primitives[yaml_id] = schema

    return schema
