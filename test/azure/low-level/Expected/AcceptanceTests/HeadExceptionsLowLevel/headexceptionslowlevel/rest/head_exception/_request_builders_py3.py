# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any

from azure.core.rest import HttpRequest
from msrest import Serializer

from ..._vendor import _get_from_dict

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_head200_request(**kwargs: Any) -> HttpRequest:
    """Return 200 status code if successful.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/200")

    return HttpRequest(method="HEAD", url=url, **kwargs)


def build_head204_request(**kwargs: Any) -> HttpRequest:
    """Return 204 status code if successful.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/204")

    return HttpRequest(method="HEAD", url=url, **kwargs)


def build_head404_request(**kwargs: Any) -> HttpRequest:
    """Return 404 status code if successful.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/404")

    return HttpRequest(method="HEAD", url=url, **kwargs)
