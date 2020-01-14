# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.credentials import TokenCredential
from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import AutoRestAzureSpecialParametersTestClientConfiguration
from .operations import XMsClientRequestIdOperations
from .operations import SubscriptionInCredentialsOperations
from .operations import SubscriptionInMethodOperations
from .operations import ApiVersionDefaultOperations
from .operations import ApiVersionLocalOperations
from .operations import SkipUrlEncodingOperations
from .operations import OdataOperations
from .operations import HeaderOperations
from . import models


class AutoRestAzureSpecialParametersTestClient(object):
    """Test Infrastructure for AutoRest


    :ivar x_ms_client_request_id: XMsClientRequestIdOperations operations
    :vartype x_ms_client_request_id: azurespecialproperties.operations.XMsClientRequestIdOperations
    :ivar subscription_in_credentials: SubscriptionInCredentialsOperations operations
    :vartype subscription_in_credentials: azurespecialproperties.operations.SubscriptionInCredentialsOperations
    :ivar subscription_in_method: SubscriptionInMethodOperations operations
    :vartype subscription_in_method: azurespecialproperties.operations.SubscriptionInMethodOperations
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
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The subscription id, which appears in the path, always modeled in credentials. The value is always '1234-5678-9012-3456'
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(self, credential, subscription_id, base_url=None, **kwargs):
        # type: ("TokenCredential", str, Optional[str], **Any) -> None
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestAzureSpecialParametersTestClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.x_ms_client_request_id = XMsClientRequestIdOperations(
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
