# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional, Union

from azure.core.pipeline.transport import HttpRequest


def _put_request(self, body: Optional[Union[int, "_models.IntEnum"]] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/nonStringEnums/int/put")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body
    return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)


def _get_request(self, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/nonStringEnums/int/get")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.get(url, query_parameters, header_parameters)


def _put_request(self, body: Optional[Union[float, "_models.FloatEnum"]] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/nonStringEnums/float/put")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body
    return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)


def _get_request(self, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/nonStringEnums/float/get")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.get(url, query_parameters, header_parameters)
