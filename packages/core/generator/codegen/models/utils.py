# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import List, Set
from .model_type import ModelType

def sort_model_types(model_types: List[ModelType]) -> List[ModelType]:
    seen_schema_names: Set[str] = set()
    seen_schema_yaml_ids: Set[int] = set()
    sorted_object_schemas: List[ModelType] = []
    for schema in sorted(model_types, key=lambda x: x.name.lower()):
        sorted_object_schemas.extend(_sort_model_types_helper(schema, seen_schema_names, seen_schema_yaml_ids))
    return sorted_object_schemas

def _sort_model_types_helper(current: ModelType, seen_schema_names: Set[str], seen_schema_yaml_ids: Set[int]) -> List[ModelType]:
    if current.id in seen_schema_yaml_ids:
        return []
    if current.name in seen_schema_names:
        raise ValueError(f"Detected a cycle in the schema hierarchy. Schema name: {current.name}")
    ancestors = [current]
    if current.parents:
        for parent in current.parents:
            if parent.id in seen_schema_yaml_ids:
                continue
            seen_schema_names.add(current.name)
            seen_schema_yaml_ids.add(current.id)
            ancestors = _sort_model_types_helper(parent, seen_schema_names, seen_schema_yaml_ids) + ancestors
    seen_schema_names.add(current.name)
    seen_schema_yaml_ids.add(current.id)
    return ancestors
