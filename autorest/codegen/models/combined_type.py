# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, Optional, TYPE_CHECKING

from autorest.codegen.models.imports import FileImport, ImportType
from .base_type import BaseType

if TYPE_CHECKING:
    from .code_model import CodeModel


class CombinedType(BaseType):
    """A type that consists of multiple different types"""

    def __init__(
        self, yaml_data: Dict[str, Any], code_model: "CodeModel", types: List[BaseType]
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.types = types

    @property
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

    def description(self, *, is_operation_file: bool) -> str:  # pylint: disable=unused-argument
        if len(self.types) == 2:
            return (
                f"Is either a {self.types[0].type} type or a {self.types[1].type} type."
            )
        return (
            f"Is one of the following types: {', '.join([t.type for t in self.types])}"
        )

    @property
    def docstring_text(self) -> str:
        return " or ".join(t.docstring_text for t in self.types)

    @property
    def docstring_type(self) -> str:
        return " or ".join(t.docstring_type for t in self.types)

    def type_annotation(self, *, is_operation_file: bool = False) -> str:  # pylint: disable=unused-argument
        """The python type used for type annotation

        Special case for enum, for instance: Union[str, "EnumName"]
        """
        return f'Union[{", ".join(type.type_annotation(is_operation_file=True) for type in self.types)}]'

    def get_json_template_representation(
        self,
        *,
        optional: bool = True,
        client_default_value_declaration: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Any:
        """Template of what this schema would look like as JSON input"""
        raise ValueError(
            "You shouldn't get a JSON template representation of multiple types"
        )

    @property
    def instance_check_template(self) -> str:
        """Template of what an instance check of a variable for this type would look like"""
        raise ValueError("You shouldn't do instance checks on a multiple type")

    def imports(self, *, is_operation_file: bool) -> FileImport:
        file_import = FileImport()
        for type in self.types:
            file_import.merge(type.imports(is_operation_file=is_operation_file))
        file_import.add_submodule_import("typing", "Union", ImportType.STDLIB)
        return file_import

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "BaseType":
        from . import build_type

        return cls(
            yaml_data,
            code_model,
            [build_type(t, code_model) for t in yaml_data["types"]],
        )
