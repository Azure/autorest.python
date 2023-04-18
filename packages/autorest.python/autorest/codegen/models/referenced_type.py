# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, TYPE_CHECKING, Optional
from .base import BaseType
from .imports import FileImport, ImportType, TypingSection

if TYPE_CHECKING:
    from .code_model import CodeModel


class ReferencedType(BaseType):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.refer = self.yaml_data["refer"]
        splits = self.refer.split(".")
        self.name = splits[-1]
        self.import_path = ".".join(splits[:-1])
        self.package = self.yaml_data.get("package")
        self.version = self.yaml_data.get("version")

    @property
    def serialization_type(self) -> str:
        return self.name

    def type_annotation(self, **kwargs: Any) -> str:
        return self.name

    def description(self, *, is_operation_file: bool) -> str:
        return ""

    @property
    def instance_check_template(self) -> str:
        return f"isinstance({{}}, {self.name})"

    def docstring_type(self, **kwargs: Any) -> str:
        return f"~{self.import_path}.{self.name}"

    def docstring_text(self, **kwargs: Any) -> str:
        return self.name

    def get_json_template_representation(
        self,
        *,
        optional: bool = True,
        client_default_value_declaration: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Any:
        return f"{{}}  # you may refer to the documentation of {self.import_path}.{self.name} for more information"

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "ReferencedType":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
        )

    def imports(self, **kwargs: Any) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import(
            self.import_path, self.name, ImportType.LOCAL, TypingSection.REGULAR
        )
        return file_import

    @property
    def type_description(self) -> str:
        return f"{self.name}"
