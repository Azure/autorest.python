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
        parameter_grouping_post_required_parameters: "models.ParameterGroupingPostRequiredParameters",
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Post a bunch of required parameters grouped.

        :param parameter_grouping_post_required_parameters: Parameter group.
        :type parameter_grouping_post_required_parameters: ~azureparametergrouping.models.ParameterGroupingPostRequiredParameters
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azureparametergrouping.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        
        custom_header = None
        query = None
        path = None
        body = None
        if parameter_grouping_post_required_parameters is not None:
            custom_header = parameter_grouping_post_required_parameters.custom_header
            query = parameter_grouping_post_required_parameters.query
            path = parameter_grouping_post_required_parameters.path
            body = parameter_grouping_post_required_parameters.body

        # Construct URL
        url = self.post_required.metadata['url']
        path_format_arguments = {
            'path': self._serialize.url("path", path, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        if query is not None:
            query_parameters['query'] = self._serialize.query("query", query, 'int')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
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
          return cls(pipeline_response, None, {})

    post_required.metadata = {'url': '/parameterGrouping/postRequired/{path}'}

    @distributed_trace_async
    async def post_optional(
        self,
        parameter_grouping_post_optional_parameters: Optional["models.ParameterGroupingPostOptionalParameters"] = None,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Post a bunch of optional parameters grouped.

        :param parameter_grouping_post_optional_parameters: Parameter group.
        :type parameter_grouping_post_optional_parameters: ~azureparametergrouping.models.ParameterGroupingPostOptionalParameters
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azureparametergrouping.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        
        custom_header = None
        query = None
        if parameter_grouping_post_optional_parameters is not None:
            custom_header = parameter_grouping_post_optional_parameters.custom_header
            query = parameter_grouping_post_optional_parameters.query

        # Construct URL
        url = self.post_optional.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        if query is not None:
            query_parameters['query'] = self._serialize.query("query", query, 'int')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
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
          return cls(pipeline_response, None, {})

    post_optional.metadata = {'url': '/parameterGrouping/postOptional'}

    @distributed_trace_async
    async def post_multi_param_groups(
        self,
        first_parameter_group: Optional["models.FirstParameterGroup"] = None,
        parameter_grouping_post_multi_param_groups_second_param_group: Optional["models.ParameterGroupingPostMultiParamGroupsSecondParamGroup"] = None,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Post parameters from multiple different parameter groups.

        :param first_parameter_group: Parameter group.
        :type first_parameter_group: ~azureparametergrouping.models.FirstParameterGroup
        :param parameter_grouping_post_multi_param_groups_second_param_group: Parameter group.
        :type parameter_grouping_post_multi_param_groups_second_param_group: ~azureparametergrouping.models.ParameterGroupingPostMultiParamGroupsSecondParamGroup
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azureparametergrouping.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        
        header_one = None
        query_one = None
        header_two = None
        query_two = None
        if first_parameter_group is not None:
            header_one = first_parameter_group.header_one
            query_one = first_parameter_group.query_one
        if parameter_grouping_post_multi_param_groups_second_param_group is not None:
            header_two = parameter_grouping_post_multi_param_groups_second_param_group.header_two
            query_two = parameter_grouping_post_multi_param_groups_second_param_group.query_two

        # Construct URL
        url = self.post_multi_param_groups.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        if query_one is not None:
            query_parameters['query-one'] = self._serialize.query("query_one", query_one, 'int')
        if query_two is not None:
            query_parameters['query-two'] = self._serialize.query("query_two", query_two, 'int')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
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
          return cls(pipeline_response, None, {})

    post_multi_param_groups.metadata = {'url': '/parameterGrouping/postMultipleParameterGroups'}

    @distributed_trace_async
    async def post_shared_parameter_group_object(
        self,
        first_parameter_group: Optional["models.FirstParameterGroup"] = None,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Post parameters with a shared parameter group object.

        :param first_parameter_group: Parameter group.
        :type first_parameter_group: ~azureparametergrouping.models.FirstParameterGroup
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azureparametergrouping.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        
        header_one = None
        query_one = None
        if first_parameter_group is not None:
            header_one = first_parameter_group.header_one
            query_one = first_parameter_group.query_one

        # Construct URL
        url = self.post_shared_parameter_group_object.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        if query_one is not None:
            query_parameters['query-one'] = self._serialize.query("query_one", query_one, 'int')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
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
          return cls(pipeline_response, None, {})

    post_shared_parameter_group_object.metadata = {'url': '/parameterGrouping/sharedParameterGroupObject'}
