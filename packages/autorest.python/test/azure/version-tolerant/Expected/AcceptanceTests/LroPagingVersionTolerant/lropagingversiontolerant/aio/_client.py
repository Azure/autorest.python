# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable

from azure.core import AsyncPipelineClient
from azure.core.pipeline import policies
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .._serialization import Deserializer, Serializer
from ._configuration import LroPagingClientConfiguration
from .operations import QuestionAnsweringProjectsOperations


class LroPagingClient:  # pylint: disable=client-accepts-api-version-keyword
    """The language service API is a suite of natural language processing (NLP) skills built with
    best-in-class Microsoft machine learning algorithms.

    :ivar question_answering_projects: QuestionAnsweringProjectsOperations operations
    :vartype question_answering_projects:
     lropagingversiontolerant.aio.operations.QuestionAnsweringProjectsOperations
    :keyword endpoint: Service URL. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    :keyword api_version: Api Version. Default value is "2021-10-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        self._config = LroPagingClientConfiguration(**kwargs)
        config_policies = [
            policies.RequestIdPolicy(**kwargs),
            self._config.headers_policy,
            self._config.user_agent_policy,
            self._config.proxy_policy,
            policies.ContentDecodePolicy(**kwargs),
            self._config.redirect_policy,
            self._config.retry_policy,
            self._config.authentication_policy,
            self._config.custom_hook_policy,
            self._config.logging_policy,
            policies.DistributedTracingPolicy(**kwargs),
            policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
            self._config.http_logging_policy,
        ]
        self._client: AsyncPipelineClient = AsyncPipelineClient(base_url=endpoint, policies=config_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.question_answering_projects = QuestionAnsweringProjectsOperations(
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

    async def __aenter__(self) -> "LroPagingClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
