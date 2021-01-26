# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from . import models
from ._configuration import StorageManagementClientConfiguration
from .operations import StorageAccountsOperations, UsageOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline import PipelineResponse
    from azure.core.pipeline.transport import HttpRequest


class StorageManagementClient(object):
    """StorageManagementClient.

    :ivar storage_accounts: StorageAccountsOperations operations
    :vartype storage_accounts: storage.operations.StorageAccountsOperations
    :ivar usage: UsageOperations operations
    :vartype usage: storage.operations.UsageOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = "https://management.azure.com"
        self._config = StorageManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.storage_accounts = StorageAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.usage = UsageOperations(self._client, self._config, self._serialize, self._deserialize)

    def invoke(self, request, **kwargs):
        # type: (HttpRequest, Any) -> PipelineResponse
        path_format_arguments = {
            "subscriptionId": self._serialize.url("self._config.subscription_id", self._config.subscription_id, "str"),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)
        return self._client._pipeline.run(request, stream=False, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> StorageManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
