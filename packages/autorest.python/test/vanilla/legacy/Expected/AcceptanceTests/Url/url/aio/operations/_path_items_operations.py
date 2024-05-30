# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Optional, Type, TypeVar

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

from ... import models as _models
from ...operations._path_items_operations import (
    build_get_all_with_values_request,
    build_get_global_and_local_query_null_request,
    build_get_global_query_null_request,
    build_get_local_path_item_query_null_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PathItemsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~url.aio.AutoRestUrlTestService`'s
        :attr:`path_items` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_all_with_values(  # pylint: disable=inconsistent-return-statements
        self,
        path_item_string_path: str,
        local_string_path: str,
        path_item_string_query: Optional[str] = None,
        local_string_query: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery='globalStringQuery',
        pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
         Required.
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'. Required.
        :type local_string_path: str
        :param path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
         parameter. Default value is None.
        :type path_item_string_query: str
        :param local_string_query: should contain value 'localStringQuery'. Default value is None.
        :type local_string_query: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_get_all_with_values_request(
            path_item_string_path=path_item_string_path,
            local_string_path=local_string_path,
            global_string_path=self._config.global_string_path,
            path_item_string_query=path_item_string_query,
            local_string_query=local_string_query,
            global_string_query=self._config.global_string_query,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def get_global_query_null(  # pylint: disable=inconsistent-return-statements
        self,
        path_item_string_path: str,
        local_string_path: str,
        path_item_string_query: Optional[str] = None,
        local_string_query: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery=null,
        pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
         Required.
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'. Required.
        :type local_string_path: str
        :param path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
         parameter. Default value is None.
        :type path_item_string_query: str
        :param local_string_query: should contain value 'localStringQuery'. Default value is None.
        :type local_string_query: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_get_global_query_null_request(
            path_item_string_path=path_item_string_path,
            local_string_path=local_string_path,
            global_string_path=self._config.global_string_path,
            path_item_string_query=path_item_string_query,
            local_string_query=local_string_query,
            global_string_query=self._config.global_string_query,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def get_global_and_local_query_null(  # pylint: disable=inconsistent-return-statements
        self,
        path_item_string_path: str,
        local_string_path: str,
        path_item_string_query: Optional[str] = None,
        local_string_query: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """send globalStringPath=globalStringPath, pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery=null,
        pathItemStringQuery='pathItemStringQuery', localStringQuery=null.

        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
         Required.
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'. Required.
        :type local_string_path: str
        :param path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
         parameter. Default value is None.
        :type path_item_string_query: str
        :param local_string_query: should contain null value. Default value is None.
        :type local_string_query: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_get_global_and_local_query_null_request(
            path_item_string_path=path_item_string_path,
            local_string_path=local_string_path,
            global_string_path=self._config.global_string_path,
            path_item_string_query=path_item_string_query,
            local_string_query=local_string_query,
            global_string_query=self._config.global_string_query,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def get_local_path_item_query_null(  # pylint: disable=inconsistent-return-statements
        self,
        path_item_string_path: str,
        local_string_path: str,
        path_item_string_query: Optional[str] = None,
        local_string_query: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery='globalStringQuery',
        pathItemStringQuery=null, localStringQuery=null.

        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
         Required.
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'. Required.
        :type local_string_path: str
        :param path_item_string_query: should contain value null. Default value is None.
        :type path_item_string_query: str
        :param local_string_query: should contain value null. Default value is None.
        :type local_string_query: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_get_local_path_item_query_null_request(
            path_item_string_path=path_item_string_path,
            local_string_path=local_string_path,
            global_string_path=self._config.global_string_path,
            path_item_string_query=path_item_string_query,
            local_string_query=local_string_query,
            global_string_query=self._config.global_string_query,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
