# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, TYPE_CHECKING
from .base_type import BaseType
from .imports import FileImport, ImportType, TypingSection

if TYPE_CHECKING:
    from .code_model import CodeModel


class DictionaryType(BaseType):
    """Schema for dictionaries that will be serialized.

    :param yaml_data: the yaml data for this schema
    :type yaml_data: dict[str, Any]
    :param element_type: The type of the value for the dictionary
    :type element_type: ~autorest.models.BaseType
    """

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        element_type: BaseType,
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.element_type = element_type

    @property
    def serialization_type(self) -> str:
        """Returns the serialization value for msrest.

        :return: The serialization value for msrest
        :rtype: str
        """
        return f"{{{self.element_type.serialization_type}}}"

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        """The python type used for type annotation

        :return: The type annotation for this schema
        :rtype: str
        """
        return f"Dict[str, {self.element_type.type_annotation(is_operation_file=is_operation_file)}]"

    def description(self, *, is_operation_file: bool) -> str:
        return "" if is_operation_file else self.yaml_data.get("description", "")

    @property
    def docstring_text(self) -> str:
        return f"dict mapping str to {self.element_type.docstring_text}"

    @property
    def docstring_type(self) -> str:
        """The python type used for RST syntax input and type annotation.

        :param str namespace: Optional. The namespace for the models.
        """
        return f"dict[str, {self.element_type.docstring_type}]"

    def xml_serialization_ctxt(self) -> Optional[str]:
        raise NotImplementedError(
            "Dictionary schema does not support XML serialization."
        )

    def get_json_template_representation(self, *, optional: bool = True, client_default_value_declaration: Optional[str] = None, description: Optional[str] = None) -> Any:
        return {
            f'"str"': self.element_type.get_json_template_representation(
                optional=optional, client_default_value_declaration=client_default_value_declaration, description=description
            )
        }

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "DictionaryType":
        """Constructs a DictionaryType from yaml data.

        :param yaml_data: the yaml data from which we will construct this schema
        :type yaml_data: dict[str, Any]

        :return: A created DictionaryType
        :rtype: ~autorest.models.DictionaryType
        """
        element_schema: Dict[str, Any] = yaml_data["elementType"]

        from . import build_type  # pylint: disable=import-outside-toplevel

        element_type = build_type(yaml_data=element_schema, code_model=code_model)

        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            element_type=element_type,
        )

    def imports(self, *, is_operation_file: bool) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import(
            "typing", "Dict", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        file_import.merge(self.element_type.imports(is_operation_file=is_operation_file))
        return file_import

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, dict)"
