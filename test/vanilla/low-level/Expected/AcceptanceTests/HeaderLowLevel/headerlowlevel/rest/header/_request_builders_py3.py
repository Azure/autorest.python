# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Optional

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_param_existing_key_request(*, user_agent_parameter: str, **kwargs: Any) -> HttpRequest:
    """Send a post request with header value "User-Agent": "overwrite".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword user_agent_parameter: Send a post request with header value "User-Agent": "overwrite".
    :paramtype user_agent_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/existingkey"

    # Construct headers
    _headers["User-Agent"] = _SERIALIZER.header("user_agent_parameter", user_agent_parameter, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_existing_key_request(**kwargs: Any) -> HttpRequest:
    """Get a response with header value "User-Agent": "overwrite".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/existingkey"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_param_protected_key_request(**kwargs: Any) -> HttpRequest:
    """Send a post request with header value "Content-Type": "text/html".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type")  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/protectedkey"

    # Construct headers
    _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_protected_key_request(**kwargs: Any) -> HttpRequest:
    """Get a response with header value "Content-Type": "text/html".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/protectedkey"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_param_integer_request(*, scenario: str, value: int, **kwargs: Any) -> HttpRequest:
    """Send a post request with header values "scenario": "positive", "value": 1 or "scenario":
    "negative", "value": -2.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "positive" or "negative".
    :paramtype scenario: str
    :keyword value: Send a post request with header values 1 or -2.
    :paramtype value: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/prim/integer"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["value"] = _SERIALIZER.header("value", value, "int")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_integer_request(*, scenario: str, **kwargs: Any) -> HttpRequest:
    """Get a response with header value "value": 1 or -2.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "positive" or "negative".
    :paramtype scenario: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/prim/integer"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_param_long_request(*, scenario: str, value: int, **kwargs: Any) -> HttpRequest:
    """Send a post request with header values "scenario": "positive", "value": 105 or "scenario":
    "negative", "value": -2.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "positive" or "negative".
    :paramtype scenario: str
    :keyword value: Send a post request with header values 105 or -2.
    :paramtype value: long
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/prim/long"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["value"] = _SERIALIZER.header("value", value, "long")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_long_request(*, scenario: str, **kwargs: Any) -> HttpRequest:
    """Get a response with header value "value": 105 or -2.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "positive" or "negative".
    :paramtype scenario: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/prim/long"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_param_float_request(*, scenario: str, value: float, **kwargs: Any) -> HttpRequest:
    """Send a post request with header values "scenario": "positive", "value": 0.07 or "scenario":
    "negative", "value": -3.0.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "positive" or "negative".
    :paramtype scenario: str
    :keyword value: Send a post request with header values 0.07 or -3.0.
    :paramtype value: float
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/prim/float"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["value"] = _SERIALIZER.header("value", value, "float")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_float_request(*, scenario: str, **kwargs: Any) -> HttpRequest:
    """Get a response with header value "value": 0.07 or -3.0.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "positive" or "negative".
    :paramtype scenario: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/prim/float"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_param_double_request(*, scenario: str, value: float, **kwargs: Any) -> HttpRequest:
    """Send a post request with header values "scenario": "positive", "value": 7e120 or "scenario":
    "negative", "value": -3.0.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "positive" or "negative".
    :paramtype scenario: str
    :keyword value: Send a post request with header values 7e120 or -3.0.
    :paramtype value: float
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/prim/double"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["value"] = _SERIALIZER.header("value", value, "float")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_double_request(*, scenario: str, **kwargs: Any) -> HttpRequest:
    """Get a response with header value "value": 7e120 or -3.0.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "positive" or "negative".
    :paramtype scenario: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/prim/double"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_param_bool_request(*, scenario: str, value: bool, **kwargs: Any) -> HttpRequest:
    """Send a post request with header values "scenario": "true", "value": true or "scenario":
    "false", "value": false.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "true" or "false".
    :paramtype scenario: str
    :keyword value: Send a post request with header values true or false.
    :paramtype value: bool
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/prim/bool"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["value"] = _SERIALIZER.header("value", value, "bool")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_bool_request(*, scenario: str, **kwargs: Any) -> HttpRequest:
    """Get a response with header value "value": true or false.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "true" or "false".
    :paramtype scenario: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/prim/bool"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_param_string_request(*, scenario: str, value: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    """Send a post request with header values "scenario": "valid", "value": "The quick brown fox jumps
    over the lazy dog" or "scenario": "null", "value": null or "scenario": "empty", "value": "".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid" or "null" or
     "empty".
    :paramtype scenario: str
    :keyword value: Send a post request with header values "The quick brown fox jumps over the lazy
     dog" or null or "". Default value is None.
    :paramtype value: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/prim/string"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    if value is not None:
        _headers["value"] = _SERIALIZER.header("value", value, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_string_request(*, scenario: str, **kwargs: Any) -> HttpRequest:
    """Get a response with header values "The quick brown fox jumps over the lazy dog" or null or "".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid" or "null" or
     "empty".
    :paramtype scenario: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/prim/string"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_param_date_request(*, scenario: str, value: datetime.date, **kwargs: Any) -> HttpRequest:
    """Send a post request with header values "scenario": "valid", "value": "2010-01-01" or
    "scenario": "min", "value": "0001-01-01".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid" or "min".
    :paramtype scenario: str
    :keyword value: Send a post request with header values "2010-01-01" or "0001-01-01".
    :paramtype value: ~datetime.date
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/prim/date"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["value"] = _SERIALIZER.header("value", value, "date")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_date_request(*, scenario: str, **kwargs: Any) -> HttpRequest:
    """Get a response with header values "2010-01-01" or "0001-01-01".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid" or "min".
    :paramtype scenario: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/prim/date"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_param_datetime_request(*, scenario: str, value: datetime.datetime, **kwargs: Any) -> HttpRequest:
    """Send a post request with header values "scenario": "valid", "value": "2010-01-01T12:34:56Z" or
    "scenario": "min", "value": "0001-01-01T00:00:00Z".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid" or "min".
    :paramtype scenario: str
    :keyword value: Send a post request with header values "2010-01-01T12:34:56Z" or
     "0001-01-01T00:00:00Z".
    :paramtype value: ~datetime.datetime
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/prim/datetime"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["value"] = _SERIALIZER.header("value", value, "iso-8601")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_datetime_request(*, scenario: str, **kwargs: Any) -> HttpRequest:
    """Get a response with header values "2010-01-01T12:34:56Z" or "0001-01-01T00:00:00Z".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid" or "min".
    :paramtype scenario: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/prim/datetime"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_param_datetime_rfc1123_request(
    *, scenario: str, value: Optional[datetime.datetime] = None, **kwargs: Any
) -> HttpRequest:
    """Send a post request with header values "scenario": "valid", "value": "Wed, 01 Jan 2010 12:34:56
    GMT" or "scenario": "min", "value": "Mon, 01 Jan 0001 00:00:00 GMT".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid" or "min".
    :paramtype scenario: str
    :keyword value: Send a post request with header values "Wed, 01 Jan 2010 12:34:56 GMT" or "Mon,
     01 Jan 0001 00:00:00 GMT". Default value is None.
    :paramtype value: ~datetime.datetime
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/prim/datetimerfc1123"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    if value is not None:
        _headers["value"] = _SERIALIZER.header("value", value, "rfc-1123")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_datetime_rfc1123_request(*, scenario: str, **kwargs: Any) -> HttpRequest:
    """Get a response with header values "Wed, 01 Jan 2010 12:34:56 GMT" or "Mon, 01 Jan 0001 00:00:00
    GMT".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid" or "min".
    :paramtype scenario: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/prim/datetimerfc1123"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_param_duration_request(*, scenario: str, value: datetime.timedelta, **kwargs: Any) -> HttpRequest:
    """Send a post request with header values "scenario": "valid", "value": "P123DT22H14M12.011S".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid".
    :paramtype scenario: str
    :keyword value: Send a post request with header values "P123DT22H14M12.011S".
    :paramtype value: ~datetime.timedelta
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/prim/duration"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["value"] = _SERIALIZER.header("value", value, "duration")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_duration_request(*, scenario: str, **kwargs: Any) -> HttpRequest:
    """Get a response with header values "P123DT22H14M12.011S".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid".
    :paramtype scenario: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/prim/duration"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_param_byte_request(*, scenario: str, value: bytearray, **kwargs: Any) -> HttpRequest:
    """Send a post request with header values "scenario": "valid", "value": "啊齄丂狛狜隣郎隣兀﨩".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid".
    :paramtype scenario: str
    :keyword value: Send a post request with header values "啊齄丂狛狜隣郎隣兀﨩".
    :paramtype value: bytearray
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/prim/byte"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["value"] = _SERIALIZER.header("value", value, "bytearray")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_byte_request(*, scenario: str, **kwargs: Any) -> HttpRequest:
    """Get a response with header values "啊齄丂狛狜隣郎隣兀﨩".

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid".
    :paramtype scenario: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/prim/byte"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_param_enum_request(*, scenario: str, value: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    """Send a post request with header values "scenario": "valid", "value": "GREY" or "scenario":
    "null", "value": null.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid" or "null" or
     "empty".
    :paramtype scenario: str
    :keyword value: Send a post request with header values 'GREY'. Possible values are: "White",
     "black", and "GREY". Default value is None.
    :paramtype value: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/param/prim/enum"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    if value is not None:
        _headers["value"] = _SERIALIZER.header("value", value, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_response_enum_request(*, scenario: str, **kwargs: Any) -> HttpRequest:
    """Get a response with header values "GREY" or null.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword scenario: Send a post request with header values "scenario": "valid" or "null" or
     "empty".
    :paramtype scenario: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/response/prim/enum"

    # Construct headers
    _headers["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_custom_request_id_request(**kwargs: Any) -> HttpRequest:
    """Send x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the
    request.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/header/custom/x-ms-client-request-id/9C4D50EE-2D56-4CD3-8152-34347DC9F2B0"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)
