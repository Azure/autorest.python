# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
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

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._enum_operations import (
    build_get_not_expandable_request,
    build_get_referenced_constant_request,
    build_get_referenced_request,
    build_put_not_expandable_request,
    build_put_referenced_constant_request,
    build_put_referenced_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class EnumOperations:
    """EnumOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodystring.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_not_expandable(self, **kwargs: Any) -> Union[str, "_models.Colors"]:
        """Get enum value 'red color' from enumeration of 'red color', 'green-color', 'blue_color'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Colors, or the result of cls(response)
        :rtype: str or ~bodystring.models.Colors
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Union[str, "_models.Colors"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _url = self._client.format_url(self.get_not_expandable.metadata["url"])

        request = build_get_not_expandable_request(
            template_url=_url,
        )
        request = _convert_request(request)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_not_expandable.metadata = {"url": "/string/enum/notExpandable"}  # type: ignore

    @distributed_trace_async
    async def put_not_expandable(self, string_body: Union[str, "_models.Colors"], **kwargs: Any) -> None:
        """Sends value 'red color' from enumeration of 'red color', 'green-color', 'blue_color'.

        :param string_body: string body.
        :type string_body: str or ~bodystring.models.Colors
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(string_body, "str")
        _url = self._client.format_url(self.put_not_expandable.metadata["url"])

        request = build_put_not_expandable_request(
            content_type=content_type,
            json=json,
            template_url=_url,
        )
        request = _convert_request(request)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_not_expandable.metadata = {"url": "/string/enum/notExpandable"}  # type: ignore

    @distributed_trace_async
    async def get_referenced(self, **kwargs: Any) -> Union[str, "_models.Colors"]:
        """Get enum value 'red color' from enumeration of 'red color', 'green-color', 'blue_color'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Colors, or the result of cls(response)
        :rtype: str or ~bodystring.models.Colors
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Union[str, "_models.Colors"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _url = self._client.format_url(self.get_referenced.metadata["url"])

        request = build_get_referenced_request(
            template_url=_url,
        )
        request = _convert_request(request)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_referenced.metadata = {"url": "/string/enum/Referenced"}  # type: ignore

    @distributed_trace_async
    async def put_referenced(self, enum_string_body: Union[str, "_models.Colors"], **kwargs: Any) -> None:
        """Sends value 'red color' from enumeration of 'red color', 'green-color', 'blue_color'.

        :param enum_string_body: enum string body.
        :type enum_string_body: str or ~bodystring.models.Colors
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(enum_string_body, "str")
        _url = self._client.format_url(self.put_referenced.metadata["url"])

        request = build_put_referenced_request(
            content_type=content_type,
            json=json,
            template_url=_url,
        )
        request = _convert_request(request)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_referenced.metadata = {"url": "/string/enum/Referenced"}  # type: ignore

    @distributed_trace_async
    async def get_referenced_constant(self, **kwargs: Any) -> "_models.RefColorConstant":
        """Get value 'green-color' from the constant.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RefColorConstant, or the result of cls(response)
        :rtype: ~bodystring.models.RefColorConstant
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.RefColorConstant"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _url = self._client.format_url(self.get_referenced_constant.metadata["url"])

        request = build_get_referenced_constant_request(
            template_url=_url,
        )
        request = _convert_request(request)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("RefColorConstant", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_referenced_constant.metadata = {"url": "/string/enum/ReferencedConstant"}  # type: ignore

    @distributed_trace_async
    async def put_referenced_constant(self, field1: Optional[str] = None, **kwargs: Any) -> None:
        """Sends value 'green-color' from a constant.

        :param field1: Sample string.
        :type field1: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        color_constant = "green-color"
        _enum_string_body = _models.RefColorConstant(color_constant=color_constant, field1=field1)
        json = self._serialize.body(_enum_string_body, "RefColorConstant")
        _url = self._client.format_url(self.put_referenced_constant.metadata["url"])

        request = build_put_referenced_constant_request(
            content_type=content_type,
            json=json,
            template_url=_url,
        )
        request = _convert_request(request)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_referenced_constant.metadata = {"url": "/string/enum/ReferencedConstant"}  # type: ignore
