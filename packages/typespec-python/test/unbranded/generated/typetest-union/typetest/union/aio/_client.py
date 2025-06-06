# coding=utf-8

from copy import deepcopy
from typing import Any, Awaitable
from typing_extensions import Self

from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .._utils.serialization import Deserializer, Serializer
from ._configuration import UnionClientConfiguration
from .operations import (
    EnumsOnlyOperations,
    FloatsOnlyOperations,
    IntsOnlyOperations,
    MixedLiteralsOperations,
    MixedTypesOperations,
    ModelsOnlyOperations,
    StringAndArrayOperations,
    StringExtensibleNamedOperations,
    StringExtensibleOperations,
    StringsOnlyOperations,
)


class UnionClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Describe scenarios for various combinations of unions.

    :ivar strings_only: StringsOnlyOperations operations
    :vartype strings_only: typetest.union.aio.operations.StringsOnlyOperations
    :ivar string_extensible: StringExtensibleOperations operations
    :vartype string_extensible: typetest.union.aio.operations.StringExtensibleOperations
    :ivar string_extensible_named: StringExtensibleNamedOperations operations
    :vartype string_extensible_named: typetest.union.aio.operations.StringExtensibleNamedOperations
    :ivar ints_only: IntsOnlyOperations operations
    :vartype ints_only: typetest.union.aio.operations.IntsOnlyOperations
    :ivar floats_only: FloatsOnlyOperations operations
    :vartype floats_only: typetest.union.aio.operations.FloatsOnlyOperations
    :ivar models_only: ModelsOnlyOperations operations
    :vartype models_only: typetest.union.aio.operations.ModelsOnlyOperations
    :ivar enums_only: EnumsOnlyOperations operations
    :vartype enums_only: typetest.union.aio.operations.EnumsOnlyOperations
    :ivar string_and_array: StringAndArrayOperations operations
    :vartype string_and_array: typetest.union.aio.operations.StringAndArrayOperations
    :ivar mixed_literals: MixedLiteralsOperations operations
    :vartype mixed_literals: typetest.union.aio.operations.MixedLiteralsOperations
    :ivar mixed_types: MixedTypesOperations operations
    :vartype mixed_types: typetest.union.aio.operations.MixedTypesOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = UnionClientConfiguration(endpoint=endpoint, **kwargs)

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
        self.strings_only = StringsOnlyOperations(self._client, self._config, self._serialize, self._deserialize)
        self.string_extensible = StringExtensibleOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.string_extensible_named = StringExtensibleNamedOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.ints_only = IntsOnlyOperations(self._client, self._config, self._serialize, self._deserialize)
        self.floats_only = FloatsOnlyOperations(self._client, self._config, self._serialize, self._deserialize)
        self.models_only = ModelsOnlyOperations(self._client, self._config, self._serialize, self._deserialize)
        self.enums_only = EnumsOnlyOperations(self._client, self._config, self._serialize, self._deserialize)
        self.string_and_array = StringAndArrayOperations(self._client, self._config, self._serialize, self._deserialize)
        self.mixed_literals = MixedLiteralsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.mixed_types = MixedTypesOperations(self._client, self._config, self._serialize, self._deserialize)

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
