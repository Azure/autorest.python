# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, Optional, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest
from msrest import Deserializer, Serializer

from .. import models
from ._configuration import MultiapiServiceClientConfiguration
from .operations import MultiapiServiceClientOperationsMixin, OperationGroupOneOperations, OperationGroupTwoOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

class MultiapiServiceClient(MultiapiServiceClientOperationsMixin):
    """Service client for multiapi client testing.

    :ivar operation_group_one: OperationGroupOneOperations operations
    :vartype operation_group_one: multiapidataplane.v3.aio.operations.OperationGroupOneOperations
    :ivar operation_group_two: OperationGroupTwoOperations operations
    :vartype operation_group_two: multiapidataplane.v3.aio.operations.OperationGroupTwoOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param base_url: Service URL
    :type base_url: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        base_url: str = "http://localhost:3000",
        **kwargs: Any
    ) -> None:
        self._config = MultiapiServiceClientConfiguration(credential, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operation_group_one = OperationGroupOneOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operation_group_two = OperationGroupTwoOperations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `multiapidataplane.v3.rest`.
        Use these helper methods to create the request you pass to this method.


        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        For advanced cases, you can also create your own :class:`~azure.core.rest.HttpRequest`
        and pass it in.

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

    async def __aenter__(self) -> "MultiapiServiceClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
