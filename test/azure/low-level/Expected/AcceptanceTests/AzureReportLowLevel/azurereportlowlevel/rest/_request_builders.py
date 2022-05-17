# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_get_report_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get test coverage report.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword qualifier: If specified, qualifies the generated report further (e.g. '2.7' vs '3.5'
     in for Python). The only effect is, that generators that run all tests several times, can
     distinguish the generated reports. Default value is None.
    :paramtype qualifier: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    qualifier = kwargs.pop('qualifier', _params.pop('qualifier', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/report/azure"

    # Construct parameters
    if qualifier is not None:
        _params['qualifier'] = _SERIALIZER.query("qualifier", qualifier, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )
