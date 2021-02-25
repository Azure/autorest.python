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

def _test_request(
    id,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "1.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/test')
    path_format_arguments = {
        'Endpoint': _SERIALIZER.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
    }
    url = self._client.format_url(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['id'] = _SERIALIZER.query("id", id, 'int')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    return self._client.put(url, query_parameters, header_parameters)