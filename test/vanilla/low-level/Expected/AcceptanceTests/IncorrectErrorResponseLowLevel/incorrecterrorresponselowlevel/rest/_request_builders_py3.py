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


def build_get_incorrect_error_from_server_request(**kwargs: Any) -> HttpRequest:
    """Get an error response from the server that is not as described in our Error object. Want to
    swallow the deserialization error and still return an HttpResponseError to the users.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    _url = "/incorrectError"

    return HttpRequest(method="GET", url=_url, **kwargs)
