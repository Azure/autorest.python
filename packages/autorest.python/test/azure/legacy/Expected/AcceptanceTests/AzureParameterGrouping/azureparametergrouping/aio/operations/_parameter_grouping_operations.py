# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
from typing import Any, Callable, Dict, Optional, TypeVar

from msrest import Deserializer, Serializer

from azure.core import AsyncPipelineClient
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ...operations._parameter_grouping_operations import (
    build_group_with_constant_request,
    build_post_multi_param_groups_request,
    build_post_optional_request,
    build_post_required_request,
    build_post_reserved_words_request,
    build_post_shared_parameter_group_object_request,
)
from .._configuration import AutoRestParameterGroupingTestServiceConfiguration

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ParameterGroupingOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azureparametergrouping.aio.AutoRestParameterGroupingTestService`'s
        :attr:`parameter_grouping` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: AutoRestParameterGroupingTestServiceConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def post_required(
        self,
        parameter_grouping_post_required_parameters: _models.ParameterGroupingPostRequiredParameters,
        **kwargs: Any
    ) -> None:
        """Post a bunch of required parameters grouped.

        :param parameter_grouping_post_required_parameters: Parameter group. Required.
        :type parameter_grouping_post_required_parameters:
         ~azureparametergrouping.models.ParameterGroupingPostRequiredParameters
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _custom_header = None
        _query = None
        _path = None
        _body = None
        if parameter_grouping_post_required_parameters is not None:
            _body = parameter_grouping_post_required_parameters.body
            _custom_header = parameter_grouping_post_required_parameters.custom_header
            _path = parameter_grouping_post_required_parameters.path
            _query = parameter_grouping_post_required_parameters.query
        _json = self._serialize.body(_body, "int")

        _request = build_post_required_request(
            path=_path,
            custom_header=_custom_header,
            query=_query,
            content_type=content_type,
            json=_json,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def post_optional(
        self,
        parameter_grouping_post_optional_parameters: Optional[_models.ParameterGroupingPostOptionalParameters] = None,
        **kwargs: Any
    ) -> None:
        """Post a bunch of optional parameters grouped.

        :param parameter_grouping_post_optional_parameters: Parameter group. Default value is None.
        :type parameter_grouping_post_optional_parameters:
         ~azureparametergrouping.models.ParameterGroupingPostOptionalParameters
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _custom_header = None
        _query = None
        if parameter_grouping_post_optional_parameters is not None:
            _custom_header = parameter_grouping_post_optional_parameters.custom_header
            _query = parameter_grouping_post_optional_parameters.query

        _request = build_post_optional_request(
            custom_header=_custom_header,
            query=_query,  # type: ignore
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def post_reserved_words(
        self,
        parameter_grouping_post_reserved_words_parameters: Optional[
            _models.ParameterGroupingPostReservedWordsParameters
        ] = None,
        **kwargs: Any
    ) -> None:
        """Post a grouped parameters with reserved words.

        :param parameter_grouping_post_reserved_words_parameters: Parameter group. Default value is
         None.
        :type parameter_grouping_post_reserved_words_parameters:
         ~azureparametergrouping.models.ParameterGroupingPostReservedWordsParameters
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _from_parameter = None
        _accept_parameter = None
        if parameter_grouping_post_reserved_words_parameters is not None:
            _accept_parameter = parameter_grouping_post_reserved_words_parameters.accept
            _from_parameter = parameter_grouping_post_reserved_words_parameters.from_property

        _request = build_post_reserved_words_request(
            from_parameter=_from_parameter,
            accept_parameter=_accept_parameter,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def post_multi_param_groups(
        self,
        first_parameter_group: Optional[_models.FirstParameterGroup] = None,
        parameter_grouping_post_multi_param_groups_second_param_group: Optional[
            _models.ParameterGroupingPostMultiParamGroupsSecondParamGroup
        ] = None,
        **kwargs: Any
    ) -> None:
        """Post parameters from multiple different parameter groups.

        :param first_parameter_group: Parameter group. Default value is None.
        :type first_parameter_group: ~azureparametergrouping.models.FirstParameterGroup
        :param parameter_grouping_post_multi_param_groups_second_param_group: Parameter group. Default
         value is None.
        :type parameter_grouping_post_multi_param_groups_second_param_group:
         ~azureparametergrouping.models.ParameterGroupingPostMultiParamGroupsSecondParamGroup
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _header_one = None
        _query_one = None
        _header_two = None
        _query_two = None
        if first_parameter_group is not None:
            _header_one = first_parameter_group.header_one
            _query_one = first_parameter_group.query_one
        if parameter_grouping_post_multi_param_groups_second_param_group is not None:
            _header_two = parameter_grouping_post_multi_param_groups_second_param_group.header_two
            _query_two = parameter_grouping_post_multi_param_groups_second_param_group.query_two

        _request = build_post_multi_param_groups_request(
            header_one=_header_one,
            query_one=_query_one,  # type: ignore
            header_two=_header_two,
            query_two=_query_two,  # type: ignore
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def post_shared_parameter_group_object(
        self, first_parameter_group: Optional[_models.FirstParameterGroup] = None, **kwargs: Any
    ) -> None:
        """Post parameters with a shared parameter group object.

        :param first_parameter_group: Parameter group. Default value is None.
        :type first_parameter_group: ~azureparametergrouping.models.FirstParameterGroup
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _header_one = None
        _query_one = None
        if first_parameter_group is not None:
            _header_one = first_parameter_group.header_one
            _query_one = first_parameter_group.query_one

        _request = build_post_shared_parameter_group_object_request(
            header_one=_header_one,
            query_one=_query_one,  # type: ignore
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def group_with_constant(self, grouper: Optional[_models.Grouper] = None, **kwargs: Any) -> None:
        """Parameter group with a constant. Pass in 'foo' for groupedConstant and 'bar' for
        groupedParameter.

        :param grouper: Parameter group. Default value is None.
        :type grouper: ~azureparametergrouping.models.Grouper
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _grouped_constant = None
        _grouped_parameter = None
        if grouper is not None:
            _grouped_constant = grouper.grouped_constant
            _grouped_parameter = grouper.grouped_parameter

        _request = build_group_with_constant_request(
            grouped_constant=_grouped_constant,  # type: ignore
            grouped_parameter=_grouped_parameter,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
