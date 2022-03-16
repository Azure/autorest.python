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
    from typing import Any

_SERIALIZER = Serializer()

# fmt: off

def build_custom_named_request_id_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword foo_client_request_id: The fooRequestId.
    :paramtype foo_client_request_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    foo_client_request_id = kwargs.pop('foo_client_request_id')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/azurespecials/customNamedRequestId"

    # Construct headers
    _headers['foo-client-request-id'] = _SERIALIZER.header("foo_client_request_id", foo_client_request_id, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_custom_named_request_id_param_grouping_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request,
    via a parameter group.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword foo_client_request_id: The fooRequestId.
    :paramtype foo_client_request_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    foo_client_request_id = kwargs.pop('foo_client_request_id')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/azurespecials/customNamedRequestIdParamGrouping"

    # Construct headers
    _headers['foo-client-request-id'] = _SERIALIZER.header("foo_client_request_id", foo_client_request_id, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_custom_named_request_id_head_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword foo_client_request_id: The fooRequestId.
    :paramtype foo_client_request_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    foo_client_request_id = kwargs.pop('foo_client_request_id')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/azurespecials/customNamedRequestIdHead"

    # Construct headers
    _headers['foo-client-request-id'] = _SERIALIZER.header("foo_client_request_id", foo_client_request_id, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="HEAD",
        url=_url,
        headers=_headers,
        **kwargs
    )
