# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import cast, Any, Dict, Union, List, Optional

from .base_model import BaseModel
from .constant_schema import ConstantSchema
from .imports import FileImport, ImportType, TypingSection
from .base_schema import BaseSchema


class Property(BaseModel):  # pylint: disable=too-many-instance-attributes
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        schema: BaseSchema,
        original_swagger_name: str,
        *,
        flattened_names: Optional[List[str]] = None,
        description: Optional[str] = None,
        client_default_value: Optional[Any] = None
    ) -> None:
        super().__init__(yaml_data)
        self.name = name
        self.schema = schema
        self.original_swagger_name = original_swagger_name
        self.flattened_names = flattened_names or []

        self.required: bool = yaml_data.get("required", False)
        self.readonly: bool = yaml_data.get("readOnly", False)
        self.is_discriminator: bool = yaml_data.get("isDiscriminator", False)
        # this bool doesn't consider you to be constant if you are a discriminator
        self.constant: bool = isinstance(self.schema, ConstantSchema) and not self.is_discriminator
        self._description = description or yaml_data["language"]["python"]["description"]

        validation_map: Dict[str, Union[bool, int, str]] = {}
        if self.required:
            validation_map["required"] = True
        if self.readonly:
            validation_map["readonly"] = True
        if self.constant:
            validation_map["constant"] = True
        if self.schema.validation_map:
            validation_map_from_schema = cast(Dict[str, Union[bool, int, str]], self.schema.validation_map)
            validation_map.update(validation_map_from_schema)
        self.validation_map = validation_map or None
        self.client_default_value = client_default_value

    @property
    def description(self) -> str:
        description = self._description.strip()
        if description and description[-1] != ".":
            description += "."
        return description + " "

    @property
    def escaped_swagger_name(self) -> str:
        """Return the RestAPI name correctly escaped for serialization.
        """
        if self.flattened_names:
            return ".".join(n.replace(".", "\\\\.") for n in self.flattened_names)
        return self.original_swagger_name.replace(".", "\\\\.")

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], **kwargs) -> "Property":
        from . import build_schema  # pylint: disable=import-outside-toplevel

        name = yaml_data["language"]["python"]["name"]
        has_additional_properties = kwargs.pop("has_additional_properties", None)
        if name == "additional_properties" and has_additional_properties:
            name = "additional_properties1"
        schema = build_schema(yaml_data=yaml_data["schema"], **kwargs)
        return cls(
            yaml_data=yaml_data,
            name=name,
            schema=schema,
            original_swagger_name=yaml_data["serializedName"],
            flattened_names=yaml_data.get("flattenedNames", []),
            client_default_value=yaml_data.get("clientDefaultValue"),
        )

    @property
    def constant_declaration(self) -> str:
        if self.schema:
            if isinstance(self.schema, ConstantSchema):
                return self.schema.get_declaration(self.schema.value)
            raise ValueError(
                "Trying to get constant declaration for a schema that is not ConstantSchema"
                )
        raise ValueError("Trying to get a declaration for a schema that doesn't exist")

    @property
    def serialization_type(self) -> str:
        return self.schema.serialization_type

    @property
    def xml_metadata(self) -> str:
        if self.schema.has_xml_serialization_ctxt:
            return f", 'xml': {{{self.schema.xml_serialization_ctxt()}}}"
        return ""

    @property
    def default_value(self) -> Any:
        return self.client_default_value or self.schema.default_value

    @property
    def default_value_declaration(self) -> Any:
        if self.client_default_value:
            return self.schema.get_declaration(self.client_default_value)
        return self.schema.default_value_declaration

    @property
    def type_annotation(self) -> str:
        if self.required:
            return self.schema.type_annotation
        return f"Optional[{self.schema.type_annotation}]"

    def model_file_imports(self) -> FileImport:
        file_import = self.schema.model_file_imports()
        if not self.required:
            file_import.add_from_import("typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL)
        return file_import
