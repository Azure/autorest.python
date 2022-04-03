# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
from typing import Any, TYPE_CHECKING, Type
import logging
from .base_schema import BaseSchema
from .dictionary_schema import DictionarySchema
from .list_schema import ListSchema
from .object_schema import ObjectSchema
from .imports import FileImport, ImportType, TypingSection, ImportModel

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

def import_mutable_mapping(file_import: FileImport):
    file_import.add_import("sys", ImportType.STDLIB)
    file_import.define_mypy_type("JSONObject", "MutableMapping[str, Any] # pylint: disable=unsubscriptable-object", None, ((3, 9), ImportModel(
        TypingSection.CONDITIONAL, ImportType.STDLIB, "collections.abc", submodule_name="MutableMapping"
    ), ImportModel(
        TypingSection.CONDITIONAL, ImportType.STDLIB, "typing", submodule_name="MutableMapping"
    )))

def is_or_contain_schema(schema: BaseSchema, t: Type) -> bool:
    if isinstance(schema, (DictionarySchema, ListSchema)):
        return is_or_contain_schema(schema.element_type, t)
    return isinstance(schema, t)
