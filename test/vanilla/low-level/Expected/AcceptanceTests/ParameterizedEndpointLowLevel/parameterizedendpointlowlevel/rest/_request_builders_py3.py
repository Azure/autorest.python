# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any

from msrest import Serializer

from azure.core.rest import HttpRequest

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(**kwargs: Any) -> HttpRequest:
    """Basic get to make sure base url formatting of 'endpoint' works.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    _url = "/parameterizedEndpoint/get"

    return HttpRequest(method="GET", url=_url, **kwargs)
