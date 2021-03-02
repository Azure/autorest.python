# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from azure.core.pipeline.transport import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def _prepare_headexception_head200_request(**kwargs) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/200")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    request = HttpRequest(
        method="HEAD",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _prepare_headexception_head204_request(**kwargs) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/204")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    request = HttpRequest(
        method="HEAD",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _prepare_headexception_head404_request(**kwargs) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/404")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    request = HttpRequest(
        method="HEAD",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request
