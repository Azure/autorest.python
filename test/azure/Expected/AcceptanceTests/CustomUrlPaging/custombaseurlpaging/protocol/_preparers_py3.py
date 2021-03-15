# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from azure.core.pipeline.transport import HttpRequest
from azure.core.pipeline.transport._base import _format_url_section
from msrest import Serializer

_SERIALIZER = Serializer()

import xml.etree.ElementTree as ET


def _request(
    method,
    url,
    params=None,
    headers=None,
    content=None,
    form_content=None,
    stream_content=None,
):
    request = HttpRequest(method, url, headers=headers)

    if params:
        request.format_parameters(params)

    if content is not None:
        content_type = request.headers.get("Content-Type")
        if isinstance(content, ET.Element):
            request.set_xml_body(content)
        # https://github.com/Azure/azure-sdk-for-python/issues/12137
        # A string is valid JSON, make the difference between text
        # and a plain JSON string.
        # Content-Type is a good indicator of intent from user
        elif content_type and content_type.startswith("text/"):
            request.set_text_body(content)
        else:
            try:
                request.set_json_body(content)
            except TypeError:
                request.data = content

    if form_content:
        request.set_formdata_body(form_content)
    elif stream_content:
        request.set_streamed_data_body(stream_content)

    return request


def _prepare_paging_get_pages_partial_url_request(account_name: str, host: str = "host", **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/customurl/partialnextlink")
    path_format_arguments = {
        "accountName": _SERIALIZER.url("account_name", account_name, "str", skip_quote=True),
        "host": _SERIALIZER.url("host", host, "str", skip_quote=True),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def _prepare_paging_get_pages_partial_url_operation_request(
    account_name: str, host: str = "host", **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/customurl/partialnextlinkop")
    path_format_arguments = {
        "accountName": _SERIALIZER.url("account_name", account_name, "str", skip_quote=True),
        "host": _SERIALIZER.url("host", host, "str", skip_quote=True),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def _get_pages_partial_url_operation_next_request(
    account_name: str, next_link: str, host: str = "host", **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/customurl/{nextLink}")
    path_format_arguments = {
        "accountName": _SERIALIZER.url("account_name", account_name, "str", skip_quote=True),
        "host": _SERIALIZER.url("host", host, "str", skip_quote=True),
        "nextLink": _SERIALIZER.url("next_link", next_link, "str", skip_quote=True),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)
