# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from ..._vendor import _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional, TypeVar

    T = TypeVar("T")
    JSONType = Any

_SERIALIZER = Serializer()

# fmt: off

def build_get_required_path_request(
    path_parameter,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Test implicitly required path parameter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param path_parameter:
    :type path_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/reqopt/implicit/required/path/{pathParameter}"
    path_format_arguments = {
        "pathParameter": _SERIALIZER.url("path_parameter", path_parameter, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_optional_query_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Test implicitly optional query parameter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword query_parameter:  Default value is None.
    :paramtype query_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    query_parameter = kwargs.pop('query_parameter', _params.pop('queryParameter', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/reqopt/implicit/optional/query"

    # Construct parameters
    if query_parameter is not None:
        _params['queryParameter'] = _SERIALIZER.query("query_parameter", query_parameter, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_put_optional_header_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Test implicitly optional header parameter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword query_parameter:  Default value is None.
    :paramtype query_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    query_parameter = kwargs.pop('query_parameter', _headers.pop('queryParameter', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/reqopt/implicit/optional/header"

    # Construct headers
    if query_parameter is not None:
        _headers['queryParameter'] = _SERIALIZER.header("query_parameter", query_parameter, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_optional_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Test implicitly optional body parameter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.  Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input).  Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = "str"  # Optional.
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/reqopt/implicit/optional/body"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_optional_binary_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Test implicitly optional body parameter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input).  Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/reqopt/implicit/optional/binary-body"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_required_global_path_request(
    required_global_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Test implicitly required path parameter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param required_global_path: number of items to skip.
    :type required_global_path: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/reqopt/global/required/path/{required-global-path}"
    path_format_arguments = {
        "required-global-path": _SERIALIZER.url("required_global_path", required_global_path, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_required_global_query_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Test implicitly required query parameter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword required_global_query: number of items to skip.
    :paramtype required_global_query: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    required_global_query = kwargs.pop('required_global_query')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/reqopt/global/required/query"

    # Construct parameters
    _params['required-global-query'] = _SERIALIZER.query("required_global_query", required_global_query, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_optional_global_query_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Test implicitly optional query parameter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword optional_global_query: number of items to skip. Default value is None.
    :paramtype optional_global_query: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    optional_global_query = kwargs.pop('optional_global_query', _params.pop('optional-global-query', None))  # type: Optional[int]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/reqopt/global/optional/query"

    # Construct parameters
    if optional_global_query is not None:
        _params['optional-global-query'] = _SERIALIZER.query("optional_global_query", optional_global_query, 'int')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )
