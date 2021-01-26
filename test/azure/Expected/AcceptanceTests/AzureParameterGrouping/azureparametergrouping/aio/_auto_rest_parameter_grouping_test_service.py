# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core import AsyncPipelineClient
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest
from msrest import Deserializer, Serializer

from ._configuration import AutoRestParameterGroupingTestServiceConfiguration
from .operations import ParameterGroupingOperations
from .. import models


class AutoRestParameterGroupingTestService(object):
    """Test Infrastructure for AutoRest.

    :ivar parameter_grouping: ParameterGroupingOperations operations
    :vartype parameter_grouping: azureparametergrouping.aio.operations.ParameterGroupingOperations
    :param str base_url: Service URL
    """

    def __init__(self, base_url: Optional[str] = None, **kwargs: Any) -> None:
        if not base_url:
            base_url = "http://localhost:3000"
        self._config = AutoRestParameterGroupingTestServiceConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.parameter_grouping = ParameterGroupingOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    async def invoke(self, request: HttpRequest, **kwargs: Any) -> PipelineResponse:
        stream = kwargs.pop("stream", False)
        return await self._client._pipeline.run(request, stream=stream, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestParameterGroupingTestService":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
