# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Iterator, Optional, TypeVar, cast

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

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_upload_file_request(*, content: IO[bytes], **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/binary/file"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, content=content, **kwargs)


def build_upload_binary_request(*, content: IO[bytes], **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/binary/octet"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, content=content, **kwargs)


def build_download_error_stream_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/octet-stream, application/json")

    # Construct URL
    _url = "/binary/error"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


class UploadOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodybinaryversiontolerant.BinaryWithContentTypeApplicationJson`'s
        :attr:`upload` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def file(self, file_param: IO[bytes], **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Uploading json file.

        :param file_param: JSON file with payload { "more": "cowbell" }. Required.
        :type file_param: IO[bytes]
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

        _content = file_param

        _request = build_upload_file_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
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
    def binary(self, file_param: IO[bytes], **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Uploading binary file.

        :param file_param: Non-empty binary file. Required.
        :type file_param: IO[bytes]
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

        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/octet-stream"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _content = file_param

        _request = build_upload_binary_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore


class DownloadOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodybinaryversiontolerant.BinaryWithContentTypeApplicationJson`'s
        :attr:`download` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def error_stream(self, **kwargs: Any) -> Iterator[bytes]:
        """Get binary error stream.

        :return: Iterator of the response bytes
        :rtype: Iterator[bytes]
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

        cls: ClsType[Iterator[bytes]] = kwargs.pop("cls", None)

        _request = build_download_error_stream_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = True
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, cast(Iterator[bytes], deserialized), {})  # type: ignore

        return cast(Iterator[bytes], deserialized)  # type: ignore
