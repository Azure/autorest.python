# coding=utf-8

from copy import deepcopy
from typing import Any, Awaitable
from typing_extensions import Self

from azure.core import AsyncPipelineClient
from azure.core.pipeline import policies
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .._serialization import Deserializer, Serializer
from ._configuration import ResiliencyServiceDrivenClientConfiguration
from ._operations import ResiliencyServiceDrivenClientOperationsMixin


class ResiliencyServiceDrivenClient(ResiliencyServiceDrivenClientOperationsMixin):
    """Test that we can grow up a service spec and service deployment into a multi-versioned service
    with full client support.

    :param endpoint: Need to be set as '`http://localhost:3000 <http://localhost:3000>`_' in
     client. Required.
    :type endpoint: str
    :param service_deployment_version: Pass in either 'v1' or 'v2'. This represents a version of
     the service deployment in history. 'v1' is for the deployment when the service had only one api
     version. 'v2' is for the deployment when the service had api-versions 'v1' and 'v2'. Required.
    :type service_deployment_version: str
    :keyword api_version: Pass in 'v1'. This represents the API version of the service. Will grow
     up in the next deployment to be both 'v1' and 'v2'. Known values are "v1" and None. Default
     value is "v1". Note that overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, endpoint: str, service_deployment_version: str, **kwargs: Any
    ) -> None:
        _endpoint = (
            "{endpoint}/resiliency/service-driven/client:v1/service:{serviceDeploymentVersion}/api-version:{apiVersion}"
        )
        self._config = ResiliencyServiceDrivenClientConfiguration(
            endpoint=endpoint, service_deployment_version=service_deployment_version, **kwargs
        )
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
            "serviceDeploymentVersion": self._serialize.url(
                "self._config.service_deployment_version",
                self._config.service_deployment_version,
                "str",
                skip_quote=True,
            ),
            "apiVersion": self._serialize.url(
                "self._config.api_version", self._config.api_version, "str", skip_quote=True
            ),
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
