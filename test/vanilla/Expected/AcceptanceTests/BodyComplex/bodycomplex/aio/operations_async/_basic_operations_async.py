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
from msrest.serialization import Model

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class BasicOperations:
    """BasicOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodycomplex.models
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
    async def get_valid(
        self,
        cls: ClsType["Basic"] = None,
        **kwargs: Any
    ) -> "Basic":
        """Get complex type {id: 2, name: 'abc', color: 'YELLOW'}.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: Basic or the result of cls(response)
        :rtype: ~bodycomplex.models.Basic
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('Basic', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_valid.metadata = {'url': '/complex/basic/valid'}

    @distributed_trace_async
    async def put_valid(
        self,
        complex_body: "Basic",
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Please put {id: 2, name: 'abc', color: 'Magenta'}.

        FIXME: add operation.summary

        :param complex_body: Please put {id: 2, name: 'abc', color: 'Magenta'}
        :type complex_body: ~bodycomplex.models.Basic
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "2016-02-29"

        # Construct URL
        url = self.put_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(complex_body, 'Basic')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_valid.metadata = {'url': '/complex/basic/valid'}

    @distributed_trace_async
    async def get_invalid(
        self,
        cls: ClsType["Basic"] = None,
        **kwargs: Any
    ) -> "Basic":
        """Get a basic complex type that is invalid for the local strong type.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: Basic or the result of cls(response)
        :rtype: ~bodycomplex.models.Basic
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_invalid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('Basic', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_invalid.metadata = {'url': '/complex/basic/invalid'}

    @distributed_trace_async
    async def get_empty(
        self,
        cls: ClsType["Basic"] = None,
        **kwargs: Any
    ) -> "Basic":
        """Get a basic complex type that is empty.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: Basic or the result of cls(response)
        :rtype: ~bodycomplex.models.Basic
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_empty.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('Basic', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_empty.metadata = {'url': '/complex/basic/empty'}

    @distributed_trace_async
    async def get_null(
        self,
        cls: ClsType["Basic"] = None,
        **kwargs: Any
    ) -> "Basic":
        """Get a basic complex type whose properties are null.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: Basic or the result of cls(response)
        :rtype: ~bodycomplex.models.Basic
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_null.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('Basic', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_null.metadata = {'url': '/complex/basic/null'}

    @distributed_trace_async
    async def get_not_provided(
        self,
        cls: ClsType["Basic"] = None,
        **kwargs: Any
    ) -> "Basic":
        """Get a basic complex type while the server doesn't provide a response payload.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: Basic or the result of cls(response)
        :rtype: ~bodycomplex.models.Basic
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_not_provided.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('Basic', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_not_provided.metadata = {'url': '/complex/basic/notprovided'}
