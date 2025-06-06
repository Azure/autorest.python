# coding=utf-8

from copy import deepcopy
from typing import Any
from typing_extensions import Self

from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient, policies

from ._configuration import ScalarClientConfiguration
from ._utils.serialization import Deserializer, Serializer
from .operations import (
    BooleanOperations,
    Decimal128TypeOperations,
    Decimal128VerifyOperations,
    DecimalTypeOperations,
    DecimalVerifyOperations,
    StringOperations,
    UnknownOperations,
)


class ScalarClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """ScalarClient.

    :ivar string: StringOperations operations
    :vartype string: typetest.scalar.operations.StringOperations
    :ivar boolean: BooleanOperations operations
    :vartype boolean: typetest.scalar.operations.BooleanOperations
    :ivar unknown: UnknownOperations operations
    :vartype unknown: typetest.scalar.operations.UnknownOperations
    :ivar decimal_type: DecimalTypeOperations operations
    :vartype decimal_type: typetest.scalar.operations.DecimalTypeOperations
    :ivar decimal128_type: Decimal128TypeOperations operations
    :vartype decimal128_type: typetest.scalar.operations.Decimal128TypeOperations
    :ivar decimal_verify: DecimalVerifyOperations operations
    :vartype decimal_verify: typetest.scalar.operations.DecimalVerifyOperations
    :ivar decimal128_verify: Decimal128VerifyOperations operations
    :vartype decimal128_verify: typetest.scalar.operations.Decimal128VerifyOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = ScalarClientConfiguration(endpoint=endpoint, **kwargs)

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
        self.string = StringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.boolean = BooleanOperations(self._client, self._config, self._serialize, self._deserialize)
        self.unknown = UnknownOperations(self._client, self._config, self._serialize, self._deserialize)
        self.decimal_type = DecimalTypeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.decimal128_type = Decimal128TypeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.decimal_verify = DecimalVerifyOperations(self._client, self._config, self._serialize, self._deserialize)
        self.decimal128_verify = Decimal128VerifyOperations(
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
