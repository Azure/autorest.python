# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

from ..._vendor import _get_from_dict

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional, TypeVar

    T = TypeVar("T")
    JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_get_null_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get null datetime value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/null')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_get_invalid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get invalid datetime value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/invalid')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_get_overflow_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get overflow datetime value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/overflow')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_get_underflow_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get underflow datetime value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/underflow')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_put_utc_max_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put max datetime value 9999-12-31T23:59:59.999Z.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. datetime body.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). datetime body.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = "2020-02-20 00:00:00"  # Optional.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/max/utc')

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


def build_put_utc_max_date_time7_digits_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put max datetime value 9999-12-31T23:59:59.9999999Z.

    This is against the recommendation that asks for 3 digits, but allow to test what happens in
    that scenario.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. datetime body.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). datetime body.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = "2020-02-20 00:00:00"  # Optional.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/max/utc7ms')

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


def build_get_utc_lowercase_max_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get max datetime value 9999-12-31t23:59:59.999z.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/max/utc/lowercase')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_get_utc_uppercase_max_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get max datetime value 9999-12-31T23:59:59.999Z.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/max/utc/uppercase')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_get_utc_uppercase_max_date_time7_digits_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get max datetime value 9999-12-31T23:59:59.9999999Z.

    This is against the recommendation that asks for 3 digits, but allow to test what happens in
    that scenario.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/max/utc7ms/uppercase')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_put_local_positive_offset_max_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put max datetime value with positive numoffset 9999-12-31t23:59:59.999+14:00.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. datetime body.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). datetime body.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = "2020-02-20 00:00:00"  # Optional.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/max/localpositiveoffset')

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


def build_get_local_positive_offset_lowercase_max_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get max datetime value with positive num offset 9999-12-31t23:59:59.999+14:00.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/max/localpositiveoffset/lowercase')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_get_local_positive_offset_uppercase_max_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get max datetime value with positive num offset 9999-12-31T23:59:59.999+14:00.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/max/localpositiveoffset/uppercase')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_put_local_negative_offset_max_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put max datetime value with positive numoffset 9999-12-31t23:59:59.999-14:00.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. datetime body.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). datetime body.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = "2020-02-20 00:00:00"  # Optional.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/max/localnegativeoffset')

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


def build_get_local_negative_offset_uppercase_max_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get max datetime value with positive num offset 9999-12-31T23:59:59.999-14:00.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/max/localnegativeoffset/uppercase')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_get_local_negative_offset_lowercase_max_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get max datetime value with positive num offset 9999-12-31t23:59:59.999-14:00.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/max/localnegativeoffset/lowercase')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_put_utc_min_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put min datetime value 0001-01-01T00:00:00Z.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. datetime body.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). datetime body.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = "2020-02-20 00:00:00"  # Optional.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/min/utc')

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


def build_get_utc_min_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get min datetime value 0001-01-01T00:00:00Z.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/min/utc')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_put_local_positive_offset_min_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put min datetime value 0001-01-01T00:00:00+14:00.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. datetime body.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). datetime body.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = "2020-02-20 00:00:00"  # Optional.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/min/localpositiveoffset')

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


def build_get_local_positive_offset_min_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get min datetime value 0001-01-01T00:00:00+14:00.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/min/localpositiveoffset')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_put_local_negative_offset_min_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put min datetime value 0001-01-01T00:00:00-14:00.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. datetime body.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). datetime body.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = "2020-02-20 00:00:00"  # Optional.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/min/localnegativeoffset')

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


def build_get_local_negative_offset_min_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get min datetime value 0001-01-01T00:00:00-14:00.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/min/localnegativeoffset')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_get_local_no_offset_min_date_time_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get min datetime value 0001-01-01T00:00:00.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/datetime/min/localnooffset')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )
