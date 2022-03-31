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

from ..._vendor import _format_url_section

T = TypeVar("T")
JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_update_pet_with_form_request(
    pet_id: int, *, data: Optional[Dict[str, Any]] = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    """Updates a pet in the store with form data.

    Updates a pet in the store with form data.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param pet_id: ID of pet that needs to be updated.
    :type pet_id: int
    :keyword data: Pass in dictionary that contains form data to include in the body of the
     request. Default value is None.
    :paramtype data: dict[str, any]
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # form-encoded input template you can fill out and use as your `data` input.
            data = {
                "name": "str",  # Optional. Updated name of the pet. Default value is None.
                "pet_age": 0,  # How many years is it old?.
                "pet_food": "str",  # Can take a value of meat, or fish, or plant. Known
                  values are: "meat", "fish", and "plant".
                "pet_type": "str",  # Can take a value of dog, or cat, or fish. Known values
                  are: "dog", "cat", and "fish".
                "status": "str"  # Optional. Updated status of the pet. Default value is
                  None.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    # Construct URL
    _url = "/formsdataurlencoded/pet/add/{petId}"
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, "int"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, data=data, content=content, **kwargs)


def build_partial_constant_body_request(
    *, data: Optional[Dict[str, Any]] = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    """Test a partially constant formdata body. Pass in { grant_type: 'access_token', access_token:
    'foo', service: 'bar' } to pass the test.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword data: Pass in dictionary that contains form data to include in the body of the
     request. Default value is None.
    :paramtype data: dict[str, any]
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # form-encoded input template you can fill out and use as your `data` input.
            data = {
                "access_token": "str",  # AAD access token, mandatory when grant_type is
                  access_token_refresh_token or access_token.
                "grant_type": "access_token",  # Default value is "access_token". Constant
                  part of a formdata body. Default value is "access_token". Note that overriding
                  this default value may result in unsupported behavior.
                "service": "str"  # Indicates the name of your Azure container registry.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    # Construct URL
    _url = "/formsdataurlencoded/partialConstantBody"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, data=data, content=content, **kwargs)
