# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional

from azure.core.protocol import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def prepare_get_report(qualifier: Optional[str] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/report/azure")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if qualifier is not None:
        query_parameters["qualifier"] = _SERIALIZER.query("qualifier", qualifier, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )
