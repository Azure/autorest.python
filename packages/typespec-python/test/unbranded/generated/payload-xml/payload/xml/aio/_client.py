# coding=utf-8

from copy import deepcopy
from typing import Any, Awaitable
from typing_extensions import Self

from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .._utils.serialization import Deserializer, Serializer
from ._configuration import XmlClientConfiguration
from .operations import (
    XmlClientModelWithArrayOfModelValueOperations,
    XmlClientModelWithAttributesValueOperations,
    XmlClientModelWithDictionaryValueOperations,
    XmlClientModelWithEmptyArrayValueOperations,
    XmlClientModelWithEncodedNamesValueOperations,
    XmlClientModelWithOptionalFieldValueOperations,
    XmlClientModelWithRenamedArraysValueOperations,
    XmlClientModelWithRenamedFieldsValueOperations,
    XmlClientModelWithSimpleArraysValueOperations,
    XmlClientModelWithTextValueOperations,
    XmlClientModelWithUnwrappedArrayValueOperations,
    XmlClientSimpleModelValueOperations,
    XmlClientXmlErrorValueOperations,
)


class XmlClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Sends and receives bodies in XML format.

    :ivar xml_client_simple_model_value: XmlClientSimpleModelValueOperations operations
    :vartype xml_client_simple_model_value:
     payload.xml.aio.operations.XmlClientSimpleModelValueOperations
    :ivar xml_client_model_with_simple_arrays_value: XmlClientModelWithSimpleArraysValueOperations
     operations
    :vartype xml_client_model_with_simple_arrays_value:
     payload.xml.aio.operations.XmlClientModelWithSimpleArraysValueOperations
    :ivar xml_client_model_with_array_of_model_value: XmlClientModelWithArrayOfModelValueOperations
     operations
    :vartype xml_client_model_with_array_of_model_value:
     payload.xml.aio.operations.XmlClientModelWithArrayOfModelValueOperations
    :ivar xml_client_model_with_optional_field_value:
     XmlClientModelWithOptionalFieldValueOperations operations
    :vartype xml_client_model_with_optional_field_value:
     payload.xml.aio.operations.XmlClientModelWithOptionalFieldValueOperations
    :ivar xml_client_model_with_attributes_value: XmlClientModelWithAttributesValueOperations
     operations
    :vartype xml_client_model_with_attributes_value:
     payload.xml.aio.operations.XmlClientModelWithAttributesValueOperations
    :ivar xml_client_model_with_unwrapped_array_value:
     XmlClientModelWithUnwrappedArrayValueOperations operations
    :vartype xml_client_model_with_unwrapped_array_value:
     payload.xml.aio.operations.XmlClientModelWithUnwrappedArrayValueOperations
    :ivar xml_client_model_with_renamed_arrays_value:
     XmlClientModelWithRenamedArraysValueOperations operations
    :vartype xml_client_model_with_renamed_arrays_value:
     payload.xml.aio.operations.XmlClientModelWithRenamedArraysValueOperations
    :ivar xml_client_model_with_renamed_fields_value:
     XmlClientModelWithRenamedFieldsValueOperations operations
    :vartype xml_client_model_with_renamed_fields_value:
     payload.xml.aio.operations.XmlClientModelWithRenamedFieldsValueOperations
    :ivar xml_client_model_with_empty_array_value: XmlClientModelWithEmptyArrayValueOperations
     operations
    :vartype xml_client_model_with_empty_array_value:
     payload.xml.aio.operations.XmlClientModelWithEmptyArrayValueOperations
    :ivar xml_client_model_with_text_value: XmlClientModelWithTextValueOperations operations
    :vartype xml_client_model_with_text_value:
     payload.xml.aio.operations.XmlClientModelWithTextValueOperations
    :ivar xml_client_model_with_dictionary_value: XmlClientModelWithDictionaryValueOperations
     operations
    :vartype xml_client_model_with_dictionary_value:
     payload.xml.aio.operations.XmlClientModelWithDictionaryValueOperations
    :ivar xml_client_model_with_encoded_names_value: XmlClientModelWithEncodedNamesValueOperations
     operations
    :vartype xml_client_model_with_encoded_names_value:
     payload.xml.aio.operations.XmlClientModelWithEncodedNamesValueOperations
    :ivar xml_client_xml_error_value: XmlClientXmlErrorValueOperations operations
    :vartype xml_client_xml_error_value:
     payload.xml.aio.operations.XmlClientXmlErrorValueOperations
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
        self.xml_client_simple_model_value = XmlClientSimpleModelValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.xml_client_model_with_simple_arrays_value = XmlClientModelWithSimpleArraysValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.xml_client_model_with_array_of_model_value = XmlClientModelWithArrayOfModelValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.xml_client_model_with_optional_field_value = XmlClientModelWithOptionalFieldValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.xml_client_model_with_attributes_value = XmlClientModelWithAttributesValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.xml_client_model_with_unwrapped_array_value = XmlClientModelWithUnwrappedArrayValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.xml_client_model_with_renamed_arrays_value = XmlClientModelWithRenamedArraysValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.xml_client_model_with_renamed_fields_value = XmlClientModelWithRenamedFieldsValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.xml_client_model_with_empty_array_value = XmlClientModelWithEmptyArrayValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.xml_client_model_with_text_value = XmlClientModelWithTextValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.xml_client_model_with_dictionary_value = XmlClientModelWithDictionaryValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.xml_client_model_with_encoded_names_value = XmlClientModelWithEncodedNamesValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.xml_client_xml_error_value = XmlClientXmlErrorValueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

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
