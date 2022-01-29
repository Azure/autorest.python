# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional

from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_report_request(
    *,
    qualifier: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Get test coverage report.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword qualifier: If specified, qualifies the generated report further (e.g. '2.7' vs '3.5'
     in for Python). The only effect is, that generators that run all tests several times, can
     distinguish the generated reports.
    :paramtype qualifier: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "str": 0  # Optional.
            }
    """

    accept = "application/json"
    # Construct URL
    url = '/report/azure'

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if qualifier is not None:
        query_parameters['qualifier'] = _SERIALIZER.query("qualifier", qualifier, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

