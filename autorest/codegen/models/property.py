# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, TYPE_CHECKING, List

from .base_model import BaseModel
from .constant_type import ConstantType
from .base_type import BaseType
from .enum_type import EnumType
from .imports import FileImport, ImportType, TypingSection
from .utils import add_to_description, add_to_pylint_disable

if TYPE_CHECKING:
    from .code_model import CodeModel
    from .model_type import ModelType


class Property(BaseModel):  # pylint: disable=too-many-instance-attributes
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        type: BaseType,
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.rest_api_name: str = self.yaml_data["restApiName"]
        self.client_name: str = self.yaml_data["clientName"]
        self.type = type
        self.optional: bool = self.yaml_data["optional"]
        self.readonly: bool = self.yaml_data.get("readonly", False)
        self.is_discriminator: bool = yaml_data.get("isDiscriminator", False)
        self.client_default_value = yaml_data.get("clientDefaultValue", None)
        if self.client_default_value is None:
            self.client_default_value = self.type.client_default_value
        self.flattened_names: List[str] = yaml_data.get("flattenedNames", [])

    @property
    def pylint_disable(self) -> str:
        retval: str = ""
        if self.yaml_data.get("pylintDisable"):
            retval = add_to_pylint_disable(retval, self.yaml_data["pylintDisable"])
        return retval

    def description(self, *, is_operation_file: bool) -> str:
        from .model_type import ModelType

        description = self.yaml_data.get("description", "")
        if not (self.optional or self.client_default_value):
            description = add_to_description(description, "Required.")
        # don't want model type documentation as part of property doc
        type_description = (
            ""
            if isinstance(self.type, ModelType)
            else self.type.description(is_operation_file=is_operation_file)
        )
        return add_to_description(description, type_description)

    @property
    def client_default_value_declaration(self) -> str:
        if self.client_default_value is not None:
            return self.type.get_declaration(self.client_default_value)
        if self.type.client_default_value is not None:
            return self.type.get_declaration(self.type.client_default_value)
        return "None"

    @property
    def constant(self) -> bool:
        # this bool doesn't consider you to be constant if you are a discriminator
        # you also have to be required to be considered a constant
        return (
            isinstance(self.type, ConstantType)
            and not self.optional
            and not self.is_discriminator
        )

    @property
    def is_input(self):
        return not (self.constant or self.readonly or self.is_discriminator)

    @property
    def serialization_type(self) -> str:
        return self.type.serialization_type

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        if self.optional and self.client_default_value is None:
            return f"Optional[{self.type.type_annotation(is_operation_file=is_operation_file)}]"
        return self.type.type_annotation(is_operation_file=is_operation_file)

    def get_json_template_representation(
        self,
        *,
        optional: bool = True,  # pylint: disable=unused-argument
        client_default_value_declaration: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Any:
        if self.client_default_value:
            client_default_value_declaration = self.type.get_declaration(
                self.client_default_value
            )
        if self.description(is_operation_file=True):
            description = self.description(is_operation_file=True)
        return self.type.get_json_template_representation(
            optional=self.optional,
            client_default_value_declaration=client_default_value_declaration,
            description=description,
        )

    def get_polymorphic_subtypes(self, polymorphic_subtypes: List["ModelType"]) -> None:
        from .model_type import ModelType

        if isinstance(self.type, ModelType):
            is_polymorphic_subtype = (
                self.type.discriminator_value and not self.type.discriminated_subtypes
            )
            if (
                self.type.name not in (m.name for m in polymorphic_subtypes)
                and is_polymorphic_subtype
            ):
                polymorphic_subtypes.append(self.type)

    @property
    def validation(self) -> Optional[Dict[str, Any]]:
        retval: Dict[str, Any] = {}
        if not self.optional:
            retval["required"] = True
        if self.readonly:
            retval["readonly"] = True
        if self.constant:
            retval["constant"] = True
        retval.update(self.type.validation or {})
        return retval or None

    @property
    def attribute_map(self) -> str:
        if self.flattened_names:
            attribute_key = ".".join(
                n.replace(".", "\\\\.") for n in self.flattened_names
            )
        else:
            attribute_key = self.rest_api_name.replace(".", "\\\\.")
        if self.type.xml_serialization_ctxt:
            xml_metadata = f", 'xml': {{{self.type.xml_serialization_ctxt}}}"
        else:
            xml_metadata = ""
        return f'"{self.client_name}": {{"key": "{attribute_key}", "type": "{self.serialization_type}"{xml_metadata}}},'

    def imports(self) -> FileImport:
        from .model_type import ModelType

        file_import = self.type.imports(is_operation_file=False)
        if self.optional and self.client_default_value is None:
            file_import.add_submodule_import("typing", "Optional", ImportType.STDLIB)
        if isinstance(self.type, ModelType):
            file_import.add_submodule_import(
                "..",
                "models",
                ImportType.LOCAL,
                TypingSection.TYPING,
                alias="_models",
            )
        if self.code_model.options["models_mode"] == "dpg":
            file_import.add_submodule_import(
                "azure.core.serialization", "rest_field", ImportType.AZURECORE
            )
            if isinstance(self.type, EnumType):
                file_import.add_submodule_import("typing", "Union", ImportType.STDLIB)
        return file_import

    @classmethod
    def from_yaml(
        cls,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
    ) -> "Property":
        from . import build_type  # pylint: disable=import-outside-toplevel

        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=build_type(yaml_data["type"], code_model),
        )
