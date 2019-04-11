# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core import PipelineClient
from msrest import Serializer, Deserializer

from ._configuration_async import AutoRestReportServiceForAzureConfiguration
from .operations_async import AutoRestReportServiceForAzureOperationsMixin
from .. import models


class AutoRestReportServiceForAzure(AutoRestReportServiceForAzureOperationsMixin):
    """Test Infrastructure for AutoRest


    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials=None, base_url=None, config=None, **kwargs):

        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = config or AutoRestReportServiceForAzureConfiguration(credentials, **kwargs)
        pipeline = kwargs.get('pipeline', self._config.build_pipeline())
        self._client = PipelineClient(base_url, config=self._config, pipeline=pipeline, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    async def __aenter__(self):
        await self.pipeline.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self.pipeline.__aexit__(*exc_details)

    async def __aenter__(self):
        await self._client.pipeline.__enter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.pipeline.__exit__(*exc_details)
