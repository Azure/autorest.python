# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ...operations._operations import (
    build_byte_get_empty_request,
    build_byte_get_invalid_request,
    build_byte_get_non_ascii_request,
    build_byte_get_null_request,
    build_byte_put_non_ascii_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ByteOperations:
    """ByteOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_null(self, **kwargs: Any) -> bytearray:
        """Get null byte value.

        :return: bytearray
        :rtype: bytearray
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bytearray]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_byte_get_null_request(
            template_url=self.get_null.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
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

    get_null.metadata = {"url": "/byte/null"}  # type: ignore

    @distributed_trace_async
    async def get_empty(self, **kwargs: Any) -> bytearray:
        """Get empty byte value ''.

        :return: bytearray
        :rtype: bytearray
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bytearray]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_byte_get_empty_request(
            template_url=self.get_empty.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
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

    get_empty.metadata = {"url": "/byte/empty"}  # type: ignore

    @distributed_trace_async
    async def get_non_ascii(self, **kwargs: Any) -> bytearray:
        """Get non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).

        :return: bytearray
        :rtype: bytearray
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bytearray]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_byte_get_non_ascii_request(
            template_url=self.get_non_ascii.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
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

    get_non_ascii.metadata = {"url": "/byte/nonAscii"}  # type: ignore

    @distributed_trace_async
    async def put_non_ascii(self, byte_body: bytearray, **kwargs: Any) -> None:
        """Put non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).

        :param byte_body: Base64-encoded non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).
        :type byte_body: bytearray
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = byte_body

        request = build_byte_put_non_ascii_request(
            content_type=content_type,
            json=json,
            template_url=self.put_non_ascii.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_non_ascii.metadata = {"url": "/byte/nonAscii"}  # type: ignore

    @distributed_trace_async
    async def get_invalid(self, **kwargs: Any) -> bytearray:
        """Get invalid byte value ':::SWAGGER::::'.

        :return: bytearray
        :rtype: bytearray
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bytearray]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_byte_get_invalid_request(
            template_url=self.get_invalid.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
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

    get_invalid.metadata = {"url": "/byte/invalid"}  # type: ignore
