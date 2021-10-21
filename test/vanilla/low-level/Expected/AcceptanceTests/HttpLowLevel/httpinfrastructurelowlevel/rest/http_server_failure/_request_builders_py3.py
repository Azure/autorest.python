# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional

from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_head501_request(**kwargs: Any) -> HttpRequest:
    """Return 501 status code - should be represented in the client as an error.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/http/failure/server/501")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    header_parameters.update(kwargs.pop("headers", {}) or {})

    return HttpRequest(method="HEAD", url=url, headers=header_parameters, **kwargs)


def build_get501_request(**kwargs: Any) -> HttpRequest:
    """Return 501 status code - should be represented in the client as an error.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/http/failure/server/501")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    header_parameters.update(kwargs.pop("headers", {}) or {})

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_post505_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Return 505 status code - should be represented in the client as an error.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = True  # Optional. Default value is True.
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/http/failure/server/505")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    header_parameters.update(kwargs.pop("headers", {}) or {})

    return HttpRequest(method="POST", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_delete505_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Return 505 status code - should be represented in the client as an error.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = True  # Optional. Default value is True.
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/http/failure/server/505")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    header_parameters.update(kwargs.pop("headers", {}) or {})

    return HttpRequest(method="DELETE", url=url, headers=header_parameters, json=json, content=content, **kwargs)
