# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models


def _cls_type_annotation(return_type):
    return Optional[Callable[[AsyncHttpResponse, return_type, Dict[str, Any]], Any]]


class ParameterGroupingOperations:
    """ParameterGroupingOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azureparametergrouping.models
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
    async def post_required(
        self,
        path: str,
        body: int,
        custom_header: Optional[str] = None,
        query: Optional[int] = None,
        *,
        cls: _cls_type_annotation(None) = None,
        **kwargs: Any
    ) -> None:
        """Post a bunch of required parameters grouped.

        FIXME: add operation.summary

        :param path: Path parameter
        :type path: str
        :param body: 
        :type body: int
        :param custom_header: MISSING·PARAMETER-DESCRIPTION
        :type custom_header: str
        :param query: Query parameter with default
        :type query: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azureparametergrouping.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_required.metadata['url']
        path_format_arguments = {
            'path': self._serialize.url("path", path, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if query is not None:
            query_parameters['query'] = self._serialize.query("query", query, 'int')


        # Construct headers
        header_parameters = {}
        if custom_header is not None:
            header_parameters['customHeader'] = self._serialize.header("custom_header", custom_header, 'str')
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(body, 'int')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_required.metadata = {'url': '/parameterGrouping/postRequired/{path}'}

    @distributed_trace_async
    async def post_optional(
        self,
        custom_header: Optional[str] = None,
        query: Optional[int] = None,
        *,
        cls: _cls_type_annotation(None) = None,
        **kwargs: Any
    ) -> None:
        """Post a bunch of optional parameters grouped.

        FIXME: add operation.summary

        :param custom_header: MISSING·PARAMETER-DESCRIPTION
        :type custom_header: str
        :param query: Query parameter with default
        :type query: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azureparametergrouping.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_optional.metadata['url']

        # Construct parameters
        query_parameters = {}
        if query is not None:
            query_parameters['query'] = self._serialize.query("query", query, 'int')


        # Construct headers
        header_parameters = {}
        if custom_header is not None:
            header_parameters['customHeader'] = self._serialize.header("custom_header", custom_header, 'str')


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_optional.metadata = {'url': '/parameterGrouping/postOptional'}

    @distributed_trace_async
    async def post_multi_param_groups(
        self,
        header_one: Optional[str] = None,
        query_one: Optional[int] = None,
        header_two: Optional[str] = None,
        query_two: Optional[int] = None,
        *,
        cls: _cls_type_annotation(None) = None,
        **kwargs: Any
    ) -> None:
        """Post parameters from multiple different parameter groups.

        FIXME: add operation.summary

        :param header_one: MISSING·PARAMETER-DESCRIPTION
        :type header_one: str
        :param query_one: Query parameter with default
        :type query_one: int
        :param header_two: MISSING·PARAMETER-DESCRIPTION
        :type header_two: str
        :param query_two: Query parameter with default
        :type query_two: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azureparametergrouping.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_multi_param_groups.metadata['url']

        # Construct parameters
        query_parameters = {}
        if query_one is not None:
            query_parameters['query-one'] = self._serialize.query("query_one", query_one, 'int')
        if query_two is not None:
            query_parameters['query-two'] = self._serialize.query("query_two", query_two, 'int')


        # Construct headers
        header_parameters = {}
        if header_one is not None:
            header_parameters['header-one'] = self._serialize.header("header_one", header_one, 'str')
        if header_two is not None:
            header_parameters['header-two'] = self._serialize.header("header_two", header_two, 'str')


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_multi_param_groups.metadata = {'url': '/parameterGrouping/postMultipleParameterGroups'}

    @distributed_trace_async
    async def post_shared_parameter_group_object(
        self,
        header_one: Optional[str] = None,
        query_one: Optional[int] = None,
        *,
        cls: _cls_type_annotation(None) = None,
        **kwargs: Any
    ) -> None:
        """Post parameters with a shared parameter group object.

        FIXME: add operation.summary

        :param header_one: MISSING·PARAMETER-DESCRIPTION
        :type header_one: str
        :param query_one: Query parameter with default
        :type query_one: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azureparametergrouping.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_shared_parameter_group_object.metadata['url']

        # Construct parameters
        query_parameters = {}
        if query_one is not None:
            query_parameters['query-one'] = self._serialize.query("query_one", query_one, 'int')


        # Construct headers
        header_parameters = {}
        if header_one is not None:
            header_parameters['header-one'] = self._serialize.header("header_one", header_one, 'str')


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_shared_parameter_group_object.metadata = {'url': '/parameterGrouping/sharedParameterGroupObject'}
