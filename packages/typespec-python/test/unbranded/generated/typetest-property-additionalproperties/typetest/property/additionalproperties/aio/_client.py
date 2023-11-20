# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable

from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .._serialization import Deserializer, Serializer
from ._configuration import AdditionalPropertiesClientConfiguration
from .operations import (
    ExtendsFloatOperations,
    ExtendsModelArrayOperations,
    ExtendsModelOperations,
    ExtendsStringOperations,
    ExtendsUnknownOperations,
    IsFloatOperations,
    IsModelArrayOperations,
    IsModelOperations,
    IsStringOperations,
    IsUnknownOperations,
)


class AdditionalPropertiesClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Tests for additional properties of models.

    :ivar extends_unknown: ExtendsUnknownOperations operations
    :vartype extends_unknown:
     typetest.property.additionalproperties.aio.operations.ExtendsUnknownOperations
    :ivar is_unknown: IsUnknownOperations operations
    :vartype is_unknown: typetest.property.additionalproperties.aio.operations.IsUnknownOperations
    :ivar extends_string: ExtendsStringOperations operations
    :vartype extends_string:
     typetest.property.additionalproperties.aio.operations.ExtendsStringOperations
    :ivar is_string: IsStringOperations operations
    :vartype is_string: typetest.property.additionalproperties.aio.operations.IsStringOperations
    :ivar extends_float: ExtendsFloatOperations operations
    :vartype extends_float:
     typetest.property.additionalproperties.aio.operations.ExtendsFloatOperations
    :ivar is_float: IsFloatOperations operations
    :vartype is_float: typetest.property.additionalproperties.aio.operations.IsFloatOperations
    :ivar extends_model: ExtendsModelOperations operations
    :vartype extends_model:
     typetest.property.additionalproperties.aio.operations.ExtendsModelOperations
    :ivar is_model: IsModelOperations operations
    :vartype is_model: typetest.property.additionalproperties.aio.operations.IsModelOperations
    :ivar extends_model_array: ExtendsModelArrayOperations operations
    :vartype extends_model_array:
     typetest.property.additionalproperties.aio.operations.ExtendsModelArrayOperations
    :ivar is_model_array: IsModelArrayOperations operations
    :vartype is_model_array:
     typetest.property.additionalproperties.aio.operations.IsModelArrayOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        self._config = AdditionalPropertiesClientConfiguration(**kwargs)
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
        self._client: AsyncPipelineClient = AsyncPipelineClient(endpoint=endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.extends_unknown = ExtendsUnknownOperations(self._client, self._config, self._serialize, self._deserialize)
        self.is_unknown = IsUnknownOperations(self._client, self._config, self._serialize, self._deserialize)
        self.extends_string = ExtendsStringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.is_string = IsStringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.extends_float = ExtendsFloatOperations(self._client, self._config, self._serialize, self._deserialize)
        self.is_float = IsFloatOperations(self._client, self._config, self._serialize, self._deserialize)
        self.extends_model = ExtendsModelOperations(self._client, self._config, self._serialize, self._deserialize)
        self.is_model = IsModelOperations(self._client, self._config, self._serialize, self._deserialize)
        self.extends_model_array = ExtendsModelArrayOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.is_model_array = IsModelArrayOperations(self._client, self._config, self._serialize, self._deserialize)

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
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AdditionalPropertiesClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)