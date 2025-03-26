# coding=utf-8

from copy import deepcopy
from typing import Any, Awaitable
from typing_extensions import Self

from azure.core import AsyncPipelineClient
from azure.core.pipeline import policies
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .._serialization import Deserializer, Serializer
from ._configuration import AccessClientConfiguration
from .operations import (
    InternalOperationOperations,
    PublicOperationOperations,
    RelativeModelInOperationOperations,
    SharedModelInOperationOperations,
)


class AccessClient:  # pylint: disable=client-accepts-api-version-keyword
    """Test for internal decorator.

    :ivar public_operation: PublicOperationOperations operations
    :vartype public_operation:
     specs.azure.clientgenerator.core.access.aio.operations.PublicOperationOperations
    :ivar internal_operation: InternalOperationOperations operations
    :vartype internal_operation:
     specs.azure.clientgenerator.core.access.aio.operations.InternalOperationOperations
    :ivar shared_model_in_operation: SharedModelInOperationOperations operations
    :vartype shared_model_in_operation:
     specs.azure.clientgenerator.core.access.aio.operations.SharedModelInOperationOperations
    :ivar relative_model_in_operation: RelativeModelInOperationOperations operations
    :vartype relative_model_in_operation:
     specs.azure.clientgenerator.core.access.aio.operations.RelativeModelInOperationOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = AccessClientConfiguration(endpoint=endpoint, **kwargs)
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
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
        self._client: AsyncPipelineClient = AsyncPipelineClient(base_url=_endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.public_operation = PublicOperationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.internal_operation = InternalOperationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.shared_model_in_operation = SharedModelInOperationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.relative_model_in_operation = RelativeModelInOperationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def send_request(
        self, request: HttpRequest, *, stream: bool = False, **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
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
