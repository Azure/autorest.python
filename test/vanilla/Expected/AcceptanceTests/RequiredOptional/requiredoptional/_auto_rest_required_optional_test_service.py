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

from azure.core import PipelineClient
from msrest import Serializer, Deserializer

from ._configuration import AutoRestRequiredOptionalTestServiceConfiguration
from azure.core.exceptions import map_error
from .operations import ImplicitOperations
from .operations import ExplicitOperations
from . import models


class AutoRestRequiredOptionalTestService(object):
    """Test Infrastructure for AutoRest


    :ivar implicit: Implicit operations
    :vartype implicit: requiredoptional.operations.ImplicitOperations
    :ivar explicit: Explicit operations
    :vartype explicit: requiredoptional.operations.ExplicitOperations

    :param required_global_path: number of items to skip
    :type required_global_path: str
    :param required_global_query: number of items to skip
    :type required_global_query: str
    :param optional_global_query: number of items to skip
    :type optional_global_query: int
    :param str base_url: Service URL
    """

    def __init__(self, required_global_path, required_global_query, optional_global_query=None, base_url=None, **kwargs):

        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestRequiredOptionalTestServiceConfiguration(required_global_path, required_global_query, optional_global_query, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.implicit = ImplicitOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.explicit = ExplicitOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
