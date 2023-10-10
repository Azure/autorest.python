# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import NonStringEnumsClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import FloatOperations, IntOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict


class NonStringEnumsClient:  # pylint: disable=client-accepts-api-version-keyword
    """Testing non-string enums.

    :ivar int: IntOperations operations
    :vartype int: nonstringenums.operations.IntOperations
    :ivar float: FloatOperations operations
    :vartype float: nonstringenums.operations.FloatOperations
    :param base_url: Service URL. Default value is "http://localhost:3000".
    :type base_url: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, base_url: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        self._config = NonStringEnumsClientConfiguration(**kwargs)
        config_policies = [
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
        self._client: PipelineClient = PipelineClient(base_url=base_url, policies=config_policies, **kwargs)

        client_models: Dict[str, Any] = {}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.int = IntOperations(self._client, self._config, self._serialize, self._deserialize)
        self.float = FloatOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "NonStringEnumsClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
