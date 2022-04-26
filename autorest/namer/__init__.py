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

    def get_operation_updater(self, yaml_data: Dict[str, Any]) -> Callable[[Dict[str, Any]], None]:
        if yaml_data["discriminator"] == "lro":
            return self.update_lro_operation
        if yaml_data["discriminator"] == "paging":
            return self.update_paging_operation
        return self.update_operation

    def update_operation(self, yaml_data: Dict[str, Any]) -> None:
        yaml_data["groupName"] = to_snake_case(yaml_data["groupName"])
        yaml_data["description"] = update_description(yaml_data["description"], yaml_data["name"])
        for parameter in yaml_data["parameters"]:
            update_parameter(parameter)
        if yaml_data["bodyParameter"]:
            update_parameter(yaml_data["bodyParameter"])
        for overload in yaml_data.get("overloads", []):
            self.update_operation(overload)

    def _update_lro_operation_helper(self, yaml_data: Dict[str, Any]) -> None:
        azure_arm = self._autorestapi.get_boolean_value("azure-arm", False)
        if not yaml_data.get("pollerSync"):
            yaml_data["pollerSync"] = "azure.core.polling.LROPoller"
        if not yaml_data.get("pollerAsync"):
            yaml_data["pollerAsync"] = "azure.core.polling.AsyncLROPoller"
        if not yaml_data.get("pollingMethodSync"):
            yaml_data["pollingMethodSync"] = (
                "azure.mgmt.core.polling.arm_polling.ARMPolling" if azure_arm else
                "azure.core.polling.base_polling.LROBasePolling"
            )
        if not yaml_data.get("pollingMethodAsync"):
            yaml_data["pollingMethodAsync"] = (
                "azure.mgmt.core.polling.async_arm_polling.AsyncARMPolling" if azure_arm else
                "azure.core.polling.async_base_polling.AsyncLROBasePolling"
            )


    def update_lro_operation(self, yaml_data: Dict[str, Any]) -> None:
        self.update_operation(yaml_data)
        self._update_lro_operation_helper(yaml_data)
        for overload in yaml_data["overloads"]:
            self._update_lro_operation_helper(overload)

    def update_paging_operation(self, yaml_data: Dict[str, Any]) -> None:
        self.update_operation(yaml_data)
        if not yaml_data.get("pagerSync"):
            yaml_data["pagerSync"] = "azure.core.paging.ItemPaged"
        if not yaml_data.get("pagerAsync"):
            yaml_data["pagerAsync"] = "azure.core.async_paging.AsyncItemPaged"
        if yaml_data.get("nextOperation"):
            yaml_data["nextOperation"]["groupName"] = to_snake_case(yaml_data["nextOperation"]["groupName"])

    def update_operation_groups(self, yaml_data: Dict[str, Any]) -> None:
        operation_groups_yaml_data = yaml_data["operationGroups"]
        for operation_group in operation_groups_yaml_data:
            operation_group["propertyName"] = to_snake_case(operation_group["propertyName"])
            operation_group["className"] = update_operation_group_class_name(yaml_data, operation_group["className"])
            for operation in operation_group["operations"]:
                self.get_operation_updater(operation)(operation)

    def update_yaml(self, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert in place the YAML str."""
        update_client(yaml_data["client"])
        update_types(yaml_data["types"])
        self.update_operation_groups(yaml_data)
        return yaml_data
