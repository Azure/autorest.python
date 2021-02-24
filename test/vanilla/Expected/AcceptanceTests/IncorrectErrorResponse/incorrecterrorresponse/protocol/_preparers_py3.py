# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from azure.core.pipeline.transport import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def _get_incorrect_error_from_server_request(**kwargs) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/incorrectError")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.get(url, query_parameters, header_parameters)
