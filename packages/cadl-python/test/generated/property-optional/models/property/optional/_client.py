﻿# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import OptionalClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    BytesOperations,
    CollectionsByteOperations,
    CollectionsModelOperations,
    DatetimeOperations,
    DurationOperations,
    RequiredAndOptionalOperations,
    StringOperations,
)


class OptionalClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Illustrates models with optional properties.

    :ivar string: StringOperations operations
    :vartype string: models.property.optional.operations.StringOperations
    :ivar bytes: BytesOperations operations
    :vartype bytes: models.property.optional.operations.BytesOperations
    :ivar datetime: DatetimeOperations operations
    :vartype datetime: models.property.optional.operations.DatetimeOperations
    :ivar duration: DurationOperations operations
    :vartype duration: models.property.optional.operations.DurationOperations
    :ivar collections_byte: CollectionsByteOperations operations
    :vartype collections_byte: models.property.optional.operations.CollectionsByteOperations
    :ivar collections_model: CollectionsModelOperations operations
    :vartype collections_model: models.property.optional.operations.CollectionsModelOperations
    :ivar required_and_optional: RequiredAndOptionalOperations operations
    :vartype required_and_optional:
     models.property.optional.operations.RequiredAndOptionalOperations
    """

    def __init__(self, **kwargs: Any) -> None:  # pylint: disable=missing-client-constructor-parameter-credential
        _endpoint = "http://localhost:3000"
        self._config = OptionalClientConfiguration(**kwargs)
        self._client = PipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.string = StringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.bytes = BytesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.datetime = DatetimeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.duration = DurationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.collections_byte = CollectionsByteOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.collections_model = CollectionsModelOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.required_and_optional = RequiredAndOptionalOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "OptionalClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details) -> None:
        self._client.__exit__(*exc_details)
