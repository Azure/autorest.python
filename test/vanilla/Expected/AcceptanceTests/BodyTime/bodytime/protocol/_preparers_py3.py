# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime

from azure.core.pipeline.transport import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def _prepare_time_get_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/time/get")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

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


def _prepare_time_put_request(body: datetime.time, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/time/put")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

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
