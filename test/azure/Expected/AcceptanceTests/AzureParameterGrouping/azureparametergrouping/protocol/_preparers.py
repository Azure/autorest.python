# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport import HttpRequest
from azure.core.pipeline.transport._base import _format_url_section
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Optional

_SERIALIZER = Serializer()


def _post_required_request(
    path,  # type: str
    body,  # type: int
    custom_header=None,  # type: Optional[str]
    query=30,  # type: Optional[int]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/parameterGrouping/postRequired/{path}")
    path_format_arguments = {
        "path": _SERIALIZER.url("path", path, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if query is not None:
        query_parameters["query"] = _SERIALIZER.query("query", query, "int")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if custom_header is not None:
        header_parameters["customHeader"] = _SERIALIZER.header("custom_header", custom_header, "str")
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_optional_request(
    custom_header=None,  # type: Optional[str]
    query=30,  # type: Optional[int]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/parameterGrouping/postOptional")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if query is not None:
        query_parameters["query"] = _SERIALIZER.query("query", query, "int")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if custom_header is not None:
        header_parameters["customHeader"] = _SERIALIZER.header("custom_header", custom_header, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _post_multi_param_groups_request(
    header_one=None,  # type: Optional[str]
    query_one=30,  # type: Optional[int]
    header_two=None,  # type: Optional[str]
    query_two=30,  # type: Optional[int]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/parameterGrouping/postMultipleParameterGroups")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if query_one is not None:
        query_parameters["query-one"] = _SERIALIZER.query("query_one", query_one, "int")
    if query_two is not None:
        query_parameters["query-two"] = _SERIALIZER.query("query_two", query_two, "int")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if header_one is not None:
        header_parameters["header-one"] = _SERIALIZER.header("header_one", header_one, "str")
    if header_two is not None:
        header_parameters["header-two"] = _SERIALIZER.header("header_two", header_two, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _post_shared_parameter_group_object_request(
    header_one=None,  # type: Optional[str]
    query_one=30,  # type: Optional[int]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/parameterGrouping/sharedParameterGroupObject")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if query_one is not None:
        query_parameters["query-one"] = _SERIALIZER.query("query_one", query_one, "int")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if header_one is not None:
        header_parameters["header-one"] = _SERIALIZER.header("header_one", header_one, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request
