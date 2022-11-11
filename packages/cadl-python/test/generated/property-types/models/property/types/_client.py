# coding=utf-8
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

from ._configuration import TypesClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    BooleanOperations,
    BytesOperations,
    CollectionsIntOperations,
    CollectionsModelOperations,
    CollectionsStringOperations,
    DatetimeOperations,
    DictionaryStringOperations,
    DurationOperations,
    EnumOperations,
    ExtensibleEnumOperations,
    FloatOperations,
    IntOperations,
    ModelOperations,
    StringOperations,
)


class TypesClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Illustrates various property types for models.

    :ivar boolean: BooleanOperations operations
    :vartype boolean: models.property.types.operations.BooleanOperations
    :ivar string: StringOperations operations
    :vartype string: models.property.types.operations.StringOperations
    :ivar bytes: BytesOperations operations
    :vartype bytes: models.property.types.operations.BytesOperations
    :ivar int: IntOperations operations
    :vartype int: models.property.types.operations.IntOperations
    :ivar float: FloatOperations operations
    :vartype float: models.property.types.operations.FloatOperations
    :ivar datetime: DatetimeOperations operations
    :vartype datetime: models.property.types.operations.DatetimeOperations
    :ivar duration: DurationOperations operations
    :vartype duration: models.property.types.operations.DurationOperations
    :ivar enum: EnumOperations operations
    :vartype enum: models.property.types.operations.EnumOperations
    :ivar extensible_enum: ExtensibleEnumOperations operations
    :vartype extensible_enum: models.property.types.operations.ExtensibleEnumOperations
    :ivar model: ModelOperations operations
    :vartype model: models.property.types.operations.ModelOperations
    :ivar collections_string: CollectionsStringOperations operations
    :vartype collections_string: models.property.types.operations.CollectionsStringOperations
    :ivar collections_int: CollectionsIntOperations operations
    :vartype collections_int: models.property.types.operations.CollectionsIntOperations
    :ivar collections_model: CollectionsModelOperations operations
    :vartype collections_model: models.property.types.operations.CollectionsModelOperations
    :ivar dictionary_string: DictionaryStringOperations operations
    :vartype dictionary_string: models.property.types.operations.DictionaryStringOperations
    """

    def __init__(self, **kwargs: Any) -> None:  # pylint: disable=missing-client-constructor-parameter-credential
        _endpoint = "http://localhost:3000"
        self._config = TypesClientConfiguration(**kwargs)
        self._client = PipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.boolean = BooleanOperations(self._client, self._config, self._serialize, self._deserialize)
        self.string = StringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.bytes = BytesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.int = IntOperations(self._client, self._config, self._serialize, self._deserialize)
        self.float = FloatOperations(self._client, self._config, self._serialize, self._deserialize)
        self.datetime = DatetimeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.duration = DurationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.enum = EnumOperations(self._client, self._config, self._serialize, self._deserialize)
        self.extensible_enum = ExtensibleEnumOperations(self._client, self._config, self._serialize, self._deserialize)
        self.model = ModelOperations(self._client, self._config, self._serialize, self._deserialize)
        self.collections_string = CollectionsStringOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.collections_int = CollectionsIntOperations(self._client, self._config, self._serialize, self._deserialize)
        self.collections_model = CollectionsModelOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dictionary_string = DictionaryStringOperations(
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

    def __enter__(self) -> "TypesClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details) -> None:
        self._client.__exit__(*exc_details)
