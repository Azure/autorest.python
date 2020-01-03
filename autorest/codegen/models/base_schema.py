# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

from .base_model import BaseModel
from .imports import FileImport


class BaseSchema(BaseModel, ABC):
    """This is the base class for all schema models.

    :param yaml_data: the yaml data for this schema
    :type yaml_data: dict[str, Any]
    """
    def __init__(self, yaml_data: Dict[str, Any]):
        super().__init__(yaml_data)
        self.default_value = yaml_data.get('defaultValue', None)

    @classmethod
    def from_yaml(cls, yaml_data, **kwargs):  # pylint: disable=unused-argument
        return cls(yaml_data=yaml_data)

    def imports(self):  # pylint: disable=no-self-use
        return FileImport()

    @abstractmethod
    def get_serialization_type(self) -> str:
        """The tag recognized by 'msrest' as a serialization/deserialization.

        'str', 'int', 'float', 'bool' or
        https://github.com/Azure/msrest-for-python/blob/b505e3627b547bd8fdc38327e86c70bdb16df061/msrest/serialization.py#L407-L416

        or the object schema name (e.g. DotSalmon).

        If list: '[str]'
        If dict: '{str}'
        """
        ...

    @abstractmethod
    def get_python_type(self, namespace: str) -> str:
        """The python type used for RST syntax input.

        Special case for enum, for instance: 'str or ~namespace.EnumName'
        """
        ...

    def get_python_type_annotation(self) -> str:
        """The python type used for type annotation

        Special case for enum, for instance: Union[str, "EnumName"]
        """
        return self.get_python_type("")

    def get_declaration(self, value) -> str: # pylint: disable=no-self-use
        """Return the current value from YAML as a Python string that represents the constant.

        Example, if schema is "bytearray" and value is "foo",
        should return bytearray("foo", encoding="utf-8")
        as a string.

        This is important for constant serialization.

        By default, return value, since it works sometimes (integer)
        """
        return str(value)

    def get_validation_map(self) -> Optional[Dict[str, Union[int, bool]]]: # pylint: disable=no-self-use
        return None

    def get_serialization_constraints(self) -> List[str]: # pylint: disable=no-self-use
        return None
