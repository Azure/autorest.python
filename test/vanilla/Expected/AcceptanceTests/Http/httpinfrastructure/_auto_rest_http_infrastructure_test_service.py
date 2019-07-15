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

from ._configuration import AutoRestHttpInfrastructureTestServiceConfiguration
from azure.core.exceptions import HttpResponseError, map_error
from .operations import HttpFailureOperations
from .operations import HttpSuccessOperations
from .operations import HttpRedirectsOperations
from .operations import HttpClientFailureOperations
from .operations import HttpServerFailureOperations
from .operations import HttpRetryOperations
from .operations import MultipleResponsesOperations
from . import models


class AutoRestHttpInfrastructureTestService(object):
    """Test Infrastructure for AutoRest


    :ivar http_failure: HttpFailure operations
    :vartype http_failure: httpinfrastructure.operations.HttpFailureOperations
    :ivar http_success: HttpSuccess operations
    :vartype http_success: httpinfrastructure.operations.HttpSuccessOperations
    :ivar http_redirects: HttpRedirects operations
    :vartype http_redirects: httpinfrastructure.operations.HttpRedirectsOperations
    :ivar http_client_failure: HttpClientFailure operations
    :vartype http_client_failure: httpinfrastructure.operations.HttpClientFailureOperations
    :ivar http_server_failure: HttpServerFailure operations
    :vartype http_server_failure: httpinfrastructure.operations.HttpServerFailureOperations
    :ivar http_retry: HttpRetry operations
    :vartype http_retry: httpinfrastructure.operations.HttpRetryOperations
    :ivar multiple_responses: MultipleResponses operations
    :vartype multiple_responses: httpinfrastructure.operations.MultipleResponsesOperations

    :param str base_url: Service URL
    """

    def __init__(self, base_url=None, **kwargs):

        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestHttpInfrastructureTestServiceConfiguration(**kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.http_failure = HttpFailureOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.http_success = HttpSuccessOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.http_redirects = HttpRedirectsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.http_client_failure = HttpClientFailureOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.http_server_failure = HttpServerFailureOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.http_retry = HttpRetryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.multiple_responses = MultipleResponsesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
