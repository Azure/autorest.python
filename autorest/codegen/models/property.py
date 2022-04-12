# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, TYPE_CHECKING

from .base_model import BaseModel
from .constant_schema import ConstantSchema
from .base_schema import BaseSchema

if TYPE_CHECKING:
    from .code_model import CodeModel


class Property(BaseModel):  # pylint: disable=too-many-instance-attributes
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        type: BaseSchema,
        *,
        client_default_value: Optional[Any] = None,
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.name = self.yaml_data["name"]
        self.type = type
        self.optional: bool = self.yaml_data["optional"]
        self.readonly: bool = self.yaml_data["readonly"]
        self.is_discriminator: bool = yaml_data.get("isDiscriminator", False)
        self.client_default_value = client_default_value

    def description(self, *, is_operation_file: bool) -> str:
        if is_operation_file:
            return ""
        return self.type.description(is_operation_file=False)

    @property
    def constant(self) -> bool:
        # this bool doesn't consider you to be constant if you are a discriminator
        # you also have to be required to be considered a constant
        return (
            isinstance(self.type, ConstantSchema)
            and not self.optional
            and not self.is_discriminator
        )

    @classmethod
    def from_yaml(
        cls,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
    ) -> "Property":
        from . import build_schema  # pylint: disable=import-outside-toplevel
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=build_schema(yaml_data["type"], code_model)
        )

    @property
    def is_input(self):
        return not (self.constant or self.readonly or self.is_discriminator)

    @property
    def serialization_type(self) -> str:
        return self.type.serialization_type

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        if self.optional:
            return f"Optional[{self.type.type_annotation(is_operation_file=is_operation_file)}]"
        return self.type.type_annotation(is_operation_file=is_operation_file)

    def get_json_template_representation(self, **kwargs: Any) -> Any:
        kwargs["optional"] = self.optional
        if self.client_default_value:
            kwargs["default_value_declaration"] = self.type.get_declaration(
                self.client_default_value
            )
        if self.description(is_operation_file=False):
            kwargs["description"] = self.description
        return self.type.get_json_template_representation(**kwargs)
