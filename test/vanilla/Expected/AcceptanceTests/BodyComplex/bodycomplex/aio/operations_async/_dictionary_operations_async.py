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

class DictionaryOperations:
    """DictionaryOperations async operations.

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
        **kwargs
    ) -> "models.DictionaryWrapper":
        """Get complex types with dictionary property.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DictionaryWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.DictionaryWrapper
        :raises: ~bodycomplex.models.ErrorException:
        """
        cls: ClsType["models.DictionaryWrapper"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_valid.metadata['url']

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

        deserialized = self._deserialize('DictionaryWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_valid.metadata = {'url': '/complex/dictionary/typed/valid'}

    @distributed_trace_async
    async def put_valid(
        self,
        default_program: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> None:
        """Put complex types with dictionary property.

        :param default_program: Dictionary of :code:`<string>`.
        :type default_program: dict[str, str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodycomplex.models.ErrorException:
        """
        cls: ClsType[None] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        _complex_body = models.DictionaryWrapper(default_program=default_program)

        # Construct URL
        url = self.put_valid.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(_complex_body, 'DictionaryWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_valid.metadata = {'url': '/complex/dictionary/typed/valid'}

    @distributed_trace_async
    async def get_empty(
        self,
        **kwargs
    ) -> "models.DictionaryWrapper":
        """Get complex types with dictionary property which is empty.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DictionaryWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.DictionaryWrapper
        :raises: ~bodycomplex.models.ErrorException:
        """
        cls: ClsType["models.DictionaryWrapper"] = kwargs.pop('cls', None )
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

        deserialized = self._deserialize('DictionaryWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_empty.metadata = {'url': '/complex/dictionary/typed/empty'}

    @distributed_trace_async
    async def put_empty(
        self,
        default_program: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> None:
        """Put complex types with dictionary property which is empty.

        :param default_program: Dictionary of :code:`<string>`.
        :type default_program: dict[str, str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodycomplex.models.ErrorException:
        """
        cls: ClsType[None] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        _complex_body = models.DictionaryWrapper(default_program=default_program)

        # Construct URL
        url = self.put_empty.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(_complex_body, 'DictionaryWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_empty.metadata = {'url': '/complex/dictionary/typed/empty'}

    @distributed_trace_async
    async def get_null(
        self,
        **kwargs
    ) -> "models.DictionaryWrapper":
        """Get complex types with dictionary property which is null.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DictionaryWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.DictionaryWrapper
        :raises: ~bodycomplex.models.ErrorException:
        """
        cls: ClsType["models.DictionaryWrapper"] = kwargs.pop('cls', None )
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

        deserialized = self._deserialize('DictionaryWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_null.metadata = {'url': '/complex/dictionary/typed/null'}

    @distributed_trace_async
    async def get_not_provided(
        self,
        **kwargs
    ) -> "models.DictionaryWrapper":
        """Get complex types with dictionary property while server doesn't provide a response payload.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DictionaryWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.DictionaryWrapper
        :raises: ~bodycomplex.models.ErrorException:
        """
        cls: ClsType["models.DictionaryWrapper"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_not_provided.metadata['url']

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

        deserialized = self._deserialize('DictionaryWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_not_provided.metadata = {'url': '/complex/dictionary/typed/notprovided'}
