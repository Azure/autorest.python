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

from ._configuration import AutoRestSwaggerBATdictionaryServiceConfiguration
from .operations import DictionaryOperations
from . import models


class AutoRestSwaggerBATdictionaryService(object):
    """Test Infrastructure for AutoRest Swagger BAT


    :ivar dictionary: Dictionary operations
    :vartype dictionary: bodydictionary.operations.DictionaryOperations

    :param str base_url: Service URL
    """

    def __init__(self, base_url=None, config=None, **kwargs):

        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = config or AutoRestSwaggerBATdictionaryServiceConfiguration(**kwargs)
        pipeline = kwargs.get('pipeline', self._config.build_pipeline())
        self._client = PipelineClient(base_url, config=self._config, pipeline=pipeline, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.dictionary = DictionaryOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def __enter__(self):
        self._client.pipeline.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.pipeline.__exit__(*exc_details)
