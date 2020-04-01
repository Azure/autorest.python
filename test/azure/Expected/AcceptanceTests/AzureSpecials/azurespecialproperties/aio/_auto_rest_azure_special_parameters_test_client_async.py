# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import AutoRestAzureSpecialParametersTestClientConfiguration
from .operations_async import XMsClientRequestIdOperations
from .operations_async import SubscriptionInCredentialsOperations
from .operations_async import SubscriptionInMethodOperations
from .operations_async import ApiVersionDefaultOperations
from .operations_async import ApiVersionLocalOperations
from .operations_async import SkipUrlEncodingOperations
from .operations_async import OdataOperations
from .operations_async import HeaderOperations
from .. import models


class AutoRestAzureSpecialParametersTestClient(object):
    """Test Infrastructure for AutoRest.

    :ivar xms_client_request_id: XMsClientRequestIdOperations operations
    :vartype xms_client_request_id: azurespecialproperties.aio.operations_async.XMsClientRequestIdOperations
    :ivar subscription_in_credentials: SubscriptionInCredentialsOperations operations
    :vartype subscription_in_credentials: azurespecialproperties.aio.operations_async.SubscriptionInCredentialsOperations
    :ivar subscription_in_method: SubscriptionInMethodOperations operations
    :vartype subscription_in_method: azurespecialproperties.aio.operations_async.SubscriptionInMethodOperations
    :ivar api_version_default: ApiVersionDefaultOperations operations
    :vartype api_version_default: azurespecialproperties.aio.operations_async.ApiVersionDefaultOperations
    :ivar api_version_local: ApiVersionLocalOperations operations
    :vartype api_version_local: azurespecialproperties.aio.operations_async.ApiVersionLocalOperations
    :ivar skip_url_encoding: SkipUrlEncodingOperations operations
    :vartype skip_url_encoding: azurespecialproperties.aio.operations_async.SkipUrlEncodingOperations
    :ivar odata: OdataOperations operations
    :vartype odata: azurespecialproperties.aio.operations_async.OdataOperations
    :ivar header: HeaderOperations operations
    :vartype header: azurespecialproperties.aio.operations_async.HeaderOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.AsyncTokenCredential
    :param subscription_id: The subscription id, which appears in the path, always modeled in credentials. The value is always '1234-5678-9012-3456'.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestAzureSpecialParametersTestClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.xms_client_request_id = XMsClientRequestIdOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subscription_in_credentials = SubscriptionInCredentialsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subscription_in_method = SubscriptionInMethodOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_version_default = ApiVersionDefaultOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_version_local = ApiVersionLocalOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.skip_url_encoding = SkipUrlEncodingOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.odata = OdataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.header = HeaderOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestAzureSpecialParametersTestClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
