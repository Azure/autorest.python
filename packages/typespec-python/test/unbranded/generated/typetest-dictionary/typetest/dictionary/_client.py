# coding=utf-8

from copy import deepcopy
from typing import Any
from typing_extensions import Self

from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient, policies

from ._configuration import DictionaryClientConfiguration
from ._utils.serialization import Deserializer, Serializer
from .operations import (
    DictionaryClientBooleanValueOperations,
    DictionaryClientDatetimeValueOperations,
    DictionaryClientDurationValueOperations,
    DictionaryClientFloat32ValueOperations,
    DictionaryClientInt32ValueOperations,
    DictionaryClientInt64ValueOperations,
    DictionaryClientModelValueOperations,
    DictionaryClientNullableFloatValueOperations,
    DictionaryClientRecursiveModelValueOperations,
    DictionaryClientStringValueOperations,
    DictionaryClientUnknownValueOperations,
)


class DictionaryClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Illustrates various of dictionaries.

    :ivar dictionary_client_int32_value: DictionaryClientInt32ValueOperations operations
    :vartype dictionary_client_int32_value:
     typetest.dictionary.operations.DictionaryClientInt32ValueOperations
    :ivar dictionary_client_int64_value: DictionaryClientInt64ValueOperations operations
    :vartype dictionary_client_int64_value:
     typetest.dictionary.operations.DictionaryClientInt64ValueOperations
    :ivar dictionary_client_boolean_value: DictionaryClientBooleanValueOperations operations
    :vartype dictionary_client_boolean_value:
     typetest.dictionary.operations.DictionaryClientBooleanValueOperations
    :ivar dictionary_client_string_value: DictionaryClientStringValueOperations operations
    :vartype dictionary_client_string_value:
     typetest.dictionary.operations.DictionaryClientStringValueOperations
    :ivar dictionary_client_float32_value: DictionaryClientFloat32ValueOperations operations
    :vartype dictionary_client_float32_value:
     typetest.dictionary.operations.DictionaryClientFloat32ValueOperations
    :ivar dictionary_client_datetime_value: DictionaryClientDatetimeValueOperations operations
    :vartype dictionary_client_datetime_value:
     typetest.dictionary.operations.DictionaryClientDatetimeValueOperations
    :ivar dictionary_client_duration_value: DictionaryClientDurationValueOperations operations
    :vartype dictionary_client_duration_value:
     typetest.dictionary.operations.DictionaryClientDurationValueOperations
    :ivar dictionary_client_unknown_value: DictionaryClientUnknownValueOperations operations
    :vartype dictionary_client_unknown_value:
     typetest.dictionary.operations.DictionaryClientUnknownValueOperations
    :ivar dictionary_client_model_value: DictionaryClientModelValueOperations operations
    :vartype dictionary_client_model_value:
     typetest.dictionary.operations.DictionaryClientModelValueOperations
    :ivar dictionary_client_recursive_model_value: DictionaryClientRecursiveModelValueOperations
     operations
    :vartype dictionary_client_recursive_model_value:
     typetest.dictionary.operations.DictionaryClientRecursiveModelValueOperations
    :ivar dictionary_client_nullable_float_value: DictionaryClientNullableFloatValueOperations
     operations
    :vartype dictionary_client_nullable_float_value:
     typetest.dictionary.operations.DictionaryClientNullableFloatValueOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = DictionaryClientConfiguration(endpoint=endpoint, **kwargs)

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
        self.dictionary_client_int32_value = DictionaryClientInt32ValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dictionary_client_int64_value = DictionaryClientInt64ValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dictionary_client_boolean_value = DictionaryClientBooleanValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dictionary_client_string_value = DictionaryClientStringValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dictionary_client_float32_value = DictionaryClientFloat32ValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dictionary_client_datetime_value = DictionaryClientDatetimeValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dictionary_client_duration_value = DictionaryClientDurationValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dictionary_client_unknown_value = DictionaryClientUnknownValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dictionary_client_model_value = DictionaryClientModelValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dictionary_client_recursive_model_value = DictionaryClientRecursiveModelValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dictionary_client_nullable_float_value = DictionaryClientNullableFloatValueOperations(
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
