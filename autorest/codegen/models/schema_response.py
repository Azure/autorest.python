# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, Optional, List, Union, Any, cast, TYPE_CHECKING

from .base_model import BaseModel
from .base_schema import BaseSchema
from .object_schema import ObjectSchema
from .imports import FileImport, ImportType
from .utils import get_schema
from .primitive_schemas import IOSchema

if TYPE_CHECKING:
    from .code_model import CodeModel


class HeaderResponse:
    def __init__(self, name: str, schema) -> None:
        self.name = name
        self.schema = schema

    @property
    def serialization_type(self) -> str:
        return self.schema.serialization_type


class SchemaResponse(BaseModel):
    def __init__(
        self,
        code_model: "CodeModel",
        yaml_data: Dict[str, Any],
        schema: Optional[BaseSchema],
        content_types: List[str],
        status_codes: List[Union[str, int]],
        headers: List[HeaderResponse],
        binary: bool,
    ) -> None:
        super().__init__(yaml_data)
        self.code_model = code_model
        self.schema = schema
        self.content_types = content_types
        self.status_codes = status_codes
        self.headers = headers
        self.binary = binary
        self.nullable = self.yaml_data.get("nullable", False)

    @property
    def has_body(self) -> bool:
        """Tell if that response defines a body.
        """
        return bool(self.schema)

    @property
    def has_headers(self) -> bool:
        """Tell if that response defines headers.
        """
        return bool(self.headers)

    @property
    def serialization_type(self) -> str:
        if self.schema:
            return self.schema.serialization_type
        return "None"

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        if not self.schema:
            return "None"
        if self.nullable:
            return f"Optional[{self.schema.type_annotation(is_operation_file=is_operation_file)}]"
        return self.schema.type_annotation(is_operation_file=is_operation_file)

    @property
    def docstring_text(self) -> str:
        if not self.schema:
            return "None"
        if self.nullable:
            return f"{self.schema.docstring_text} or None"
        return self.schema.docstring_text

    @property
    def docstring_type(self) -> str:
        if not self.schema:
            return "None"
        if self.nullable:
            return f"{self.schema.docstring_type} or None"
        return self.schema.docstring_type

    @property
    def is_stream_response(self) -> bool:
        """Is the response expected to be streamable, like a download."""
        return self.binary

    @property
    def is_exception(self) -> bool:
        if self.schema:
            return cast(ObjectSchema, self.schema).is_exception
        return False

    @property
    def is_xml(self) -> bool:
        return any(["xml" in ct for ct in self.content_types])

    def imports(self, code_model) -> FileImport:
        file_import = FileImport()
        if not code_model.options["models_mode"] and self.is_xml:
            file_import.add_submodule_import("xml.etree", "ElementTree", ImportType.STDLIB, alias="ET")
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], *, code_model: "CodeModel") -> "SchemaResponse":
        binary = yaml_data.get("binary", False)
        if binary:
            schema: BaseSchema = IOSchema(namespace=None, yaml_data={})
        else:
            schema = get_schema(code_model, yaml_data.get("schema"))
        return cls(
            code_model=code_model,
            yaml_data=yaml_data,
            schema=schema,
            content_types=yaml_data["protocol"]["http"].get("mediaTypes", []),
            status_codes=[
                int(code) if code != "default" else "default" for code in yaml_data["protocol"]["http"]["statusCodes"]
            ],
            headers=[
                HeaderResponse(
                    header_prop["header"], get_schema(code_model, header_prop["schema"], header_prop["header"])
                )
                for header_prop in yaml_data["protocol"]["http"].get("headers", [])
            ],
            binary=binary,
        )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.status_codes}>"
