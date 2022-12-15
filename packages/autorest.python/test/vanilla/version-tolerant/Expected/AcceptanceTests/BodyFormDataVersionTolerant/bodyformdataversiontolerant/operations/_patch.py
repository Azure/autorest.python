# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import Any, Dict, List, Iterator, cast, Union

from azure.core.tracing.decorator import distributed_trace
from azure.core.exceptions import (
    ClientAuthenticationError,
    ResourceExistsError,
    ResourceNotFoundError,
    HttpResponseError,
    map_error,
)
from azure.core.utils import case_insensitive_dict
from azure.core.rest import HttpRequest
from azure.core import PipelineClient, AsyncPipelineClient
from azure.core.pipeline import PipelineResponse

from ._operations import FormdataOperations as _FormdataOperations

ClientType = Union[PipelineClient, AsyncPipelineClient]


def _upload_file_request(files: Dict[str, Any], **kwargs: Any):
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = kwargs.pop("params", {}) or {}

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/octet-stream, application/json")

    if content_type is not None:
        _headers["Content-Type"] = content_type
    _headers["Accept"] = accept
    return HttpRequest(
        method="POST",
        url="/formdata/stream/uploadfile",
        headers=_headers,
        files=files,
        params=_params,
    )


def _upload_file_deserialize(pipeline_response, **kwargs):
    cls = kwargs.pop("cls", None)
    error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
    error_map.update(kwargs.pop("error_map", {}) or {})
    response = pipeline_response.http_response

    if response.status_code not in [200]:
        map_error(status_code=response.status_code, response=response, error_map=error_map)
        raise HttpResponseError(response=response)
    deserialized = response.iter_bytes()

    if cls:
        return cls(pipeline_response, cast(Iterator[bytes], deserialized), {})
    return cast(Iterator[bytes], deserialized)


def _upload_files_request(files: Dict[str, Any], **kwargs):
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/octet-stream, application/json")
    if content_type is not None:
        _headers["Content-Type"] = content_type
    _headers["Accept"] = accept

    return HttpRequest(
        method="POST",
        url="/formdata/stream/uploadfiles",
        headers=_headers,
        files=files,
        params=kwargs.pop("params", {}),
    )


def _upload_files_deserialize(pipeline_response, **kwargs):
    cls = kwargs.pop("cls", None)
    error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
    error_map.update(kwargs.pop("error_map", {}) or {})
    response = pipeline_response.http_response

    if response.status_code not in [200]:
        map_error(status_code=response.status_code, response=response, error_map=error_map)
        raise HttpResponseError(response=response)
    deserialized = response.iter_bytes()

    if cls:
        return cls(pipeline_response, cast(Iterator[bytes], deserialized), {})
    return cast(Iterator[bytes], deserialized)


class FormdataOperations(_FormdataOperations):
    def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs) -> PipelineResponse:
        kwargs.pop("cls", None)
        request.url = self._client.format_url(request.url)
        return self._client._pipeline.run(request, stream=stream, **kwargs)  # pylint: disable=protected-access

    @distributed_trace
    def upload_file(self, files: Dict[str, Any], **kwargs: Any) -> Iterator[bytes]:
        """Upload file.

        :param files: Multipart input for files. See the template in our example to find the input
         shape.
        :type files: dict[str, any]
        :return: Iterator[bytes]
        :rtype: Iterator[bytes]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python
                # multipart input template you can fill out and use as your `files` input.
                files = {
                    "file_content": b'bytes',  # File to upload.
                    "file_name": "str"  # File name to upload. Name has to be spelled exactly as
                      written here.
                }
        """
        request = _upload_file_request(files=files, **kwargs)
        request.url = self._client.format_url(request.url)
        return _upload_file_deserialize(self._send_request(request, stream=True, **kwargs), **kwargs)

    @distributed_trace
    def upload_files(self, files: Dict[str, Any], **kwargs: Any) -> Iterator[bytes]:
        """Upload multiple files.

        :param files: Multipart input for files. See the template in our example to find the input
         shape.
        :type files: dict[str, any]
        :return: Iterator[bytes]
        :rtype: Iterator[bytes]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python
                # multipart input template you can fill out and use as your `files` input.
                files = {
                    "file_content": [
                        b'bytes'  # Files to upload.
                    ]
                }
        """
        request = _upload_files_request(files=files, **kwargs)
        request.url = self._client.format_url(request.url)
        return _upload_files_deserialize(self._send_request(request, stream=True, **kwargs), **kwargs)


__all__: List[str] = [
    "FormdataOperations"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
