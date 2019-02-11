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

from .._configuration import AutoRestSwaggerBATXMLServiceConfiguration
from msrest.exceptions import HttpOperationError
from .operations_async import XmlOperations
from .. import models


class AutoRestSwaggerBATXMLService(SDKClientAsync):
    """Test Infrastructure for AutoRest Swagger BAT

    :ivar config: Configuration for client.
    :vartype config: AutoRestSwaggerBATXMLServiceConfiguration

    :ivar xml: Xml operations
    :vartype xml: xmlservice.operations_async.XmlOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        self.config = AutoRestSwaggerBATXMLServiceConfiguration(base_url)
        super(AutoRestSwaggerBATXMLService, self).__init__(self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.xml = XmlOperations(
            self._client, self.config, self._serialize, self._deserialize)
