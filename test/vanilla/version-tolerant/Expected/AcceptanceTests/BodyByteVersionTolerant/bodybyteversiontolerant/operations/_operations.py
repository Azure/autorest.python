# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_byte_get_null_request(**kwargs: Any) -> HttpRequest:
    accept = "application/json"
    # Construct URL
    url = "/byte/null"

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_byte_get_empty_request(**kwargs: Any) -> HttpRequest:
    accept = "application/json"
    # Construct URL
    url = "/byte/empty"

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_byte_get_non_ascii_request(**kwargs: Any) -> HttpRequest:
    accept = "application/json"
    # Construct URL
    url = "/byte/nonAscii"

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_byte_put_non_ascii_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = "/byte/nonAscii"

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_byte_get_invalid_request(**kwargs: Any) -> HttpRequest:
    accept = "application/json"
    # Construct URL
    url = "/byte/invalid"

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


class ByteOperations(object):
    """ByteOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_null(self, **kwargs: Any) -> bytearray:
        """Get null byte value.

        :return: bytearray
        :rtype: bytearray
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bytearray]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_byte_get_null_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace
    def get_empty(self, **kwargs: Any) -> bytearray:
        """Get empty byte value ''.

        :return: bytearray
        :rtype: bytearray
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bytearray]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_byte_get_empty_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace
    def get_non_ascii(self, **kwargs: Any) -> bytearray:
        """Get non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).

        :return: bytearray
        :rtype: bytearray
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bytearray]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_byte_get_non_ascii_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace
    def put_non_ascii(  # pylint: disable=inconsistent-return-statements
        self, byte_body: bytearray, **kwargs: Any
    ) -> None:
        """Put non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).

        :param byte_body: Base64-encoded non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).
        :type byte_body: bytearray
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = byte_body

        request = build_byte_put_non_ascii_request(
            content_type=content_type,
            json=_json,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def get_invalid(self, **kwargs: Any) -> bytearray:
        """Get invalid byte value ':::SWAGGER::::'.

        :return: bytearray
        :rtype: bytearray
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bytearray]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_byte_get_invalid_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
