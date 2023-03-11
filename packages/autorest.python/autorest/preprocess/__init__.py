# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""The preprocessing autorest plugin.
"""
import copy
from typing import Callable, Dict, Any, List, Optional

from .._utils import to_snake_case
from .helpers import (
    add_redefined_builtin_info,
    pad_builtin_namespaces,
    pad_special_chars,
)
from .python_mappings import CADL_RESERVED_WORDS, RESERVED_WORDS, PadType

from .. import YamlUpdatePlugin, YamlUpdatePluginAutorest
from .._utils import parse_args


def _remove_paging_maxpagesize(yaml_data: Dict[str, Any]) -> None:
    # we don't expose maxpagesize for version tolerant generation
    # users should be passing this into `by_page`
    yaml_data["parameters"] = [
        p
        for p in yaml_data.get("parameters", [])
        if p["restApiName"].lower() not in ["maxpagesize", "$maxpagesize"]
    ]


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
        return yaml_data["name"] + "OperationsMixin"
    if class_name == "Operations":
        return "Operations"
    return class_name + "Operations"


def update_paging_response(yaml_data: Dict[str, Any]) -> None:
    yaml_data["discriminator"] = "paging"
    yaml_data["pagerSync"] = yaml_data.get("pagerSync") or "azure.core.paging.ItemPaged"
    yaml_data["pagerAsync"] = (
        yaml_data.get("pagerAsync") or "azure.core.async_paging.AsyncItemPaged"
    )


class PreProcessPlugin(YamlUpdatePlugin):  # pylint: disable=abstract-method
    """Add Python naming information."""

    @property
    def version_tolerant(self) -> bool:
        return self.options.get("version-tolerant", True)

    @property
    def models_mode(self) -> Optional[str]:
        return self.options.get("models-mode", "dpg" if self.is_cadl else None)

    @property
    def is_cadl(self) -> bool:
        return self.options.get("cadl_file", False)

    def pad_reserved_words(self, name: str, pad_type: PadType):
        # we want to pad hidden variables as well
        if not name:
            # we'll pass in empty operation groups sometime etc.
            return name

        if self.is_cadl:
            reserved_words = copy.copy(CADL_RESERVED_WORDS)
            reserved_words.update(RESERVED_WORDS)
        else:
            reserved_words = RESERVED_WORDS
        name = pad_special_chars(name)
        name_prefix = "_" if name[0] == "_" else ""
        name = name[1:] if name[0] == "_" else name
        if name.lower() in reserved_words[pad_type]:
            return name_prefix + name + pad_type
        return name_prefix + name

    def update_types(self, yaml_data: List[Dict[str, Any]]) -> None:
        for type in yaml_data:
            for property in type.get("properties", []):
                property["description"] = update_description(property["description"])
                property["clientName"] = self.pad_reserved_words(
                    property["clientName"].lower(), PadType.PROPERTY
                )
                add_redefined_builtin_info(property["clientName"], property)
            if type.get("name"):
                type["description"] = update_description(
                    type["description"], type["name"]
                )
                type["snakeCaseName"] = to_snake_case(type["name"])

    def update_client(self, yaml_data: Dict[str, Any]) -> None:
        yaml_data["description"] = update_description(
            yaml_data["description"], default_description=yaml_data["name"]
        )
        yaml_data["legacyFilename"] = to_snake_case(yaml_data["name"].replace(" ", "_"))
        for parameter in yaml_data["parameters"]:
            self.update_parameter(parameter)
        prop_name = yaml_data["name"]
        if prop_name.endswith("Client"):
            prop_name = prop_name[: len(prop_name) - len("Client")]
        yaml_data["builderPadName"] = to_snake_case(prop_name)

    def get_operation_updater(
        self, yaml_data: Dict[str, Any]
    ) -> Callable[[Dict[str, Any], Dict[str, Any]], None]:
        if yaml_data["discriminator"] == "lropaging":
            return self.update_lro_paging_operation
        if yaml_data["discriminator"] == "lro":
            return self.update_lro_operation
        if yaml_data["discriminator"] == "paging":
            return self.update_paging_operation
        return self.update_operation

    def update_parameter(self, yaml_data: Dict[str, Any]) -> None:
        yaml_data["description"] = update_description(yaml_data["description"])
        if not (
            yaml_data["location"] == "header"
            and yaml_data["clientName"] in ("content_type", "accept")
        ):
            yaml_data["clientName"] = self.pad_reserved_words(
                yaml_data["clientName"].lower(), PadType.PARAMETER
            )
        if yaml_data.get("propertyToParameterName"):
            # need to create a new one with padded keys and values
            yaml_data["propertyToParameterName"] = {
                self.pad_reserved_words(prop, PadType.PROPERTY)
                .lower(): self.pad_reserved_words(param_name, PadType.PARAMETER)
                .lower()
                for prop, param_name in yaml_data["propertyToParameterName"].items()
            }

    def update_operation(
        self,
        code_model: Dict[str, Any],
        yaml_data: Dict[str, Any],
    ) -> None:
        yaml_data["groupName"] = self.pad_reserved_words(
            yaml_data["groupName"], PadType.OPERATION_GROUP
        )
        yaml_data["groupName"] = to_snake_case(yaml_data["groupName"])
        yaml_data["name"] = yaml_data["name"].lower()
        yaml_data["name"] = self.pad_reserved_words(yaml_data["name"], PadType.METHOD)
        yaml_data["description"] = update_description(
            yaml_data["description"], yaml_data["name"]
        )
        yaml_data["summary"] = update_description(yaml_data.get("summary", ""))
        for parameter in yaml_data["parameters"]:
            self.update_parameter(parameter)
        if yaml_data.get("bodyParameter"):
            self.update_parameter(yaml_data["bodyParameter"])
            for entry in yaml_data["bodyParameter"].get("entries", []):
                self.update_parameter(entry)
        for overload in yaml_data.get("overloads", []):
            self.update_operation(code_model, overload)
        for response in yaml_data.get("responses", []):
            response["discriminator"] = "operation"

    def _update_lro_operation_helper(self, yaml_data: Dict[str, Any]) -> None:
        azure_arm = self.options.get("azure-arm", False)
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

    def update_lro_paging_operation(
        self,
        code_model: Dict[str, Any],
        yaml_data: Dict[str, Any],
    ) -> None:
        self.update_lro_operation(code_model, yaml_data)
        self.update_paging_operation(code_model, yaml_data)
        yaml_data["discriminator"] = "lropaging"
        for response in yaml_data.get("responses", []):
            response["discriminator"] = "lropaging"
        for overload in yaml_data.get("overloads", []):
            self.update_lro_paging_operation(code_model, overload)

    def update_lro_operation(
        self,
        code_model: Dict[str, Any],
        yaml_data: Dict[str, Any],
    ) -> None:
        self.update_operation(code_model, yaml_data)
        self.update_operation(code_model, yaml_data["initialOperation"])
        self._update_lro_operation_helper(yaml_data)
        for overload in yaml_data.get("overloads", []):
            self._update_lro_operation_helper(overload)
            self.update_operation(code_model, overload["initialOperation"])

    def update_paging_operation(
        self,
        code_model: Dict[str, Any],
        yaml_data: Dict[str, Any],
    ) -> None:
        self.update_operation(code_model, yaml_data)
        if not yaml_data.get("pagerSync"):
            yaml_data["pagerSync"] = "azure.core.paging.ItemPaged"
        if not yaml_data.get("pagerAsync"):
            yaml_data["pagerAsync"] = "azure.core.async_paging.AsyncItemPaged"
        returned_response_object = (
            yaml_data["nextOperation"]["responses"][0]
            if yaml_data.get("nextOperation")
            else yaml_data["responses"][0]
        )
        if self.version_tolerant:
            # if we're in version tolerant, hide the paging model
            returned_response_object["type"]["isPublic"] = False
            _remove_paging_maxpagesize(yaml_data)
        item_type = next(
            p["type"]["elementType"]
            for p in returned_response_object["type"]["properties"]
            if p["restApiName"] == (yaml_data.get("itemName") or "value")
        )
        if yaml_data.get("nextOperation"):
            if self.version_tolerant:
                _remove_paging_maxpagesize(yaml_data["nextOperation"])
            yaml_data["nextOperation"]["groupName"] = self.pad_reserved_words(
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
            self.update_paging_operation(code_model, overload)

    def update_operation_groups(
        self, code_model: Dict[str, Any], client: Dict[str, Any]
    ) -> None:
        operation_groups_yaml_data = client["operationGroups"]
        for operation_group in operation_groups_yaml_data:
            operation_group["clientName"] = client["name"]
            operation_group["propertyName"] = self.pad_reserved_words(
                operation_group["propertyName"], PadType.OPERATION_GROUP
            )
            operation_group["propertyName"] = to_snake_case(
                operation_group["propertyName"]
            )
            operation_group["className"] = update_operation_group_class_name(
                client, operation_group["className"]
            )
            for operation in operation_group["operations"]:
                self.get_operation_updater(operation)(code_model, operation)

    def update_yaml(self, yaml_data: Dict[str, Any]) -> None:
        """Convert in place the YAML str."""
        self.update_types(yaml_data["types"])
        for client in yaml_data["clients"]:
            self.update_client(client)
            self.update_operation_groups(yaml_data, client)
        for clients in yaml_data["subnamespaceToClients"].values():
            for client in clients:
                self.update_client(client)
                self.update_operation_groups(yaml_data, client)
        if yaml_data.get("namespace"):
            yaml_data["namespace"] = pad_builtin_namespaces(yaml_data["namespace"])


class PreProcessPluginAutorest(YamlUpdatePluginAutorest, PreProcessPlugin):
    def get_options(self) -> Dict[str, Any]:
        options = {
            "version-tolerant": self._autorestapi.get_boolean_value("version-tolerant"),
            "azure-arm": self._autorestapi.get_boolean_value("azure-arm"),
            "models-mode": self._autorestapi.get_value("models-mode"),
        }
        return {k: v for k, v in options.items() if v is not None}


if __name__ == "__main__":
    # CADL pipeline will call this
    args, unknown_args = parse_args()
    PreProcessPlugin(
        output_folder=args.output_folder, cadl_file=args.cadl_file, **unknown_args
    ).process()
