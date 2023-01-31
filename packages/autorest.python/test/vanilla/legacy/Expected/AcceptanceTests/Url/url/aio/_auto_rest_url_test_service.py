# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, Optional

from msrest import Deserializer, Serializer

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .. import models as _models
from ._configuration import AutoRestUrlTestServiceConfiguration
from .operations import PathItemsOperations, PathsOperations, QueriesOperations


class AutoRestUrlTestService:  # pylint: disable=client-accepts-api-version-keyword
    """Test Infrastructure for AutoRest.

    :ivar paths: PathsOperations operations
    :vartype paths: url.aio.operations.PathsOperations
    :ivar queries: QueriesOperations operations
    :vartype queries: url.aio.operations.QueriesOperations
    :ivar path_items: PathItemsOperations operations
    :vartype path_items: url.aio.operations.PathItemsOperations
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
     Required.
    :type global_string_path: str
    :param global_string_query: should contain value null. Default value is None.
    :type global_string_query: str
    :param base_url: Service URL. Default value is "http://localhost:3000".
    :type base_url: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self,
        global_string_path: str,
        global_string_query: Optional[str] = None,
        base_url: str = "http://localhost:3000",
        **kwargs: Any
    ) -> None:
        self._config = AutoRestUrlTestServiceConfiguration(
            global_string_path=global_string_path, global_string_query=global_string_query, **kwargs
        )
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self.paths = PathsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.queries = QueriesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.path_items = PathItemsOperations(self._client, self._config, self._serialize, self._deserialize)

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

    async def __aenter__(self) -> "AutoRestUrlTestService":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
