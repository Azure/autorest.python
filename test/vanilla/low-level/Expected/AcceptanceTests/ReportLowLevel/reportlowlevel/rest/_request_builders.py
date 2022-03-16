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
    from typing import Any, Dict, Optional

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

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "str": 0  # Optional.
            }
    """

    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)
    _params = kwargs.pop("params", {}) or {}
    if isinstance(_params, dict):
        _params = case_insensitive_dict(_params)

    qualifier = kwargs.pop('qualifier', _params.pop('qualifier', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/report"

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


def build_get_optional_report_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get optional test coverage report.

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

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "str": 0  # Optional.
            }
    """

    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)
    _params = kwargs.pop("params", {}) or {}
    if isinstance(_params, dict):
        _params = case_insensitive_dict(_params)

    qualifier = kwargs.pop('qualifier', _params.pop('qualifier', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/report/optional"

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
