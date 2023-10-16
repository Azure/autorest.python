# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar, cast

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
from .._vendor import ReservedWordsClientMixinABC, raise_if_not_implemented

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_import_operations_operation_one_request(  # pylint: disable=name-too-long
    *, parameter1: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/operationGroup/import"

    # Construct parameters
    _params["parameter1"] = _SERIALIZER.query("parameter1", parameter1, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_reserved_words_operation_with_content_param_request(  # pylint: disable=name-too-long
    *, content: IO, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/operation/content"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, content=content, **kwargs)


def build_reserved_words_operation_with_json_param_request(  # pylint: disable=name-too-long
    *, json: Any, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/operation/json"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, json=json, **kwargs)


def build_reserved_words_operation_with_url_request(  # pylint: disable=name-too-long
    url: str, *, header_parameters: str, query_parameters: Optional[List[str]] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/{url}"
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if query_parameters is not None:
        _params["queryParameters"] = [
            _SERIALIZER.query("query_parameters", q, "str") if q is not None else "" for q in query_parameters
        ]

    # Construct headers
    _headers["headerParameters"] = _SERIALIZER.header("header_parameters", header_parameters, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_reserved_words_reserved_enum_request(  # pylint: disable=name-too-long
    *, enum_parameter: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/reservedWords/enum"

    # Construct headers
    _headers["enumParameter"] = _SERIALIZER.header("enum_parameter", enum_parameter, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


class ImportOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~reservedwordsversiontolerant.ReservedWordsClient`'s
        :attr:`import_operations` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def operation_one(self, *, parameter1: str, **kwargs: Any) -> JSON:
        """Operation in operation group import, a reserved word.

        :keyword parameter1: Pass in 'foo' to pass this test. Required.
        :paramtype parameter1: str
        :return: JSON
        :rtype: JSON
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

        cls: ClsType[JSON] = kwargs.pop("cls", None)

        request = build_import_operations_operation_one_request(
            parameter1=parameter1,
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

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore


class ReservedWordsClientOperationsMixin(ReservedWordsClientMixinABC):  # pylint: disable=abstract-class-instantiated
    def __init__(self):
        raise_if_not_implemented(
            self.__class__,
            [
                "operation_with_data_param",
                "operation_with_files_param",
            ],
        )

    @distributed_trace
    def operation_with_content_param(self, content: IO, **kwargs: Any) -> JSON:
        """Operation with body param called content. Pass in b'hello, world'.

        :param content: Pass in b'hello, world'. Required.
        :type content: IO
        :return: JSON
        :rtype: JSON
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

        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/octet-stream"))
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        _content = content

        request = build_reserved_words_operation_with_content_param_request(
            content_type=content_type,
            content=_content,
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

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore

    @distributed_trace
    def operation_with_json_param(self, json: Any, **kwargs: Any) -> JSON:
        """Operation with body param called 'json'. Pass in {'hello': 'world'}.

        :param json: Pass in {'hello': 'world'}. Required.
        :type json: any
        :return: JSON
        :rtype: JSON
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
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        _json = json

        request = build_reserved_words_operation_with_json_param_request(
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

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore

    @distributed_trace
    def operation_with_url(
        self, url: str, *, header_parameters: str, query_parameters: Optional[List[str]] = None, **kwargs: Any
    ) -> JSON:
        """Operation with path format argument URL, header param headerParameters, and query param
        queryParameters.

        :param url: Pass in 'foo'. Required.
        :type url: str
        :keyword header_parameters: Header arg that uses same name as headerParameters in generated
         code. Pass in 'x-ms-header' to pass. Required.
        :paramtype header_parameters: str
        :keyword query_parameters: Query args that uses same name as queryParameters in generated code.
         Pass in ['one', 'two'] to pass test. Default value is None.
        :paramtype query_parameters: list[str]
        :return: JSON
        :rtype: JSON
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

        cls: ClsType[JSON] = kwargs.pop("cls", None)

        request = build_reserved_words_operation_with_url_request(
            url=url,
            header_parameters=header_parameters,
            query_parameters=query_parameters,
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

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore

    @distributed_trace
    def reserved_enum(self, *, enum_parameter: str, **kwargs: Any) -> JSON:
        """Operation that accepts a reserved enum value.

        :keyword enum_parameter: Pass in MyEnum.IMPORT to pass. Known values are: "import" and "other".
         Required.
        :paramtype enum_parameter: str
        :return: JSON
        :rtype: JSON
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

        cls: ClsType[JSON] = kwargs.pop("cls", None)

        request = build_reserved_words_reserved_enum_request(
            enum_parameter=enum_parameter,
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

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})  # type: ignore

        return cast(JSON, deserialized)  # type: ignore
