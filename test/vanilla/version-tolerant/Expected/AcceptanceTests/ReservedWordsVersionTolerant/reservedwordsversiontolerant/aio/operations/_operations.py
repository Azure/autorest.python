# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, IO, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ...operations._operations import (
    build_import_builders_operation_one_request,
    build_operation_with_content_param_request,
    build_operation_with_data_param_request,
    build_operation_with_files_param_request,
    build_operation_with_json_param_request,
)

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ImportOperations:
    """ImportOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def operation_one(self, *, parameter1: str, **kwargs: Any) -> Any:
        """Operation in operation group import, a reserved word.

        :keyword parameter1: Pass in 'foo' to pass this test.
        :paramtype parameter1: str
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_import_builders_operation_one_request(
            parameter1=parameter1,
            template_url=self.operation_one.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    operation_one.metadata = {"url": "/reservedWords/operationGroup/import"}  # type: ignore


class ReservedWordsClientOperationsMixin:
    @distributed_trace_async
    async def operation_with_content_param(self, content: IO, **kwargs: Any) -> Any:
        """Operation with body param called content. Pass in b'hello, world'.

        :param content: Pass in b'hello, world'.
        :type content: IO
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/octet-stream")  # type: Optional[str]

        _content = content

        request = build_operation_with_content_param_request(
            content_type=content_type,
            content=_content,
            template_url=self.operation_with_content_param.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    operation_with_content_param.metadata = {"url": "/reservedWords/operation/content"}  # type: ignore

    @distributed_trace_async
    async def operation_with_json_param(self, json: Any, **kwargs: Any) -> Any:
        """Operation with body param called 'json'. Pass in {'hello': 'world'}.

        :param json: Pass in {'hello': 'world'}.
        :type json: any
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = json

        request = build_operation_with_json_param_request(
            content_type=content_type,
            json=_json,
            template_url=self.operation_with_json_param.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    operation_with_json_param.metadata = {"url": "/reservedWords/operation/json"}  # type: ignore

    @distributed_trace_async
    async def operation_with_data_param(self, data: Dict[str, Any], **kwargs: Any) -> Any:
        """Operation with urlencoded body param called 'data'.

        :param data: Form-encoded input for data. See the template in our example to find the input
         shape.
        :type data: dict[str, any]
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # form-encoded input template you can fill out and use as your `data` input.
                data = {
                    "data": "str",  # Pass in 'hello'.
                    "world": "str"  # Pass in 'world'.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/x-www-form-urlencoded")  # type: Optional[str]

        request = build_operation_with_data_param_request(
            content_type=content_type,
            data=data,
            template_url=self.operation_with_data_param.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    operation_with_data_param.metadata = {"url": "/reservedWords/operation/data"}  # type: ignore

    @distributed_trace_async
    async def operation_with_files_param(self, files: Dict[str, Any], **kwargs: Any) -> Any:
        """Operation with multipart body param called 'files'.

        :param files: Multipart input for files. See the template in our example to find the input
         shape.
        :type files: dict[str, any]
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # multipart input template you can fill out and use as your `files` input.
                files = {
                    "file_name": "str",  # File name to upload. Pass in 'my.txt'.
                    "files": b'bytes'  # Files to upload. Pass in list of input streams.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", None)  # type: Optional[str]

        request = build_operation_with_files_param_request(
            content_type=content_type,
            files=files,
            template_url=self.operation_with_files_param.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    operation_with_files_param.metadata = {"url": "/reservedWords/operation/files"}  # type: ignore
