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
from .utils import MultipleTypeModel

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

class Response(BaseModel, MultipleTypeModel):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        *,
        headers: List[ResponseHeader] = [],
        content_type_to_type: Optional[Dict[str, BaseType]] = None
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model, content_type_to_type=content_type_to_type)
        self.status_codes = yaml_data["statusCodes"]
        self.headers = headers
        self.is_error = yaml_data["isError"]

    @property
    def is_stream_response(self) -> bool:
        """Is the response expected to be streamable, like a download."""
        return isinstance(self.types[0], IOType)

    def imports(self, code_model) -> FileImport:
        file_import = FileImport()
        if not code_model.options["models_mode"] and any(t for t in self.types if getattr(t, "is_xml")):
            file_import.add_submodule_import(
                "xml.etree", "ElementTree", ImportType.STDLIB, alias="ET"
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
        return f"<{self.__class__.__name__} {self.status_codes}>"
