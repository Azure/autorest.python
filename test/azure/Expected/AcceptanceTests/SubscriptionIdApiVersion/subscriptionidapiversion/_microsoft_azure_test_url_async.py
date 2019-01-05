# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.async_client import SDKClientAsync
from msrest import Serializer, Deserializer

from ._configuration import MicrosoftAzureTestUrlConfiguration
from .operations_async import GroupOperations
from . import models


class MicrosoftAzureTestUrlAsync(SDKClientAsync):
    """Some cool documentation.

    :ivar config: Configuration for client.
    :vartype config: MicrosoftAzureTestUrlConfiguration

    :ivar group: Group operations
    :vartype group: subscriptionidapiversion.operations.GroupOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = MicrosoftAzureTestUrlConfiguration(credentials, subscription_id, base_url)
        super(MicrosoftAzureTestUrlAsync, self).__init__(self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2014-04-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.group = GroupOperations(
            self._client, self.config, self._serialize, self._deserialize)
