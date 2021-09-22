# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_list_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
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
                        "currentValue": 0,  # Optional. Gets the current count of the allocated resources in the subscription.
                        "limit": 0,  # Optional. Gets the maximum count of the resources that can be allocated in the subscription.
                        "name": {
                            "localizedValue": "str",  # Optional. Gets a localized string describing the resource name.
                            "value": "str"  # Optional. Gets a string describing the resource name.
                        },
                        "unit": "str"  # Optional. Gets the unit of measurement. Possible values include: "Count", "Bytes", "Seconds", "Percent", "CountsPerSecond", "BytesPerSecond".
                    }
                ]
            }
    """

    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"
    # Construct URL
    url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/usages")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)
