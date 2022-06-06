# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient

from . import models
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
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.credentials import TokenCredential
    from azure.core.rest import HttpRequest, HttpResponse


class AutoRestAzureSpecialParametersTestClient(
    object
):  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Test Infrastructure for AutoRest.

    :ivar xms_client_request_id: XMsClientRequestIdOperations operations
    :vartype xms_client_request_id: azurespecialproperties.operations.XMsClientRequestIdOperations
    :ivar subscription_in_credentials: SubscriptionInCredentialsOperations operations
    :vartype subscription_in_credentials:
     azurespecialproperties.operations.SubscriptionInCredentialsOperations
    :ivar subscription_in_method: SubscriptionInMethodOperations operations
    :vartype subscription_in_method:
     azurespecialproperties.operations.SubscriptionInMethodOperations
    :ivar api_version_default: ApiVersionDefaultOperations operations
    :vartype api_version_default: azurespecialproperties.operations.ApiVersionDefaultOperations
    :ivar api_version_local: ApiVersionLocalOperations operations
    :vartype api_version_local: azurespecialproperties.operations.ApiVersionLocalOperations
    :ivar skip_url_encoding: SkipUrlEncodingOperations operations
    :vartype skip_url_encoding: azurespecialproperties.operations.SkipUrlEncodingOperations
    :ivar odata: OdataOperations operations
    :vartype odata: azurespecialproperties.operations.OdataOperations
    :ivar header: HeaderOperations operations
    :vartype header: azurespecialproperties.operations.HeaderOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
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
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url="http://localhost:3000",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        self._config = AutoRestAzureSpecialParametersTestClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
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

    def _send_request(
        self,
        request,  # type: HttpRequest
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpResponse
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
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
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestAzureSpecialParametersTestClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
