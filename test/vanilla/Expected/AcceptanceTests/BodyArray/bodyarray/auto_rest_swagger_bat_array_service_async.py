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
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations_async import ArrayOperations
from . import models


class AutoRestSwaggerBATArrayServiceConfiguration(Configuration):
    """Configuration for AutoRestSwaggerBATArrayService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestSwaggerBATArrayServiceConfiguration, self).__init__(base_url)

        self.add_user_agent('autorestswaggerbatarrayservice/{}'.format(VERSION))


class AutoRestSwaggerBATArrayServiceAsync(SDKClientAsync):
    """Test Infrastructure for AutoRest Swagger BAT

    :ivar config: Configuration for client.
    :vartype config: AutoRestSwaggerBATArrayServiceConfiguration

    :ivar array: Array operations
    :vartype array: bodyarray.operations.ArrayOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        self.config = AutoRestSwaggerBATArrayServiceConfiguration(base_url)
        super(AutoRestSwaggerBATArrayServiceAsync, self).__init__(self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.array = ArrayOperations(
            self._client, self.config, self._serialize, self._deserialize)
