# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING
from typing_extensions import Self

from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.settings import settings
from azure.mgmt.core import ARMPipelineClient
from azure.mgmt.core.policies import ARMAutoResourceProviderRegistrationPolicy
from azure.mgmt.core.tools import get_arm_endpoints

from ._configuration import AutoRestAzureSpecialParametersTestClientConfiguration
from ._serialization import Deserializer, Serializer
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
    from azure.core.credentials import TokenCredential


class AutoRestAzureSpecialParametersTestClient:  # pylint: disable=too-many-instance-attributes
    """Test Infrastructure for AutoRest.

    :ivar xms_client_request_id: XMsClientRequestIdOperations operations
    :vartype xms_client_request_id:
     azurespecialpropertiesversiontolerant.operations.XMsClientRequestIdOperations
    :ivar subscription_in_credentials: SubscriptionInCredentialsOperations operations
    :vartype subscription_in_credentials:
     azurespecialpropertiesversiontolerant.operations.SubscriptionInCredentialsOperations
    :ivar subscription_in_method: SubscriptionInMethodOperations operations
    :vartype subscription_in_method:
     azurespecialpropertiesversiontolerant.operations.SubscriptionInMethodOperations
    :ivar api_version_default: ApiVersionDefaultOperations operations
    :vartype api_version_default:
     azurespecialpropertiesversiontolerant.operations.ApiVersionDefaultOperations
    :ivar api_version_local: ApiVersionLocalOperations operations
    :vartype api_version_local:
     azurespecialpropertiesversiontolerant.operations.ApiVersionLocalOperations
    :ivar skip_url_encoding: SkipUrlEncodingOperations operations
    :vartype skip_url_encoding:
     azurespecialpropertiesversiontolerant.operations.SkipUrlEncodingOperations
    :ivar odata: OdataOperations operations
    :vartype odata: azurespecialpropertiesversiontolerant.operations.OdataOperations
    :ivar header: HeaderOperations operations
    :vartype header: azurespecialpropertiesversiontolerant.operations.HeaderOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription id, which appears in the path, always modeled in
     credentials. The value is always '1234-5678-9012-3456'. Required.
    :type subscription_id: str
    :param endpoint: Service URL. Required. Default value is "".
    :type endpoint: str
    :keyword api_version: Api Version. Default value is "2015-07-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(self, credential: "TokenCredential", subscription_id: str, endpoint: str = "", **kwargs: Any) -> None:
        _cloud = kwargs.pop("cloud_setting", None) or settings.current.azure_cloud  # type: ignore
        _endpoints = get_arm_endpoints(_cloud)
        if not base_url:
            base_url = _endpoints["resource_manager"]
        credential_scopes = kwargs.pop("credential_scopes", _endpoints["credential_scopes"])
        self._config = AutoRestAzureSpecialParametersTestClientConfiguration(
            credential=credential, subscription_id=subscription_id, credential_scopes=credential_scopes, **kwargs
        )

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
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
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
