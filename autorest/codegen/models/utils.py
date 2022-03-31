# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
from typing import Any, List, Dict, TYPE_CHECKING, TypeVar
import logging

from .base_schema import BaseSchema

if TYPE_CHECKING:
    from .code_model import CodeModel
    from .schema_request import SchemaRequest


T = TypeVar('T')
OrderedSet = Dict[T, None]

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

def build_content_type_to_schema_request(schema_requests: List["SchemaRequest"], yaml_data: Dict[str, Any]) -> Dict[str, "SchemaRequest"]:
    retval: Dict[str, SchemaRequest] = {}
    for content_type, schema_request_yaml in yaml_data.items():
        try:
            schema_request = next(sr for sr in schema_requests if id(sr.yaml_data) == id(schema_request_yaml))
        except StopIteration:
            raise ValueError(f"Can't find a match for {schema_request_yaml} in {schema_requests}")
        schema_request.content_types.append(content_type)
        retval[content_type] = schema_request
    return retval
