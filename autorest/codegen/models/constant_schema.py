# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, Any, Optional, TYPE_CHECKING
from .base_schema import BaseSchema
from .primitive_schemas import get_primitive_schema, PrimitiveSchema
from .imports import FileImport

if TYPE_CHECKING:
    from .code_model import CodeModel

_LOGGER = logging.getLogger(__name__)


class ConstantSchema(BaseSchema):
    """Schema for constants that will be serialized.

    :param yaml_data: the yaml data for this schema
    :type yaml_data: dict[str, Any]
    :param str value: The actual value of this constant.
    :param schema: The schema for the value of this constant.
    :type schema: ~autorest.models.PrimitiveSchema
    """

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        schema: PrimitiveSchema,
        value: Optional[str],
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.value = value
        self.schema = schema

    def get_declaration(self, value: Any):
        if value != self.value:
            _LOGGER.warning(
                "Passed in value of %s differs from constant value of %s. Choosing constant value",
                str(value),
                str(self.value),
            )
        if self.value is None:
            return "None"
        return self.schema.get_declaration(self.value)

    @property
    def serialization_type(self) -> str:
        """Returns the serialization value for msrest.

        :return: The serialization value for msrest
        :rtype: str
        """
        return self.schema.serialization_type

    @property
    def docstring_text(self) -> str:
        return "constant"

    @property
    def docstring_type(self) -> str:
        """The python type used for RST syntax input and type annotation.

        :param str namespace: Optional. The namespace for the models.
        """
        return self.schema.docstring_type

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        return self.schema.type_annotation(is_operation_file=is_operation_file)

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "ConstantSchema":
        """Constructs a ConstantSchema from yaml data.

        :param yaml_data: the yaml data from which we will construct this schema
        :type yaml_data: dict[str, Any]

        :return: A created ConstantSchema
        :rtype: ~autorest.models.ConstantSchema
        """
        name = (
            yaml_data["language"]["python"]["name"]
            if yaml_data["language"]["python"].get("name")
            else ""
        )
        _LOGGER.debug("Parsing %s constant", name)
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            schema=get_primitive_schema(
                yaml_data=yaml_data["valueType"], code_model=code_model
            ),
            value=yaml_data.get("value", {}).get("value", None),
        )

    def get_json_template_representation(self, **kwargs: Any) -> Any:
        kwargs["default_value_declaration"] = self.schema.get_declaration(self.value)
        return self.schema.get_json_template_representation(**kwargs)

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.merge(self.schema.imports())
        return file_import

    def model_file_imports(self) -> FileImport:
        file_import = self.imports()
        file_import.merge(self.schema.model_file_imports())
        return file_import
