# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import AutoRestParameterizedHostTestClientConfiguration
from .operations_async import PathsOperations
from .. import models


class AutoRestParameterizedHostTestClient(object):
    """Test Infrastructure for AutoRest

    :ivar paths: PathsOperations operations
    :vartype paths: custombaseurl.aio.operations_async.PathsOperations
    :param host: A string value that is used as a global part of the parameterized host
    :type host: str
    """

    def __init__(self['host: str'], **kwargs) -> None:
        base_url = 'http://{accountName}{host}'
        self._config = AutoRestParameterizedHostTestClientConfiguration(host, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.paths = PathsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestParameterizedHostTestClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
