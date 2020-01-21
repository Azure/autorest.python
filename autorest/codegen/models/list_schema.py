# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, Union
from .base_schema import BaseSchema


class ListSchema(BaseSchema):
    def __init__(
        self,
        namespace: str,
        yaml_data: Dict[str, Any],
        element_type: BaseSchema,
        *,
        max_items: int = None,
        min_items: int = None,
        unique_items: int = None
    ):
        super(ListSchema, self).__init__(namespace=namespace, yaml_data=yaml_data)
        self.element_type = element_type
        self.max_items = max_items
        self.min_items = min_items
        self.unique_items = unique_items


    def get_serialization_type(self) -> str:
        return '[{}]'.format(self.element_type.get_serialization_type())

    def get_python_type_annotation(self) -> str:
        return f'List[{self.element_type.get_python_type_annotation()}]'

    @property
    def docstring_type(self) -> str:
        return f'list[{self.element_type.docstring_type}]'

    @property
    def docstring_text(self) -> str:
        return "list"

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
    def from_yaml(cls, namespace: str, yaml_data: Dict[str, Any], **kwargs) -> "ListSchema":
        # TODO: for items, if the type is a primitive is it listed in type instead of $ref?
        element_schema = yaml_data['elementType']

        from . import build_schema  # pylint: disable=import-outside-toplevel
        element_type = build_schema(
            yaml_data=element_schema,
            **kwargs
        )

        return cls(
            namespace=namespace,
            yaml_data=yaml_data,
            element_type=element_type,
            max_items=yaml_data.get('maxItems'),
            min_items=yaml_data.get('minItems'),
            unique_items=yaml_data.get('uniqueItems'),
        )
