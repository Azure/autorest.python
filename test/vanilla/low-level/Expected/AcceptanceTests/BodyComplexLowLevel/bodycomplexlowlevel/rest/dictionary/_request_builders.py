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
    from typing import Any, Dict, Optional, TypeVar

    T = TypeVar("T")
    JSONType = Any

_SERIALIZER = Serializer()

# fmt: off

def build_get_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get complex types with dictionary property.

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
                "defaultProgram": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                }
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop('Accept', "application/json")

    # Construct URL
    _url = "/complex/dictionary/typed/valid"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put complex types with dictionary property.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Please put a dictionary with 5 key-value pairs:
     "txt":"notepad", "bmp":"mspaint", "xls":"excel", "exe":"", "":null. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Please put a dictionary with 5 key-value pairs:
     "txt":"notepad", "bmp":"mspaint", "xls":"excel", "exe":"", "":null. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "defaultProgram": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                }
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', case_insensitive_dict(_headers).pop('Content-Type', None))  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop('Accept', "application/json")

    # Construct URL
    _url = "/complex/dictionary/typed/valid"

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


def build_get_empty_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get complex types with dictionary property which is empty.

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
                "defaultProgram": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                }
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop('Accept', "application/json")

    # Construct URL
    _url = "/complex/dictionary/typed/empty"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_empty_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put complex types with dictionary property which is empty.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Please put an empty dictionary. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Please put an empty dictionary. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "defaultProgram": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                }
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', case_insensitive_dict(_headers).pop('Content-Type', None))  # type: Optional[str]
    accept = case_insensitive_dict(_headers).pop('Accept', "application/json")

    # Construct URL
    _url = "/complex/dictionary/typed/empty"

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


def build_get_null_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get complex types with dictionary property which is null.

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
                "defaultProgram": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                }
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop('Accept', "application/json")

    # Construct URL
    _url = "/complex/dictionary/typed/null"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_not_provided_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get complex types with dictionary property while server doesn't provide a response payload.

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
                "defaultProgram": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                }
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = case_insensitive_dict(_headers).pop('Accept', "application/json")

    # Construct URL
    _url = "/complex/dictionary/typed/notprovided"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )
