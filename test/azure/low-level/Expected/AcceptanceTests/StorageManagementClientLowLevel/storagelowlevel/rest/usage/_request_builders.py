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

from ..._vendor import _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_list_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Gets the current usage count and the limit for the resources under the subscription.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "value": [
                    {
                        "currentValue": 0,  # Optional. Gets the current count of the
                          allocated resources in the subscription.
                        "limit": 0,  # Optional. Gets the maximum count of the
                          resources that can be allocated in the subscription.
                        "name": {
                            "localizedValue": "str",  # Optional. Gets a
                              localized string describing the resource name.
                            "value": "str"  # Optional. Gets a string describing
                              the resource name.
                        },
                        "unit": "str"  # Optional. Gets the unit of measurement.
                          Possible values include: "Count", "Bytes", "Seconds", "Percent",
                          "CountsPerSecond", "BytesPerSecond".
                    }
                ]
            }
    """

    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)
    _params = kwargs.pop("params", {}) or {}
    if isinstance(_params, dict):
        _params = case_insensitive_dict(_params)

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2015-05-01-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json, text/json")

    # Construct URL
    _url = "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/usages"
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )
