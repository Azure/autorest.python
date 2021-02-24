# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.pipeline.transport import HttpRequest

_SERIALIZER = Serializer()


def _poll_with_parameterized_endpoints_initial_request(
    account_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/lroParameterizedEndpoints")
    path_format_arguments = {
        "accountName": _SERIALIZER.url("account_name", account_name, "str", skip_quote=True),
        "host": _SERIALIZER.url("self._config.host", self._config.host, "str", skip_quote=True),
    }
    url = self._client.format_url(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)
