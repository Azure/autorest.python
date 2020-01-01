# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from .base_schema import BaseSchema
from .primitive_schemas import get_primitive_schema
from typing import Dict, Any, Optional

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
        value: Optional[str],
        schema: Optional["PrimitiveSchema"]
    ):
        super(ConstantSchema, self).__init__(yaml_data)
        self.value = value
        self.schema = schema

    def get_declaration(self, value):
        raise TypeError('Should not call get_declaration on a ConstantSchema. Call get_constant_value instead')

    def get_constant_value(self):
        """This string is used directly in template, as-is
        """
        if self.value is None:
            return "None"
        return self.schema.get_declaration(self.value)

    def get_serialization_type(self) -> str:
        """Returns the serialization value for msrest.

        :return: The serialization value for msrest
        :rtype: str
        """
        return self.schema.get_serialization_type()

    def get_python_type(self, namespace: Optional[str] = None) -> str:
        """The python type used for RST syntax input and type annotation.

        :param str namespace: Optional. The namespace for the models.
        """
        return self.schema.get_python_type(namespace)

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], **kwargs) -> "ConstantSchema":
        """Constructs a ConstantSchema from yaml data.

        :param yaml_data: the yaml data from which we will construct this schema
        :type yaml_data: dict[str, Any]

        :return: A created ConstantSchema
        :rtype: ~autorest.models.ConstantSchema
        """
        name = yaml_data["language"]["python"]["name"] if yaml_data["language"]["python"].get('name') else ""
        _LOGGER.debug("Parsing %s constant", name)
        return cls(
            yaml_data=yaml_data,
            value=yaml_data.get("value", {}).get("value", None),
            schema=get_primitive_schema(yaml_data['valueType'])
        )