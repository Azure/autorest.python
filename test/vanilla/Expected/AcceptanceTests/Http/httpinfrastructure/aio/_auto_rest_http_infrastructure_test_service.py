# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Optional

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest
from msrest import Deserializer, Serializer

from ._configuration import AutoRestHttpInfrastructureTestServiceConfiguration
from .operations import HttpFailureOperations
from .operations import HttpSuccessOperations
from .operations import HttpRedirectsOperations
from .operations import HttpClientFailureOperations
from .operations import HttpServerFailureOperations
from .operations import HttpRetryOperations
from .operations import MultipleResponsesOperations
from .. import models


class AutoRestHttpInfrastructureTestService(object):
    """Test Infrastructure for AutoRest.

    :ivar http_failure: HttpFailureOperations operations
    :vartype http_failure: httpinfrastructure.aio.operations.HttpFailureOperations
    :ivar http_success: HttpSuccessOperations operations
    :vartype http_success: httpinfrastructure.aio.operations.HttpSuccessOperations
    :ivar http_redirects: HttpRedirectsOperations operations
    :vartype http_redirects: httpinfrastructure.aio.operations.HttpRedirectsOperations
    :ivar http_client_failure: HttpClientFailureOperations operations
    :vartype http_client_failure: httpinfrastructure.aio.operations.HttpClientFailureOperations
    :ivar http_server_failure: HttpServerFailureOperations operations
    :vartype http_server_failure: httpinfrastructure.aio.operations.HttpServerFailureOperations
    :ivar http_retry: HttpRetryOperations operations
    :vartype http_retry: httpinfrastructure.aio.operations.HttpRetryOperations
    :ivar multiple_responses: MultipleResponsesOperations operations
    :vartype multiple_responses: httpinfrastructure.aio.operations.MultipleResponsesOperations
    :param base_url: Service URL
    :type base_url: str
    """

    def __init__(self, base_url: Optional[str] = None, **kwargs: Any) -> None:
        if not base_url:
            base_url = "http://localhost:3000"
        self._config = AutoRestHttpInfrastructureTestServiceConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

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

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `httpinfrastructure.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from httpinfrastructure.rest import build_httpfailure_get_empty_error_request
        >>> request = build_httpfailure_get_empty_error_request()
        <HttpRequest [GET], url: '/http/failure/emptybody/error'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/llcwiki

        For advanced cases, you can also create your own :class:`~azure.core.rest.HttpRequest`
        and pass it in.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.rest.HttpRequest
        :keyword bool stream_response: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """
        request_copy = deepcopy(http_request)
        request_copy.url = self._client.format_url(request_copy.url)
        stream_response = kwargs.pop("stream_response", False)
        pipeline_response = await self._client._pipeline.run(request_copy, stream=stream_response, **kwargs)
        return AsyncHttpResponse(
            status_code=pipeline_response.http_response.status_code,
            request=request_copy,
            _internal_response=pipeline_response.http_response,
        )

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestHttpInfrastructureTestService":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
