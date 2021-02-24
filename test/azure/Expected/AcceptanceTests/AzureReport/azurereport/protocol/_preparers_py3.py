# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional

from azure.core.pipeline.transport import HttpRequest


def _get_report_request(self, qualifier: Optional[str] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/report/azure")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if qualifier is not None:
        query_parameters["qualifier"] = self._serialize.query("qualifier", qualifier, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.get(url, query_parameters, header_parameters)
