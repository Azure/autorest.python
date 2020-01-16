# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import AutoRestParameterizedHostTestPagingClientConfiguration
from .operations_async import PagingOperations
from .. import models


class AutoRestParameterizedHostTestPagingClient(object):
    """Test Infrastructure for AutoRest

    :ivar paging: PagingOperations operations
    :vartype paging: custombaseurlpaging.aio.operations_async.PagingOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param host: A string value that is used as a global part of the parameterized host
    :type host: str
    """

    def __init__(self, credential, host, **kwargs):
        base_url = 'http://{accountName}{host}'
        self._config = AutoRestParameterizedHostTestPagingClientConfiguration(credential, host, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.paging = PagingOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self):
        await self._client.close()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
