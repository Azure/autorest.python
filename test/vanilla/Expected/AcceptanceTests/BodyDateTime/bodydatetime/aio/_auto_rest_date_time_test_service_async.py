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

from .._configuration import AutoRestDateTimeTestServiceConfiguration
from .operations_async import DatetimeModelOperations
from .. import models


class AutoRestDateTimeTestService(SDKClientAsync):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestDateTimeTestServiceConfiguration

    :ivar datetime_model: DatetimeModel operations
    :vartype datetime_model: bodydatetime.aio.operations_async.DatetimeModelOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        self.config = AutoRestDateTimeTestServiceConfiguration(base_url)
        super(AutoRestDateTimeTestService, self).__init__(self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.datetime_model = DatetimeModelOperations(
            self._client, self.config, self._serialize, self._deserialize)
