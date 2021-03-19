# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.protocol import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional, Union

_SERIALIZER = Serializer()


def prepare_storageaccounts_check_name_availability(
    subscription_id,  # type: str
    body,  # type: "_models.StorageAccountCheckNameAvailabilityParameters"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-05-01-preview"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/checkNameAvailability"
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = body

    return HttpRequest(
        method="POST", url=url, params=query_parameters, headers=header_parameters, **body_content_kwargs
    )


def prepare_storageaccounts_create_initial(
    resource_group_name,  # type: str
    account_name,  # type: str
    subscription_id,  # type: str
    body,  # type: "_models.StorageAccountCreateParameters"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-05-01-preview"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = body

    return HttpRequest(method="PUT", url=url, params=query_parameters, headers=header_parameters, **body_content_kwargs)


def prepare_storageaccounts_delete(
    resource_group_name,  # type: str
    account_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-05-01-preview"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
    )


def prepare_storageaccounts_get_properties(
    resource_group_name,  # type: str
    account_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_storageaccounts_update(
    resource_group_name,  # type: str
    account_name,  # type: str
    subscription_id,  # type: str
    body,  # type: "_models.StorageAccountUpdateParameters"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-05-01-preview"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = body

    return HttpRequest(
        method="PATCH", url=url, params=query_parameters, headers=header_parameters, **body_content_kwargs
    )


def prepare_storageaccounts_list_keys(
    resource_group_name,  # type: str
    account_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/listKeys",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_storageaccounts_list(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/storageAccounts")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_storageaccounts_list_by_resource_group(
    resource_group_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_storageaccounts_regenerate_key(
    resource_group_name,  # type: str
    account_name,  # type: str
    subscription_id,  # type: str
    body,  # type: "_models.StorageAccountRegenerateKeyParameters"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-05-01-preview"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/regenerateKey",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = body

    return HttpRequest(
        method="POST", url=url, params=query_parameters, headers=header_parameters, **body_content_kwargs
    )


def prepare_usage_list(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/usages")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )
