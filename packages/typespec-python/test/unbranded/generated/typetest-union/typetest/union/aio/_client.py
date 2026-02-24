# coding=utf-8

from copy import deepcopy
from typing import Any, Awaitable
from typing_extensions import Self

from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .._utils.serialization import Deserializer, Serializer
from ._configuration import UnionClientConfiguration
from .operations import (
    UnionClientEnumsOnlyOperations,
    UnionClientFloatsOnlyOperations,
    UnionClientIntsOnlyOperations,
    UnionClientMixedLiteralsOperations,
    UnionClientMixedTypesOperations,
    UnionClientModelsOnlyOperations,
    UnionClientStringAndArrayOperations,
    UnionClientStringExtensibleNamedOperations,
    UnionClientStringExtensibleOperations,
    UnionClientStringsOnlyOperations,
)


class UnionClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Describe scenarios for various combinations of unions.

    :ivar union_client_strings_only: UnionClientStringsOnlyOperations operations
    :vartype union_client_strings_only:
     typetest.union.aio.operations.UnionClientStringsOnlyOperations
    :ivar union_client_string_extensible: UnionClientStringExtensibleOperations operations
    :vartype union_client_string_extensible:
     typetest.union.aio.operations.UnionClientStringExtensibleOperations
    :ivar union_client_string_extensible_named: UnionClientStringExtensibleNamedOperations
     operations
    :vartype union_client_string_extensible_named:
     typetest.union.aio.operations.UnionClientStringExtensibleNamedOperations
    :ivar union_client_ints_only: UnionClientIntsOnlyOperations operations
    :vartype union_client_ints_only: typetest.union.aio.operations.UnionClientIntsOnlyOperations
    :ivar union_client_floats_only: UnionClientFloatsOnlyOperations operations
    :vartype union_client_floats_only:
     typetest.union.aio.operations.UnionClientFloatsOnlyOperations
    :ivar union_client_models_only: UnionClientModelsOnlyOperations operations
    :vartype union_client_models_only:
     typetest.union.aio.operations.UnionClientModelsOnlyOperations
    :ivar union_client_enums_only: UnionClientEnumsOnlyOperations operations
    :vartype union_client_enums_only: typetest.union.aio.operations.UnionClientEnumsOnlyOperations
    :ivar union_client_string_and_array: UnionClientStringAndArrayOperations operations
    :vartype union_client_string_and_array:
     typetest.union.aio.operations.UnionClientStringAndArrayOperations
    :ivar union_client_mixed_literals: UnionClientMixedLiteralsOperations operations
    :vartype union_client_mixed_literals:
     typetest.union.aio.operations.UnionClientMixedLiteralsOperations
    :ivar union_client_mixed_types: UnionClientMixedTypesOperations operations
    :vartype union_client_mixed_types:
     typetest.union.aio.operations.UnionClientMixedTypesOperations
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
        self.union_client_strings_only = UnionClientStringsOnlyOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.union_client_string_extensible = UnionClientStringExtensibleOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.union_client_string_extensible_named = UnionClientStringExtensibleNamedOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.union_client_ints_only = UnionClientIntsOnlyOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.union_client_floats_only = UnionClientFloatsOnlyOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.union_client_models_only = UnionClientModelsOnlyOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.union_client_enums_only = UnionClientEnumsOnlyOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.union_client_string_and_array = UnionClientStringAndArrayOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.union_client_mixed_literals = UnionClientMixedLiteralsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.union_client_mixed_types = UnionClientMixedTypesOperations(
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
