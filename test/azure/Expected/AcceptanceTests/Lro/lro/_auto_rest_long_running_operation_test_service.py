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

from ._configuration import AutoRestLongRunningOperationTestServiceConfiguration
from .operations import LROsOperations
from .operations import LRORetrysOperations
from .operations import LROSADsOperations
from .operations import LROsCustomHeaderOperations
from . import models


class AutoRestLongRunningOperationTestService(object):
    """Long-running Operation for AutoRest


    :ivar lros: LROs operations
    :vartype lros: lro.operations.LROsOperations
    :ivar lro_retrys: LRORetrys operations
    :vartype lro_retrys: lro.operations.LRORetrysOperations
    :ivar lrosads: LROSADs operations
    :vartype lrosads: lro.operations.LROSADsOperations
    :ivar lr_os_custom_header: LROsCustomHeader operations
    :vartype lr_os_custom_header: lro.operations.LROsCustomHeaderOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None, **kwargs):

        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestLongRunningOperationTestServiceConfiguration(credentials, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.lros = LROsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.lro_retrys = LRORetrysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.lrosads = LROSADsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.lr_os_custom_header = LROsCustomHeaderOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
