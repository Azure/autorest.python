# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, TypeVar

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

T = TypeVar("T")
JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_object_request(**kwargs: Any) -> HttpRequest:
    """Basic get that returns an object as anything. Returns object { 'message': 'An object was
    successfully returned' }.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/anything/object"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_put_object_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Basic put that puts an object as anything. Pass in {'foo': 'bar'} to get a 200 and anything
    else to get an object error.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Pass in {'foo': 'bar'} for a 200, anything else for an
     object error. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Pass in {'foo': 'bar'} for a 200, anything else for an
     object error. Default value is None.
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

    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    # Construct URL
    _url = "/anything/object"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_get_string_request(**kwargs: Any) -> HttpRequest:
    """Basic get that returns an string as anything. Returns string 'foo'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/anything/string"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_put_string_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Basic put that puts an string as anything. Pass in 'anything' to get a 200 and anything else to
    get an object error.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Pass in 'anything' for a 200, anything else for an object
     error. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Pass in 'anything' for a 200, anything else for an object
     error. Default value is None.
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

    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    # Construct URL
    _url = "/anything/string"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, json=json, content=content, **kwargs)


def build_get_array_request(**kwargs: Any) -> HttpRequest:
    """Basic get that returns an array as anything. Returns string ['foo', 'bar'].

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/anything/array"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_put_array_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Basic put that puts an array as anything. Pass in ['foo', 'bar'] to get a 200 and anything else
    to get an object error.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Pass in ['foo', 'bar'] for a 200, anything else for an
     object error. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Pass in ['foo', 'bar'] for a 200, anything else for an
     object error. Default value is None.
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

    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    # Construct URL
    _url = "/anything/array"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, json=json, content=content, **kwargs)
