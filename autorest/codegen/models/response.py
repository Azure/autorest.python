# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, Optional, List, Set, Any, TYPE_CHECKING

from .base_model import BaseModel
from .base_type import BaseType
from .imports import FileImport, ImportType
from .primitive_types import IOType

if TYPE_CHECKING:
    from .code_model import CodeModel


class ResponseHeader(BaseModel):
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel", type: BaseType) -> None:
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
        type: Optional[BaseType] = None,
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.status_codes = yaml_data["statusCodes"]
        self.headers = headers
        self.is_error = yaml_data["isError"]
        self.type = type

    @property
    def is_stream_response(self) -> bool:
        """Is the response expected to be streamable, like a download."""
        return isinstance(self.type, IOType)

    def serialization_type(self, content_type: str) -> str:
        if self.type:
            return self.type.serialization_type
        return "None"

    def type_annotation(self) -> str:
        if self.type:
            return self.type.type_annotation(is_operation_file=True)
        return "None"

    @property
    def docstring_text(self) -> str:
        # if self.nullable:
        #     return f"{self.schema.docstring_text} or None"
        return self.type.docstring_text if self.type else ""

    @property
    def docstring_type(self) -> str:
        # if self.nullable:
        #     return f"{self.schema.docstring_type} or None"
        return self.type.docstring_type if self.type else ""

    def imports(self) -> FileImport:
        file_import = FileImport()
        if self.type:
            file_import.merge(self.type.imports(is_operation_file=True))
        return file_import

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "Response":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            headers=[ResponseHeader(header, code_model, code_model.lookup_schema(header["type"])) for header in yaml_data["headers"]],
            type=code_model.lookup_schema(id(yaml_data["type"])) if yaml_data.get("type") else None
        )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.status_codes}>"
