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

from ..._vendor import _format_url_section

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_pages_partial_url_request(**kwargs: Any) -> HttpRequest:
    """A paging operation that combines custom url, paging and partial URL and expect to concat after
    host.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "nextLink": "str",  # Optional.
                "values": [
                    {
                        "properties": {
                            "id": 0,  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                ]
            }
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/paging/customurl/partialnextlink")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get_pages_partial_url_operation_request(**kwargs: Any) -> HttpRequest:
    """A paging operation that combines custom url, paging and partial URL with next operation.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "nextLink": "str",  # Optional.
                "values": [
                    {
                        "properties": {
                            "id": 0,  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                ]
            }
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/paging/customurl/partialnextlinkop")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get_pages_partial_url_operation_next_request(next_link: str, **kwargs: Any) -> HttpRequest:
    """A paging operation that combines custom url, paging and partial URL.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param next_link: Next link for the list operation.
    :type next_link: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "nextLink": "str",  # Optional.
                "values": [
                    {
                        "properties": {
                            "id": 0,  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                ]
            }
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/paging/customurl/{nextLink}")
    path_format_arguments = {
        "nextLink": _SERIALIZER.url("next_link", next_link, "str", skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)
