# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict
from .base_model import BaseModel
from .code_model import CodeModel
from .credential_schema import AzureKeyCredentialSchema, TokenCredentialSchema
from .object_schema import ObjectSchema
from .dictionary_schema import DictionarySchema
from .list_schema import ListSchema
from .primitive_schemas import (
    Base64Schema,
    DateSchema,
    DatetimeSchema,
    DurationSchema,
    NumberSchema,
    StringSchema,
    TimeSchema,
    AnySchema,
    PrimitiveSchema,
    IOSchema,
)
from .enum_schema import EnumSchema
from .base_schema import BaseSchema
from .constant_schema import ConstantSchema
from .imports import FileImport, ImportType, TypingSection
from .lro_operation import LROOperation
from .paging_operation import PagingOperation
from .parameter import Parameter
from .operation import Operation
from .property import Property
from .operation_group import OperationGroup
from .response import Response
from .parameter_list import ParameterList, ClientGlobalParameterList, ConfigGlobalParameterList
from .request_builder import RequestBuilder
from .base_builder import BaseBuilder
from .lro_paging_operation import LROPagingOperation
from .request_builder_parameter import RequestBuilderParameter

__all__ = [
    "AzureKeyCredentialSchema",
    "AnySchema",
    "BaseModel",
    "BaseSchema",
    "CodeModel",
    "ConstantSchema",
    "ObjectSchema",
    "DictionarySchema",
    "ListSchema",
    "EnumSchema",
    "FileImport",
    "ImportType",
    "TypingSection",
    "PrimitiveSchema",
    "LROOperation",
    "Operation",
    "PagingOperation",
    "Parameter",
    "ParameterList",
    "OperationGroup",
    "Property",
    "RequestBuilder",
    "Response",
    "TokenCredentialSchema",
    "LROPagingOperation",
    "BaseBuilder",
    "RequestBuilderParameter",
    "IOSchema",
    "ClientGlobalParameterList",
    "ConfigGlobalParameterList",
]

TYPE_TO_OBJECT = {
    "integer": NumberSchema,
    "string": StringSchema,
    "model": ObjectSchema,
    "list": ListSchema,
    "dict": DictionarySchema,
    "constant": ConstantSchema,
    "enum": EnumSchema,
    "bytes": IOSchema,
    "any": AnySchema,
    "datetime": DatetimeSchema,
    "time": TimeSchema,
    "duration": DurationSchema,
    "date": DateSchema,
    "base64": Base64Schema,
}

def build_schema(yaml_data: Dict[str, Any], code_model: CodeModel) -> BaseSchema:
    yaml_id = id(yaml_data)
    try:
        return code_model.lookup_schema(yaml_id)
    except KeyError:
        # Not created yet, let's create it and add it to the index
        pass
    response = TYPE_TO_OBJECT[yaml_data["type"]].from_yaml(
        yaml_data, code_model
    )
    code_model.types_map[yaml_id] = response
    return response
