# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, Union, TYPE_CHECKING
from .base_type import BaseType
from .imports import FileImport, ImportType, TypingSection

if TYPE_CHECKING:
    from .code_model import CodeModel


class ListType(BaseType):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        element_type: BaseType,
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.element_type = element_type
        self.max_items = yaml_data.get("maxItems")
        self.min_items = yaml_data.get("minItems")
        self.unique_items = yaml_data.get("uniqueItems")

    @property
    def serialization_type(self) -> str:
        return f"[{self.element_type.serialization_type}]"

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        if self.code_model.options["version_tolerant"] and self.element_type.is_xml:
            # this means we're version tolerant XML, we just return the XML element
            return self.element_type.type_annotation(
                is_operation_file=is_operation_file
            )
        return f"List[{self.element_type.type_annotation(is_operation_file=is_operation_file)}]"

    def description(self, *, is_operation_file: bool) -> str:
        return "" if is_operation_file else self.yaml_data.get("description", "")

    def xml_serialization_ctxt(self) -> Optional[str]:
        attrs_list = []
        base_xml_map = super().xml_serialization_ctxt()
        if base_xml_map:
            attrs_list.append(base_xml_map)

        # Attribute at the list level
        if self.xml_metadata.get("wrapped", False):
            attrs_list.append("'wrapped': True")

        # Attributes of the items
        item_xml_metadata = self.element_type.xml_metadata
        if item_xml_metadata.get("name"):
            attrs_list.append(f"'itemsName': '{item_xml_metadata['name']}'")
        if item_xml_metadata.get("prefix", False):
            attrs_list.append(f"'itemsPrefix': '{item_xml_metadata['prefix']}'")
        if item_xml_metadata.get("namespace", False):
            attrs_list.append(f"'itemsNs': '{item_xml_metadata['namespace']}'")

        return ", ".join(attrs_list)

    @property
    def docstring_type(self) -> str:
        if self.code_model.options["version_tolerant"] and self.element_type.xml_metadata:
            # this means we're version tolerant XML, we just return the XML element
            return self.element_type.docstring_type
        return f"list[{self.element_type.docstring_type}]"

    @property
    def docstring_text(self) -> str:
        if self.code_model.options["version_tolerant"] and self.element_type.xml_metadata:
            # this means we're version tolerant XML, we just return the XML element
            return self.element_type.docstring_text
        return f"list of {self.element_type.docstring_text}"

    @property
    def validation_map(self) -> Optional[Dict[str, Union[bool, int, str]]]:
        validation_map: Dict[str, Union[bool, int, str]] = {}
        if self.max_items:
            validation_map["max_items"] = self.max_items
            validation_map["min_items"] = self.min_items or 0
        if self.min_items:
            validation_map["min_items"] = self.min_items
        if self.unique_items:
            validation_map["unique"] = True
        return validation_map or None

    def get_json_template_representation(self, *, optional: bool = True, client_default_value_declaration: Optional[str] = None, description: Optional[str] = None) -> Any:
        return [self.element_type.get_json_template_representation(
            optional=optional, client_default_value_declaration=client_default_value_declaration, description=description
        )]

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, list)"

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "ListType":
        from . import build_type
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            element_type=build_type(yaml_data=yaml_data["elementType"], code_model=code_model),
        )

    def imports(self, *, is_operation_file: bool) -> FileImport:
        file_import = FileImport()
        if not (self.code_model.options["version_tolerant"] and self.element_type.is_xml):
            file_import.add_submodule_import(
                "typing", "List", ImportType.STDLIB, TypingSection.CONDITIONAL
            )
        file_import.merge(self.element_type.imports(is_operation_file=is_operation_file))
        return file_import
