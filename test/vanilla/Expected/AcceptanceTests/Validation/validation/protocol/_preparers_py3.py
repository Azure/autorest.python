# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional

from azure.core.pipeline.transport import HttpRequest
from azure.core.pipeline.transport._base import _format_url_section
from msrest import Serializer

_SERIALIZER = Serializer()


def _prepare_validation_of_method_parameters_request(
    subscription_id: str, resource_group_name: str, id: int, **kwargs
) -> HttpRequest:
    api_version = "1.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/fakepath/{subscriptionId}/{resourceGroupName}/{id}")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=10, min_length=3, pattern=r"[a-zA-Z0-9\']+"
        ),
        "id": _SERIALIZER.url("id", id, "int", maximum=1000, minimum=100, multiple=10),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["apiVersion"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _prepare_validation_of_body_request(
    subscription_id: str, resource_group_name: str, id: int, body: Optional["_models.Product"] = None, **kwargs
) -> HttpRequest:
    api_version = "1.0.0"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/fakepath/{subscriptionId}/{resourceGroupName}/{id}")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=10, min_length=3, pattern=r"[a-zA-Z0-9]+"
        ),
        "id": _SERIALIZER.url("id", id, "int", maximum=1000, minimum=100, multiple=10),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["apiVersion"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    content = body

    request = HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _prepare_get_with_constant_in_path_request(**kwargs) -> HttpRequest:
    constant_param = "constant"

    # Construct URL
    url = kwargs.pop("template_url", "/validation/constantsInPath/{constantParam}/value")
    path_format_arguments = {
        "constantParam": _SERIALIZER.url("constant_param", constant_param, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _prepare_post_with_constant_in_body_request(body: Optional["_models.Product"] = None, **kwargs) -> HttpRequest:
    constant_param = "constant"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/validation/constantsInPath/{constantParam}/value")
    path_format_arguments = {
        "constantParam": _SERIALIZER.url("constant_param", constant_param, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request
