# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, TypeVar

from azure.core.rest import HttpRequest
from msrest import Serializer

T = TypeVar("T")
JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_null_request(**kwargs: Any) -> HttpRequest:
    """Get null byte value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    _url = "/byte/null"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)


def build_get_empty_request(**kwargs: Any) -> HttpRequest:
    """Get empty byte value ''.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    _url = "/byte/empty"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)


def build_get_non_ascii_request(**kwargs: Any) -> HttpRequest:
    """Get non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    _url = "/byte/nonAscii"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)


def build_put_non_ascii_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Base64-encoded non-ascii byte string hex(FF FE FD FC FB FA
     F9 F8 F7 F6).
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Base64-encoded non-ascii byte string hex(FF FE FD FC FB FA
     F9 F8 F7 F6).
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = bytearray("bytearray", encoding="utf-8")  # Optional.
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/byte/nonAscii"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_header_parameters, json=json, content=content, **kwargs)


def build_get_invalid_request(**kwargs: Any) -> HttpRequest:
    """Get invalid byte value ':::SWAGGER::::'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    _url = "/byte/invalid"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)
