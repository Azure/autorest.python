# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .._serialization import Serializer

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_parameter_grouping_post_required_request(  # pylint: disable=name-too-long
    path: str, *, json: int, custom_header: Optional[str] = None, query: int = 30, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/parameterGrouping/postRequired/{path}"
    path_format_arguments = {
        "path": _SERIALIZER.url("path", path, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if query is not None:
        _params["query"] = _SERIALIZER.query("query", query, "int")

    # Construct headers
    if custom_header is not None:
        _headers["customHeader"] = _SERIALIZER.header("custom_header", custom_header, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, json=json, **kwargs)


def build_parameter_grouping_post_optional_request(  # pylint: disable=name-too-long
    *, custom_header: Optional[str] = None, query: int = 30, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/parameterGrouping/postOptional"

    # Construct parameters
    if query is not None:
        _params["query"] = _SERIALIZER.query("query", query, "int")

    # Construct headers
    if custom_header is not None:
        _headers["customHeader"] = _SERIALIZER.header("custom_header", custom_header, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_parameter_grouping_post_reserved_words_request(  # pylint: disable=name-too-long
    *, from_parameter: Optional[str] = None, accept_parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/parameterGrouping/postReservedWords"

    # Construct parameters
    if from_parameter is not None:
        _params["from"] = _SERIALIZER.query("from_parameter", from_parameter, "str")
    if accept_parameter is not None:
        _params["accept"] = _SERIALIZER.query("accept_parameter", accept_parameter, "str")

    return HttpRequest(method="POST", url=_url, params=_params, **kwargs)


def build_parameter_grouping_post_multi_param_groups_request(  # pylint: disable=name-too-long
    *,
    header_one: Optional[str] = None,
    query_one: int = 30,
    header_two: Optional[str] = None,
    query_two: int = 30,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/parameterGrouping/postMultipleParameterGroups"

    # Construct parameters
    if query_one is not None:
        _params["query-one"] = _SERIALIZER.query("query_one", query_one, "int")
    if query_two is not None:
        _params["query-two"] = _SERIALIZER.query("query_two", query_two, "int")

    # Construct headers
    if header_one is not None:
        _headers["header-one"] = _SERIALIZER.header("header_one", header_one, "str")
    if header_two is not None:
        _headers["header-two"] = _SERIALIZER.header("header_two", header_two, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_parameter_grouping_post_shared_parameter_group_object_request(  # pylint: disable=name-too-long
    *, header_one: Optional[str] = None, query_one: int = 30, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/parameterGrouping/sharedParameterGroupObject"

    # Construct parameters
    if query_one is not None:
        _params["query-one"] = _SERIALIZER.query("query_one", query_one, "int")

    # Construct headers
    if header_one is not None:
        _headers["header-one"] = _SERIALIZER.header("header_one", header_one, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_parameter_grouping_group_with_constant_request(  # pylint: disable=name-too-long
    *, grouped_constant: Optional[Literal["foo"]] = None, grouped_parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/parameterGrouping/groupWithConstant"

    # Construct headers
    if grouped_constant is not None:
        _headers["groupedConstant"] = _SERIALIZER.header("grouped_constant", grouped_constant, "str")
    if grouped_parameter is not None:
        _headers["groupedParameter"] = _SERIALIZER.header("grouped_parameter", grouped_parameter, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


class ParameterGroupingOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azureparametergroupingversiontolerant.AutoRestParameterGroupingTestService`'s
        :attr:`parameter_grouping` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def post_required(  # pylint: disable=inconsistent-return-statements
        self, path: str, body: int, *, custom_header: Optional[str] = None, query: int = 30, **kwargs: Any
    ) -> None:
        """Post a bunch of required parameters grouped.

        :param path: Path parameter. Required.
        :type path: str
        :param body: Required.
        :type body: int
        :keyword custom_header: Default value is None.
        :paramtype custom_header: str
        :keyword query: Query parameter with default. Default value is 30.
        :paramtype query: int
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
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

        _json = body

        request = build_parameter_grouping_post_required_request(
            path=path,
            custom_header=custom_header,
            query=query,
            content_type=content_type,
            json=_json,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def post_optional(  # pylint: disable=inconsistent-return-statements
        self, *, custom_header: Optional[str] = None, query: int = 30, **kwargs: Any
    ) -> None:
        """Post a bunch of optional parameters grouped.

        :keyword custom_header: Default value is None.
        :paramtype custom_header: str
        :keyword query: Query parameter with default. Default value is 30.
        :paramtype query: int
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_parameter_grouping_post_optional_request(
            custom_header=custom_header,
            query=query,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def post_reserved_words(  # pylint: disable=inconsistent-return-statements
        self, *, from_parameter: Optional[str] = None, accept_parameter: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Post a grouped parameters with reserved words.

        :keyword from_parameter: 'from' is a reserved word. Pass in 'bob' to pass. Default value is
         None.
        :paramtype from_parameter: str
        :keyword accept_parameter: 'accept' is a reserved word. Pass in 'yes' to pass. Default value is
         None.
        :paramtype accept_parameter: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_parameter_grouping_post_reserved_words_request(
            from_parameter=from_parameter,
            accept_parameter=accept_parameter,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def post_multi_param_groups(  # pylint: disable=inconsistent-return-statements
        self,
        *,
        header_one: Optional[str] = None,
        query_one: int = 30,
        header_two: Optional[str] = None,
        query_two: int = 30,
        **kwargs: Any
    ) -> None:
        """Post parameters from multiple different parameter groups.

        :keyword header_one: Default value is None.
        :paramtype header_one: str
        :keyword query_one: Query parameter with default. Default value is 30.
        :paramtype query_one: int
        :keyword header_two: Default value is None.
        :paramtype header_two: str
        :keyword query_two: Query parameter with default. Default value is 30.
        :paramtype query_two: int
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_parameter_grouping_post_multi_param_groups_request(
            header_one=header_one,
            query_one=query_one,
            header_two=header_two,
            query_two=query_two,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def post_shared_parameter_group_object(  # pylint: disable=inconsistent-return-statements
        self, *, header_one: Optional[str] = None, query_one: int = 30, **kwargs: Any
    ) -> None:
        """Post parameters with a shared parameter group object.

        :keyword header_one: Default value is None.
        :paramtype header_one: str
        :keyword query_one: Query parameter with default. Default value is 30.
        :paramtype query_one: int
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_parameter_grouping_post_shared_parameter_group_object_request(
            header_one=header_one,
            query_one=query_one,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def group_with_constant(  # pylint: disable=inconsistent-return-statements
        self,
        *,
        grouped_constant: Optional[Literal["foo"]] = None,
        grouped_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Parameter group with a constant. Pass in 'foo' for groupedConstant and 'bar' for
        groupedParameter.

        :keyword grouped_constant: A grouped parameter that is a constant. Known values are "foo" and
         None. Default value is None.
        :paramtype grouped_constant: str
        :keyword grouped_parameter: Optional parameter part of a parameter grouping. Default value is
         None.
        :paramtype grouped_parameter: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_parameter_grouping_group_with_constant_request(
            grouped_constant=grouped_constant,
            grouped_parameter=grouped_parameter,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
