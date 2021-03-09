# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import List, Optional

_SERIALIZER = Serializer()


def _prepare_queries_array_string_multi_null_request(
    array_query=None,  # type: Optional[List[str]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/queries/array/multi/string/null")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if array_query is not None:
        query_parameters["arrayQuery"] = [
            _SERIALIZER.query("array_query", q, "str") if q is not None else "" for q in array_query
        ]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_queries_array_string_multi_empty_request(
    array_query=None,  # type: Optional[List[str]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/queries/array/multi/string/empty")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if array_query is not None:
        query_parameters["arrayQuery"] = [
            _SERIALIZER.query("array_query", q, "str") if q is not None else "" for q in array_query
        ]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_queries_array_string_multi_valid_request(
    array_query=None,  # type: Optional[List[str]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/queries/array/multi/string/valid")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if array_query is not None:
        query_parameters["arrayQuery"] = [
            _SERIALIZER.query("array_query", q, "str") if q is not None else "" for q in array_query
        ]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request
