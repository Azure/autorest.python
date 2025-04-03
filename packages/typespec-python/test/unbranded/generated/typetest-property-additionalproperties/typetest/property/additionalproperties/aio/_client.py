# coding=utf-8

from copy import deepcopy
from typing import Any, Awaitable
from typing_extensions import Self

from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .._serialization import Deserializer, Serializer
from ._configuration import AdditionalPropertiesClientConfiguration
from .operations import (
    ExtendsDifferentSpreadFloatOperations,
    ExtendsDifferentSpreadModelArrayOperations,
    ExtendsDifferentSpreadModelOperations,
    ExtendsDifferentSpreadStringOperations,
    ExtendsFloatOperations,
    ExtendsModelArrayOperations,
    ExtendsModelOperations,
    ExtendsStringOperations,
    ExtendsUnknownDerivedOperations,
    ExtendsUnknownDiscriminatedOperations,
    ExtendsUnknownOperations,
    IsFloatOperations,
    IsModelArrayOperations,
    IsModelOperations,
    IsStringOperations,
    IsUnknownDerivedOperations,
    IsUnknownDiscriminatedOperations,
    IsUnknownOperations,
    MultipleSpreadOperations,
    SpreadDifferentFloatOperations,
    SpreadDifferentModelArrayOperations,
    SpreadDifferentModelOperations,
    SpreadDifferentStringOperations,
    SpreadFloatOperations,
    SpreadModelArrayOperations,
    SpreadModelOperations,
    SpreadRecordNonDiscriminatedUnion2Operations,
    SpreadRecordNonDiscriminatedUnion3Operations,
    SpreadRecordNonDiscriminatedUnionOperations,
    SpreadRecordUnionOperations,
    SpreadStringOperations,
)


class AdditionalPropertiesClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Tests for additional properties of models.

    :ivar extends_unknown: ExtendsUnknownOperations operations
    :vartype extends_unknown:
     typetest.property.additionalproperties.aio.operations.ExtendsUnknownOperations
    :ivar extends_unknown_derived: ExtendsUnknownDerivedOperations operations
    :vartype extends_unknown_derived:
     typetest.property.additionalproperties.aio.operations.ExtendsUnknownDerivedOperations
    :ivar extends_unknown_discriminated: ExtendsUnknownDiscriminatedOperations operations
    :vartype extends_unknown_discriminated:
     typetest.property.additionalproperties.aio.operations.ExtendsUnknownDiscriminatedOperations
    :ivar is_unknown: IsUnknownOperations operations
    :vartype is_unknown: typetest.property.additionalproperties.aio.operations.IsUnknownOperations
    :ivar is_unknown_derived: IsUnknownDerivedOperations operations
    :vartype is_unknown_derived:
     typetest.property.additionalproperties.aio.operations.IsUnknownDerivedOperations
    :ivar is_unknown_discriminated: IsUnknownDiscriminatedOperations operations
    :vartype is_unknown_discriminated:
     typetest.property.additionalproperties.aio.operations.IsUnknownDiscriminatedOperations
    :ivar extends_string: ExtendsStringOperations operations
    :vartype extends_string:
     typetest.property.additionalproperties.aio.operations.ExtendsStringOperations
    :ivar is_string: IsStringOperations operations
    :vartype is_string: typetest.property.additionalproperties.aio.operations.IsStringOperations
    :ivar spread_string: SpreadStringOperations operations
    :vartype spread_string:
     typetest.property.additionalproperties.aio.operations.SpreadStringOperations
    :ivar extends_float: ExtendsFloatOperations operations
    :vartype extends_float:
     typetest.property.additionalproperties.aio.operations.ExtendsFloatOperations
    :ivar is_float: IsFloatOperations operations
    :vartype is_float: typetest.property.additionalproperties.aio.operations.IsFloatOperations
    :ivar spread_float: SpreadFloatOperations operations
    :vartype spread_float:
     typetest.property.additionalproperties.aio.operations.SpreadFloatOperations
    :ivar extends_model: ExtendsModelOperations operations
    :vartype extends_model:
     typetest.property.additionalproperties.aio.operations.ExtendsModelOperations
    :ivar is_model: IsModelOperations operations
    :vartype is_model: typetest.property.additionalproperties.aio.operations.IsModelOperations
    :ivar spread_model: SpreadModelOperations operations
    :vartype spread_model:
     typetest.property.additionalproperties.aio.operations.SpreadModelOperations
    :ivar extends_model_array: ExtendsModelArrayOperations operations
    :vartype extends_model_array:
     typetest.property.additionalproperties.aio.operations.ExtendsModelArrayOperations
    :ivar is_model_array: IsModelArrayOperations operations
    :vartype is_model_array:
     typetest.property.additionalproperties.aio.operations.IsModelArrayOperations
    :ivar spread_model_array: SpreadModelArrayOperations operations
    :vartype spread_model_array:
     typetest.property.additionalproperties.aio.operations.SpreadModelArrayOperations
    :ivar spread_different_string: SpreadDifferentStringOperations operations
    :vartype spread_different_string:
     typetest.property.additionalproperties.aio.operations.SpreadDifferentStringOperations
    :ivar spread_different_float: SpreadDifferentFloatOperations operations
    :vartype spread_different_float:
     typetest.property.additionalproperties.aio.operations.SpreadDifferentFloatOperations
    :ivar spread_different_model: SpreadDifferentModelOperations operations
    :vartype spread_different_model:
     typetest.property.additionalproperties.aio.operations.SpreadDifferentModelOperations
    :ivar spread_different_model_array: SpreadDifferentModelArrayOperations operations
    :vartype spread_different_model_array:
     typetest.property.additionalproperties.aio.operations.SpreadDifferentModelArrayOperations
    :ivar extends_different_spread_string: ExtendsDifferentSpreadStringOperations operations
    :vartype extends_different_spread_string:
     typetest.property.additionalproperties.aio.operations.ExtendsDifferentSpreadStringOperations
    :ivar extends_different_spread_float: ExtendsDifferentSpreadFloatOperations operations
    :vartype extends_different_spread_float:
     typetest.property.additionalproperties.aio.operations.ExtendsDifferentSpreadFloatOperations
    :ivar extends_different_spread_model: ExtendsDifferentSpreadModelOperations operations
    :vartype extends_different_spread_model:
     typetest.property.additionalproperties.aio.operations.ExtendsDifferentSpreadModelOperations
    :ivar extends_different_spread_model_array: ExtendsDifferentSpreadModelArrayOperations
     operations
    :vartype extends_different_spread_model_array:
     typetest.property.additionalproperties.aio.operations.ExtendsDifferentSpreadModelArrayOperations
    :ivar multiple_spread: MultipleSpreadOperations operations
    :vartype multiple_spread:
     typetest.property.additionalproperties.aio.operations.MultipleSpreadOperations
    :ivar spread_record_union: SpreadRecordUnionOperations operations
    :vartype spread_record_union:
     typetest.property.additionalproperties.aio.operations.SpreadRecordUnionOperations
    :ivar spread_record_non_discriminated_union: SpreadRecordNonDiscriminatedUnionOperations
     operations
    :vartype spread_record_non_discriminated_union:
     typetest.property.additionalproperties.aio.operations.SpreadRecordNonDiscriminatedUnionOperations
    :ivar spread_record_non_discriminated_union2: SpreadRecordNonDiscriminatedUnion2Operations
     operations
    :vartype spread_record_non_discriminated_union2:
     typetest.property.additionalproperties.aio.operations.SpreadRecordNonDiscriminatedUnion2Operations
    :ivar spread_record_non_discriminated_union3: SpreadRecordNonDiscriminatedUnion3Operations
     operations
    :vartype spread_record_non_discriminated_union3:
     typetest.property.additionalproperties.aio.operations.SpreadRecordNonDiscriminatedUnion3Operations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = AdditionalPropertiesClientConfiguration(endpoint=endpoint, **kwargs)
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
        self.extends_unknown = ExtendsUnknownOperations(self._client, self._config, self._serialize, self._deserialize)
        self.extends_unknown_derived = ExtendsUnknownDerivedOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.extends_unknown_discriminated = ExtendsUnknownDiscriminatedOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.is_unknown = IsUnknownOperations(self._client, self._config, self._serialize, self._deserialize)
        self.is_unknown_derived = IsUnknownDerivedOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.is_unknown_discriminated = IsUnknownDiscriminatedOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.extends_string = ExtendsStringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.is_string = IsStringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.spread_string = SpreadStringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.extends_float = ExtendsFloatOperations(self._client, self._config, self._serialize, self._deserialize)
        self.is_float = IsFloatOperations(self._client, self._config, self._serialize, self._deserialize)
        self.spread_float = SpreadFloatOperations(self._client, self._config, self._serialize, self._deserialize)
        self.extends_model = ExtendsModelOperations(self._client, self._config, self._serialize, self._deserialize)
        self.is_model = IsModelOperations(self._client, self._config, self._serialize, self._deserialize)
        self.spread_model = SpreadModelOperations(self._client, self._config, self._serialize, self._deserialize)
        self.extends_model_array = ExtendsModelArrayOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.is_model_array = IsModelArrayOperations(self._client, self._config, self._serialize, self._deserialize)
        self.spread_model_array = SpreadModelArrayOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.spread_different_string = SpreadDifferentStringOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.spread_different_float = SpreadDifferentFloatOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.spread_different_model = SpreadDifferentModelOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.spread_different_model_array = SpreadDifferentModelArrayOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.extends_different_spread_string = ExtendsDifferentSpreadStringOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.extends_different_spread_float = ExtendsDifferentSpreadFloatOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.extends_different_spread_model = ExtendsDifferentSpreadModelOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.extends_different_spread_model_array = ExtendsDifferentSpreadModelArrayOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.multiple_spread = MultipleSpreadOperations(self._client, self._config, self._serialize, self._deserialize)
        self.spread_record_union = SpreadRecordUnionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.spread_record_non_discriminated_union = SpreadRecordNonDiscriminatedUnionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.spread_record_non_discriminated_union2 = SpreadRecordNonDiscriminatedUnion2Operations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.spread_record_non_discriminated_union3 = SpreadRecordNonDiscriminatedUnion3Operations(
            self._client, self._config, self._serialize, self._deserialize
        )

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
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> Self:
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
