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

class HttpRetryOperations:
    """HttpRetryOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~httpinfrastructure.models
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
    async def head408(
        self,
        **kwargs
    ) -> None:
        """Return 408 status code, then 200 after retry.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.head408.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    head408.metadata = {'url': '/http/retry/408'}

    @distributed_trace_async
    async def put500(
        self,
        *,
        content_type: Optional[str] = None,
        **kwargs
    ) -> None:
        """Return 500 status code, then 200 after retry.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.put500.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        __body_content_kwargs = {}
        if header_parameters['Content-Type'] in ['application/json']:
            if boolean_value is not None:
                body_content = self._serialize.body(boolean_value, 'bool')
            else:
                body_content = None
            __body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **__body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put500.metadata = {'url': '/http/retry/500'}

    @distributed_trace_async
    async def patch500(
        self,
        *,
        content_type: Optional[str] = None,
        **kwargs
    ) -> None:
        """Return 500 status code, then 200 after retry.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.patch500.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        __body_content_kwargs = {}
        if header_parameters['Content-Type'] in ['application/json']:
            if boolean_value is not None:
                body_content = self._serialize.body(boolean_value, 'bool')
            else:
                body_content = None
            __body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **__body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    patch500.metadata = {'url': '/http/retry/500'}

    @distributed_trace_async
    async def get502(
        self,
        **kwargs
    ) -> None:
        """Return 502 status code, then 200 after retry.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get502.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    get502.metadata = {'url': '/http/retry/502'}

    @distributed_trace_async
    async def options502(
        self,
        **kwargs
    ) -> bool:
        """Return 502 status code, then 200 after retry.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[bool] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.options502.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.options(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('bool', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    options502.metadata = {'url': '/http/retry/502'}

    @distributed_trace_async
    async def post503(
        self,
        *,
        content_type: Optional[str] = None,
        **kwargs
    ) -> None:
        """Return 503 status code, then 200 after retry.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.post503.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        __body_content_kwargs = {}
        if header_parameters['Content-Type'] in ['application/json']:
            if boolean_value is not None:
                body_content = self._serialize.body(boolean_value, 'bool')
            else:
                body_content = None
            __body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **__body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    post503.metadata = {'url': '/http/retry/503'}

    @distributed_trace_async
    async def delete503(
        self,
        *,
        content_type: Optional[str] = None,
        **kwargs
    ) -> None:
        """Return 503 status code, then 200 after retry.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.delete503.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        __body_content_kwargs = {}
        if header_parameters['Content-Type'] in ['application/json']:
            if boolean_value is not None:
                body_content = self._serialize.body(boolean_value, 'bool')
            else:
                body_content = None
            __body_content_kwargs['content'] = body_content
        request = self._client.delete(url, query_parameters, header_parameters, **__body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    delete503.metadata = {'url': '/http/retry/503'}

    @distributed_trace_async
    async def put504(
        self,
        *,
        content_type: Optional[str] = None,
        **kwargs
    ) -> None:
        """Return 504 status code, then 200 after retry.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.put504.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        __body_content_kwargs = {}
        if header_parameters['Content-Type'] in ['application/json']:
            if boolean_value is not None:
                body_content = self._serialize.body(boolean_value, 'bool')
            else:
                body_content = None
            __body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **__body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put504.metadata = {'url': '/http/retry/504'}

    @distributed_trace_async
    async def patch504(
        self,
        *,
        content_type: Optional[str] = None,
        **kwargs
    ) -> None:
        """Return 504 status code, then 200 after retry.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.patch504.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        __body_content_kwargs = {}
        if header_parameters['Content-Type'] in ['application/json']:
            if boolean_value is not None:
                body_content = self._serialize.body(boolean_value, 'bool')
            else:
                body_content = None
            __body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **__body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    patch504.metadata = {'url': '/http/retry/504'}
