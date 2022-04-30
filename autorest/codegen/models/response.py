# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, Optional, List, Set, Any, TYPE_CHECKING, Union

from .base_model import BaseModel
from .base_type import BaseType
from .imports import FileImport, ImportType
from .primitive_types import BinaryType

if TYPE_CHECKING:
    from .code_model import CodeModel


class ResponseHeader(BaseModel):
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel", type: BaseType) -> None:
        super().__init__(yaml_data, code_model)
        self.rest_api_name: str = yaml_data["restApiName"]
        self.type = type

    @property
    def serialization_type(self) -> str:
        return self.type.serialization_type

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "ResponseHeader":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=code_model.lookup_type(id(yaml_data["type"]))
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
        self.status_codes: List[Union[int, str]] = yaml_data["statusCodes"]
        self.headers = headers
        self.is_error: bool = yaml_data["isError"]
        self.type = type
        self.nullable = yaml_data.get("nullable")

    @property
    def is_stream_response(self) -> bool:
        """Is the response expected to be streamable, like a download."""
        return isinstance(self.type, BinaryType)

    @property
    def serialization_type(self) -> str:
        if self.type:
            return self.type.serialization_type
        return "None"

    def type_annotation(self) -> str:
        if self.type:
            type_annot = self.type.type_annotation(is_operation_file=True)
            if self.nullable:
                return f"Optional[{type_annot}]"
            return type_annot
        return "None"

    @property
    def docstring_text(self) -> str:
        if self.nullable and self.type:
            return f"{self.type.docstring_text} or None"
        return self.type.docstring_text if self.type else ""

    @property
    def docstring_type(self) -> str:
        if self.nullable and self.type:
            return f"{self.type.docstring_type} or None"
        return self.type.docstring_type if self.type else ""

    def imports(self) -> FileImport:
        file_import = FileImport()
        if self.type:
            file_import.merge(self.type.imports(is_operation_file=True))
        if self.nullable:
            file_import.add_submodule_import("typing", "Optional", ImportType.STDLIB)
        return file_import

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "Response":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            headers=[ResponseHeader.from_yaml(header, code_model) for header in yaml_data["headers"]],
            type=code_model.lookup_type(id(yaml_data["type"])) if yaml_data.get("type") else None
        )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.status_codes}>"
