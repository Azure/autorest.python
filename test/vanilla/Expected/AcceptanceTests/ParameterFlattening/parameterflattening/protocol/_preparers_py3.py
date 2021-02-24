# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Dict

from azure.core.pipeline.transport import HttpRequest


def _update_request(
    self, resource_group_name: str, avset: str, body: "_models.AvailabilitySetUpdateParameters", **kwargs
) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")

    # Construct URL
    url = kwargs.pop("template_url", "/parameterFlattening/{resourceGroupName}/{availabilitySetName}")
    path_format_arguments = {
        "resourceGroupName": self._serialize.url("resource_group_name", resource_group_name, "str"),
        "availabilitySetName": self._serialize.url("avset", avset, "str", max_length=80, min_length=0),
    }
    url = self._client.format_url(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body
    return self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
