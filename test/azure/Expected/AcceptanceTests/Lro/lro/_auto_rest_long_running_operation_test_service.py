# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import AutoRestLongRunningOperationTestServiceConfiguration
from .operations import LROsOperations
from .operations import LRORetrysOperations
from .operations import LROSADsOperations
from .operations import LROsCustomHeaderOperations
from . import models


class AutoRestLongRunningOperationTestService(object):
    """Long-running Operation for AutoRest.

    :ivar lros: LROsOperations operations
    :vartype lros: lro.operations.LROsOperations
    :ivar lro_retrys: LRORetrysOperations operations
    :vartype lro_retrys: lro.operations.LRORetrysOperations
    :ivar lrosads: LROSADsOperations operations
    :vartype lrosads: lro.operations.LROSADsOperations
    :ivar lr_os_custom_header: LROsCustomHeaderOperations operations
    :vartype lr_os_custom_header: lro.operations.LROsCustomHeaderOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestLongRunningOperationTestServiceConfiguration(credential, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
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
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestLongRunningOperationTestService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
