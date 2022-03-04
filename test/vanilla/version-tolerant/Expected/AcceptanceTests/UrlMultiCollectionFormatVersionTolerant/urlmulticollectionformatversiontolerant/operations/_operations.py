# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_queries_array_string_multi_null_request(
    *, array_query: Optional[List[str]] = None, **kwargs: Any
) -> HttpRequest:
    accept = "application/json"
    # Construct URL
    _url = "/queries/array/multi/string/null"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if array_query is not None:
        _query_parameters["arrayQuery"] = [
            _SERIALIZER.query("array_query", q, "str") if q is not None else "" for q in array_query
        ]

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_query_parameters, headers=_header_parameters, **kwargs)


def build_queries_array_string_multi_empty_request(
    *, array_query: Optional[List[str]] = None, **kwargs: Any
) -> HttpRequest:
    accept = "application/json"
    # Construct URL
    _url = "/queries/array/multi/string/empty"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if array_query is not None:
        _query_parameters["arrayQuery"] = [
            _SERIALIZER.query("array_query", q, "str") if q is not None else "" for q in array_query
        ]

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_query_parameters, headers=_header_parameters, **kwargs)


def build_queries_array_string_multi_valid_request(
    *, array_query: Optional[List[str]] = None, **kwargs: Any
) -> HttpRequest:
    accept = "application/json"
    # Construct URL
    _url = "/queries/array/multi/string/valid"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if array_query is not None:
        _query_parameters["arrayQuery"] = [
            _SERIALIZER.query("array_query", q, "str") if q is not None else "" for q in array_query
        ]

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_query_parameters, headers=_header_parameters, **kwargs)


class QueriesOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through :class:`~urlmulticollectionformatversiontolerant.AutoRestUrlMutliCollectionFormatTestService`'s
        :attr:`~urlmulticollectionformatversiontolerant.AutoRestUrlMutliCollectionFormatTestService.queries` attribute.
    """

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def array_string_multi_null(  # pylint: disable=inconsistent-return-statements
        self, *, array_query: Optional[List[str]] = None, **kwargs: Any
    ) -> None:
        """Get a null array of string using the multi-array format.

        :keyword array_query: a null array of string using the multi-array format. Default value is
         None.
        :paramtype array_query: list[str]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_queries_array_string_multi_null_request(
            array_query=array_query,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def array_string_multi_empty(  # pylint: disable=inconsistent-return-statements
        self, *, array_query: Optional[List[str]] = None, **kwargs: Any
    ) -> None:
        """Get an empty array [] of string using the multi-array format.

        :keyword array_query: an empty array [] of string using the multi-array format. Default value
         is None.
        :paramtype array_query: list[str]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_queries_array_string_multi_empty_request(
            array_query=array_query,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def array_string_multi_valid(  # pylint: disable=inconsistent-return-statements
        self, *, array_query: Optional[List[str]] = None, **kwargs: Any
    ) -> None:
        """Get an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' , null, ''] using the
        mult-array format.

        :keyword array_query: an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' , null,
         ''] using the mult-array format. Default value is None.
        :paramtype array_query: list[str]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_queries_array_string_multi_valid_request(
            array_query=array_query,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
