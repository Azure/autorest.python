# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

from ._configuration import AutoRestDateTimeTestServiceConfiguration
from .operations import DatetimeOperations
from . import models


class AutoRestDateTimeTestService(object):
    """Test Infrastructure for AutoRest

    :ivar datetime_model: DatetimeOperations operations
    :vartype datetime_model: bodydatetime.operations.DatetimeOperations
    :param str base_url: Service URL
    """

    def __init__(self[], base_url=None, **kwargs):
        # type: (Optional[str], **Any) -> None
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestDateTimeTestServiceConfiguration(**kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.datetime_model = DatetimeOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestDateTimeTestService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
