# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_get_all_with_values_request(
    path_item_string_path,  # type: str
    global_string_path,  # type: str
    local_string_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    path_item_string_query = kwargs.pop('path_item_string_query', None)  # type: Optional[str]
    global_string_query = kwargs.pop('global_string_query', None)  # type: Optional[str]
    local_string_query = kwargs.pop('local_string_query', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/pathItemStringQuery/localStringQuery')
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, 'str'),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, 'str'),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if path_item_string_query is not None:
        query_parameters['pathItemStringQuery'] = _SERIALIZER.query("path_item_string_query", path_item_string_query, 'str')
    if global_string_query is not None:
        query_parameters['globalStringQuery'] = _SERIALIZER.query("global_string_query", global_string_query, 'str')
    if local_string_query is not None:
        query_parameters['localStringQuery'] = _SERIALIZER.query("local_string_query", local_string_query, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_global_query_null_request(
    path_item_string_path,  # type: str
    global_string_path,  # type: str
    local_string_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    path_item_string_query = kwargs.pop('path_item_string_query', None)  # type: Optional[str]
    global_string_query = kwargs.pop('global_string_query', None)  # type: Optional[str]
    local_string_query = kwargs.pop('local_string_query', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/localStringQuery')
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, 'str'),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, 'str'),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if path_item_string_query is not None:
        query_parameters['pathItemStringQuery'] = _SERIALIZER.query("path_item_string_query", path_item_string_query, 'str')
    if global_string_query is not None:
        query_parameters['globalStringQuery'] = _SERIALIZER.query("global_string_query", global_string_query, 'str')
    if local_string_query is not None:
        query_parameters['localStringQuery'] = _SERIALIZER.query("local_string_query", local_string_query, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_global_and_local_query_null_request(
    path_item_string_path,  # type: str
    global_string_path,  # type: str
    local_string_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    path_item_string_query = kwargs.pop('path_item_string_query', None)  # type: Optional[str]
    global_string_query = kwargs.pop('global_string_query', None)  # type: Optional[str]
    local_string_query = kwargs.pop('local_string_query', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/null')
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, 'str'),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, 'str'),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if path_item_string_query is not None:
        query_parameters['pathItemStringQuery'] = _SERIALIZER.query("path_item_string_query", path_item_string_query, 'str')
    if global_string_query is not None:
        query_parameters['globalStringQuery'] = _SERIALIZER.query("global_string_query", global_string_query, 'str')
    if local_string_query is not None:
        query_parameters['localStringQuery'] = _SERIALIZER.query("local_string_query", local_string_query, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_local_path_item_query_null_request(
    path_item_string_path,  # type: str
    global_string_path,  # type: str
    local_string_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    path_item_string_query = kwargs.pop('path_item_string_query', None)  # type: Optional[str]
    global_string_query = kwargs.pop('global_string_query', None)  # type: Optional[str]
    local_string_query = kwargs.pop('local_string_query', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/null/null')
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, 'str'),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, 'str'),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if path_item_string_query is not None:
        query_parameters['pathItemStringQuery'] = _SERIALIZER.query("path_item_string_query", path_item_string_query, 'str')
    if global_string_query is not None:
        query_parameters['globalStringQuery'] = _SERIALIZER.query("global_string_query", global_string_query, 'str')
    if local_string_query is not None:
        query_parameters['localStringQuery'] = _SERIALIZER.query("local_string_query", local_string_query, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class PathItemsOperations(object):
    """PathItemsOperations operations.

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

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_all_with_values(
        self,
        path_item_string_path,  # type: str
        local_string_path,  # type: str
        path_item_string_query=None,  # type: Optional[str]
        local_string_query=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
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

        request = build_get_all_with_values_request(
            path_item_string_path=path_item_string_path,
            global_string_path=self._config.global_string_path,
            local_string_path=local_string_path,
            path_item_string_query=path_item_string_query,
            global_string_query=self._config.global_string_query,
            local_string_query=local_string_query,
            template_url=self.get_all_with_values.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_all_with_values.metadata = {"url": "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/pathItemStringQuery/localStringQuery"}  # type: ignore

    @distributed_trace
    def get_global_query_null(
        self,
        path_item_string_path,  # type: str
        local_string_path,  # type: str
        path_item_string_query=None,  # type: Optional[str]
        local_string_query=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
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

        request = build_get_global_query_null_request(
            path_item_string_path=path_item_string_path,
            global_string_path=self._config.global_string_path,
            local_string_path=local_string_path,
            path_item_string_query=path_item_string_query,
            global_string_query=self._config.global_string_query,
            local_string_query=local_string_query,
            template_url=self.get_global_query_null.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_global_query_null.metadata = {"url": "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/localStringQuery"}  # type: ignore

    @distributed_trace
    def get_global_and_local_query_null(
        self,
        path_item_string_path,  # type: str
        local_string_path,  # type: str
        path_item_string_query=None,  # type: Optional[str]
        local_string_query=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
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

        request = build_get_global_and_local_query_null_request(
            path_item_string_path=path_item_string_path,
            global_string_path=self._config.global_string_path,
            local_string_path=local_string_path,
            path_item_string_query=path_item_string_query,
            global_string_query=self._config.global_string_query,
            local_string_query=local_string_query,
            template_url=self.get_global_and_local_query_null.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_global_and_local_query_null.metadata = {"url": "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/null"}  # type: ignore

    @distributed_trace
    def get_local_path_item_query_null(
        self,
        path_item_string_path,  # type: str
        local_string_path,  # type: str
        path_item_string_query=None,  # type: Optional[str]
        local_string_query=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
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

        request = build_get_local_path_item_query_null_request(
            path_item_string_path=path_item_string_path,
            global_string_path=self._config.global_string_path,
            local_string_path=local_string_path,
            path_item_string_query=path_item_string_query,
            global_string_query=self._config.global_string_query,
            local_string_query=local_string_query,
            template_url=self.get_local_path_item_query_null.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_local_path_item_query_null.metadata = {"url": "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/null/null"}  # type: ignore
