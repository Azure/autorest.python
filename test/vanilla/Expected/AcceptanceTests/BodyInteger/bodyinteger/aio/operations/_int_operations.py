# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
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
from azure.core.protocol import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._protocol import *

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class IntOperations:
    """IntOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodyinteger.models
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
    async def get_null(self, **kwargs) -> Optional[int]:
        """Get null Int value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: int or None, or the result of cls(response)
        :rtype: int or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[int]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_int_get_null(template_url=self.get_null.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("int", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null.metadata = {"url": "/int/null"}  # type: ignore

    @distributed_trace_async
    async def get_invalid(self, **kwargs) -> int:
        """Get invalid Int value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: int, or the result of cls(response)
        :rtype: int
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[int]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_int_get_invalid(template_url=self.get_invalid.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("int", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_invalid.metadata = {"url": "/int/invalid"}  # type: ignore

    @distributed_trace_async
    async def get_overflow_int32(self, **kwargs) -> int:
        """Get overflow Int32 value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: int, or the result of cls(response)
        :rtype: int
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[int]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_int_get_overflow_int32(template_url=self.get_overflow_int32.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("int", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_overflow_int32.metadata = {"url": "/int/overflowint32"}  # type: ignore

    @distributed_trace_async
    async def get_underflow_int32(self, **kwargs) -> int:
        """Get underflow Int32 value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: int, or the result of cls(response)
        :rtype: int
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[int]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_int_get_underflow_int32(template_url=self.get_underflow_int32.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("int", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_underflow_int32.metadata = {"url": "/int/underflowint32"}  # type: ignore

    @distributed_trace_async
    async def get_overflow_int64(self, **kwargs) -> int:
        """Get overflow Int64 value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: long, or the result of cls(response)
        :rtype: long
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[int]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_int_get_overflow_int64(template_url=self.get_overflow_int64.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("long", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_overflow_int64.metadata = {"url": "/int/overflowint64"}  # type: ignore

    @distributed_trace_async
    async def get_underflow_int64(self, **kwargs) -> int:
        """Get underflow Int64 value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: long, or the result of cls(response)
        :rtype: long
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[int]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_int_get_underflow_int64(template_url=self.get_underflow_int64.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("long", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_underflow_int64.metadata = {"url": "/int/underflowint64"}  # type: ignore

    @distributed_trace_async
    async def put_max32(self, int_body: int, **kwargs) -> None:
        """Put max int32 value.

        :param int_body: int body.
        :type int_body: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        int_body = self._serialize.body(int_body, "int")

        request = prepare_int_put_max32(body=int_body, template_url=self.put_max32.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_max32.metadata = {"url": "/int/max/32"}  # type: ignore

    @distributed_trace_async
    async def put_max64(self, int_body: int, **kwargs) -> None:
        """Put max int64 value.

        :param int_body: int body.
        :type int_body: long
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        int_body = self._serialize.body(int_body, "long")

        request = prepare_int_put_max64(body=int_body, template_url=self.put_max64.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_max64.metadata = {"url": "/int/max/64"}  # type: ignore

    @distributed_trace_async
    async def put_min32(self, int_body: int, **kwargs) -> None:
        """Put min int32 value.

        :param int_body: int body.
        :type int_body: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        int_body = self._serialize.body(int_body, "int")

        request = prepare_int_put_min32(body=int_body, template_url=self.put_min32.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_min32.metadata = {"url": "/int/min/32"}  # type: ignore

    @distributed_trace_async
    async def put_min64(self, int_body: int, **kwargs) -> None:
        """Put min int64 value.

        :param int_body: int body.
        :type int_body: long
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        int_body = self._serialize.body(int_body, "long")

        request = prepare_int_put_min64(body=int_body, template_url=self.put_min64.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_min64.metadata = {"url": "/int/min/64"}  # type: ignore

    @distributed_trace_async
    async def get_unix_time(self, **kwargs) -> datetime.datetime:
        """Get datetime encoded as Unix time value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_int_get_unix_time(template_url=self.get_unix_time.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("unix-time", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_unix_time.metadata = {"url": "/int/unixtime"}  # type: ignore

    @distributed_trace_async
    async def put_unix_time_date(self, int_body: datetime.datetime, **kwargs) -> None:
        """Put datetime encoded as Unix time.

        :param int_body: int body.
        :type int_body: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        int_body = self._serialize.body(int_body, "unix-time")

        request = prepare_int_put_unix_time_date(
            body=int_body, template_url=self.put_unix_time_date.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_unix_time_date.metadata = {"url": "/int/unixtime"}  # type: ignore

    @distributed_trace_async
    async def get_invalid_unix_time(self, **kwargs) -> datetime.datetime:
        """Get invalid Unix time value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_int_get_invalid_unix_time(template_url=self.get_invalid_unix_time.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("unix-time", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_invalid_unix_time.metadata = {"url": "/int/invalidunixtime"}  # type: ignore

    @distributed_trace_async
    async def get_null_unix_time(self, **kwargs) -> Optional[datetime.datetime]:
        """Get null Unix time value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime or None, or the result of cls(response)
        :rtype: ~datetime.datetime or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[datetime.datetime]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_int_get_null_unix_time(template_url=self.get_null_unix_time.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("unix-time", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null_unix_time.metadata = {"url": "/int/nullunixtime"}  # type: ignore
