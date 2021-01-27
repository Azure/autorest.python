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

from ._configuration import AutoRestParameterizedCustomHostTestClientConfiguration
from .operations import PathsOperations
from .. import models


class AutoRestParameterizedCustomHostTestClient(object):
    """Test Infrastructure for AutoRest.

    :ivar paths: PathsOperations operations
    :vartype paths: custombaseurlmoreoptions.aio.operations.PathsOperations
    :param subscription_id: The subscription id with value 'test12'.
    :type subscription_id: str
    :param dns_suffix: A string value that is used as a global part of the parameterized host. Default value 'host'.
    :type dns_suffix: str
    """

    def __init__(self, subscription_id: str, dns_suffix: str = "host", **kwargs: Any) -> None:
        base_url = "{vault}{secret}{dnsSuffix}"
        self._config = AutoRestParameterizedCustomHostTestClientConfiguration(subscription_id, dns_suffix, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.paths = PathsOperations(self._client, self._config, self._serialize, self._deserialize)

    async def invoke(self, request: HttpRequest, **kwargs: Any) -> PipelineResponse:
        path_format_arguments = {
            "subscriptionId": self._serialize.url("self._config.subscription_id", self._config.subscription_id, "str"),
            "dnsSuffix": self._serialize.url(
                "self._config.dns_suffix", self._config.dns_suffix, "str", skip_quote=True
            ),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)
        stream = kwargs.pop("stream", False)
        pipeline_response = await self._client._pipeline.run(request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestParameterizedCustomHostTestClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
