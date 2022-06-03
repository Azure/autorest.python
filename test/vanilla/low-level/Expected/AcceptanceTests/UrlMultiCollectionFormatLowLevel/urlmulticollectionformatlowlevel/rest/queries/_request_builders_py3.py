# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, List, Optional

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_array_string_multi_null_request(
    *,
    array_query: Optional[List[str]] = None,
    **kwargs: Any
) -> HttpRequest:
    """Get a null array of string using the multi-array format.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword array_query: a null array of string using the multi-array format. Default value is
     None.
    :paramtype array_query: list[str]
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/queries/array/multi/string/null"

    # Construct parameters
    if array_query is not None:
        _params['arrayQuery'] = [_SERIALIZER.query("array_query", q, 'str') if q is not None else '' for q in array_query]

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_array_string_multi_empty_request(
    *,
    array_query: Optional[List[str]] = None,
    **kwargs: Any
) -> HttpRequest:
    """Get an empty array [] of string using the multi-array format.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword array_query: an empty array [] of string using the multi-array format. Default value
     is None.
    :paramtype array_query: list[str]
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/queries/array/multi/string/empty"

    # Construct parameters
    if array_query is not None:
        _params['arrayQuery'] = [_SERIALIZER.query("array_query", q, 'str') if q is not None else '' for q in array_query]

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_array_string_multi_valid_request(
    *,
    array_query: Optional[List[str]] = None,
    **kwargs: Any
) -> HttpRequest:
    """Get an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' , null, ''] using the
    mult-array format.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword array_query: an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' , null,
     ''] using the mult-array format. Default value is None.
    :paramtype array_query: list[str]
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/queries/array/multi/string/valid"

    # Construct parameters
    if array_query is not None:
        _params['arrayQuery'] = [_SERIALIZER.query("array_query", q, 'str') if q is not None else '' for q in array_query]

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )
