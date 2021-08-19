# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

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

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional

    from azure.core.rest import HttpRequest, HttpResponse


class AutoRestHttpInfrastructureTestService(object):
    """Test Infrastructure for AutoRest.

    :ivar http_failure: HttpFailureOperations operations
    :vartype http_failure: httpinfrastructureversiontolerant.operations.HttpFailureOperations
    :ivar http_success: HttpSuccessOperations operations
    :vartype http_success: httpinfrastructureversiontolerant.operations.HttpSuccessOperations
    :ivar http_redirects: HttpRedirectsOperations operations
    :vartype http_redirects: httpinfrastructureversiontolerant.operations.HttpRedirectsOperations
    :ivar http_client_failure: HttpClientFailureOperations operations
    :vartype http_client_failure:
     httpinfrastructureversiontolerant.operations.HttpClientFailureOperations
    :ivar http_server_failure: HttpServerFailureOperations operations
    :vartype http_server_failure:
     httpinfrastructureversiontolerant.operations.HttpServerFailureOperations
    :ivar http_retry: HttpRetryOperations operations
    :vartype http_retry: httpinfrastructureversiontolerant.operations.HttpRetryOperations
    :ivar multiple_responses: MultipleResponsesOperations operations
    :vartype multiple_responses:
     httpinfrastructureversiontolerant.operations.MultipleResponsesOperations
    :keyword endpoint: Service URL. Default value is 'http://localhost:3000'.
    :paramtype endpoint: str
    """

    def __init__(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        endpoint = kwargs.pop("endpoint", "http://localhost:3000")  # type: str

        self._config = AutoRestHttpInfrastructureTestServiceConfiguration(**kwargs)
        self._client = PipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
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

    def send_request(
        self,
        request,  # type: HttpRequest
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpResponse
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `httpinfrastructureversiontolerant.rest`.
        Use these helper methods to create the request you pass to this method.


        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        For advanced cases, you can also create your own :class:`~azure.core.rest.HttpRequest`
        and pass it in.

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
