# coding=utf-8

from copy import deepcopy
from typing import Any, Awaitable
from typing_extensions import Self

from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .._utils.serialization import Deserializer, Serializer
from ._configuration import DictionaryClientConfiguration
from .operations import (
    BooleanValueOperations,
    DatetimeValueOperations,
    DurationValueOperations,
    Float32ValueOperations,
    Int32ValueOperations,
    Int64ValueOperations,
    ModelValueOperations,
    NullableFloatValueOperations,
    RecursiveModelValueOperations,
    StringValueOperations,
    UnknownValueOperations,
)


class DictionaryClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Illustrates various of dictionaries.

    :ivar int32_value: Int32ValueOperations operations
    :vartype int32_value: typetest.dictionary.aio.operations.Int32ValueOperations
    :ivar int64_value: Int64ValueOperations operations
    :vartype int64_value: typetest.dictionary.aio.operations.Int64ValueOperations
    :ivar boolean_value: BooleanValueOperations operations
    :vartype boolean_value: typetest.dictionary.aio.operations.BooleanValueOperations
    :ivar string_value: StringValueOperations operations
    :vartype string_value: typetest.dictionary.aio.operations.StringValueOperations
    :ivar float32_value: Float32ValueOperations operations
    :vartype float32_value: typetest.dictionary.aio.operations.Float32ValueOperations
    :ivar datetime_value: DatetimeValueOperations operations
    :vartype datetime_value: typetest.dictionary.aio.operations.DatetimeValueOperations
    :ivar duration_value: DurationValueOperations operations
    :vartype duration_value: typetest.dictionary.aio.operations.DurationValueOperations
    :ivar unknown_value: UnknownValueOperations operations
    :vartype unknown_value: typetest.dictionary.aio.operations.UnknownValueOperations
    :ivar model_value: ModelValueOperations operations
    :vartype model_value: typetest.dictionary.aio.operations.ModelValueOperations
    :ivar recursive_model_value: RecursiveModelValueOperations operations
    :vartype recursive_model_value:
     typetest.dictionary.aio.operations.RecursiveModelValueOperations
    :ivar nullable_float_value: NullableFloatValueOperations operations
    :vartype nullable_float_value: typetest.dictionary.aio.operations.NullableFloatValueOperations
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
        self._client: AsyncPipelineClient = AsyncPipelineClient(endpoint=_endpoint, policies=_policies, **kwargs)

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
        self.recursive_model_value = RecursiveModelValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.nullable_float_value = NullableFloatValueOperations(
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
