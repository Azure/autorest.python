# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterator, Callable, Dict, IO, List, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._formdata_operations import (
    build_upload_file_request,
    build_upload_file_via_body_request,
    build_upload_files_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class FormdataOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodyformdata.aio.AutoRestSwaggerBATFormDataService`'s
        :attr:`formdata` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def upload_file(self, file_content: IO, file_name: str, **kwargs: Any) -> AsyncIterator[bytes]:
        """Upload file.

        :param file_content: File to upload. Required.
        :type file_content: IO
        :param file_name: File name to upload. Name has to be spelled exactly as written here.
         Required.
        :type file_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Async iterator of the response bytes or the result of cls(response)
        :rtype: AsyncIterator[bytes]
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
        cls = kwargs.pop("cls", None)  # type: ClsType[AsyncIterator[bytes]]

        # Construct form data
        _files = {
            "fileContent": file_content,
            "fileName": file_name,
        }

        request = build_upload_file_request(
            content_type=content_type,
            files=_files,
            template_url=self.upload_file.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request, _files)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=True, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    upload_file.metadata = {"url": "/formdata/stream/uploadfile"}  # type: ignore

    @distributed_trace_async
    async def upload_file_via_body(self, file_content: IO, **kwargs: Any) -> AsyncIterator[bytes]:
        """Upload file.

        :param file_content: File to upload. Required.
        :type file_content: IO
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Async iterator of the response bytes or the result of cls(response)
        :rtype: AsyncIterator[bytes]
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
        cls = kwargs.pop("cls", None)  # type: ClsType[AsyncIterator[bytes]]

        _content = file_content

        request = build_upload_file_via_body_request(
            content_type=content_type,
            content=_content,
            template_url=self.upload_file_via_body.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=True, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    upload_file_via_body.metadata = {"url": "/formdata/stream/uploadfile"}  # type: ignore

    @distributed_trace_async
    async def upload_files(self, file_content: List[IO], **kwargs: Any) -> AsyncIterator[bytes]:
        """Upload multiple files.

        :param file_content: Files to upload. Required.
        :type file_content: list[IO]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Async iterator of the response bytes or the result of cls(response)
        :rtype: AsyncIterator[bytes]
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
        cls = kwargs.pop("cls", None)  # type: ClsType[AsyncIterator[bytes]]

        # Construct form data
        _files = {
            "fileContent": file_content,
        }

        request = build_upload_files_request(
            content_type=content_type,
            files=_files,
            template_url=self.upload_files.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request, _files)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=True, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    upload_files.metadata = {"url": "/formdata/stream/uploadfiles"}  # type: ignore
