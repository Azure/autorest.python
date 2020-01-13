# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import AutoRestHeadExceptionTestServiceConfiguration
from .operations_async import HeadExceptionOperations


class AutoRestHeadExceptionTestService(object):
    """Test Infrastructure for AutoRest


    :ivar head_exception: HeadExceptionOperations operations
    :vartype head_exception: headexceptions.aio.operations_async.HeadExceptionOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param str base_url: Service URL
    """

    def __init__(self, , base_url=None, **kwargs):
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestHeadExceptionTestServiceConfiguration(credential, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.head_exception = HeadExceptionOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self):
        await self._client.close()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
