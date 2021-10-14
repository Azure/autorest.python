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
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, IO, List, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_upload_file_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/octet-stream, application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/formdata/stream/uploadfile')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_upload_file_via_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/octet-stream, application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/formdata/stream/uploadfile')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_upload_files_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/octet-stream, application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/formdata/stream/uploadfiles')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class FormdataOperations(object):
    """FormdataOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodyformdata.models
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
    def upload_file(
        self,
        file_content,  # type: IO
        file_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """Upload file.

        :param file_content: File to upload.
        :type file_content: IO
        :param file_name: File name to upload. Name has to be spelled exactly as written here.
        :type file_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[IO]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", None)  # type: Optional[str]

        files = None
        data = None
        # Construct form data
        files = {
            "fileContent": file_content,
            "fileName": file_name,
        }
        _url = self._client.format_url(self.upload_file.metadata["url"])

        request = build_upload_file_request(
            content_type=content_type,
            files=files,
            data=data,
            template_url=_url,
        )
        request = _convert_request(request, files)

        pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs)
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

    @distributed_trace
    def upload_file_via_body(
        self,
        file_content,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """Upload file.

        :param file_content: File to upload.
        :type file_content: IO
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[IO]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/octet-stream")  # type: Optional[str]

        content = file_content
        _url = self._client.format_url(self.upload_file_via_body.metadata["url"])

        request = build_upload_file_via_body_request(
            content_type=content_type,
            content=content,
            template_url=_url,
        )
        request = _convert_request(request)

        pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs)
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

    @distributed_trace
    def upload_files(
        self,
        file_content,  # type: List[IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """Upload multiple files.

        :param file_content: Files to upload.
        :type file_content: list[IO]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[IO]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", None)  # type: Optional[str]

        files = None
        data = None
        # Construct form data
        files = {
            "fileContent": file_content,
        }
        _url = self._client.format_url(self.upload_files.metadata["url"])

        request = build_upload_files_request(
            content_type=content_type,
            files=files,
            data=data,
            template_url=_url,
        )
        request = _convert_request(request, files)

        pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs)
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
