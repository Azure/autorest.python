# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import AutoRestSwaggerBATHeaderServiceConfiguration
from .operations_async import HeaderOperations
from .. import models


class AutoRestSwaggerBATHeaderService(object):
    """Test Infrastructure for AutoRest

    :ivar header: HeaderOperations operations
    :vartype header: header.aio.operations_async.HeaderOperations
    :param str base_url: Service URL
    """

    def __init__(self, base_url=None, **kwargs):
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestSwaggerBATHeaderServiceConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.header = HeaderOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self):
        await self._client.close()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
