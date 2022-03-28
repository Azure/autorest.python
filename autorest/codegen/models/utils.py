# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Union
import re
from typing import Any, TYPE_CHECKING
import logging
from .base_schema import BaseSchema

if TYPE_CHECKING:
    from .code_model import CodeModel


_LOGGER = logging.getLogger(__name__)

JSON_REGEXP = re.compile(r'^(application|text)/(.+\+)?json$')

def get_schema(code_model: "CodeModel", schema: Any, serialized_name: str = "unknown") -> BaseSchema:
    if not isinstance(schema, dict):
        return schema
    schema_id = id(schema)
    _LOGGER.debug("Looking for id %s for member %s", schema_id, serialized_name)
    try:
        return code_model.lookup_schema(schema_id)
    except KeyError:
        _LOGGER.critical("Unable to ref the object")
        raise
from .parameter import Parameter
from .object_schema import ObjectSchema
from .schema_response import SchemaResponse

def has_json_content_types(content_types: List[str]) -> bool:
    return any(JSON_REGEXP.match(c) for c in content_types)

def has_object_schema(parameters: List[Union[Parameter, SchemaResponse]]) -> bool:
    for param in parameters or []:
        if isinstance(param.schema, ObjectSchema):
            return True
    return False
