# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from azure.mgmt.core.policies import ARMAutoResourceProviderRegistrationPolicy

from ._configuration import AzureSphereClientConfiguration
from ._serialization import Deserializer, Serializer
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

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class AzureSphereClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Azure Sphere resource management API.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.spheredpg.operations.Operations
    :ivar catalogs: CatalogsOperations operations
    :vartype catalogs: azure.mgmt.spheredpg.operations.CatalogsOperations
    :ivar certificates: CertificatesOperations operations
    :vartype certificates: azure.mgmt.spheredpg.operations.CertificatesOperations
    :ivar images: ImagesOperations operations
    :vartype images: azure.mgmt.spheredpg.operations.ImagesOperations
    :ivar products: ProductsOperations operations
    :vartype products: azure.mgmt.spheredpg.operations.ProductsOperations
    :ivar device_groups: DeviceGroupsOperations operations
    :vartype device_groups: azure.mgmt.spheredpg.operations.DeviceGroupsOperations
    :ivar deployments: DeploymentsOperations operations
    :vartype deployments: azure.mgmt.spheredpg.operations.DeploymentsOperations
    :ivar devices: DevicesOperations operations
    :vartype devices: azure.mgmt.spheredpg.operations.DevicesOperations
    :param credential: Credential used to authenticate requests to the service. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service host. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: The API version to use for this operation. Default value is "2024-04-01".
     Note that overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AzureSphereClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                ARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.catalogs = CatalogsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.certificates = CertificatesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.images = ImagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.products = ProductsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.device_groups = DeviceGroupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.deployments = DeploymentsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.devices = DevicesOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
