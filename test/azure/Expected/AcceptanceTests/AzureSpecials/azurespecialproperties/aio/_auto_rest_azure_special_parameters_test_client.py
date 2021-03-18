# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.protocol import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import AutoRestAzureSpecialParametersTestClientConfiguration
from .operations import XMsClientRequestIdOperations
from .operations import SubscriptionInCredentialsOperations
from .operations import SubscriptionInMethodOperations
from .operations import ApiVersionDefaultOperations
from .operations import ApiVersionLocalOperations
from .operations import SkipUrlEncodingOperations
from .operations import OdataOperations
from .operations import HeaderOperations
from .. import models


class AutoRestAzureSpecialParametersTestClient(object):
    """Test Infrastructure for AutoRest.

    :ivar xms_client_request_id: XMsClientRequestIdOperations operations
    :vartype xms_client_request_id: azurespecialproperties.aio.operations.XMsClientRequestIdOperations
    :ivar subscription_in_credentials: SubscriptionInCredentialsOperations operations
    :vartype subscription_in_credentials: azurespecialproperties.aio.operations.SubscriptionInCredentialsOperations
    :ivar subscription_in_method: SubscriptionInMethodOperations operations
    :vartype subscription_in_method: azurespecialproperties.aio.operations.SubscriptionInMethodOperations
    :ivar api_version_default: ApiVersionDefaultOperations operations
    :vartype api_version_default: azurespecialproperties.aio.operations.ApiVersionDefaultOperations
    :ivar api_version_local: ApiVersionLocalOperations operations
    :vartype api_version_local: azurespecialproperties.aio.operations.ApiVersionLocalOperations
    :ivar skip_url_encoding: SkipUrlEncodingOperations operations
    :vartype skip_url_encoding: azurespecialproperties.aio.operations.SkipUrlEncodingOperations
    :ivar odata: OdataOperations operations
    :vartype odata: azurespecialproperties.aio.operations.OdataOperations
    :ivar header: HeaderOperations operations
    :vartype header: azurespecialproperties.aio.operations.HeaderOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription id, which appears in the path, always modeled in credentials. The value is always '1234-5678-9012-3456'.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self, credential: "AsyncTokenCredential", subscription_id: str, base_url: Optional[str] = None, **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = "http://localhost:3000"
        self._config = AutoRestAzureSpecialParametersTestClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.xms_client_request_id = XMsClientRequestIdOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.subscription_in_credentials = SubscriptionInCredentialsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.subscription_in_method = SubscriptionInMethodOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.api_version_default = ApiVersionDefaultOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.api_version_local = ApiVersionLocalOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.skip_url_encoding = SkipUrlEncodingOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.odata = OdataOperations(self._client, self._config, self._serialize, self._deserialize)
        self.header = HeaderOperations(self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.protocol.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.protocol.AsyncHttpResponse
        """
        http_request.url = self._client.format_url(http_request.url)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return AsyncHttpResponse(
            status_code=pipeline_response.http_response.status_code,
            request=http_request,
            _internal_response=pipeline_response.http_response,
        )

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestAzureSpecialParametersTestClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
