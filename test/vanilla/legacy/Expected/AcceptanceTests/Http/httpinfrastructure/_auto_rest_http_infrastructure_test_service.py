# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any

from msrest import Deserializer, Serializer

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from . import models
from ._configuration import AutoRestHttpInfrastructureTestServiceConfiguration
from .operations import (
    HttpClientFailureOperations,
    HttpFailureOperations,
    HttpRedirectsOperations,
    HttpRetryOperations,
    HttpServerFailureOperations,
    HttpSuccessOperations,
    MultipleResponsesOperations,
)


class AutoRestHttpInfrastructureTestService:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Test Infrastructure for AutoRest.

    :ivar http_failure: HttpFailureOperations operations
    :vartype http_failure: httpinfrastructure.operations.HttpFailureOperations
    :ivar http_success: HttpSuccessOperations operations
    :vartype http_success: httpinfrastructure.operations.HttpSuccessOperations
    :ivar http_redirects: HttpRedirectsOperations operations
    :vartype http_redirects: httpinfrastructure.operations.HttpRedirectsOperations
    :ivar http_client_failure: HttpClientFailureOperations operations
    :vartype http_client_failure: httpinfrastructure.operations.HttpClientFailureOperations
    :ivar http_server_failure: HttpServerFailureOperations operations
    :vartype http_server_failure: httpinfrastructure.operations.HttpServerFailureOperations
    :ivar http_retry: HttpRetryOperations operations
    :vartype http_retry: httpinfrastructure.operations.HttpRetryOperations
    :ivar multiple_responses: MultipleResponsesOperations operations
    :vartype multiple_responses: httpinfrastructure.operations.MultipleResponsesOperations
    :param base_url: Service URL. Default value is "http://localhost:3000".
    :type base_url: str
    """

    def __init__(self, base_url: str = "http://localhost:3000", **kwargs: Any) -> None:
        self._config = AutoRestHttpInfrastructureTestServiceConfiguration(**kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.http_failure = HttpFailureOperations(self._client, self._config, self._serialize, self._deserialize)
        self.http_success = HttpSuccessOperations(self._client, self._config, self._serialize, self._deserialize)
        self.http_redirects = HttpRedirectsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.http_client_failure = HttpClientFailureOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.http_server_failure = HttpServerFailureOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.http_retry = HttpRetryOperations(self._client, self._config, self._serialize, self._deserialize)
        self.multiple_responses = MultipleResponsesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestHttpInfrastructureTestService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
