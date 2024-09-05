# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any
from typing_extensions import Self

from azure.core import PipelineClient
from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import ResiliencyServiceDrivenClientConfiguration
from ._operations import ResiliencyServiceDrivenClientOperationsMixin
from ._serialization import Deserializer, Serializer


class ResiliencyServiceDrivenClient(ResiliencyServiceDrivenClientOperationsMixin):
    """Test that we can grow up a service spec and service deployment into a multi-versioned service
    with full client support.

    There are three concepts that should be clarified:


    #. Client spec version: refers to the spec that the client is generated from. 'v1' is a client
    generated from old.tsp and 'v2' is a client generated from main.tsp.
    #. Service deployment version: refers to a deployment version of the service. 'v1' represents
    the initial deployment of the service with a single api version. 'v2' represents the new
    deployment of a service with multiple api versions
    #. Api version: The initial deployment of the service only supports api version 'v1'. The new
    deployment of the service supports api versions 'v1' and 'v2'.

    We test the following configurations from this service spec:


    * A client generated from the second service spec can call the second deployment of a service
    with api version v1
    * A client generated from the second service spec can call the second deployment of a service
    with api version v2.

    :param endpoint: Need to be set as 'http://localhost:3000' in client. Required.
    :type endpoint: str
    :param service_deployment_version: Pass in either 'v1' or 'v2'. This represents a version of
     the service deployment in history. 'v1' is for the deployment when the service had only one api
     version. 'v2' is for the deployment when the service had api-versions 'v1' and 'v2'. Required.
    :type service_deployment_version: str
    :keyword api_version: Pass in either 'v1' or 'v2'. This represents the API version of a
     service. Known values are "v2" and None. Default value is "v2". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, endpoint: str, service_deployment_version: str, **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}/resiliency/service-driven/client:v2/service:{serviceDeploymentVersion}/api-version:{apiVersion}"  # pylint: disable=line-too-long
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
        self._client: PipelineClient = PipelineClient(base_url=_endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    def send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
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
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "serviceDeploymentVersion": self._serialize.url(
                "self._config.service_deployment_version", self._config.service_deployment_version, "str"
            ),
            "apiVersion": self._serialize.url("self._config.api_version", self._config.api_version, "str"),
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
