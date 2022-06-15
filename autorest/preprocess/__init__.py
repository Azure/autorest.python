# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""The preprocessing autorest plugin.
"""
from typing import Callable, Dict, Any, List, Optional
from .helpers import to_snake_case, pad_reserved_words, add_redefined_builtin_info
from .python_mappings import PadType

from .. import YamlUpdatePlugin


def update_description(
    description: Optional[str], default_description: str = ""
) -> str:
    if not description:
        description = default_description
    description.rstrip(" ")
    if description and description[-1] != ".":
        description += "."
    return description


def update_operation_group_class_name(
    yaml_data: Dict[str, Any], class_name: str
) -> str:
    if class_name == "":
        return yaml_data["client"]["name"] + "OperationsMixin"
    if class_name == "Operations":
        return "Operations"
    return class_name + "Operations"


def update_parameter(yaml_data: Dict[str, Any]) -> None:
    yaml_data["description"] = update_description(yaml_data["description"])
    if not (
        yaml_data["location"] == "header"
        and yaml_data["clientName"] in ("content_type", "accept")
    ):
        yaml_data["clientName"] = pad_reserved_words(
            yaml_data["clientName"].lower(), PadType.PARAMETER
        )
    if yaml_data.get("propertyToParameterName"):
        # need to create a new one with padded keys and values
        yaml_data["propertyToParameterName"] = {
            pad_reserved_words(prop, PadType.PROPERTY)
            .lower(): pad_reserved_words(param_name, PadType.PARAMETER)
            .lower()
            for prop, param_name in yaml_data["propertyToParameterName"].items()
        }


def update_types(yaml_data: List[Dict[str, Any]]) -> None:
    for type in yaml_data:
        for property in type.get("properties", []):
            property["description"] = update_description(property["description"])
            property["clientName"] = pad_reserved_words(
                property["clientName"].lower(), PadType.PROPERTY
            )
            add_redefined_builtin_info(property["clientName"], property)
        if type.get("name"):
            type["description"] = update_description(type["description"], type["name"])
            type["snakeCaseName"] = to_snake_case(type["name"])


def update_client(yaml_data: Dict[str, Any]) -> None:
    yaml_data["description"] = update_description(
        yaml_data["description"], default_description=yaml_data["name"]
    )
    yaml_data["moduleName"] = to_snake_case(yaml_data["name"].replace(" ", "_"))
    for parameter in yaml_data["parameters"]:
        update_parameter(parameter)


def update_paging_response(yaml_data: Dict[str, Any]) -> None:
    yaml_data["discriminator"] = "paging"
    yaml_data["pagerSync"] = yaml_data.get("pagerSync") or "azure.core.paging.ItemPaged"
    yaml_data["pagerAsync"] = (
        yaml_data.get("pagerAsync") or "azure.core.async_paging.AsyncItemPaged"
    )


class PreProcessPlugin(YamlUpdatePlugin):
    """Add Python naming information."""

    def get_operation_updater(
        self, yaml_data: Dict[str, Any]
    ) -> Callable[[Dict[str, Any]], None]:
        if yaml_data["discriminator"] == "lropaging":
            return self.update_lro_paging_operation
        if yaml_data["discriminator"] == "lro":
            return self.update_lro_operation
        if yaml_data["discriminator"] == "paging":
            return self.update_paging_operation
        return self.update_operation

    def update_operation(self, yaml_data: Dict[str, Any]) -> None:
        yaml_data["groupName"] = pad_reserved_words(
            yaml_data["groupName"], PadType.OPERATION_GROUP
        )
        yaml_data["groupName"] = to_snake_case(yaml_data["groupName"])
        yaml_data["name"] = yaml_data["name"].lower()
        yaml_data["name"] = pad_reserved_words(yaml_data["name"], PadType.METHOD)
        yaml_data["description"] = update_description(
            yaml_data["description"], yaml_data["name"]
        )
        yaml_data["summary"] = update_description(yaml_data.get("summary", ""))
        for parameter in yaml_data["parameters"]:
            update_parameter(parameter)
        if yaml_data.get("bodyParameter"):
            update_parameter(yaml_data["bodyParameter"])
            for entry in yaml_data["bodyParameter"].get("entries", []):
                update_parameter(entry)
        for overload in yaml_data.get("overloads", []):
            self.update_operation(overload)
        for response in yaml_data.get("responses", []):
            response["discriminator"] = "operation"

    def _update_lro_operation_helper(self, yaml_data: Dict[str, Any]) -> None:
        azure_arm = self._autorestapi.get_boolean_value("azure-arm", False)
        for response in yaml_data.get("responses", []):
            response["discriminator"] = "lro"
            response["pollerSync"] = (
                response.get("pollerSync") or "azure.core.polling.LROPoller"
            )
            response["pollerAsync"] = (
                response.get("pollerAsync") or "azure.core.polling.AsyncLROPoller"
            )
            if not response.get("pollingMethodSync"):
                response["pollingMethodSync"] = (
                    "azure.mgmt.core.polling.arm_polling.ARMPolling"
                    if azure_arm
                    else "azure.core.polling.base_polling.LROBasePolling"
                )
            if not response.get("pollingMethodAsync"):
                response["pollingMethodAsync"] = (
                    "azure.mgmt.core.polling.async_arm_polling.AsyncARMPolling"
                    if azure_arm
                    else "azure.core.polling.async_base_polling.AsyncLROBasePolling"
                )

    def update_lro_paging_operation(self, yaml_data: Dict[str, Any]) -> None:
        self.update_lro_operation(yaml_data)
        self.update_paging_operation(yaml_data)
        for response in yaml_data.get("responses", []):
            response["discriminator"] = "lropaging"

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
        returned_response_object = (
            yaml_data["nextOperation"]["responses"][0]
            if yaml_data.get("nextOperation")
            else yaml_data["responses"][0]
        )
        # if we're in version tolerant, hide the paging model
        if self._autorestapi.get_boolean_value("version-tolerant", True):
            returned_response_object["type"]["isPublic"] = False
        item_type = next(
            p["type"]["elementType"]
            for p in returned_response_object["type"]["properties"]
            if p["restApiName"] == yaml_data["itemName"]
        )
        if yaml_data.get("nextOperation"):
            yaml_data["nextOperation"]["groupName"] = pad_reserved_words(
                yaml_data["nextOperation"]["groupName"], PadType.OPERATION_GROUP
            )
            yaml_data["nextOperation"]["groupName"] = to_snake_case(
                yaml_data["nextOperation"]["groupName"]
            )
            for response in yaml_data["nextOperation"].get("responses", []):
                update_paging_response(response)
                response["itemType"] = item_type
        for response in yaml_data.get("responses", []):
            update_paging_response(response)
            response["itemType"] = item_type
        for overload in yaml_data.get("overloads", []):
            self.update_paging_operation(overload)

    def update_operation_groups(self, yaml_data: Dict[str, Any]) -> None:
        operation_groups_yaml_data = yaml_data["operationGroups"]
        for operation_group in operation_groups_yaml_data:
            operation_group["propertyName"] = pad_reserved_words(
                operation_group["propertyName"], PadType.OPERATION_GROUP
            )
            operation_group["propertyName"] = to_snake_case(
                operation_group["propertyName"]
            )
            operation_group["className"] = update_operation_group_class_name(
                yaml_data, operation_group["className"]
            )
            for operation in operation_group["operations"]:
                self.get_operation_updater(operation)(operation)

    def update_yaml(self, yaml_data: Dict[str, Any]) -> None:
        """Convert in place the YAML str."""
        update_client(yaml_data["client"])
        update_types(yaml_data["types"])
        self.update_operation_groups(yaml_data)
