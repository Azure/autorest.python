# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional

from azure.core.pipeline.transport import HttpRequest
from azure.core.pipeline.transport._base import _format_url_section
from msrest import Serializer

_SERIALIZER = Serializer()


def _prepare_paths_get_empty_request(
    vault: str,
    secret: str,
    key_name: str,
    subscription_id: str,
    dns_suffix: str = "host",
    key_version: Optional[str] = "v1",
    **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/customuri/{subscriptionId}/{keyName}")
    path_format_arguments = {
        "vault": _SERIALIZER.url("vault", vault, "str", skip_quote=True),
        "secret": _SERIALIZER.url("secret", secret, "str", skip_quote=True),
        "dnsSuffix": _SERIALIZER.url("dns_suffix", dns_suffix, "str", skip_quote=True),
        "keyName": _SERIALIZER.url("key_name", key_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if key_version is not None:
        query_parameters["keyVersion"] = _SERIALIZER.query("key_version", key_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request
