# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import cast, Any, Dict, Union, List, Optional

from .base_model import BaseModel
from .constant_schema import ConstantSchema
from .imports import FileImport, ImportType
from .base_schema import BaseSchema


class Property(BaseModel):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        schema: BaseSchema,
        original_swagger_name: str,
        *,
        flattened_names: Optional[List[str]] = None,
        description: Optional[str] = None,
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

        if description:
            self.description = description
        else:
            self.description = yaml_data["language"]["python"]["description"]

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
        )

    @property
    def type_annotation(self) -> str:
        if self.required:
            return self.schema.type_annotation
        return f"Optional[{self.schema.type_annotation}]"

    def model_file_imports(self) -> FileImport:
        file_import = self.schema.model_file_imports()
        if not self.required:
            file_import.add_from_import("typing", "Optional", ImportType.STDLIB)
        return file_import
