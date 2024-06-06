# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
import sys
from typing import Any, Awaitable, Union

from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import ServiceClientConfiguration
from .operations import BarOperations, BazOperations, FooOperations, QuxOperations, ServiceClientOperationsMixin

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self  # type: ignore  # pylint: disable=ungrouped-imports


class ServiceClient(ServiceClientOperationsMixin):  # pylint: disable=client-accepts-api-version-keyword
    """Test that we can use @client and @operationGroup decorators to customize client side code
    structure, such as:


    #. have everything as default.
    #. to rename client or operation group
    #. one client can have more than one operations groups
    #. split one interface into two clients
    #. have two clients with operations come from different interfaces
    #. have two clients with a hierarchy relation.

    :ivar baz: BazOperations operations
    :vartype baz: client.structure.service.aio.operations.BazOperations
    :ivar qux: QuxOperations operations
    :vartype qux: client.structure.service.aio.operations.QuxOperations
    :ivar foo: FooOperations operations
    :vartype foo: client.structure.service.aio.operations.FooOperations
    :ivar bar: BarOperations operations
    :vartype bar: client.structure.service.aio.operations.BarOperations
    :param endpoint: Need to be set as 'http://localhost:3000' in client. Required.
    :type endpoint: str
    :param client: Need to be set as 'default', 'multi-client', 'renamed-operation',
     'two-operation-group' in client. Known values are: "default", "multi-client",
     "renamed-operation", and "two-operation-group". Required.
    :type client: str or ~client.structure.service.models.ClientType
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, endpoint: str, client: Union[str, _models.ClientType], **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}/client/structure/{client}"
        self._config = ServiceClientConfiguration(endpoint=endpoint, client=client, **kwargs)
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
        self.baz = BazOperations(self._client, self._config, self._serialize, self._deserialize)
        self.qux = QuxOperations(self._client, self._config, self._serialize, self._deserialize)
        self.foo = FooOperations(self._client, self._config, self._serialize, self._deserialize)
        self.bar = BarOperations(self._client, self._config, self._serialize, self._deserialize)

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
            "client": self._serialize.url("self._config.client", self._config.client, "str"),
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
