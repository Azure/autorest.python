# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.protocol import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict

_SERIALIZER = Serializer()


def prepare_availabilitysets_update(
    resource_group_name,  # type: str
    avset,  # type: str
    body,  # type: "_models.AvailabilitySetUpdateParameters"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop("content_type", "application/json")

    # Construct URL
    url = kwargs.pop("template_url", "/parameterFlattening/{resourceGroupName}/{availabilitySetName}")
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "availabilitySetName": _SERIALIZER.url("avset", avset, "str", max_length=80, min_length=0),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = body

    return HttpRequest(method="PATCH", url=url, headers=header_parameters, **body_content_kwargs)
