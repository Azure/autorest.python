# coding=utf-8

from copy import deepcopy
from typing import Any
from typing_extensions import Self

from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient, policies

from ._configuration import ValueTypesClientConfiguration
from ._utils.serialization import Deserializer, Serializer
from .operations import (
    ValueTypesClientBooleanLiteralOperations,
    ValueTypesClientBooleanOperations,
    ValueTypesClientBytesOperations,
    ValueTypesClientCollectionsIntOperations,
    ValueTypesClientCollectionsModelOperations,
    ValueTypesClientCollectionsStringOperations,
    ValueTypesClientDatetimeOperations,
    ValueTypesClientDecimal128Operations,
    ValueTypesClientDecimalOperations,
    ValueTypesClientDictionaryStringOperations,
    ValueTypesClientDurationOperations,
    ValueTypesClientEnumOperations,
    ValueTypesClientExtensibleEnumOperations,
    ValueTypesClientFloatLiteralOperations,
    ValueTypesClientFloatOperations,
    ValueTypesClientIntLiteralOperations,
    ValueTypesClientIntOperations,
    ValueTypesClientModelOperations,
    ValueTypesClientNeverOperations,
    ValueTypesClientStringLiteralOperations,
    ValueTypesClientStringOperations,
    ValueTypesClientUnionEnumValueOperations,
    ValueTypesClientUnionFloatLiteralOperations,
    ValueTypesClientUnionIntLiteralOperations,
    ValueTypesClientUnionStringLiteralOperations,
    ValueTypesClientUnknownArrayOperations,
    ValueTypesClientUnknownDictOperations,
    ValueTypesClientUnknownIntOperations,
    ValueTypesClientUnknownStringOperations,
)


class ValueTypesClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Illustrates various property types for models.

    :ivar value_types_client_boolean: ValueTypesClientBooleanOperations operations
    :vartype value_types_client_boolean:
     typetest.property.valuetypes.operations.ValueTypesClientBooleanOperations
    :ivar value_types_client_string: ValueTypesClientStringOperations operations
    :vartype value_types_client_string:
     typetest.property.valuetypes.operations.ValueTypesClientStringOperations
    :ivar value_types_client_bytes: ValueTypesClientBytesOperations operations
    :vartype value_types_client_bytes:
     typetest.property.valuetypes.operations.ValueTypesClientBytesOperations
    :ivar value_types_client_int: ValueTypesClientIntOperations operations
    :vartype value_types_client_int:
     typetest.property.valuetypes.operations.ValueTypesClientIntOperations
    :ivar value_types_client_float: ValueTypesClientFloatOperations operations
    :vartype value_types_client_float:
     typetest.property.valuetypes.operations.ValueTypesClientFloatOperations
    :ivar value_types_client_decimal: ValueTypesClientDecimalOperations operations
    :vartype value_types_client_decimal:
     typetest.property.valuetypes.operations.ValueTypesClientDecimalOperations
    :ivar value_types_client_decimal128: ValueTypesClientDecimal128Operations operations
    :vartype value_types_client_decimal128:
     typetest.property.valuetypes.operations.ValueTypesClientDecimal128Operations
    :ivar value_types_client_datetime: ValueTypesClientDatetimeOperations operations
    :vartype value_types_client_datetime:
     typetest.property.valuetypes.operations.ValueTypesClientDatetimeOperations
    :ivar value_types_client_duration: ValueTypesClientDurationOperations operations
    :vartype value_types_client_duration:
     typetest.property.valuetypes.operations.ValueTypesClientDurationOperations
    :ivar value_types_client_enum: ValueTypesClientEnumOperations operations
    :vartype value_types_client_enum:
     typetest.property.valuetypes.operations.ValueTypesClientEnumOperations
    :ivar value_types_client_extensible_enum: ValueTypesClientExtensibleEnumOperations operations
    :vartype value_types_client_extensible_enum:
     typetest.property.valuetypes.operations.ValueTypesClientExtensibleEnumOperations
    :ivar value_types_client_model: ValueTypesClientModelOperations operations
    :vartype value_types_client_model:
     typetest.property.valuetypes.operations.ValueTypesClientModelOperations
    :ivar value_types_client_collections_string: ValueTypesClientCollectionsStringOperations
     operations
    :vartype value_types_client_collections_string:
     typetest.property.valuetypes.operations.ValueTypesClientCollectionsStringOperations
    :ivar value_types_client_collections_int: ValueTypesClientCollectionsIntOperations operations
    :vartype value_types_client_collections_int:
     typetest.property.valuetypes.operations.ValueTypesClientCollectionsIntOperations
    :ivar value_types_client_collections_model: ValueTypesClientCollectionsModelOperations
     operations
    :vartype value_types_client_collections_model:
     typetest.property.valuetypes.operations.ValueTypesClientCollectionsModelOperations
    :ivar value_types_client_dictionary_string: ValueTypesClientDictionaryStringOperations
     operations
    :vartype value_types_client_dictionary_string:
     typetest.property.valuetypes.operations.ValueTypesClientDictionaryStringOperations
    :ivar value_types_client_never: ValueTypesClientNeverOperations operations
    :vartype value_types_client_never:
     typetest.property.valuetypes.operations.ValueTypesClientNeverOperations
    :ivar value_types_client_unknown_string: ValueTypesClientUnknownStringOperations operations
    :vartype value_types_client_unknown_string:
     typetest.property.valuetypes.operations.ValueTypesClientUnknownStringOperations
    :ivar value_types_client_unknown_int: ValueTypesClientUnknownIntOperations operations
    :vartype value_types_client_unknown_int:
     typetest.property.valuetypes.operations.ValueTypesClientUnknownIntOperations
    :ivar value_types_client_unknown_dict: ValueTypesClientUnknownDictOperations operations
    :vartype value_types_client_unknown_dict:
     typetest.property.valuetypes.operations.ValueTypesClientUnknownDictOperations
    :ivar value_types_client_unknown_array: ValueTypesClientUnknownArrayOperations operations
    :vartype value_types_client_unknown_array:
     typetest.property.valuetypes.operations.ValueTypesClientUnknownArrayOperations
    :ivar value_types_client_string_literal: ValueTypesClientStringLiteralOperations operations
    :vartype value_types_client_string_literal:
     typetest.property.valuetypes.operations.ValueTypesClientStringLiteralOperations
    :ivar value_types_client_int_literal: ValueTypesClientIntLiteralOperations operations
    :vartype value_types_client_int_literal:
     typetest.property.valuetypes.operations.ValueTypesClientIntLiteralOperations
    :ivar value_types_client_float_literal: ValueTypesClientFloatLiteralOperations operations
    :vartype value_types_client_float_literal:
     typetest.property.valuetypes.operations.ValueTypesClientFloatLiteralOperations
    :ivar value_types_client_boolean_literal: ValueTypesClientBooleanLiteralOperations operations
    :vartype value_types_client_boolean_literal:
     typetest.property.valuetypes.operations.ValueTypesClientBooleanLiteralOperations
    :ivar value_types_client_union_string_literal: ValueTypesClientUnionStringLiteralOperations
     operations
    :vartype value_types_client_union_string_literal:
     typetest.property.valuetypes.operations.ValueTypesClientUnionStringLiteralOperations
    :ivar value_types_client_union_int_literal: ValueTypesClientUnionIntLiteralOperations
     operations
    :vartype value_types_client_union_int_literal:
     typetest.property.valuetypes.operations.ValueTypesClientUnionIntLiteralOperations
    :ivar value_types_client_union_float_literal: ValueTypesClientUnionFloatLiteralOperations
     operations
    :vartype value_types_client_union_float_literal:
     typetest.property.valuetypes.operations.ValueTypesClientUnionFloatLiteralOperations
    :ivar value_types_client_union_enum_value: ValueTypesClientUnionEnumValueOperations operations
    :vartype value_types_client_union_enum_value:
     typetest.property.valuetypes.operations.ValueTypesClientUnionEnumValueOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = ValueTypesClientConfiguration(endpoint=endpoint, **kwargs)

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
        self._client: PipelineClient = PipelineClient(endpoint=_endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.value_types_client_boolean = ValueTypesClientBooleanOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_string = ValueTypesClientStringOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_bytes = ValueTypesClientBytesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_int = ValueTypesClientIntOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_float = ValueTypesClientFloatOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_decimal = ValueTypesClientDecimalOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_decimal128 = ValueTypesClientDecimal128Operations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_datetime = ValueTypesClientDatetimeOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_duration = ValueTypesClientDurationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_enum = ValueTypesClientEnumOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_extensible_enum = ValueTypesClientExtensibleEnumOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_model = ValueTypesClientModelOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_collections_string = ValueTypesClientCollectionsStringOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_collections_int = ValueTypesClientCollectionsIntOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_collections_model = ValueTypesClientCollectionsModelOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_dictionary_string = ValueTypesClientDictionaryStringOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_never = ValueTypesClientNeverOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_unknown_string = ValueTypesClientUnknownStringOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_unknown_int = ValueTypesClientUnknownIntOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_unknown_dict = ValueTypesClientUnknownDictOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_unknown_array = ValueTypesClientUnknownArrayOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_string_literal = ValueTypesClientStringLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_int_literal = ValueTypesClientIntLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_float_literal = ValueTypesClientFloatLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_boolean_literal = ValueTypesClientBooleanLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_union_string_literal = ValueTypesClientUnionStringLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_union_int_literal = ValueTypesClientUnionIntLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_union_float_literal = ValueTypesClientUnionFloatLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.value_types_client_union_enum_value = ValueTypesClientUnionEnumValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from corehttp.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~corehttp.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~corehttp.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
