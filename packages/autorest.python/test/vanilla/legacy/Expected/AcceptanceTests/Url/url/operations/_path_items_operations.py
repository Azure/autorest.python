# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, MutableMapping, Optional, Type, TypeVar

from msrest import Serializer

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._vendor import _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()


def build_get_all_with_values_request(
    path_item_string_path: str,
    local_string_path: str,
    global_string_path: str,
    *,
    path_item_string_query: Optional[str] = None,
    local_string_query: Optional[str] = None,
    global_string_query: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/pathItemStringQuery/localStringQuery",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, "str"),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, "str"),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if path_item_string_query is not None:
        _params["pathItemStringQuery"] = _SERIALIZER.query("path_item_string_query", path_item_string_query, "str")
    if global_string_query is not None:
        _params["globalStringQuery"] = _SERIALIZER.query("global_string_query", global_string_query, "str")
    if local_string_query is not None:
        _params["localStringQuery"] = _SERIALIZER.query("local_string_query", local_string_query, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_global_query_null_request(
    path_item_string_path: str,
    local_string_path: str,
    global_string_path: str,
    *,
    path_item_string_query: Optional[str] = None,
    local_string_query: Optional[str] = None,
    global_string_query: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/localStringQuery",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, "str"),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, "str"),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if path_item_string_query is not None:
        _params["pathItemStringQuery"] = _SERIALIZER.query("path_item_string_query", path_item_string_query, "str")
    if global_string_query is not None:
        _params["globalStringQuery"] = _SERIALIZER.query("global_string_query", global_string_query, "str")
    if local_string_query is not None:
        _params["localStringQuery"] = _SERIALIZER.query("local_string_query", local_string_query, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_global_and_local_query_null_request(  # pylint: disable=name-too-long
    path_item_string_path: str,
    local_string_path: str,
    global_string_path: str,
    *,
    path_item_string_query: Optional[str] = None,
    local_string_query: Optional[str] = None,
    global_string_query: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/null",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, "str"),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, "str"),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if path_item_string_query is not None:
        _params["pathItemStringQuery"] = _SERIALIZER.query("path_item_string_query", path_item_string_query, "str")
    if global_string_query is not None:
        _params["globalStringQuery"] = _SERIALIZER.query("global_string_query", global_string_query, "str")
    if local_string_query is not None:
        _params["localStringQuery"] = _SERIALIZER.query("local_string_query", local_string_query, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_local_path_item_query_null_request(  # pylint: disable=name-too-long
    path_item_string_path: str,
    local_string_path: str,
    global_string_path: str,
    *,
    path_item_string_query: Optional[str] = None,
    local_string_query: Optional[str] = None,
    global_string_query: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/null/null",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, "str"),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, "str"),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if path_item_string_query is not None:
        _params["pathItemStringQuery"] = _SERIALIZER.query("path_item_string_query", path_item_string_query, "str")
    if global_string_query is not None:
        _params["globalStringQuery"] = _SERIALIZER.query("global_string_query", global_string_query, "str")
    if local_string_query is not None:
        _params["localStringQuery"] = _SERIALIZER.query("local_string_query", local_string_query, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class PathItemsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~url.AutoRestUrlTestService`'s
        :attr:`path_items` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_all_with_values(  # pylint: disable=inconsistent-return-statements
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def get_global_query_null(  # pylint: disable=inconsistent-return-statements
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def get_global_and_local_query_null(  # pylint: disable=inconsistent-return-statements
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def get_local_path_item_query_null(  # pylint: disable=inconsistent-return-statements
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
