# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

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

from .. import models as _models
from .._vendor import _convert_request

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, List, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_array_string_multi_null_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    array_query = kwargs.pop('array_query', None)  # type: Optional[List[str]]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/queries/array/multi/string/null")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if array_query is not None:
        _query_parameters['arrayQuery'] = [_SERIALIZER.query("array_query", q, 'str') if q is not None else '' for q in array_query]

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_array_string_multi_empty_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    array_query = kwargs.pop('array_query', None)  # type: Optional[List[str]]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/queries/array/multi/string/empty")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if array_query is not None:
        _query_parameters['arrayQuery'] = [_SERIALIZER.query("array_query", q, 'str') if q is not None else '' for q in array_query]

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_array_string_multi_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    array_query = kwargs.pop('array_query', None)  # type: Optional[List[str]]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/queries/array/multi/string/valid")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if array_query is not None:
        _query_parameters['arrayQuery'] = [_SERIALIZER.query("array_query", q, 'str') if q is not None else '' for q in array_query]

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class QueriesOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through :class:`~urlmulticollectionformat.AutoRestUrlMutliCollectionFormatTestService`'s
        :attr:`~urlmulticollectionformat.AutoRestUrlMutliCollectionFormatTestService.queries` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        self._client = kwargs.pop("client", args[0])
        self._config = kwargs.pop("config", args[1])
        self._serialize = kwargs.pop("serializer", args[2])
        self._deserialize = kwargs.pop("deserializer", args[3])

    @distributed_trace
    def array_string_multi_null(  # pylint: disable=inconsistent-return-statements
        self,
        array_query=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get a null array of string using the multi-array format.

        :param array_query: a null array of string using the multi-array format. Default value is None.
        :type array_query: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_array_string_multi_null_request(
            array_query=array_query,
            template_url=self.array_string_multi_null.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    array_string_multi_null.metadata = {"url": "/queries/array/multi/string/null"}  # type: ignore

    @distributed_trace
    def array_string_multi_empty(  # pylint: disable=inconsistent-return-statements
        self,
        array_query=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get an empty array [] of string using the multi-array format.

        :param array_query: an empty array [] of string using the multi-array format. Default value is
         None.
        :type array_query: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_array_string_multi_empty_request(
            array_query=array_query,
            template_url=self.array_string_multi_empty.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    array_string_multi_empty.metadata = {"url": "/queries/array/multi/string/empty"}  # type: ignore

    @distributed_trace
    def array_string_multi_valid(  # pylint: disable=inconsistent-return-statements
        self,
        array_query=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' , null, ''] using the
        mult-array format.

        :param array_query: an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' , null,
         ''] using the mult-array format. Default value is None.
        :type array_query: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_array_string_multi_valid_request(
            array_query=array_query,
            template_url=self.array_string_multi_valid.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    array_string_multi_valid.metadata = {"url": "/queries/array/multi/string/valid"}  # type: ignore
