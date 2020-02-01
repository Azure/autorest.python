# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ByteOperations:
    """ByteOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodybyte.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_null(
        self,
        cls: ClsType[bytearray] = None,
        **kwargs: Any
    ) -> bytearray:
        """Get null byte value.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: bytearray or the result of cls(response)
        :rtype: bytearray
        :raises: ~bodybyte.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_null.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('bytearray', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_null.metadata = {'url': '/byte/null'}

    @distributed_trace_async
    async def get_empty(
        self,
        cls: ClsType[bytearray] = None,
        **kwargs: Any
    ) -> bytearray:
        """Get empty byte value ''.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: bytearray or the result of cls(response)
        :rtype: bytearray
        :raises: ~bodybyte.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_empty.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('bytearray', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_empty.metadata = {'url': '/byte/empty'}

    @distributed_trace_async
    async def get_non_ascii(
        self,
        cls: ClsType[bytearray] = None,
        **kwargs: Any
    ) -> bytearray:
        """Get non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).

        :param callable cls: A custom type or function that will be passed the direct response
        :return: bytearray or the result of cls(response)
        :rtype: bytearray
        :raises: ~bodybyte.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_non_ascii.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('bytearray', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_non_ascii.metadata = {'url': '/byte/nonAscii'}

    @distributed_trace_async
    async def put_non_ascii(
        self,
        byte_body: bytearray,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Put non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).

        :param byte_body: Base64-encoded non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).
        :type byte_body: bytearray
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodybyte.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.put_non_ascii.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(byte_body, 'bytearray')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_non_ascii.metadata = {'url': '/byte/nonAscii'}

    @distributed_trace_async
    async def get_invalid(
        self,
        cls: ClsType[bytearray] = None,
        **kwargs: Any
    ) -> bytearray:
        """Get invalid byte value ':::SWAGGER::::'.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: bytearray or the result of cls(response)
        :rtype: bytearray
        :raises: ~bodybyte.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_invalid.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('bytearray', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_invalid.metadata = {'url': '/byte/invalid'}
