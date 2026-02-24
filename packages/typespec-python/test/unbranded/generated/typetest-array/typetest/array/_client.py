# coding=utf-8

from copy import deepcopy
from typing import Any
from typing_extensions import Self

from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient, policies

from ._configuration import ArrayClientConfiguration
from ._utils.serialization import Deserializer, Serializer
from .operations import (
    ArrayClientBooleanValueOperations,
    ArrayClientDatetimeValueOperations,
    ArrayClientDurationValueOperations,
    ArrayClientFloat32ValueOperations,
    ArrayClientInt32ValueOperations,
    ArrayClientInt64ValueOperations,
    ArrayClientModelValueOperations,
    ArrayClientNullableBooleanValueOperations,
    ArrayClientNullableFloatValueOperations,
    ArrayClientNullableInt32ValueOperations,
    ArrayClientNullableModelValueOperations,
    ArrayClientNullableStringValueOperations,
    ArrayClientStringValueOperations,
    ArrayClientUnknownValueOperations,
)


class ArrayClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Illustrates various types of arrays.

    :ivar array_client_int32_value: ArrayClientInt32ValueOperations operations
    :vartype array_client_int32_value: typetest.array.operations.ArrayClientInt32ValueOperations
    :ivar array_client_int64_value: ArrayClientInt64ValueOperations operations
    :vartype array_client_int64_value: typetest.array.operations.ArrayClientInt64ValueOperations
    :ivar array_client_boolean_value: ArrayClientBooleanValueOperations operations
    :vartype array_client_boolean_value:
     typetest.array.operations.ArrayClientBooleanValueOperations
    :ivar array_client_string_value: ArrayClientStringValueOperations operations
    :vartype array_client_string_value: typetest.array.operations.ArrayClientStringValueOperations
    :ivar array_client_float32_value: ArrayClientFloat32ValueOperations operations
    :vartype array_client_float32_value:
     typetest.array.operations.ArrayClientFloat32ValueOperations
    :ivar array_client_datetime_value: ArrayClientDatetimeValueOperations operations
    :vartype array_client_datetime_value:
     typetest.array.operations.ArrayClientDatetimeValueOperations
    :ivar array_client_duration_value: ArrayClientDurationValueOperations operations
    :vartype array_client_duration_value:
     typetest.array.operations.ArrayClientDurationValueOperations
    :ivar array_client_unknown_value: ArrayClientUnknownValueOperations operations
    :vartype array_client_unknown_value:
     typetest.array.operations.ArrayClientUnknownValueOperations
    :ivar array_client_model_value: ArrayClientModelValueOperations operations
    :vartype array_client_model_value: typetest.array.operations.ArrayClientModelValueOperations
    :ivar array_client_nullable_float_value: ArrayClientNullableFloatValueOperations operations
    :vartype array_client_nullable_float_value:
     typetest.array.operations.ArrayClientNullableFloatValueOperations
    :ivar array_client_nullable_int32_value: ArrayClientNullableInt32ValueOperations operations
    :vartype array_client_nullable_int32_value:
     typetest.array.operations.ArrayClientNullableInt32ValueOperations
    :ivar array_client_nullable_boolean_value: ArrayClientNullableBooleanValueOperations operations
    :vartype array_client_nullable_boolean_value:
     typetest.array.operations.ArrayClientNullableBooleanValueOperations
    :ivar array_client_nullable_string_value: ArrayClientNullableStringValueOperations operations
    :vartype array_client_nullable_string_value:
     typetest.array.operations.ArrayClientNullableStringValueOperations
    :ivar array_client_nullable_model_value: ArrayClientNullableModelValueOperations operations
    :vartype array_client_nullable_model_value:
     typetest.array.operations.ArrayClientNullableModelValueOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = ArrayClientConfiguration(endpoint=endpoint, **kwargs)

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
        self.array_client_int32_value = ArrayClientInt32ValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.array_client_int64_value = ArrayClientInt64ValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.array_client_boolean_value = ArrayClientBooleanValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.array_client_string_value = ArrayClientStringValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.array_client_float32_value = ArrayClientFloat32ValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.array_client_datetime_value = ArrayClientDatetimeValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.array_client_duration_value = ArrayClientDurationValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.array_client_unknown_value = ArrayClientUnknownValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.array_client_model_value = ArrayClientModelValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.array_client_nullable_float_value = ArrayClientNullableFloatValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.array_client_nullable_int32_value = ArrayClientNullableInt32ValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.array_client_nullable_boolean_value = ArrayClientNullableBooleanValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.array_client_nullable_string_value = ArrayClientNullableStringValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.array_client_nullable_model_value = ArrayClientNullableModelValueOperations(
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
