# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Optional

from azure.core import PipelineClient
from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import AutoRestRequiredOptionalTestServiceConfiguration
from ._serialization import Deserializer, Serializer
from .operations import ExplicitOperations, ImplicitOperations


class AutoRestRequiredOptionalTestService:  # pylint: disable=client-accepts-api-version-keyword
    """Test Infrastructure for AutoRest.

    :ivar implicit: ImplicitOperations operations
    :vartype implicit: requiredoptionalversiontolerant.operations.ImplicitOperations
    :ivar explicit: ExplicitOperations operations
    :vartype explicit: requiredoptionalversiontolerant.operations.ExplicitOperations
    :param required_global_path: number of items to skip. Required.
    :type required_global_path: str
    :param required_global_query: number of items to skip. Required.
    :type required_global_query: str
    :param optional_global_query: number of items to skip. Default value is None.
    :type optional_global_query: int
    :keyword endpoint: Service URL. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self,
        required_global_path: str,
        required_global_query: str,
        optional_global_query: Optional[int] = None,
        *,
        endpoint: str = "http://localhost:3000",
        **kwargs: Any
    ) -> None:
        self._config = AutoRestRequiredOptionalTestServiceConfiguration(
            required_global_path=required_global_path,
            required_global_query=required_global_query,
            optional_global_query=optional_global_query,
            **kwargs
        )
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
        self._client: PipelineClient = PipelineClient(base_url=endpoint, policies=config_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.implicit = ImplicitOperations(self._client, self._config, self._serialize, self._deserialize)
        self.explicit = ExplicitOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
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

    def __enter__(self) -> "AutoRestRequiredOptionalTestService":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
