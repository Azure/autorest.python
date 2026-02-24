# coding=utf-8

from copy import deepcopy
from typing import Any
from typing_extensions import Self

from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient, policies

from ._configuration import ScalarClientConfiguration
from ._utils.serialization import Deserializer, Serializer
from .operations import (
    ScalarClientBooleanOperations,
    ScalarClientDecimal128TypeOperations,
    ScalarClientDecimal128VerifyOperations,
    ScalarClientDecimalTypeOperations,
    ScalarClientDecimalVerifyOperations,
    ScalarClientStringOperations,
    ScalarClientUnknownOperations,
)


class ScalarClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """ScalarClient.

    :ivar scalar_client_string: ScalarClientStringOperations operations
    :vartype scalar_client_string: typetest.scalar.operations.ScalarClientStringOperations
    :ivar scalar_client_boolean: ScalarClientBooleanOperations operations
    :vartype scalar_client_boolean: typetest.scalar.operations.ScalarClientBooleanOperations
    :ivar scalar_client_unknown: ScalarClientUnknownOperations operations
    :vartype scalar_client_unknown: typetest.scalar.operations.ScalarClientUnknownOperations
    :ivar scalar_client_decimal_type: ScalarClientDecimalTypeOperations operations
    :vartype scalar_client_decimal_type:
     typetest.scalar.operations.ScalarClientDecimalTypeOperations
    :ivar scalar_client_decimal128_type: ScalarClientDecimal128TypeOperations operations
    :vartype scalar_client_decimal128_type:
     typetest.scalar.operations.ScalarClientDecimal128TypeOperations
    :ivar scalar_client_decimal_verify: ScalarClientDecimalVerifyOperations operations
    :vartype scalar_client_decimal_verify:
     typetest.scalar.operations.ScalarClientDecimalVerifyOperations
    :ivar scalar_client_decimal128_verify: ScalarClientDecimal128VerifyOperations operations
    :vartype scalar_client_decimal128_verify:
     typetest.scalar.operations.ScalarClientDecimal128VerifyOperations
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
        self.scalar_client_string = ScalarClientStringOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.scalar_client_boolean = ScalarClientBooleanOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.scalar_client_unknown = ScalarClientUnknownOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.scalar_client_decimal_type = ScalarClientDecimalTypeOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.scalar_client_decimal128_type = ScalarClientDecimal128TypeOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.scalar_client_decimal_verify = ScalarClientDecimalVerifyOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.scalar_client_decimal128_verify = ScalarClientDecimal128VerifyOperations(
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
