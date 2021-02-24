# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.pipeline.transport import HttpRequest


def _head200_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/200")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.head(url, query_parameters, header_parameters)


def _head204_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/204")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.head(url, query_parameters, header_parameters)


def _head404_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/http/success/404")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.head(url, query_parameters, header_parameters)
