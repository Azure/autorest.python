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

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional, Union

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_analyze_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Analyze body, that could be different media types.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Input parameter. Default value is None.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Input parameter. Default value is None.
    :paramtype content: any
    :keyword content_type: Media type of the body sent to the API. Known values are:
     "application/pdf", "image/jpeg", "image/png", "image/tiff", and "application/json". Default
     value is None.
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = b'bytes'  # Optional.
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/mediatypes/analyze"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_analyze_body_no_accept_header_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
    type.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Input parameter. Default value is None.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Input parameter. Default value is None.
    :paramtype content: any
    :keyword content_type: Media type of the body sent to the API. Known values are:
     "application/pdf", "image/jpeg", "image/png", "image/tiff", and "application/json". Default
     value is None.
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = b'bytes'  # Optional.
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: str
    # Construct URL
    _url = "/mediatypes/analyzeNoAccept"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_content_type_with_encoding_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Pass in contentType 'text/plain; charset=UTF-8' to pass test. Value for input does not matter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Input parameter. Default value is None.
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
    _url = "/mediatypes/contentTypeWithEncoding"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_binary_body_with_two_content_types_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Binary body with two content types. Pass in of {'hello': 'world'} for the application/json
    content type, and a byte stream of 'hello, world!' for application/octet-stream.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. The payload body. Required. Default value is None.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). The payload body. Required. Default value is None.
    :paramtype content: any
    :keyword content_type: Media type of the body sent to the API. Known values are:
     "application/json" or "application/octet-stream". Default value is None.
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = b'bytes'  # Optional.
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "text/plain")

    # Construct URL
    _url = "/mediatypes/binaryBodyTwoContentTypes"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_binary_body_with_three_content_types_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Binary body with three content types. Pass in string 'hello, world' with content type
    'text/plain', {'hello': world'} with content type 'application/json' and a byte string for
    'application/octet-stream'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. The payload body. Required. Default value is None.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). The payload body. Required. Default value is None.
    :paramtype content: any
    :keyword content_type: Media type of the body sent to the API. Known values are:
     "application/json", "application/octet-stream", and "text/plain". Default value is None.
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = b'bytes'  # Optional.
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: str
    accept = _headers.pop('Accept', "text/plain")

    # Construct URL
    _url = "/mediatypes/binaryBodyThreeContentTypes"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_text_and_json_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Body that's either text/plain or application/json.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. The payload body. Required. Default value is None.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). The payload body. Required. Default value is None.
    :paramtype content: any
    :keyword content_type: Media type of the body sent to the API. Known values are: "text/plain"
     or "application/json". Default value is None.
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
    accept = _headers.pop('Accept', "text/plain")

    # Construct URL
    _url = "/mediatypes/textAndJson"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )
