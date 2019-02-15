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

from .._configuration import AutoRestRFC1123DateTimeTestServiceConfiguration
from .operations_async import Datetimerfc1123Operations
from .. import models


class AutoRestRFC1123DateTimeTestService(SDKClientAsync):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestRFC1123DateTimeTestServiceConfiguration

    :ivar datetimerfc1123: Datetimerfc1123 operations
    :vartype datetimerfc1123: bodydatetimerfc1123.aio.operations_async.Datetimerfc1123Operations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        self.config = AutoRestRFC1123DateTimeTestServiceConfiguration(base_url)
        super(AutoRestRFC1123DateTimeTestService, self).__init__(self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.datetimerfc1123 = Datetimerfc1123Operations(
            self._client, self.config, self._serialize, self._deserialize)
