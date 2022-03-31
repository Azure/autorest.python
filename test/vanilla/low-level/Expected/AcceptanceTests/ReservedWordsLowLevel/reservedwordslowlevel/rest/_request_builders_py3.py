# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, IO, List, Optional, TypeVar

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from .._vendor import _format_url_section

T = TypeVar("T")
JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_operation_with_content_param_request(*, content: Any, **kwargs: Any) -> HttpRequest:
    """Operation with body param called content. Pass in b'hello, world'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input).
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/operation/content"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, content=content, **kwargs)


def build_operation_with_json_param_request(
    *, json: JSONType = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    """Operation with body param called 'json'. Pass in {'hello': 'world'}.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Pass in {'hello': 'world'}. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {}  # Optional.
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/operation/json"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_operation_with_data_param_request(
    *, data: Optional[Dict[str, Any]] = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    """Operation with urlencoded body param called 'data'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword data: Pass in dictionary that contains form data to include in the body of the
     request. Default value is None.
    :paramtype data: dict[str, any]
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # form-encoded input template you can fill out and use as your `data` input.
            data = {
                "data": "str",  # Pass in 'hello'.
                "world": "str"  # Pass in 'world'.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/operation/data"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, data=data, content=content, **kwargs)


def build_operation_with_files_param_request(
    *, files: Optional[Dict[str, Any]] = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    """Operation with multipart body param called 'files'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword files: Multipart input for files. See the template in our example to find the input
     shape. Default value is None.
    :paramtype files: dict[str, any]
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # multipart input template you can fill out and use as your `files` input.
            files = {
                "file_name": "str",  # File name to upload. Pass in 'my.txt'.
                "files": b'bytes'  # Files to upload. Pass in list of input streams.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/operation/files"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, files=files, content=content, **kwargs)


def build_operation_with_url_request(
    url: str, *, header_parameters: str, query_parameters: Optional[List[str]] = None, **kwargs: Any
) -> HttpRequest:
    """Operation with path format argument URL, header param headerParameters, and query param
    queryParameters.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param url: Pass in 'foo'.
    :type url: str
    :keyword header_parameters: Header arg that uses same name as headerParameters in generated
     code. Pass in 'x-ms-header' to pass.
    :paramtype header_parameters: str
    :keyword query_parameters: Query args that uses same name as queryParameters in generated code.
     Pass in ['one', 'two'] to pass test. Default value is None.
    :paramtype query_parameters: list[str]
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/{url}"
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if query_parameters is not None:
        _params["queryParameters"] = [
            _SERIALIZER.query("query_parameters", q, "str") if q is not None else "" for q in query_parameters
        ]

    # Construct headers
    _headers["headerParameters"] = _SERIALIZER.header("header_parameters", header_parameters, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)
