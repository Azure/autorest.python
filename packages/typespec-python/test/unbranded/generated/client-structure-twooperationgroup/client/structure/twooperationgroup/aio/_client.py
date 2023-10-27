# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, Union

from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import TwoOperationGroupClientConfiguration
from .operations import Group1Operations, Group2Operations


class TwoOperationGroupClient:  # pylint: disable=client-accepts-api-version-keyword
    """TwoOperationGroupClient.

    :ivar group1: Group1Operations operations
    :vartype group1: client.structure.twooperationgroup.aio.operations.Group1Operations
    :ivar group2: Group2Operations operations
    :vartype group2: client.structure.twooperationgroup.aio.operations.Group2Operations
    :param endpoint: Need to be set as 'http://localhost:3000' in client. Required.
    :type endpoint: str
    :param client: Need to be set as 'default', 'multi-client', 'renamed-operation',
     'two-operation-group' in client. Known values are: "default", "multi-client",
     "renamed-operation", and "two-operation-group". Required.
    :type client: str or ~client.structure.twooperationgroup.models.ClientType
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, endpoint: str, client: Union[str, _models.ClientType], **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}/client/structure/{client}"
        self._config = TwoOperationGroupClientConfiguration(endpoint=endpoint, client=client, **kwargs)
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.logging_policy,
            ]
        self._client: AsyncPipelineClient = AsyncPipelineClient(endpoint=_endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.group1 = Group1Operations(self._client, self._config, self._serialize, self._deserialize)
        self.group2 = Group2Operations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(
        self, request: HttpRequest, *, stream: bool = False, **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from corehttp.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~corehttp.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~corehttp.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "client": self._serialize.url("self._config.client", self._config.client, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "TwoOperationGroupClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
