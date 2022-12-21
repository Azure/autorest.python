﻿# coding=utf-8
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
from ._configuration import ItemTypesClientConfiguration
from .operations import (
    BooleanValueOperations,
    DatetimeValueOperations,
    DurationValueOperations,
    Float32ValueOperations,
    Int32ValueOperations,
    Int64ValueOperations,
    ModelValueOperations,
    StringValueOperations,
    UnknownValueOperations,
)


class ItemTypesClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Illustrates various of dictionaries.

    :ivar int32_value: Int32ValueOperations operations
    :vartype int32_value: arrays.itemtypes.aio.operations.Int32ValueOperations
    :ivar int64_value: Int64ValueOperations operations
    :vartype int64_value: arrays.itemtypes.aio.operations.Int64ValueOperations
    :ivar boolean_value: BooleanValueOperations operations
    :vartype boolean_value: arrays.itemtypes.aio.operations.BooleanValueOperations
    :ivar string_value: StringValueOperations operations
    :vartype string_value: arrays.itemtypes.aio.operations.StringValueOperations
    :ivar float32_value: Float32ValueOperations operations
    :vartype float32_value: arrays.itemtypes.aio.operations.Float32ValueOperations
    :ivar datetime_value: DatetimeValueOperations operations
    :vartype datetime_value: arrays.itemtypes.aio.operations.DatetimeValueOperations
    :ivar duration_value: DurationValueOperations operations
    :vartype duration_value: arrays.itemtypes.aio.operations.DurationValueOperations
    :ivar unknown_value: UnknownValueOperations operations
    :vartype unknown_value: arrays.itemtypes.aio.operations.UnknownValueOperations
    :ivar model_value: ModelValueOperations operations
    :vartype model_value: arrays.itemtypes.aio.operations.ModelValueOperations
    """

    def __init__(self, **kwargs: Any) -> None:  # pylint: disable=missing-client-constructor-parameter-credential
        _endpoint = "http://localhost:3000"
        self._config = ItemTypesClientConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.int32_value = Int32ValueOperations(self._client, self._config, self._serialize, self._deserialize)
        self.int64_value = Int64ValueOperations(self._client, self._config, self._serialize, self._deserialize)
        self.boolean_value = BooleanValueOperations(self._client, self._config, self._serialize, self._deserialize)
        self.string_value = StringValueOperations(self._client, self._config, self._serialize, self._deserialize)
        self.float32_value = Float32ValueOperations(self._client, self._config, self._serialize, self._deserialize)
        self.datetime_value = DatetimeValueOperations(self._client, self._config, self._serialize, self._deserialize)
        self.duration_value = DurationValueOperations(self._client, self._config, self._serialize, self._deserialize)
        self.unknown_value = UnknownValueOperations(self._client, self._config, self._serialize, self._deserialize)
        self.model_value = ModelValueOperations(self._client, self._config, self._serialize, self._deserialize)

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

    async def __aenter__(self) -> "ItemTypesClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
