# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict

from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_operation_one_request(*, parameter1: str, **kwargs: Any) -> HttpRequest:
    """Operation in operation group import, a reserved word.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword parameter1: Pass in 'foo' to pass this test.
    :paramtype parameter1: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    _url = "/reservedWords/operationGroup/import"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["parameter1"] = _SERIALIZER.query("parameter1", parameter1, "str")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, headers=_header_parameters, **kwargs)
