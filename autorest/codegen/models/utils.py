# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
from typing import Any, TypeVar, Dict, TYPE_CHECKING, List, Set
import logging

from .imports import FileImport, ImportType
from .base_schema import BaseSchema

if TYPE_CHECKING:
    from .code_model import CodeModel


_LOGGER = logging.getLogger(__name__)

JSON_REGEXP = re.compile(r"^(application|text)/(.+\+)?json$")

T = TypeVar("T")
OrderedSet = Dict[T, None]

UNDEFINED = object()

def _create_types_property(content_type_to_type: Dict[str, BaseSchema], code_model: "CodeModel") -> List[BaseSchema]:
    types: List[BaseSchema] = []
    seen_ids: Set[int] = set()
    for type in content_type_to_type.values():
        if id(type.yaml_data) not in seen_ids:
            types.append(type)
        seen_ids.add(id(type.yaml_data))
    return types


def get_schema(
    code_model: "CodeModel", schema: Any, serialized_name: str = "unknown"
) -> BaseSchema:
    if not isinstance(schema, dict):
        return schema
    schema_id = id(schema)
    _LOGGER.debug("Looking for id %s for member %s", schema_id, serialized_name)
    try:
        return code_model.lookup_schema(schema_id)
    except KeyError:
        _LOGGER.critical("Unable to ref the object")
        raise

class MultipleTypeModel:
    def __init__(self, content_type_to_type: Dict[str, BaseSchema]):
        self.content_type_to_type = content_type_to_type
        self.types = self._create_types_property()

    def _create_types_property(self) -> List[BaseSchema]:
        types: List[BaseSchema] = []
        seen_ids: Set[int] = set()
        for type in self.content_type_to_type.values():
            if id(type.yaml_data) not in seen_ids:
                types.append(type)
            seen_ids.add(id(type.yaml_data))
        return types

    def serialization_type(self, content_type: str) -> str:
        if self.content_type_to_type:
            return self.content_type_to_type[content_type].serialization_type
        return "None"

    def type_annotation(self) -> str:
        if not self.types:
            return "None"
        if len(self.types) > 1:
            return f'Union[{", ".join(type.type_annotation(is_operation_file=True) for type in self.types)}]'
        return self.types[0].type_annotation(is_operation_file=True)

    @property
    def docstring_text(self) -> str:
        # if self.nullable:
        #     return f"{self.schema.docstring_text} or None"
        return " or ".join(t.docstring_text for t in self.types) or "None"

    @property
    def docstring_type(self) -> str:
        # if self.nullable:
        #     return f"{self.schema.docstring_type} or None"
        return " or ".join(t.docstring_type for t in self.types) or "None"

    def type_to_content_types(self, yaml_id: int) -> List[str]:
        return [
            k for k, v in self.content_type_to_type.items()
            if id(v.yaml_data) == yaml_id
        ]

    def imports(self) -> FileImport:
        file_import = FileImport
        if len(self.types) > 1:
            file_import.add_import("typing", "Union", ImportType.STDLIB)
        for type in self.types:
            file_import.merge(type.imports())
        return file_import
