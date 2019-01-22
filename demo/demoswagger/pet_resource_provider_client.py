# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.exceptions import HttpOperationError
from .operations import DogsOperations
from . import models


class PetResourceProviderClientConfiguration(Configuration):
    """Configuration for PetResourceProviderClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, subscription_id, base_url=None):

        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(PetResourceProviderClientConfiguration, self).__init__(base_url)

        self.add_user_agent('petresourceproviderclient/{}'.format(VERSION))

        self.subscription_id = subscription_id


class PetResourceProviderClient(SDKClient):
    """The Pets Resource Provider Client.

    :ivar config: Configuration for client.
    :vartype config: PetResourceProviderClientConfiguration

    :ivar dogs: Dogs operations
    :vartype dogs: demoswagger.operations.DogsOperations

    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, subscription_id, base_url=None):

        self.config = PetResourceProviderClientConfiguration(subscription_id, base_url)
        super(PetResourceProviderClient, self).__init__(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-04-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.dogs = DogsOperations(
            self._client, self.config, self._serialize, self._deserialize)
