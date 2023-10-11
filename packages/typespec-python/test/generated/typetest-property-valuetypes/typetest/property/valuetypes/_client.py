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
from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import ValueTypesClientConfiguration
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
    NeverOperations,
    StringOperations,
    UnknownArrayOperations,
    UnknownDictOperations,
    UnknownIntOperations,
    UnknownStringOperations,
)


class ValueTypesClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Illustrates various property types for models.

    :ivar boolean: BooleanOperations operations
    :vartype boolean: typetest.property.valuetypes.operations.BooleanOperations
    :ivar string: StringOperations operations
    :vartype string: typetest.property.valuetypes.operations.StringOperations
    :ivar bytes: BytesOperations operations
    :vartype bytes: typetest.property.valuetypes.operations.BytesOperations
    :ivar int: IntOperations operations
    :vartype int: typetest.property.valuetypes.operations.IntOperations
    :ivar float: FloatOperations operations
    :vartype float: typetest.property.valuetypes.operations.FloatOperations
    :ivar datetime: DatetimeOperations operations
    :vartype datetime: typetest.property.valuetypes.operations.DatetimeOperations
    :ivar duration: DurationOperations operations
    :vartype duration: typetest.property.valuetypes.operations.DurationOperations
    :ivar enum: EnumOperations operations
    :vartype enum: typetest.property.valuetypes.operations.EnumOperations
    :ivar extensible_enum: ExtensibleEnumOperations operations
    :vartype extensible_enum: typetest.property.valuetypes.operations.ExtensibleEnumOperations
    :ivar model: ModelOperations operations
    :vartype model: typetest.property.valuetypes.operations.ModelOperations
    :ivar collections_string: CollectionsStringOperations operations
    :vartype collections_string:
     typetest.property.valuetypes.operations.CollectionsStringOperations
    :ivar collections_int: CollectionsIntOperations operations
    :vartype collections_int: typetest.property.valuetypes.operations.CollectionsIntOperations
    :ivar collections_model: CollectionsModelOperations operations
    :vartype collections_model: typetest.property.valuetypes.operations.CollectionsModelOperations
    :ivar dictionary_string: DictionaryStringOperations operations
    :vartype dictionary_string: typetest.property.valuetypes.operations.DictionaryStringOperations
    :ivar never: NeverOperations operations
    :vartype never: typetest.property.valuetypes.operations.NeverOperations
    :ivar unknown_string: UnknownStringOperations operations
    :vartype unknown_string: typetest.property.valuetypes.operations.UnknownStringOperations
    :ivar unknown_int: UnknownIntOperations operations
    :vartype unknown_int: typetest.property.valuetypes.operations.UnknownIntOperations
    :ivar unknown_dict: UnknownDictOperations operations
    :vartype unknown_dict: typetest.property.valuetypes.operations.UnknownDictOperations
    :ivar unknown_array: UnknownArrayOperations operations
    :vartype unknown_array: typetest.property.valuetypes.operations.UnknownArrayOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        self._config = ValueTypesClientConfiguration(**kwargs)
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
        self._client: PipelineClient = PipelineClient(base_url=endpoint, policies=config_policies, **kwargs)

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
        self.never = NeverOperations(self._client, self._config, self._serialize, self._deserialize)
        self.unknown_string = UnknownStringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.unknown_int = UnknownIntOperations(self._client, self._config, self._serialize, self._deserialize)
        self.unknown_dict = UnknownDictOperations(self._client, self._config, self._serialize, self._deserialize)
        self.unknown_array = UnknownArrayOperations(self._client, self._config, self._serialize, self._deserialize)

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

    def __enter__(self) -> "ValueTypesClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
