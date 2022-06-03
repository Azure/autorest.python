# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

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
    from typing import Dict


class AutoRestHttpInfrastructureTestService:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Test Infrastructure for AutoRest.

    :ivar http_failure: HttpFailureOperations operations
    :vartype http_failure: httpinfrastructureversiontolerant.aio.operations.HttpFailureOperations
    :ivar http_success: HttpSuccessOperations operations
    :vartype http_success: httpinfrastructureversiontolerant.aio.operations.HttpSuccessOperations
    :ivar http_redirects: HttpRedirectsOperations operations
    :vartype http_redirects:
     httpinfrastructureversiontolerant.aio.operations.HttpRedirectsOperations
    :ivar http_client_failure: HttpClientFailureOperations operations
    :vartype http_client_failure:
     httpinfrastructureversiontolerant.aio.operations.HttpClientFailureOperations
    :ivar http_server_failure: HttpServerFailureOperations operations
    :vartype http_server_failure:
     httpinfrastructureversiontolerant.aio.operations.HttpServerFailureOperations
    :ivar http_retry: HttpRetryOperations operations
    :vartype http_retry: httpinfrastructureversiontolerant.aio.operations.HttpRetryOperations
    :ivar multiple_responses: MultipleResponsesOperations operations
    :vartype multiple_responses:
     httpinfrastructureversiontolerant.aio.operations.MultipleResponsesOperations
    :keyword endpoint: Service URL. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(self, *, endpoint: str = "http://localhost:3000", **kwargs: Any) -> None:
        self._config = AutoRestHttpInfrastructureTestServiceConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=endpoint, config=self._config, **kwargs)

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

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestHttpInfrastructureTestService":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
