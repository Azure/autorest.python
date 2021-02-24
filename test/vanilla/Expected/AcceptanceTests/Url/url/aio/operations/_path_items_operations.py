# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PathItemsOperations:
    """PathItemsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~url.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _get_all_with_values_request(
        self,
        path_item_string_path,  # type: str
        local_string_path,  # type: str
        path_item_string_query=None,  # type: Optional[str]
        local_string_query=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop(
            "template_url",
            "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/pathItemStringQuery/localStringQuery",
        )
        path_format_arguments = {
            "pathItemStringPath": self._serialize.url("path_item_string_path", path_item_string_path, "str"),
            "globalStringPath": self._serialize.url(
                "self._config.global_string_path", self._config.global_string_path, "str"
            ),
            "localStringPath": self._serialize.url("local_string_path", local_string_path, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if path_item_string_query is not None:
            query_parameters["pathItemStringQuery"] = self._serialize.query(
                "path_item_string_query", path_item_string_query, "str"
            )
        if self._config.global_string_query is not None:
            query_parameters["globalStringQuery"] = self._serialize.query(
                "self._config.global_string_query", self._config.global_string_query, "str"
            )
        if local_string_query is not None:
            query_parameters["localStringQuery"] = self._serialize.query(
                "local_string_query", local_string_query, "str"
            )

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace_async
    async def get_all_with_values(
        self,
        path_item_string_path: str,
        local_string_path: str,
        path_item_string_query: Optional[str] = None,
        local_string_query: Optional[str] = None,
        **kwargs
    ) -> None:
        """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery='globalStringQuery',
        pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'.
        :type local_string_path: str
        :param path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
         parameter.
        :type path_item_string_query: str
        :param local_string_query: should contain value 'localStringQuery'.
        :type local_string_query: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_all_with_values_request(
            path_item_string_path=path_item_string_path,
            local_string_path=local_string_path,
            path_item_string_query=path_item_string_query,
            local_string_query=local_string_query,
            template_url=self.get_all_with_values.metadata["url"],
            **kwargs
        )
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_all_with_values.metadata = {"url": "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/pathItemStringQuery/localStringQuery"}  # type: ignore

    def _get_global_query_null_request(
        self,
        path_item_string_path,  # type: str
        local_string_path,  # type: str
        path_item_string_query=None,  # type: Optional[str]
        local_string_query=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop(
            "template_url",
            "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/localStringQuery",
        )
        path_format_arguments = {
            "pathItemStringPath": self._serialize.url("path_item_string_path", path_item_string_path, "str"),
            "globalStringPath": self._serialize.url(
                "self._config.global_string_path", self._config.global_string_path, "str"
            ),
            "localStringPath": self._serialize.url("local_string_path", local_string_path, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if path_item_string_query is not None:
            query_parameters["pathItemStringQuery"] = self._serialize.query(
                "path_item_string_query", path_item_string_query, "str"
            )
        if self._config.global_string_query is not None:
            query_parameters["globalStringQuery"] = self._serialize.query(
                "self._config.global_string_query", self._config.global_string_query, "str"
            )
        if local_string_query is not None:
            query_parameters["localStringQuery"] = self._serialize.query(
                "local_string_query", local_string_query, "str"
            )

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace_async
    async def get_global_query_null(
        self,
        path_item_string_path: str,
        local_string_path: str,
        path_item_string_query: Optional[str] = None,
        local_string_query: Optional[str] = None,
        **kwargs
    ) -> None:
        """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery=null,
        pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'.
        :type local_string_path: str
        :param path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
         parameter.
        :type path_item_string_query: str
        :param local_string_query: should contain value 'localStringQuery'.
        :type local_string_query: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_global_query_null_request(
            path_item_string_path=path_item_string_path,
            local_string_path=local_string_path,
            path_item_string_query=path_item_string_query,
            local_string_query=local_string_query,
            template_url=self.get_global_query_null.metadata["url"],
            **kwargs
        )
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_global_query_null.metadata = {"url": "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/localStringQuery"}  # type: ignore

    def _get_global_and_local_query_null_request(
        self,
        path_item_string_path,  # type: str
        local_string_path,  # type: str
        path_item_string_query=None,  # type: Optional[str]
        local_string_query=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop(
            "template_url",
            "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/null",
        )
        path_format_arguments = {
            "pathItemStringPath": self._serialize.url("path_item_string_path", path_item_string_path, "str"),
            "globalStringPath": self._serialize.url(
                "self._config.global_string_path", self._config.global_string_path, "str"
            ),
            "localStringPath": self._serialize.url("local_string_path", local_string_path, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if path_item_string_query is not None:
            query_parameters["pathItemStringQuery"] = self._serialize.query(
                "path_item_string_query", path_item_string_query, "str"
            )
        if self._config.global_string_query is not None:
            query_parameters["globalStringQuery"] = self._serialize.query(
                "self._config.global_string_query", self._config.global_string_query, "str"
            )
        if local_string_query is not None:
            query_parameters["localStringQuery"] = self._serialize.query(
                "local_string_query", local_string_query, "str"
            )

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace_async
    async def get_global_and_local_query_null(
        self,
        path_item_string_path: str,
        local_string_path: str,
        path_item_string_query: Optional[str] = None,
        local_string_query: Optional[str] = None,
        **kwargs
    ) -> None:
        """send globalStringPath=globalStringPath, pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery=null,
        pathItemStringQuery='pathItemStringQuery', localStringQuery=null.

        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'.
        :type local_string_path: str
        :param path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
         parameter.
        :type path_item_string_query: str
        :param local_string_query: should contain null value.
        :type local_string_query: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_global_and_local_query_null_request(
            path_item_string_path=path_item_string_path,
            local_string_path=local_string_path,
            path_item_string_query=path_item_string_query,
            local_string_query=local_string_query,
            template_url=self.get_global_and_local_query_null.metadata["url"],
            **kwargs
        )
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_global_and_local_query_null.metadata = {"url": "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/null"}  # type: ignore

    def _get_local_path_item_query_null_request(
        self,
        path_item_string_path,  # type: str
        local_string_path,  # type: str
        path_item_string_query=None,  # type: Optional[str]
        local_string_query=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = kwargs.pop(
            "template_url",
            "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/null/null",
        )
        path_format_arguments = {
            "pathItemStringPath": self._serialize.url("path_item_string_path", path_item_string_path, "str"),
            "globalStringPath": self._serialize.url(
                "self._config.global_string_path", self._config.global_string_path, "str"
            ),
            "localStringPath": self._serialize.url("local_string_path", local_string_path, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if path_item_string_query is not None:
            query_parameters["pathItemStringQuery"] = self._serialize.query(
                "path_item_string_query", path_item_string_query, "str"
            )
        if self._config.global_string_query is not None:
            query_parameters["globalStringQuery"] = self._serialize.query(
                "self._config.global_string_query", self._config.global_string_query, "str"
            )
        if local_string_query is not None:
            query_parameters["localStringQuery"] = self._serialize.query(
                "local_string_query", local_string_query, "str"
            )

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    @distributed_trace_async
    async def get_local_path_item_query_null(
        self,
        path_item_string_path: str,
        local_string_path: str,
        path_item_string_query: Optional[str] = None,
        local_string_query: Optional[str] = None,
        **kwargs
    ) -> None:
        """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery='globalStringQuery',
        pathItemStringQuery=null, localStringQuery=null.

        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'.
        :type local_string_path: str
        :param path_item_string_query: should contain value null.
        :type path_item_string_query: str
        :param local_string_query: should contain value null.
        :type local_string_query: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_local_path_item_query_null_request(
            path_item_string_path=path_item_string_path,
            local_string_path=local_string_path,
            path_item_string_query=path_item_string_query,
            local_string_query=local_string_query,
            template_url=self.get_local_path_item_query_null.metadata["url"],
            **kwargs
        )
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_local_path_item_query_null.metadata = {"url": "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/null/null"}  # type: ignore
