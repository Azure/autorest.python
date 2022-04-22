# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""The namer autorest plugin.
"""
from typing import Callable, Dict, Any, List, Optional
from .helpers import to_snake_case

from .. import YamlUpdatePlugin

def update_description(description: Optional[str], default_description: str = "") -> str:
    if not description:
        description = default_description
    if description and description[-1] != ".":
        description += "."
    return description

def update_operation_group_class_name(yaml_data: Dict[str, Any], class_name: str) -> str:
    if class_name == "":
        return yaml_data["client"]["name"] + "OperationsMixin"
    if class_name == "Operations":
        return "Operations"
    return class_name + "Operations"

def update_parameter(yaml_data: Dict[str, Any]) -> None:
    yaml_data["description"] = update_description(yaml_data["description"])

def get_operation_updater(yaml_data: Dict[str, Any]) -> Callable[[Dict[str, Any]], None]:
    if yaml_data["discriminator"] == "paging":
        return update_paging_operation
    return update_operation

def update_operation(yaml_data: Dict[str, Any]) -> None:
    yaml_data["groupName"] = to_snake_case(yaml_data["groupName"])
    yaml_data["description"] = update_description(yaml_data["description"], yaml_data["name"])
    for parameter in yaml_data["parameters"]:
        update_parameter(parameter)
    if yaml_data["bodyParameter"]:
        update_parameter(yaml_data["bodyParameter"])
    for overload in yaml_data.get("overloads", []):
        update_operation(overload)

def update_paging_operation(yaml_data: Dict[str, Any]) -> None:
    update_operation(yaml_data)
    if not yaml_data.get("pagerSync"):
        yaml_data["pagerSync"] = "azure.core.paging.ItemPaged"
    if not yaml_data.get("pagerAsync"):
        yaml_data["pagerAsync"] = "azure.core.async_paging.AsyncItemPaged"


def update_operation_groups(yaml_data: Dict[str, Any]) -> None:
    operation_groups_yaml_data = yaml_data["operationGroups"]
    for operation_group in operation_groups_yaml_data:
        operation_group["propertyName"] = to_snake_case(operation_group["propertyName"])
        operation_group["className"] = update_operation_group_class_name(yaml_data, operation_group["className"])
        for operation in operation_group["operations"]:
            get_operation_updater(operation)(operation)


def update_types(yaml_data: List[Dict[str, Any]]) -> None:
    for type in yaml_data:
        for property in type.get("properties", []):
            property["description"] = update_description(property["description"])
        if type.get("name"):
            type["description"] = update_description(type["description"], type["name"])

def update_client(yaml_data: Dict[str, Any]) -> None:
    yaml_data["description"] = update_description(yaml_data["description"], default_description=yaml_data["name"])
    for parameter in yaml_data["parameters"]:
        update_parameter(parameter)

class Namer(YamlUpdatePlugin):
    """Add Python naming information."""

    def update_yaml(self, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert in place the YAML str."""
        update_client(yaml_data["client"])
        update_types(yaml_data["types"])
        update_operation_groups(yaml_data)
        return yaml_data
