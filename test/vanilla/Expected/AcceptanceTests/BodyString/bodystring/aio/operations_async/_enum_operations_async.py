# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class EnumOperations:
    """EnumOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodystring.models
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
    async def get_not_expandable(
        self,
        **kwargs
    ) -> Union[str, "models.Colors"]:
        """Get enum value 'red color' from enumeration of 'red color', 'green-color', 'blue_color'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Colors or the result of cls(response)
        :rtype: str or ~bodystring.models.Colors
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[Union[str, "models.Colors"]] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_not_expandable.metadata['url']

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

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_not_expandable.metadata = {'url': '/string/enum/notExpandable'}

    @distributed_trace_async
    async def put_not_expandable(
        self,
        string_body: Union[str, "models.Colors"],
        **kwargs
    ) -> None:
        """Sends value 'red color' from enumeration of 'red color', 'green-color', 'blue_color'.

        :param string_body:
        :type string_body: str or ~bodystring.models.Colors
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_not_expandable.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        body_content_kwargs = {}
        body_content = self._serialize.body(string_body, 'str')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_not_expandable.metadata = {'url': '/string/enum/notExpandable'}

    @distributed_trace_async
    async def get_referenced(
        self,
        **kwargs
    ) -> Union[str, "models.Colors"]:
        """Get enum value 'red color' from enumeration of 'red color', 'green-color', 'blue_color'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Colors or the result of cls(response)
        :rtype: str or ~bodystring.models.Colors
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[Union[str, "models.Colors"]] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_referenced.metadata['url']

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

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_referenced.metadata = {'url': '/string/enum/Referenced'}

    @distributed_trace_async
    async def put_referenced(
        self,
        enum_string_body: Union[str, "models.Colors"],
        **kwargs
    ) -> None:
        """Sends value 'red color' from enumeration of 'red color', 'green-color', 'blue_color'.

        :param enum_string_body:
        :type enum_string_body: str or ~bodystring.models.Colors
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_referenced.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        body_content_kwargs = {}
        body_content = self._serialize.body(enum_string_body, 'str')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_referenced.metadata = {'url': '/string/enum/Referenced'}

    @distributed_trace_async
    async def get_referenced_constant(
        self,
        **kwargs
    ) -> "models.RefColorConstant":
        """Get value 'green-color' from the constant.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RefColorConstant or the result of cls(response)
        :rtype: ~bodystring.models.RefColorConstant
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType["models.RefColorConstant"] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_referenced_constant.metadata['url']

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

        deserialized = self._deserialize('RefColorConstant', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_referenced_constant.metadata = {'url': '/string/enum/ReferencedConstant'}

    @distributed_trace_async
    async def put_referenced_constant(
        self,
        field1: Optional[str] = None,
        **kwargs
    ) -> None:
        """Sends value 'green-color' from a constant.

        :param field1: Sample string.
        :type field1: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        _enum_string_body = models.RefColorConstant(field1=field1)

        # Construct URL
        url = self.put_referenced_constant.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        body_content_kwargs = {}
        body_content = self._serialize.body(_enum_string_body, 'RefColorConstant')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_referenced_constant.metadata = {'url': '/string/enum/ReferencedConstant'}
