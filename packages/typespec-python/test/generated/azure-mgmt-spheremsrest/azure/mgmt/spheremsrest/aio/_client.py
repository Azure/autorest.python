# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.pipeline import policies
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from azure.mgmt.core.policies import AsyncARMAutoResourceProviderRegistrationPolicy

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import AzureSphereClientConfiguration
from .operations import (
    CatalogsOperations,
    CertificatesOperations,
    DeploymentsOperations,
    DeviceGroupsOperations,
    DevicesOperations,
    ImagesOperations,
    Operations,
    ProductsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class AzureSphereClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Azure Sphere resource management API.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.spheremsrest.aio.operations.Operations
    :ivar catalogs: CatalogsOperations operations
    :vartype catalogs: azure.mgmt.spheremsrest.aio.operations.CatalogsOperations
    :ivar images: ImagesOperations operations
    :vartype images: azure.mgmt.spheremsrest.aio.operations.ImagesOperations
    :ivar device_groups: DeviceGroupsOperations operations
    :vartype device_groups: azure.mgmt.spheremsrest.aio.operations.DeviceGroupsOperations
    :ivar certificates: CertificatesOperations operations
    :vartype certificates: azure.mgmt.spheremsrest.aio.operations.CertificatesOperations
    :ivar deployments: DeploymentsOperations operations
    :vartype deployments: azure.mgmt.spheremsrest.aio.operations.DeploymentsOperations
    :ivar devices: DevicesOperations operations
    :vartype devices: azure.mgmt.spheremsrest.aio.operations.DevicesOperations
    :ivar products: ProductsOperations operations
    :vartype products: azure.mgmt.spheremsrest.aio.operations.ProductsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service host. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: The API version to use for this operation. Default value is
     "2022-09-01-preview". Note that overriding this default value may result in unsupported
     behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AzureSphereClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        config_policies = [
            policies.RequestIdPolicy(**kwargs),
            self._config.headers_policy,
            self._config.user_agent_policy,
            self._config.proxy_policy,
            policies.ContentDecodePolicy(**kwargs),
            AsyncARMAutoResourceProviderRegistrationPolicy(),
            self._config.redirect_policy,
            self._config.retry_policy,
            self._config.authentication_policy,
            self._config.custom_hook_policy,
            self._config.logging_policy,
            policies.DistributedTracingPolicy(**kwargs),
            policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
            self._config.http_logging_policy,
        ]
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(
            base_url=base_url, policies=config_policies, **kwargs
        )

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.catalogs = CatalogsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.images = ImagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.device_groups = DeviceGroupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.certificates = CertificatesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.deployments = DeploymentsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.devices = DevicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.products = ProductsOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
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

    async def __aenter__(self) -> "AzureSphereClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
