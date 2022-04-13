# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""The namer autorest plugin.
"""
from typing import Dict, Any, List
from .helpers import to_snake_case

from .. import YamlUpdatePlugin

def update_operation_groups(yaml_data: List[Dict[str, Any]]) -> None:
    for operation_group in yaml_data:
        operation_group["propertyName"] = to_snake_case(operation_group["propertyName"])
        for operation in operation_group["operations"]:
            operation["groupName"] = to_snake_case(operation["groupName"])

def update_types(yaml_data: Dict[str, Any]) -> None:
    pass

def update_client(yaml_data: Dict[str, Any]) -> None:
    pass

class Namer(YamlUpdatePlugin):
    """Add Python naming information."""

    def update_yaml(self, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert in place the YAML str."""
        update_client(yaml_data["client"])
        update_types(yaml_data["types"])
        update_operation_groups(yaml_data["operationGroups"])
        return yaml_data
