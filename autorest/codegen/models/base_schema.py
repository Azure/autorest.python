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


class BaseSchema(BaseModel, ABC):
    """This is the base class for all schema models.

    :param yaml_data: the yaml data for this schema
    :type yaml_data: dict[str, Any]
    """

    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        super().__init__(yaml_data, code_model)
        self.default_value = yaml_data.get("defaultValue", None)
        self.xml_metadata = yaml_data.get("serialization", {}).get("xml", {})
        self.api_versions = set(value_dict["version"] for value_dict in yaml_data.get("apiVersions", []))

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "BaseSchema":
        return cls(yaml_data=yaml_data, code_model=code_model)

    @property
    def extra_description_information(self) -> str:
        return ""

    @property
    def has_xml_serialization_ctxt(self) -> bool:
        return bool(self.xml_metadata)

    def xml_serialization_ctxt(self) -> Optional[str]:
        """Return the serialization context in case this schema is used in an operation."""
        attrs_list = []
        if self.xml_metadata.get("name"):
            attrs_list.append(f"'name': '{self.xml_metadata['name']}'")
        if self.xml_metadata.get("attribute", False):
            attrs_list.append("'attr': True")
        if self.xml_metadata.get("prefix", False):
            attrs_list.append(f"'prefix': '{self.xml_metadata['prefix']}'")
        if self.xml_metadata.get("namespace", False):
            attrs_list.append(f"'ns': '{self.xml_metadata['namespace']}'")
        if self.xml_metadata.get("text"):
            attrs_list.append(f"'text': True")
        return ", ".join(attrs_list)

    def imports(self) -> FileImport:  # pylint: disable=no-self-use
        return FileImport()

    def model_file_imports(self) -> FileImport:
        return self.imports()

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
    @abstractmethod
    def docstring_text(self) -> str:
        """The names used in rtype documentation
        """
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

    def get_declaration(self, value: Any) -> str:  # pylint: disable=no-self-use
        """Return the current value from YAML as a Python string that represents the constant.

        Example, if schema is "bytearray" and value is "foo",
        should return bytearray("foo", encoding="utf-8")
        as a string.

        This is important for constant serialization.

        By default, return value, since it works sometimes (integer)
        """
        return str(value)

    @property
    def default_value_declaration(self) -> str:
        """Return the default value as string using get_declaration.
        """
        if self.default_value is None:
            return "None"
        return self.get_declaration(self.default_value)

    @property
    def validation_map(self) -> Optional[Dict[str, Union[bool, int, str]]]:  # pylint: disable=no-self-use
        return None

    @property
    def serialization_constraints(self) -> Optional[List[str]]:  # pylint: disable=no-self-use
        return None

    @abstractmethod
    def get_json_template_representation(self, **kwargs: Any) -> Any:
        """Template of what this schema would look like as JSON input"""
        ...
