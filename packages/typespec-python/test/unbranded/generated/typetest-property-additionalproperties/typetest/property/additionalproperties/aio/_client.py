# pylint: disable=line-too-long,useless-suppression
# coding=utf-8

from copy import deepcopy
from typing import Any, Awaitable
from typing_extensions import Self

from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .._utils.serialization import Deserializer, Serializer
from ._configuration import AdditionalPropertiesClientConfiguration
from .operations import (
    AdditionalPropertiesClientExtendsDifferentSpreadFloatOperations,
    AdditionalPropertiesClientExtendsDifferentSpreadModelArrayOperations,
    AdditionalPropertiesClientExtendsDifferentSpreadModelOperations,
    AdditionalPropertiesClientExtendsDifferentSpreadStringOperations,
    AdditionalPropertiesClientExtendsFloatOperations,
    AdditionalPropertiesClientExtendsModelArrayOperations,
    AdditionalPropertiesClientExtendsModelOperations,
    AdditionalPropertiesClientExtendsStringOperations,
    AdditionalPropertiesClientExtendsUnknownDerivedOperations,
    AdditionalPropertiesClientExtendsUnknownDiscriminatedOperations,
    AdditionalPropertiesClientExtendsUnknownOperations,
    AdditionalPropertiesClientIsFloatOperations,
    AdditionalPropertiesClientIsModelArrayOperations,
    AdditionalPropertiesClientIsModelOperations,
    AdditionalPropertiesClientIsStringOperations,
    AdditionalPropertiesClientIsUnknownDerivedOperations,
    AdditionalPropertiesClientIsUnknownDiscriminatedOperations,
    AdditionalPropertiesClientIsUnknownOperations,
    AdditionalPropertiesClientMultipleSpreadOperations,
    AdditionalPropertiesClientSpreadDifferentFloatOperations,
    AdditionalPropertiesClientSpreadDifferentModelArrayOperations,
    AdditionalPropertiesClientSpreadDifferentModelOperations,
    AdditionalPropertiesClientSpreadDifferentStringOperations,
    AdditionalPropertiesClientSpreadFloatOperations,
    AdditionalPropertiesClientSpreadModelArrayOperations,
    AdditionalPropertiesClientSpreadModelOperations,
    AdditionalPropertiesClientSpreadRecordNonDiscriminatedUnion2Operations,
    AdditionalPropertiesClientSpreadRecordNonDiscriminatedUnion3Operations,
    AdditionalPropertiesClientSpreadRecordNonDiscriminatedUnionOperations,
    AdditionalPropertiesClientSpreadRecordUnionOperations,
    AdditionalPropertiesClientSpreadStringOperations,
)


class AdditionalPropertiesClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Tests for additional properties of models.

    :ivar additional_properties_client_extends_unknown:
     AdditionalPropertiesClientExtendsUnknownOperations operations
    :vartype additional_properties_client_extends_unknown:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientExtendsUnknownOperations
    :ivar additional_properties_client_extends_unknown_derived:
     AdditionalPropertiesClientExtendsUnknownDerivedOperations operations
    :vartype additional_properties_client_extends_unknown_derived:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientExtendsUnknownDerivedOperations
    :ivar additional_properties_client_extends_unknown_discriminated:
     AdditionalPropertiesClientExtendsUnknownDiscriminatedOperations operations
    :vartype additional_properties_client_extends_unknown_discriminated:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientExtendsUnknownDiscriminatedOperations
    :ivar additional_properties_client_is_unknown: AdditionalPropertiesClientIsUnknownOperations
     operations
    :vartype additional_properties_client_is_unknown:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientIsUnknownOperations
    :ivar additional_properties_client_is_unknown_derived:
     AdditionalPropertiesClientIsUnknownDerivedOperations operations
    :vartype additional_properties_client_is_unknown_derived:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientIsUnknownDerivedOperations
    :ivar additional_properties_client_is_unknown_discriminated:
     AdditionalPropertiesClientIsUnknownDiscriminatedOperations operations
    :vartype additional_properties_client_is_unknown_discriminated:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientIsUnknownDiscriminatedOperations
    :ivar additional_properties_client_extends_string:
     AdditionalPropertiesClientExtendsStringOperations operations
    :vartype additional_properties_client_extends_string:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientExtendsStringOperations
    :ivar additional_properties_client_is_string: AdditionalPropertiesClientIsStringOperations
     operations
    :vartype additional_properties_client_is_string:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientIsStringOperations
    :ivar additional_properties_client_spread_string:
     AdditionalPropertiesClientSpreadStringOperations operations
    :vartype additional_properties_client_spread_string:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientSpreadStringOperations
    :ivar additional_properties_client_extends_float:
     AdditionalPropertiesClientExtendsFloatOperations operations
    :vartype additional_properties_client_extends_float:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientExtendsFloatOperations
    :ivar additional_properties_client_is_float: AdditionalPropertiesClientIsFloatOperations
     operations
    :vartype additional_properties_client_is_float:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientIsFloatOperations
    :ivar additional_properties_client_spread_float:
     AdditionalPropertiesClientSpreadFloatOperations operations
    :vartype additional_properties_client_spread_float:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientSpreadFloatOperations
    :ivar additional_properties_client_extends_model:
     AdditionalPropertiesClientExtendsModelOperations operations
    :vartype additional_properties_client_extends_model:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientExtendsModelOperations
    :ivar additional_properties_client_is_model: AdditionalPropertiesClientIsModelOperations
     operations
    :vartype additional_properties_client_is_model:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientIsModelOperations
    :ivar additional_properties_client_spread_model:
     AdditionalPropertiesClientSpreadModelOperations operations
    :vartype additional_properties_client_spread_model:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientSpreadModelOperations
    :ivar additional_properties_client_extends_model_array:
     AdditionalPropertiesClientExtendsModelArrayOperations operations
    :vartype additional_properties_client_extends_model_array:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientExtendsModelArrayOperations
    :ivar additional_properties_client_is_model_array:
     AdditionalPropertiesClientIsModelArrayOperations operations
    :vartype additional_properties_client_is_model_array:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientIsModelArrayOperations
    :ivar additional_properties_client_spread_model_array:
     AdditionalPropertiesClientSpreadModelArrayOperations operations
    :vartype additional_properties_client_spread_model_array:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientSpreadModelArrayOperations
    :ivar additional_properties_client_spread_different_string:
     AdditionalPropertiesClientSpreadDifferentStringOperations operations
    :vartype additional_properties_client_spread_different_string:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientSpreadDifferentStringOperations
    :ivar additional_properties_client_spread_different_float:
     AdditionalPropertiesClientSpreadDifferentFloatOperations operations
    :vartype additional_properties_client_spread_different_float:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientSpreadDifferentFloatOperations
    :ivar additional_properties_client_spread_different_model:
     AdditionalPropertiesClientSpreadDifferentModelOperations operations
    :vartype additional_properties_client_spread_different_model:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientSpreadDifferentModelOperations
    :ivar additional_properties_client_spread_different_model_array:
     AdditionalPropertiesClientSpreadDifferentModelArrayOperations operations
    :vartype additional_properties_client_spread_different_model_array:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientSpreadDifferentModelArrayOperations
    :ivar additional_properties_client_extends_different_spread_string:
     AdditionalPropertiesClientExtendsDifferentSpreadStringOperations operations
    :vartype additional_properties_client_extends_different_spread_string:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientExtendsDifferentSpreadStringOperations
    :ivar additional_properties_client_extends_different_spread_float:
     AdditionalPropertiesClientExtendsDifferentSpreadFloatOperations operations
    :vartype additional_properties_client_extends_different_spread_float:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientExtendsDifferentSpreadFloatOperations
    :ivar additional_properties_client_extends_different_spread_model:
     AdditionalPropertiesClientExtendsDifferentSpreadModelOperations operations
    :vartype additional_properties_client_extends_different_spread_model:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientExtendsDifferentSpreadModelOperations
    :ivar additional_properties_client_extends_different_spread_model_array:
     AdditionalPropertiesClientExtendsDifferentSpreadModelArrayOperations operations
    :vartype additional_properties_client_extends_different_spread_model_array:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientExtendsDifferentSpreadModelArrayOperations
    :ivar additional_properties_client_multiple_spread:
     AdditionalPropertiesClientMultipleSpreadOperations operations
    :vartype additional_properties_client_multiple_spread:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientMultipleSpreadOperations
    :ivar additional_properties_client_spread_record_union:
     AdditionalPropertiesClientSpreadRecordUnionOperations operations
    :vartype additional_properties_client_spread_record_union:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientSpreadRecordUnionOperations
    :ivar additional_properties_client_spread_record_non_discriminated_union:
     AdditionalPropertiesClientSpreadRecordNonDiscriminatedUnionOperations operations
    :vartype additional_properties_client_spread_record_non_discriminated_union:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientSpreadRecordNonDiscriminatedUnionOperations
    :ivar additional_properties_client_spread_record_non_discriminated_union2:
     AdditionalPropertiesClientSpreadRecordNonDiscriminatedUnion2Operations operations
    :vartype additional_properties_client_spread_record_non_discriminated_union2:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientSpreadRecordNonDiscriminatedUnion2Operations
    :ivar additional_properties_client_spread_record_non_discriminated_union3:
     AdditionalPropertiesClientSpreadRecordNonDiscriminatedUnion3Operations operations
    :vartype additional_properties_client_spread_record_non_discriminated_union3:
     typetest.property.additionalproperties.aio.operations.AdditionalPropertiesClientSpreadRecordNonDiscriminatedUnion3Operations
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
        self.additional_properties_client_extends_unknown = AdditionalPropertiesClientExtendsUnknownOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_extends_unknown_derived = (
            AdditionalPropertiesClientExtendsUnknownDerivedOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.additional_properties_client_extends_unknown_discriminated = (
            AdditionalPropertiesClientExtendsUnknownDiscriminatedOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.additional_properties_client_is_unknown = AdditionalPropertiesClientIsUnknownOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_is_unknown_derived = AdditionalPropertiesClientIsUnknownDerivedOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_is_unknown_discriminated = (
            AdditionalPropertiesClientIsUnknownDiscriminatedOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.additional_properties_client_extends_string = AdditionalPropertiesClientExtendsStringOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_is_string = AdditionalPropertiesClientIsStringOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_spread_string = AdditionalPropertiesClientSpreadStringOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_extends_float = AdditionalPropertiesClientExtendsFloatOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_is_float = AdditionalPropertiesClientIsFloatOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_spread_float = AdditionalPropertiesClientSpreadFloatOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_extends_model = AdditionalPropertiesClientExtendsModelOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_is_model = AdditionalPropertiesClientIsModelOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_spread_model = AdditionalPropertiesClientSpreadModelOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_extends_model_array = AdditionalPropertiesClientExtendsModelArrayOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_is_model_array = AdditionalPropertiesClientIsModelArrayOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_spread_model_array = AdditionalPropertiesClientSpreadModelArrayOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_spread_different_string = (
            AdditionalPropertiesClientSpreadDifferentStringOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.additional_properties_client_spread_different_float = (
            AdditionalPropertiesClientSpreadDifferentFloatOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.additional_properties_client_spread_different_model = (
            AdditionalPropertiesClientSpreadDifferentModelOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.additional_properties_client_spread_different_model_array = (
            AdditionalPropertiesClientSpreadDifferentModelArrayOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.additional_properties_client_extends_different_spread_string = (
            AdditionalPropertiesClientExtendsDifferentSpreadStringOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.additional_properties_client_extends_different_spread_float = (
            AdditionalPropertiesClientExtendsDifferentSpreadFloatOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.additional_properties_client_extends_different_spread_model = (
            AdditionalPropertiesClientExtendsDifferentSpreadModelOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.additional_properties_client_extends_different_spread_model_array = (
            AdditionalPropertiesClientExtendsDifferentSpreadModelArrayOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.additional_properties_client_multiple_spread = AdditionalPropertiesClientMultipleSpreadOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_spread_record_union = AdditionalPropertiesClientSpreadRecordUnionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.additional_properties_client_spread_record_non_discriminated_union = (
            AdditionalPropertiesClientSpreadRecordNonDiscriminatedUnionOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.additional_properties_client_spread_record_non_discriminated_union2 = (
            AdditionalPropertiesClientSpreadRecordNonDiscriminatedUnion2Operations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.additional_properties_client_spread_record_non_discriminated_union3 = (
            AdditionalPropertiesClientSpreadRecordNonDiscriminatedUnion3Operations(
                self._client, self._config, self._serialize, self._deserialize
            )
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
