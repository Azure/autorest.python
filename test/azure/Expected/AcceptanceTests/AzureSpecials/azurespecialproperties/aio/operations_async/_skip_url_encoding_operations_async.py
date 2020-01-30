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

def _cls_type_annotation(return_type):
    return Optional[Callable[[AsyncHttpResponse, return_type, Dict[str, Any]], Any]]


class SkipUrlEncodingOperations:
    """SkipUrlEncodingOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azurespecialproperties.models
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
    async def get_method_path_valid(
        self,
        unencoded_path_param: str,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Get method with unencoded path parameter with value 'path1/path2/path3'.

        FIXME: add operation.summary

        :param unencoded_path_param: Unencoded path parameter with value 'path1/path2/path3'.
        :type unencoded_path_param: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_method_path_valid.metadata['url']
        path_format_arguments = {
            'unencodedPathParam': self._serialize.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    get_method_path_valid.metadata = {'url': '/azurespecials/skipUrlEncoding/method/path/valid/{unencodedPathParam}'}

    @distributed_trace_async
    async def get_path_path_valid(
        self,
        unencoded_path_param: str,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Get method with unencoded path parameter with value 'path1/path2/path3'.

        FIXME: add operation.summary

        :param unencoded_path_param: Unencoded path parameter with value 'path1/path2/path3'.
        :type unencoded_path_param: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_path_path_valid.metadata['url']
        path_format_arguments = {
            'unencodedPathParam': self._serialize.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    get_path_path_valid.metadata = {'url': '/azurespecials/skipUrlEncoding/path/path/valid/{unencodedPathParam}'}

    @distributed_trace_async
    async def get_swagger_path_valid(
        self,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Get method with unencoded path parameter with value 'path1/path2/path3'.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        unencoded_path_param = "path1/path2/path3"

        # Construct URL
        url = self.get_swagger_path_valid.metadata['url']
        path_format_arguments = {
            'unencodedPathParam': self._serialize.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    get_swagger_path_valid.metadata = {'url': '/azurespecials/skipUrlEncoding/swagger/path/valid/{unencodedPathParam}'}

    @distributed_trace_async
    async def get_method_query_valid(
        self,
        q1: str,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

        FIXME: add operation.summary

        :param q1: Unencoded query parameter with value 'value1&q2=value2&q3=value3'.
        :type q1: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_method_query_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['q1'] = self._serialize.query("q1", q1, 'str', skip_quote=True)


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    get_method_query_valid.metadata = {'url': '/azurespecials/skipUrlEncoding/method/query/valid'}

    @distributed_trace_async
    async def get_method_query_null(
        self,
        q1: Optional[str] = None,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Get method with unencoded query parameter with value null.

        FIXME: add operation.summary

        :param q1: Unencoded query parameter with value null.
        :type q1: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_method_query_null.metadata['url']

        # Construct parameters
        query_parameters = {}
        if q1 is not None:
            query_parameters['q1'] = self._serialize.query("q1", q1, 'str', skip_quote=True)


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    get_method_query_null.metadata = {'url': '/azurespecials/skipUrlEncoding/method/query/null'}

    @distributed_trace_async
    async def get_path_query_valid(
        self,
        q1: str,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

        FIXME: add operation.summary

        :param q1: Unencoded query parameter with value 'value1&q2=value2&q3=value3'.
        :type q1: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_path_query_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['q1'] = self._serialize.query("q1", q1, 'str', skip_quote=True)


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    get_path_query_valid.metadata = {'url': '/azurespecials/skipUrlEncoding/path/query/valid'}

    @distributed_trace_async
    async def get_swagger_query_valid(
        self,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        q1 = "value1&q2=value2&q3=value3"

        # Construct URL
        url = self.get_swagger_query_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['q1'] = self._serialize.query("q1", q1, 'str', skip_quote=True)


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    get_swagger_query_valid.metadata = {'url': '/azurespecials/skipUrlEncoding/swagger/query/valid'}
