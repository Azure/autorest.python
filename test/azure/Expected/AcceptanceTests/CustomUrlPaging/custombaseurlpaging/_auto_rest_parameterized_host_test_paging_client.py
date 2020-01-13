# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import AutoRestParameterizedHostTestPagingClientConfiguration
from .operations import PagingOperations
from . import models


class AutoRestParameterizedHostTestPagingClient(object):
    """Test Infrastructure for AutoRest


    :ivar paging: PagingOperations operations
    :vartype paging: custombaseurlpaging.operations.PagingOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param host: A string value that is used as a global part of the parameterized host
    :type host: str
    """

    def __init__(self, credential, host, **kwargs):
        # type: (azure.core.credentials.TokenCredential, str, **Any) -> None
        base_url = 'http://{accountName}{host}'
        self._config = AutoRestParameterizedHostTestPagingClientConfiguration(credential, host, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.paging = PagingOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestParameterizedHostTestPagingClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
