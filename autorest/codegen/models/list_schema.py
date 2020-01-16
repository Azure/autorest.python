# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, Union
from .base_schema import BaseSchema
from .imports import FileImport, ImportType


class ListSchema(BaseSchema):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        element_type: BaseSchema,
        *,
        max_items: int = None,
        min_items: int = None,
        unique_items: int = None
    ):
        super(ListSchema, self).__init__(yaml_data)
        self.element_type = element_type
        self.max_items = max_items
        self.min_items = min_items
        self.unique_items = unique_items


    def get_serialization_type(self) -> str:
        return '[{}]'.format(self.element_type.get_serialization_type())

    @property
    def type_annotation(self) -> str:
        return f'List[{self.element_type.type_annotation}]'

    def get_python_type(self, namespace: str) -> str:
        return f'list[{self.element_type.get_python_type(namespace)}]'

    def get_validation_map(self) -> Optional[Dict[str, Union[bool, int, str]]]:
        validation_map: Dict[str, Union[bool, int, str]] = {}
        if self.max_items:
            validation_map['max_items'] = self.max_items
            validation_map['min_items'] = self.min_items or 0
        if self.min_items:
            validation_map['min_items'] = self.min_items
        if self.unique_items:
            validation_map['unique'] = True
        return validation_map or None

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], **kwargs) -> "ListSchema":
        # TODO: for items, if the type is a primitive is it listed in type instead of $ref?
        element_schema = yaml_data['elementType']

        from . import build_schema  # pylint: disable=import-outside-toplevel
        element_type = build_schema(
            yaml_data=element_schema,
            **kwargs
        )

        return cls(
            yaml_data=yaml_data,
            element_type=element_type,
            max_items=yaml_data.get('maxItems'),
            min_items=yaml_data.get('minItems'),
            unique_items=yaml_data.get('uniqueItems'),
        )

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_from_import("typing", "List", ImportType.STDLIB)
        file_import.merge(self.element_type.imports())
        return file_import
