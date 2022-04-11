# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, Optional, List, Set, Any, TYPE_CHECKING

from .base_model import BaseModel
from .base_schema import BaseSchema
from .imports import FileImport, ImportType
from .primitive_schemas import IOSchema

if TYPE_CHECKING:
    from .code_model import CodeModel


class ResponseHeader(BaseModel):
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel", type: BaseSchema) -> None:
        super().__init__(yaml_data, code_model)
        self.name = yaml_data["name"]
        self.type = type

    @property
    def serialization_type(self) -> str:
        return self.type.serialization_type

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "ResponseHeader":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=code_model.lookup_schema(id(yaml_data["type"]))
        )

class Response(BaseModel):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        *,
        headers: List[ResponseHeader] = [],
        content_type_to_type: Optional[Dict[str, BaseSchema]] = None
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.status_code = yaml_data["statusCode"]
        self.headers = headers
        self.is_error = yaml_data["isError"]
        self.content_type_to_type = content_type_to_type or {}
        self.types = self._get_types()

    def _get_types(self):
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

    @property
    def is_stream_response(self) -> bool:
        """Is the response expected to be streamable, like a download."""
        return isinstance(self.types[0], IOSchema)

    def imports(self, code_model) -> FileImport:
        file_import = FileImport()
        if not code_model.options["models_mode"] and any(t for t in self.types if getattr(t, "is_xml")):
            file_import.add_submodule_import(
                "xml.etree", "ElementTree", ImportType.STDLIB, alias="ET"
            )
        if len(self.types) > 1:
            file_import.add_submodule_import(
                "typing", "Union", ImportType.STDLIB
            )
        return file_import

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "Response":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            headers=[ResponseHeader(header, code_model, code_model.lookup_schema(header["type"])) for header in yaml_data["headers"]],
            content_type_to_type={
                content_type: code_model.lookup_schema(id(type_yaml_data))
                for content_type, type_yaml_data in yaml_data.get("contentTypeToType", {}).items()
            }
        )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.status_code}>"
