# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
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

from ..._vendor import _convert_request
from ...operations._object_type_client_operations import build_get_request, build_put_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ObjectTypeClientOperationsMixin:
    @distributed_trace_async
    async def get(self, **kwargs: Any) -> Any:
        """Basic get that returns an object. Returns object { 'message': 'An object was successfully
        returned' }.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: any, or the result of cls(response)
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _url = self._client.format_url(self.get.metadata["url"])

        request = build_get_request(
            template_url=_url,
        )
        request = _convert_request(request)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize("object", pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/objectType/get"}  # type: ignore

    @distributed_trace_async
    async def put(self, put_object: Any, **kwargs: Any) -> None:
        """Basic put that puts an object. Pass in {'foo': 'bar'} to get a 200 and anything else to get an
        object error.

        :param put_object: Pass in {'foo': 'bar'} for a 200, anything else for an object error.
        :type put_object: any
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(put_object, "object")
        _url = self._client.format_url(self.put.metadata["url"])

        request = build_put_request(
            content_type=content_type,
            json=json,
            template_url=_url,
        )
        request = _convert_request(request)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize("object", pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put.metadata = {"url": "/objectType/put"}  # type: ignore
