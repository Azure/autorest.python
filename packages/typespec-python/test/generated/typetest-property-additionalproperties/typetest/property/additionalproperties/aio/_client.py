# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .._serialization import Deserializer, Serializer
from ._configuration import AdditionalPropertiesClientConfiguration
from .operations import (
    ExtendsFloatOperations,
    ExtendsStringOperations,
    ExtendsUnknownOperations,
    IsFloatOperations,
    IsStringOperations,
    IsUnknownOperations,
)


class AdditionalPropertiesClient:  # pylint: disable=client-accepts-api-version-keyword
    """Illustrates various property types for models.

    :ivar extends_unknown: ExtendsUnknownOperations operations
    :vartype extends_unknown:
     typetest.property.additionalproperties.aio.operations.ExtendsUnknownOperations
    :ivar is_unknown: IsUnknownOperations operations
    :vartype is_unknown: typetest.property.additionalproperties.aio.operations.IsUnknownOperations
    :ivar extends_string: ExtendsStringOperations operations
    :vartype extends_string:
     typetest.property.additionalproperties.aio.operations.ExtendsStringOperations
    :ivar is_string: IsStringOperations operations
    :vartype is_string: typetest.property.additionalproperties.aio.operations.IsStringOperations
    :ivar extends_float: ExtendsFloatOperations operations
    :vartype extends_float:
     typetest.property.additionalproperties.aio.operations.ExtendsFloatOperations
    :ivar is_float: IsFloatOperations operations
    :vartype is_float: typetest.property.additionalproperties.aio.operations.IsFloatOperations
    """

    def __init__(self, **kwargs: Any) -> None:  # pylint: disable=missing-client-constructor-parameter-credential
        _endpoint = "http://localhost:3000"
        self._config = AdditionalPropertiesClientConfiguration(**kwargs)
        self._client: AsyncPipelineClient = AsyncPipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.extends_unknown = ExtendsUnknownOperations(self._client, self._config, self._serialize, self._deserialize)
        self.is_unknown = IsUnknownOperations(self._client, self._config, self._serialize, self._deserialize)
        self.extends_string = ExtendsStringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.is_string = IsStringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.extends_float = ExtendsFloatOperations(self._client, self._config, self._serialize, self._deserialize)
        self.is_float = IsFloatOperations(self._client, self._config, self._serialize, self._deserialize)

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

    async def __aenter__(self) -> "AdditionalPropertiesClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
