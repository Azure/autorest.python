# coding=utf-8


from copy import deepcopy
from typing import Any, Awaitable, Union

from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import ClientAClientConfiguration, ClientBClientConfiguration
from ._operations import ClientAClientOperationsMixin, ClientBClientOperationsMixin


class ClientAClient(ClientAClientOperationsMixin):  # pylint: disable=client-accepts-api-version-keyword
    """ClientAClient.

    :param endpoint: Need to be set as 'http://localhost:3000' in client. Required.
    :type endpoint: str
    :param client: Need to be set as 'default', 'multi-client', 'renamed-operation',
     'two-operation-group' in client. Known values are: "default", "multi-client",
     "renamed-operation", and "two-operation-group". Required.
    :type client: str or ~client.structure.multiclient.models.ClientType
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, endpoint: str, client: Union[str, _models.ClientType], **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}/client/structure/{client}"
        self._config = ClientAClientConfiguration(endpoint=endpoint, client=client, **kwargs)
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

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
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
            "client": self._serialize.url("self._config.client", self._config.client, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ClientAClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)


class ClientBClient(ClientBClientOperationsMixin):  # pylint: disable=client-accepts-api-version-keyword
    """ClientBClient.

    :param endpoint: Need to be set as 'http://localhost:3000' in client. Required.
    :type endpoint: str
    :param client: Need to be set as 'default', 'multi-client', 'renamed-operation',
     'two-operation-group' in client. Known values are: "default", "multi-client",
     "renamed-operation", and "two-operation-group". Required.
    :type client: str or ~client.structure.multiclient.models.ClientType
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, endpoint: str, client: Union[str, _models.ClientType], **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}/client/structure/{client}"
        self._config = ClientBClientConfiguration(endpoint=endpoint, client=client, **kwargs)
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

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
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
            "client": self._serialize.url("self._config.client", self._config.client, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ClientBClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
