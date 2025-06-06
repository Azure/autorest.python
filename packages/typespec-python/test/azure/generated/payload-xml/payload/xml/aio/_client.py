# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable
from typing_extensions import Self

from azure.core import AsyncPipelineClient
from azure.core.pipeline import policies
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .._utils.serialization import Deserializer, Serializer
from ._configuration import XmlClientConfiguration
from .operations import (
    ModelWithArrayOfModelValueOperations,
    ModelWithAttributesValueOperations,
    ModelWithDictionaryValueOperations,
    ModelWithEmptyArrayValueOperations,
    ModelWithEncodedNamesValueOperations,
    ModelWithOptionalFieldValueOperations,
    ModelWithRenamedArraysValueOperations,
    ModelWithRenamedFieldsValueOperations,
    ModelWithSimpleArraysValueOperations,
    ModelWithTextValueOperations,
    ModelWithUnwrappedArrayValueOperations,
    SimpleModelValueOperations,
)


class XmlClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Sends and receives bodies in XML format.

    :ivar simple_model_value: SimpleModelValueOperations operations
    :vartype simple_model_value: payload.xml.aio.operations.SimpleModelValueOperations
    :ivar model_with_simple_arrays_value: ModelWithSimpleArraysValueOperations operations
    :vartype model_with_simple_arrays_value:
     payload.xml.aio.operations.ModelWithSimpleArraysValueOperations
    :ivar model_with_array_of_model_value: ModelWithArrayOfModelValueOperations operations
    :vartype model_with_array_of_model_value:
     payload.xml.aio.operations.ModelWithArrayOfModelValueOperations
    :ivar model_with_optional_field_value: ModelWithOptionalFieldValueOperations operations
    :vartype model_with_optional_field_value:
     payload.xml.aio.operations.ModelWithOptionalFieldValueOperations
    :ivar model_with_attributes_value: ModelWithAttributesValueOperations operations
    :vartype model_with_attributes_value:
     payload.xml.aio.operations.ModelWithAttributesValueOperations
    :ivar model_with_unwrapped_array_value: ModelWithUnwrappedArrayValueOperations operations
    :vartype model_with_unwrapped_array_value:
     payload.xml.aio.operations.ModelWithUnwrappedArrayValueOperations
    :ivar model_with_renamed_arrays_value: ModelWithRenamedArraysValueOperations operations
    :vartype model_with_renamed_arrays_value:
     payload.xml.aio.operations.ModelWithRenamedArraysValueOperations
    :ivar model_with_renamed_fields_value: ModelWithRenamedFieldsValueOperations operations
    :vartype model_with_renamed_fields_value:
     payload.xml.aio.operations.ModelWithRenamedFieldsValueOperations
    :ivar model_with_empty_array_value: ModelWithEmptyArrayValueOperations operations
    :vartype model_with_empty_array_value:
     payload.xml.aio.operations.ModelWithEmptyArrayValueOperations
    :ivar model_with_text_value: ModelWithTextValueOperations operations
    :vartype model_with_text_value: payload.xml.aio.operations.ModelWithTextValueOperations
    :ivar model_with_dictionary_value: ModelWithDictionaryValueOperations operations
    :vartype model_with_dictionary_value:
     payload.xml.aio.operations.ModelWithDictionaryValueOperations
    :ivar model_with_encoded_names_value: ModelWithEncodedNamesValueOperations operations
    :vartype model_with_encoded_names_value:
     payload.xml.aio.operations.ModelWithEncodedNamesValueOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = XmlClientConfiguration(endpoint=endpoint, **kwargs)

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
        self.simple_model_value = SimpleModelValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_simple_arrays_value = ModelWithSimpleArraysValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_array_of_model_value = ModelWithArrayOfModelValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_optional_field_value = ModelWithOptionalFieldValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_attributes_value = ModelWithAttributesValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_unwrapped_array_value = ModelWithUnwrappedArrayValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_renamed_arrays_value = ModelWithRenamedArraysValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_renamed_fields_value = ModelWithRenamedFieldsValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_empty_array_value = ModelWithEmptyArrayValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_text_value = ModelWithTextValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_dictionary_value = ModelWithDictionaryValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_with_encoded_names_value = ModelWithEncodedNamesValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

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
