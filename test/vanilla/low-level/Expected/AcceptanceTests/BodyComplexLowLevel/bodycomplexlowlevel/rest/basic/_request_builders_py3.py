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

T = TypeVar("T")
JSONType = Any

_SERIALIZER = Serializer()


def build_get_valid_request(**kwargs: Any) -> HttpRequest:
    """Get complex type {id: 2, name: 'abc', color: 'YELLOW'}.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "color": "str",  # Optional. Possible values include: "cyan", "Magenta",
                  "YELLOW", "blacK".
                "id": 0,  # Optional. Basic Id.
                "name": "str"  # Optional. Name property with a very long description that
                  does not fit on a single line and a line break.
            }
    """

    accept = "application/json"
    # Construct URL
    _url = "/complex/basic/valid"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)


def build_put_valid_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Please put {id: 2, name: 'abc', color: 'Magenta'}.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Please put {id: 2, name: 'abc', color: 'Magenta'}. Default
     value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Please put {id: 2, name: 'abc', color: 'Magenta'}. Default
     value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "color": "str",  # Optional. Possible values include: "cyan", "Magenta",
                  "YELLOW", "blacK".
                "id": 0,  # Optional. Basic Id.
                "name": "str"  # Optional. Name property with a very long description that
                  does not fit on a single line and a line break.
            }
    """

    api_version = kwargs.pop("api_version", "2016-02-29")  # type: str
    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/complex/basic/valid"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_get_invalid_request(**kwargs: Any) -> HttpRequest:
    """Get a basic complex type that is invalid for the local strong type.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "color": "str",  # Optional. Possible values include: "cyan", "Magenta",
                  "YELLOW", "blacK".
                "id": 0,  # Optional. Basic Id.
                "name": "str"  # Optional. Name property with a very long description that
                  does not fit on a single line and a line break.
            }
    """

    accept = "application/json"
    # Construct URL
    _url = "/complex/basic/invalid"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)


def build_get_empty_request(**kwargs: Any) -> HttpRequest:
    """Get a basic complex type that is empty.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "color": "str",  # Optional. Possible values include: "cyan", "Magenta",
                  "YELLOW", "blacK".
                "id": 0,  # Optional. Basic Id.
                "name": "str"  # Optional. Name property with a very long description that
                  does not fit on a single line and a line break.
            }
    """

    accept = "application/json"
    # Construct URL
    _url = "/complex/basic/empty"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)


def build_get_null_request(**kwargs: Any) -> HttpRequest:
    """Get a basic complex type whose properties are null.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "color": "str",  # Optional. Possible values include: "cyan", "Magenta",
                  "YELLOW", "blacK".
                "id": 0,  # Optional. Basic Id.
                "name": "str"  # Optional. Name property with a very long description that
                  does not fit on a single line and a line break.
            }
    """

    accept = "application/json"
    # Construct URL
    _url = "/complex/basic/null"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)


def build_get_not_provided_request(**kwargs: Any) -> HttpRequest:
    """Get a basic complex type while the server doesn't provide a response payload.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "color": "str",  # Optional. Possible values include: "cyan", "Magenta",
                  "YELLOW", "blacK".
                "id": 0,  # Optional. Basic Id.
                "name": "str"  # Optional. Name property with a very long description that
                  does not fit on a single line and a line break.
            }
    """

    accept = "application/json"
    # Construct URL
    _url = "/complex/basic/notprovided"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)
