# coding=utf-8


from copy import deepcopy
from typing import Any

from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient, policies

from ._configuration import NullableClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    BytesOperations,
    CollectionsByteOperations,
    CollectionsModelOperations,
    DatetimeOperations,
    DurationOperations,
    StringOperations,
)


class NullableClient:  # pylint: disable=client-accepts-api-version-keyword
    """Illustrates models with nullable properties.

    :ivar string: StringOperations operations
    :vartype string: typetest.property.nullable.operations.StringOperations
    :ivar bytes: BytesOperations operations
    :vartype bytes: typetest.property.nullable.operations.BytesOperations
    :ivar datetime: DatetimeOperations operations
    :vartype datetime: typetest.property.nullable.operations.DatetimeOperations
    :ivar duration: DurationOperations operations
    :vartype duration: typetest.property.nullable.operations.DurationOperations
    :ivar collections_byte: CollectionsByteOperations operations
    :vartype collections_byte: typetest.property.nullable.operations.CollectionsByteOperations
    :ivar collections_model: CollectionsModelOperations operations
    :vartype collections_model: typetest.property.nullable.operations.CollectionsModelOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        self._config = NullableClientConfiguration(**kwargs)
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
        self._client: PipelineClient = PipelineClient(endpoint=endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.string = StringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.bytes = BytesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.datetime = DatetimeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.duration = DurationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.collections_byte = CollectionsByteOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.collections_model = CollectionsModelOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
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
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "NullableClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
