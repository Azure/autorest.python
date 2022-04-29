# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union, TYPE_CHECKING

from .base_model import BaseModel
from .imports import FileImport

if TYPE_CHECKING:
    from .code_model import CodeModel


class BaseType(BaseModel, ABC):
    """This is the base class for all schema models.

    :param yaml_data: the yaml data for this schema
    :type yaml_data: dict[str, Any]
    """

    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        super().__init__(yaml_data, code_model)
        self.type = yaml_data["type"]

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "BaseType":
        return cls(yaml_data=yaml_data, code_model=code_model)

    def imports(self, *, is_operation_file: bool) -> FileImport:  # pylint: disable=no-self-use
        return FileImport()

    @property
    @abstractmethod
    def serialization_type(self) -> str:
        """The tag recognized by 'msrest' as a serialization/deserialization.

        'str', 'int', 'float', 'bool' or
        https://github.com/Azure/msrest-for-python/blob/b505e3627b547bd8fdc38327e86c70bdb16df061/msrest/serialization.py#L407-L416

        or the object schema name (e.g. DotSalmon).

        If list: '[str]'
        If dict: '{str}'
        """
        ...

    @property
    def client_default_value(self) -> Any:
        return self.yaml_data.get("clientDefaultValue")

    @abstractmethod
    def description(self, *, is_operation_file: bool) -> str:
        """The description"""
        ...

    @property
    @abstractmethod
    def docstring_text(self) -> str:
        """The names used in rtype documentation"""
        ...

    @property
    @abstractmethod
    def docstring_type(self) -> str:
        """The python type used for RST syntax input.

        Special case for enum, for instance: 'str or ~namespace.EnumName'
        """
        ...

    @abstractmethod
    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        """The python type used for type annotation

        Special case for enum, for instance: Union[str, "EnumName"]
        """
        ...

    @property
    def validation(self) -> Optional[Dict[str, Any]]:
        return None

    def get_declaration(self, value: Any) -> str:  # pylint: disable=no-self-use
        """Return the current value from YAML as a Python string that represents the constant.

        Example, if schema is "bytearray" and value is "foo",
        should return bytearray("foo", encoding="utf-8")
        as a string.

        This is important for constant serialization.

        By default, return value, since it works sometimes (integer)
        """
        return str(value)

    @abstractmethod
    def get_json_template_representation(self, *, optional: bool = True, client_default_value_declaration: Optional[str] = None, description: Optional[str] = None) -> Any:
        """Template of what this schema would look like as JSON input"""
        ...

    @property
    @abstractmethod
    def instance_check_template(self) -> str:
        """Template of what an instance check of a variable for this type would look like"""
        ...

    @property
    def serialization_constraints(self) -> List[str]:
        return []
