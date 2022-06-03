# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models
from ._configuration import AutoRestAzureSpecialParametersTestClientConfiguration
from .operations import (
    ApiVersionDefaultOperations,
    ApiVersionLocalOperations,
    HeaderOperations,
    OdataOperations,
    SkipUrlEncodingOperations,
    SubscriptionInCredentialsOperations,
    SubscriptionInMethodOperations,
    XMsClientRequestIdOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class AutoRestAzureSpecialParametersTestClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Test Infrastructure for AutoRest.

    :ivar xms_client_request_id: XMsClientRequestIdOperations operations
    :vartype xms_client_request_id:
     azurespecialproperties.aio.operations.XMsClientRequestIdOperations
    :ivar subscription_in_credentials: SubscriptionInCredentialsOperations operations
    :vartype subscription_in_credentials:
     azurespecialproperties.aio.operations.SubscriptionInCredentialsOperations
    :ivar subscription_in_method: SubscriptionInMethodOperations operations
    :vartype subscription_in_method:
     azurespecialproperties.aio.operations.SubscriptionInMethodOperations
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
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription id, which appears in the path, always modeled in
     credentials. The value is always '1234-5678-9012-3456'. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "http://localhost:3000".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2015-07-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "http://localhost:3000",
        **kwargs: Any
    ) -> None:
        self._config = AutoRestAzureSpecialParametersTestClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
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

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestAzureSpecialParametersTestClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
