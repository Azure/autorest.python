# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

from .._vendor import _get_from_dict

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional, TypeVar

    T = TypeVar("T")
    JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_get_horse_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get a horse with name 'Fred' and isAShowHorse true.

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
                "isAShowHorse": bool,  # Optional.
                "name": "str"  # Required. 
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multipleInheritance/horse')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_put_horse_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put a horse with name 'General' and isAShowHorse false.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Put a horse with name 'General' and isAShowHorse false.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Put a horse with name 'General' and isAShowHorse false.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "isAShowHorse": bool,  # Optional.
                "name": "str"  # Required. 
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multipleInheritance/horse')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_get_pet_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get a pet with name 'Peanut'.

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
                "name": "str"  # Required. 
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multipleInheritance/pet')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_put_pet_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put a pet with name 'Butter'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Put a pet with name 'Butter'.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Put a pet with name 'Butter'.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "name": "str"  # Required. 
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multipleInheritance/pet')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_get_feline_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get a feline where meows and hisses are true.

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
                "hisses": bool,  # Optional.
                "meows": bool  # Optional.
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multipleInheritance/feline')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_put_feline_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put a feline who hisses and doesn't meow.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Put a feline who hisses and doesn't meow.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Put a feline who hisses and doesn't meow.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "hisses": bool,  # Optional.
                "meows": bool  # Optional.
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multipleInheritance/feline')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_get_cat_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get a cat with name 'Whiskers' where likesMilk, meows, and hisses is true.

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
                "hisses": bool,  # Optional.
                "likesMilk": bool,  # Optional.
                "meows": bool,  # Optional.
                "name": "str"  # Required. 
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multipleInheritance/cat')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_put_cat_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put a cat with name 'Boots' where likesMilk and hisses is false, meows is true.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Put a cat with name 'Boots' where likesMilk and hisses is
     false, meows is true.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Put a cat with name 'Boots' where likesMilk and hisses is
     false, meows is true.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "hisses": bool,  # Optional.
                "likesMilk": bool,  # Optional.
                "meows": bool,  # Optional.
                "name": "str"  # Required. 
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multipleInheritance/cat')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_get_kitten_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get a kitten with name 'Gatito' where likesMilk and meows is true, and hisses and eatsMiceYet
    is false.

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
                "eatsMiceYet": bool,  # Optional.
                "hisses": bool,  # Optional.
                "likesMilk": bool,  # Optional.
                "meows": bool,  # Optional.
                "name": "str"  # Required. 
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multipleInheritance/kitten')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_put_kitten_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and eatsMiceYet is
    true.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Put a kitten with name 'Kitty' where likesMilk and hisses
     is false, meows and eatsMiceYet is true.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Put a kitten with name 'Kitty' where likesMilk and hisses is
     false, meows and eatsMiceYet is true.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "eatsMiceYet": bool,  # Optional.
                "hisses": bool,  # Optional.
                "likesMilk": bool,  # Optional.
                "meows": bool,  # Optional.
                "name": "str"  # Required. 
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multipleInheritance/kitten')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=_headers,
        **kwargs
    )
