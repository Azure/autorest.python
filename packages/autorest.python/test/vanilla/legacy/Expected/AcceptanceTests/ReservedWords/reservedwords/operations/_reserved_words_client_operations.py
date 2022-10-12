# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

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
from .._serialization import Serializer
from .._vendor import MixinABC, _convert_request, _format_url_section

JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_operation_with_content_param_request(*, content: IO, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/reservedWords/operation/content")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, content=content, **kwargs)


def build_operation_with_json_param_request(*, json: Any, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/reservedWords/operation/json")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, json=json, **kwargs)


def build_operation_with_data_param_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/reservedWords/operation/data")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_operation_with_files_param_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/reservedWords/operation/files")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_operation_with_url_request(
    url: str, *, header_parameters: str, query_parameters: Optional[List[str]] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/reservedWords/{url}")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if query_parameters is not None:
        _params["queryParameters"] = [
            _SERIALIZER.query("query_parameters", q, "str") if q is not None else "" for q in query_parameters
        ]

    # Construct headers
    _headers["headerParameters"] = _SERIALIZER.header("header_parameters", header_parameters, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class ReservedWordsClientOperationsMixin(MixinABC):
    @distributed_trace
    def operation_with_content_param(self, content: IO, **kwargs: Any) -> JSON:
        """Operation with body param called content. Pass in b'hello, world'.

        :param content: Pass in b'hello, world'. Required.
        :type content: IO
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON or the result of cls(response)
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

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/octet-stream"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        _content = content

        request = build_operation_with_content_param_request(
            content_type=content_type,
            content=_content,
            template_url=self.operation_with_content_param.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    operation_with_content_param.metadata = {"url": "/reservedWords/operation/content"}  # type: ignore

    @distributed_trace
    def operation_with_json_param(self, json: Any, **kwargs: Any) -> JSON:
        """Operation with body param called 'json'. Pass in {'hello': 'world'}.

        :param json: Pass in {'hello': 'world'}. Required.
        :type json: any
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON or the result of cls(response)
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

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        _json = self._serialize.body(json, "object")

        request = build_operation_with_json_param_request(
            content_type=content_type,
            json=_json,
            template_url=self.operation_with_json_param.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    operation_with_json_param.metadata = {"url": "/reservedWords/operation/json"}  # type: ignore

    @distributed_trace
    def operation_with_data_param(self, data: str, world: str, **kwargs: Any) -> JSON:
        """Operation with urlencoded body param called 'data'.

        :param data: Pass in 'hello'. Required.
        :type data: str
        :param world: Pass in 'world'. Required.
        :type world: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON or the result of cls(response)
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

        content_type = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/x-www-form-urlencoded")
        )  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        # Construct form data
        _data = {
            "data": data,
            "world": world,
        }

        request = build_operation_with_data_param_request(
            content_type=content_type,
            data=_data,
            template_url=self.operation_with_data_param.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    operation_with_data_param.metadata = {"url": "/reservedWords/operation/data"}  # type: ignore

    @distributed_trace
    def operation_with_files_param(self, files: IO, file_name: str, **kwargs: Any) -> JSON:
        """Operation with multipart body param called 'files'.

        :param files: Files to upload. Pass in list of input streams. Required.
        :type files: IO
        :param file_name: File name to upload. Pass in 'my.txt'. Required.
        :type file_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON or the result of cls(response)
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

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        # Construct form data
        _files = {
            "files": files,
            "fileName": file_name,
        }

        request = build_operation_with_files_param_request(
            content_type=content_type,
            files=_files,
            template_url=self.operation_with_files_param.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request, _files)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    operation_with_files_param.metadata = {"url": "/reservedWords/operation/files"}  # type: ignore

    @distributed_trace
    def operation_with_url(
        self, url: str, header_parameters: str, query_parameters: Optional[List[str]] = None, **kwargs: Any
    ) -> JSON:
        """Operation with path format argument URL, header param headerParameters, and query param
        queryParameters.

        :param url: Pass in 'foo'. Required.
        :type url: str
        :param header_parameters: Header arg that uses same name as headerParameters in generated code.
         Pass in 'x-ms-header' to pass. Required.
        :type header_parameters: str
        :param query_parameters: Query args that uses same name as queryParameters in generated code.
         Pass in ['one', 'two'] to pass test. Default value is None.
        :type query_parameters: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON or the result of cls(response)
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

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_operation_with_url_request(
            url=url,
            header_parameters=header_parameters,
            query_parameters=query_parameters,
            template_url=self.operation_with_url.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    operation_with_url.metadata = {"url": "/reservedWords/{url}"}  # type: ignore
