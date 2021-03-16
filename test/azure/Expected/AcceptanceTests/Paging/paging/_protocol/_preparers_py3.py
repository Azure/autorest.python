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


def prepare_paging_get_no_item_name_pages_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/noitemname")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_null_next_link_name_pages_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/nullnextlink")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_single_pages_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/single")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_first_response_empty_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/firstResponseEmpty/1")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_multiple_pages_request(
    client_request_id: Optional[str] = None, maxresults: Optional[int] = None, timeout: Optional[int] = 30, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters["client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    if maxresults is not None:
        header_parameters["maxresults"] = _SERIALIZER.header("maxresults", maxresults, "int")
    if timeout is not None:
        header_parameters["timeout"] = _SERIALIZER.header("timeout", timeout, "int")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_with_query_params_request(required_query_parameter: int, **kwargs) -> HttpRequest:
    query_constant = True
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/getWithQueryParams")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["requiredQueryParameter"] = _SERIALIZER.query(
        "required_query_parameter", required_query_parameter, "int"
    )
    query_parameters["queryConstant"] = _SERIALIZER.query("query_constant", query_constant, "bool")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def _get_with_query_params_next_request(**kwargs) -> HttpRequest:
    query_constant = True
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/nextOperationWithQueryParams")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["queryConstant"] = _SERIALIZER.query("query_constant", query_constant, "bool")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_odata_multiple_pages_request(
    client_request_id: Optional[str] = None, maxresults: Optional[int] = None, timeout: Optional[int] = 30, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/odata")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters["client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    if maxresults is not None:
        header_parameters["maxresults"] = _SERIALIZER.header("maxresults", maxresults, "int")
    if timeout is not None:
        header_parameters["timeout"] = _SERIALIZER.header("timeout", timeout, "int")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_multiple_pages_with_offset_request(
    offset: int,
    client_request_id: Optional[str] = None,
    maxresults: Optional[int] = None,
    timeout: Optional[int] = 30,
    **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/withpath/{offset}")
    path_format_arguments = {
        "offset": _SERIALIZER.url("offset", offset, "int"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters["client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    if maxresults is not None:
        header_parameters["maxresults"] = _SERIALIZER.header("maxresults", maxresults, "int")
    if timeout is not None:
        header_parameters["timeout"] = _SERIALIZER.header("timeout", timeout, "int")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_multiple_pages_retry_first_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/retryfirst")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_multiple_pages_retry_second_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/retrysecond")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_single_pages_failure_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/single/failure")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_multiple_pages_failure_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/failure")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_multiple_pages_failure_uri_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/failureuri")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_multiple_pages_fragment_next_link_request(
    api_version: str, tenant: str, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/fragment/{tenant}")
    path_format_arguments = {
        "tenant": _SERIALIZER.url("tenant", tenant, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api_version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_multiple_pages_fragment_with_grouping_next_link_request(
    api_version: str, tenant: str, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/fragmentwithgrouping/{tenant}")
    path_format_arguments = {
        "tenant": _SERIALIZER.url("tenant", tenant, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api_version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_multiple_pages_lro_initial_request(
    client_request_id: Optional[str] = None, maxresults: Optional[int] = None, timeout: Optional[int] = 30, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/lro")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters["client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    if maxresults is not None:
        header_parameters["maxresults"] = _SERIALIZER.header("maxresults", maxresults, "int")
    if timeout is not None:
        header_parameters["timeout"] = _SERIALIZER.header("timeout", timeout, "int")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def _get_multiple_pages_fragment_next_link_next_request(
    api_version: str, tenant: str, next_link: str, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/fragment/{tenant}/{nextLink}")
    path_format_arguments = {
        "tenant": _SERIALIZER.url("tenant", tenant, "str"),
        "nextLink": _SERIALIZER.url("next_link", next_link, "str", skip_quote=True),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api_version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def _get_multiple_pages_fragment_with_grouping_next_link_next_request(
    api_version: str, tenant: str, next_link: str, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/fragmentwithgrouping/{tenant}/{nextLink}")
    path_format_arguments = {
        "tenant": _SERIALIZER.url("tenant", tenant, "str"),
        "nextLink": _SERIALIZER.url("next_link", next_link, "str", skip_quote=True),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api_version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_paging_get_paging_model_with_item_name_with_xms_client_name_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/itemNameWithXMSClientName")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)
