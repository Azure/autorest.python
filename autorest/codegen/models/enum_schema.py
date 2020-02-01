# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, Optional, Set
from .base_schema import BaseSchema
from .imports import FileImport, ImportType

class EnumValue:
    """Model containing necessary information for a single value of an enum.

    :param str name: The name of this enum value
    :param str value: The value of this enum value
    :param str description: Optional. The description for this enum value
    """
    def __init__(self, name: str, value: str, description: Optional[str] = None):
        self.name = name
        self.value = value
        self.description = description

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any]) -> "EnumValue":
        """Constructs an EnumValue from yaml data.

        :param yaml_data: the yaml data from which we will construct this object
        :type yaml_data: dict[str, Any]

        :return: A created EnumValue
        :rtype: ~autorest.models.EnumValue
        """
        return cls(
            name=yaml_data['language']['python']['name'],
            value=yaml_data['value'],
            description=yaml_data['language']['python'].get('description')
        )

class EnumSchema(BaseSchema):
    """Schema for enums that will be serialized.

    :param yaml_data: the yaml data for this schema
    :type yaml_data: dict[str, Any]
    :param str description: The description of this enum
    :param enum_type: The type of the enum. Currently we're only allowing strings.
    :type element_type: ~autorest.models.PrimitiveSchema
    :param values: List of the values for this enum
    :type values: list[~autorest.models.EnumValue]
    """
    def __init__(
        self,
        namespace: str,
        yaml_data: Dict[str, Any],
        description: str,
        enum_type: str,
        values: List["EnumValue"]
    ):
        super(EnumSchema, self).__init__(namespace=namespace, yaml_data=yaml_data)
        self.description = description
        self.enum_type = enum_type
        self.values = values

    @property
    def serialization_type(self) -> str:
        """Returns the serialization value for msrest.

        :return: The serialization value for msrest
        :rtype: str
        """
        return "str"

    @property
    def type_annotation(self) -> str:
        """The python type used for type annotation

        :return: The type annotation for this schema
        :rtype: str
        """
        return f'Union[str, \"{self.enum_type}\"]'

    @property
    def operation_type_annotation(self) -> str:
        """The python type used for type annotation

        :return: The type annotation for this schema
        :rtype: str
        """
        return f'Union[str, \"models.{self.enum_type}\"]'

    def get_declaration(self, value) -> str:
        return f'"{value}"'

    @property
    def docstring_text(self) -> str:
        return self.enum_type

    @property
    def docstring_type(self) -> str:
        """The python type used for RST syntax input and type annotation.
        """
        return f"str or ~{self.namespace}.models.{self.enum_type}"

    @staticmethod
    def _get_enum_values(yaml_data: List[Dict[str, Any]]) -> List["EnumValue"]:
        """Creates the list of values for this enum.

        :param yaml_data: yaml data about the enum's values
        :type yaml_data: dict[str, Any]
        :return: The list of values for this enum
        :rtype: list[~autorest.models.EnumValue]
        """
        values = []
        seen_enums: Set[str] = set()

        for enum in yaml_data:
            enum_name = enum['language']['python']['name']
            if enum_name in seen_enums:
                continue
            values.append(EnumValue.from_yaml(enum))
            seen_enums.add(enum_name)
        return values

    @classmethod
    def from_yaml(cls, namespace: str, yaml_data: Dict[str, Any], **kwargs) -> "EnumSchema":
        """Constructs an EnumSchema from yaml data.

        :param yaml_data: the yaml data from which we will construct this schema
        :type yaml_data: dict[str, Any]

        :return: A created EnumSchema
        :rtype: ~autorest.models.EnumSchema
        """
        enum_type = yaml_data['language']['python']['name']
        values = EnumSchema._get_enum_values(yaml_data['choices'])

        return cls(
            namespace=namespace,
            yaml_data=yaml_data,
            description=yaml_data['language']['python']['description'],
            enum_type=enum_type,
            values=values
        )

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_from_import("typing", "Union", ImportType.STDLIB)
        return file_import
