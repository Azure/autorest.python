# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core import AsyncPipelineClient
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest
from msrest import Deserializer, Serializer

from ._configuration import AutoRestParameterizedHostTestPagingClientConfiguration
from .operations import PagingOperations
from .. import models


class AutoRestParameterizedHostTestPagingClient(object):
    """Test Infrastructure for AutoRest.

    :ivar paging: PagingOperations operations
    :vartype paging: custombaseurlpaging.aio.operations.PagingOperations
    :param host: A string value that is used as a global part of the parameterized host.
    :type host: str
    """

    def __init__(self, host: str = "host", **kwargs: Any) -> None:
        base_url = "http://{accountName}{host}"
        self._config = AutoRestParameterizedHostTestPagingClientConfiguration(host, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.paging = PagingOperations(self._client, self._config, self._serialize, self._deserialize)

    async def invoke(self, request: HttpRequest, **kwargs: Any) -> PipelineResponse:
        path_format_arguments = {
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)
        stream = kwargs.pop("stream", False)
        return await self._client._pipeline.run(request, stream=stream, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestParameterizedHostTestPagingClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
