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

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import AutoRestDateTimeTestServiceConfiguration
from .operations import DatetimeOperations


class AutoRestDateTimeTestService:  # pylint: disable=client-accepts-api-version-keyword
    """Test Infrastructure for AutoRest.

    :ivar datetime: DatetimeOperations operations
    :vartype datetime: bodydatetime.aio.operations.DatetimeOperations
    :param base_url: Service URL. Default value is "http://localhost:3000".
    :type base_url: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, base_url: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        self._config = AutoRestDateTimeTestServiceConfiguration(**kwargs)
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
        self._client: AsyncPipelineClient = AsyncPipelineClient(base_url=base_url, policies=config_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.datetime = DatetimeOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
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

    async def __aenter__(self) -> "AutoRestDateTimeTestService":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
