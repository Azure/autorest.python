# coding=utf-8

from copy import deepcopy
from typing import Any, Awaitable
from typing_extensions import Self

from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .._utils.serialization import Deserializer, Serializer
from ._configuration import OptionalClientConfiguration
from .operations import (
    OptionalClientBooleanLiteralOperations,
    OptionalClientBytesOperations,
    OptionalClientCollectionsByteOperations,
    OptionalClientCollectionsModelOperations,
    OptionalClientDatetimeOperations,
    OptionalClientDurationOperations,
    OptionalClientFloatLiteralOperations,
    OptionalClientIntLiteralOperations,
    OptionalClientPlainDateOperations,
    OptionalClientPlainTimeOperations,
    OptionalClientRequiredAndOptionalOperations,
    OptionalClientStringLiteralOperations,
    OptionalClientStringOperations,
    OptionalClientUnionFloatLiteralOperations,
    OptionalClientUnionIntLiteralOperations,
    OptionalClientUnionStringLiteralOperations,
)


class OptionalClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Illustrates models with optional properties.

    :ivar optional_client_string: OptionalClientStringOperations operations
    :vartype optional_client_string:
     typetest.property.optional.aio.operations.OptionalClientStringOperations
    :ivar optional_client_bytes: OptionalClientBytesOperations operations
    :vartype optional_client_bytes:
     typetest.property.optional.aio.operations.OptionalClientBytesOperations
    :ivar optional_client_datetime: OptionalClientDatetimeOperations operations
    :vartype optional_client_datetime:
     typetest.property.optional.aio.operations.OptionalClientDatetimeOperations
    :ivar optional_client_duration: OptionalClientDurationOperations operations
    :vartype optional_client_duration:
     typetest.property.optional.aio.operations.OptionalClientDurationOperations
    :ivar optional_client_plain_date: OptionalClientPlainDateOperations operations
    :vartype optional_client_plain_date:
     typetest.property.optional.aio.operations.OptionalClientPlainDateOperations
    :ivar optional_client_plain_time: OptionalClientPlainTimeOperations operations
    :vartype optional_client_plain_time:
     typetest.property.optional.aio.operations.OptionalClientPlainTimeOperations
    :ivar optional_client_collections_byte: OptionalClientCollectionsByteOperations operations
    :vartype optional_client_collections_byte:
     typetest.property.optional.aio.operations.OptionalClientCollectionsByteOperations
    :ivar optional_client_collections_model: OptionalClientCollectionsModelOperations operations
    :vartype optional_client_collections_model:
     typetest.property.optional.aio.operations.OptionalClientCollectionsModelOperations
    :ivar optional_client_string_literal: OptionalClientStringLiteralOperations operations
    :vartype optional_client_string_literal:
     typetest.property.optional.aio.operations.OptionalClientStringLiteralOperations
    :ivar optional_client_int_literal: OptionalClientIntLiteralOperations operations
    :vartype optional_client_int_literal:
     typetest.property.optional.aio.operations.OptionalClientIntLiteralOperations
    :ivar optional_client_float_literal: OptionalClientFloatLiteralOperations operations
    :vartype optional_client_float_literal:
     typetest.property.optional.aio.operations.OptionalClientFloatLiteralOperations
    :ivar optional_client_boolean_literal: OptionalClientBooleanLiteralOperations operations
    :vartype optional_client_boolean_literal:
     typetest.property.optional.aio.operations.OptionalClientBooleanLiteralOperations
    :ivar optional_client_union_string_literal: OptionalClientUnionStringLiteralOperations
     operations
    :vartype optional_client_union_string_literal:
     typetest.property.optional.aio.operations.OptionalClientUnionStringLiteralOperations
    :ivar optional_client_union_int_literal: OptionalClientUnionIntLiteralOperations operations
    :vartype optional_client_union_int_literal:
     typetest.property.optional.aio.operations.OptionalClientUnionIntLiteralOperations
    :ivar optional_client_union_float_literal: OptionalClientUnionFloatLiteralOperations operations
    :vartype optional_client_union_float_literal:
     typetest.property.optional.aio.operations.OptionalClientUnionFloatLiteralOperations
    :ivar optional_client_required_and_optional: OptionalClientRequiredAndOptionalOperations
     operations
    :vartype optional_client_required_and_optional:
     typetest.property.optional.aio.operations.OptionalClientRequiredAndOptionalOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = OptionalClientConfiguration(endpoint=endpoint, **kwargs)

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
        self.optional_client_string = OptionalClientStringOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_bytes = OptionalClientBytesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_datetime = OptionalClientDatetimeOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_duration = OptionalClientDurationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_plain_date = OptionalClientPlainDateOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_plain_time = OptionalClientPlainTimeOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_collections_byte = OptionalClientCollectionsByteOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_collections_model = OptionalClientCollectionsModelOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_string_literal = OptionalClientStringLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_int_literal = OptionalClientIntLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_float_literal = OptionalClientFloatLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_boolean_literal = OptionalClientBooleanLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_union_string_literal = OptionalClientUnionStringLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_union_int_literal = OptionalClientUnionIntLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_union_float_literal = OptionalClientUnionFloatLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.optional_client_required_and_optional = OptionalClientRequiredAndOptionalOperations(
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
