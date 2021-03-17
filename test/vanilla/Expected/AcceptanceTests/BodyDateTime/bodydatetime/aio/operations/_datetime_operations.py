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


class DatetimeOperations:
    """DatetimeOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodydatetime.models
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
    async def get_null(self, **kwargs) -> Optional[datetime.datetime]:
        """Get null datetime value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime or None, or the result of cls(response)
        :rtype: ~datetime.datetime or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[datetime.datetime]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_null_request(template_url=self.get_null.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null.metadata = {"url": "/datetime/null"}  # type: ignore

    @distributed_trace_async
    async def get_invalid(self, **kwargs) -> datetime.datetime:
        """Get invalid datetime value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_invalid_request(template_url=self.get_invalid.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_invalid.metadata = {"url": "/datetime/invalid"}  # type: ignore

    @distributed_trace_async
    async def get_overflow(self, **kwargs) -> datetime.datetime:
        """Get overflow datetime value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_overflow_request(template_url=self.get_overflow.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_overflow.metadata = {"url": "/datetime/overflow"}  # type: ignore

    @distributed_trace_async
    async def get_underflow(self, **kwargs) -> datetime.datetime:
        """Get underflow datetime value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_underflow_request(template_url=self.get_underflow.metadata["url"], **kwargs)
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_underflow.metadata = {"url": "/datetime/underflow"}  # type: ignore

    @distributed_trace_async
    async def put_utc_max_date_time(self, datetime_body: datetime.datetime, **kwargs) -> None:
        """Put max datetime value 9999-12-31T23:59:59.999Z.

        :param datetime_body: datetime body.
        :type datetime_body: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        datetime_body = self._serialize.body(datetime_body, "iso-8601")

        request = prepare_datetime_put_utc_max_date_time_request(
            body=datetime_body, template_url=self.put_utc_max_date_time.metadata["url"], **kwargs
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

    put_utc_max_date_time.metadata = {"url": "/datetime/max/utc"}  # type: ignore

    @distributed_trace_async
    async def put_utc_max_date_time7_digits(self, datetime_body: datetime.datetime, **kwargs) -> None:
        """Put max datetime value 9999-12-31T23:59:59.9999999Z.

        This is against the recommendation that asks for 3 digits, but allow to test what happens in
        that scenario.

        :param datetime_body: datetime body.
        :type datetime_body: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        datetime_body = self._serialize.body(datetime_body, "iso-8601")

        request = prepare_datetime_put_utc_max_date_time7_digits_request(
            body=datetime_body, template_url=self.put_utc_max_date_time7_digits.metadata["url"], **kwargs
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

    put_utc_max_date_time7_digits.metadata = {"url": "/datetime/max/utc7ms"}  # type: ignore

    @distributed_trace_async
    async def get_utc_lowercase_max_date_time(self, **kwargs) -> datetime.datetime:
        """Get max datetime value 9999-12-31t23:59:59.999z.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_utc_lowercase_max_date_time_request(
            template_url=self.get_utc_lowercase_max_date_time.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_utc_lowercase_max_date_time.metadata = {"url": "/datetime/max/utc/lowercase"}  # type: ignore

    @distributed_trace_async
    async def get_utc_uppercase_max_date_time(self, **kwargs) -> datetime.datetime:
        """Get max datetime value 9999-12-31T23:59:59.999Z.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_utc_uppercase_max_date_time_request(
            template_url=self.get_utc_uppercase_max_date_time.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_utc_uppercase_max_date_time.metadata = {"url": "/datetime/max/utc/uppercase"}  # type: ignore

    @distributed_trace_async
    async def get_utc_uppercase_max_date_time7_digits(self, **kwargs) -> datetime.datetime:
        """Get max datetime value 9999-12-31T23:59:59.9999999Z.

        This is against the recommendation that asks for 3 digits, but allow to test what happens in
        that scenario.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_utc_uppercase_max_date_time7_digits_request(
            template_url=self.get_utc_uppercase_max_date_time7_digits.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_utc_uppercase_max_date_time7_digits.metadata = {"url": "/datetime/max/utc7ms/uppercase"}  # type: ignore

    @distributed_trace_async
    async def put_local_positive_offset_max_date_time(self, datetime_body: datetime.datetime, **kwargs) -> None:
        """Put max datetime value with positive numoffset 9999-12-31t23:59:59.999+14:00.

        :param datetime_body: datetime body.
        :type datetime_body: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        datetime_body = self._serialize.body(datetime_body, "iso-8601")

        request = prepare_datetime_put_local_positive_offset_max_date_time_request(
            body=datetime_body, template_url=self.put_local_positive_offset_max_date_time.metadata["url"], **kwargs
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

    put_local_positive_offset_max_date_time.metadata = {"url": "/datetime/max/localpositiveoffset"}  # type: ignore

    @distributed_trace_async
    async def get_local_positive_offset_lowercase_max_date_time(self, **kwargs) -> datetime.datetime:
        """Get max datetime value with positive num offset 9999-12-31t23:59:59.999+14:00.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_local_positive_offset_lowercase_max_date_time_request(
            template_url=self.get_local_positive_offset_lowercase_max_date_time.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_local_positive_offset_lowercase_max_date_time.metadata = {"url": "/datetime/max/localpositiveoffset/lowercase"}  # type: ignore

    @distributed_trace_async
    async def get_local_positive_offset_uppercase_max_date_time(self, **kwargs) -> datetime.datetime:
        """Get max datetime value with positive num offset 9999-12-31T23:59:59.999+14:00.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_local_positive_offset_uppercase_max_date_time_request(
            template_url=self.get_local_positive_offset_uppercase_max_date_time.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_local_positive_offset_uppercase_max_date_time.metadata = {"url": "/datetime/max/localpositiveoffset/uppercase"}  # type: ignore

    @distributed_trace_async
    async def put_local_negative_offset_max_date_time(self, datetime_body: datetime.datetime, **kwargs) -> None:
        """Put max datetime value with positive numoffset 9999-12-31t23:59:59.999-14:00.

        :param datetime_body: datetime body.
        :type datetime_body: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        datetime_body = self._serialize.body(datetime_body, "iso-8601")

        request = prepare_datetime_put_local_negative_offset_max_date_time_request(
            body=datetime_body, template_url=self.put_local_negative_offset_max_date_time.metadata["url"], **kwargs
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

    put_local_negative_offset_max_date_time.metadata = {"url": "/datetime/max/localnegativeoffset"}  # type: ignore

    @distributed_trace_async
    async def get_local_negative_offset_uppercase_max_date_time(self, **kwargs) -> datetime.datetime:
        """Get max datetime value with positive num offset 9999-12-31T23:59:59.999-14:00.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_local_negative_offset_uppercase_max_date_time_request(
            template_url=self.get_local_negative_offset_uppercase_max_date_time.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_local_negative_offset_uppercase_max_date_time.metadata = {"url": "/datetime/max/localnegativeoffset/uppercase"}  # type: ignore

    @distributed_trace_async
    async def get_local_negative_offset_lowercase_max_date_time(self, **kwargs) -> datetime.datetime:
        """Get max datetime value with positive num offset 9999-12-31t23:59:59.999-14:00.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_local_negative_offset_lowercase_max_date_time_request(
            template_url=self.get_local_negative_offset_lowercase_max_date_time.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_local_negative_offset_lowercase_max_date_time.metadata = {"url": "/datetime/max/localnegativeoffset/lowercase"}  # type: ignore

    @distributed_trace_async
    async def put_utc_min_date_time(self, datetime_body: datetime.datetime, **kwargs) -> None:
        """Put min datetime value 0001-01-01T00:00:00Z.

        :param datetime_body: datetime body.
        :type datetime_body: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        datetime_body = self._serialize.body(datetime_body, "iso-8601")

        request = prepare_datetime_put_utc_min_date_time_request(
            body=datetime_body, template_url=self.put_utc_min_date_time.metadata["url"], **kwargs
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

    put_utc_min_date_time.metadata = {"url": "/datetime/min/utc"}  # type: ignore

    @distributed_trace_async
    async def get_utc_min_date_time(self, **kwargs) -> datetime.datetime:
        """Get min datetime value 0001-01-01T00:00:00Z.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_utc_min_date_time_request(
            template_url=self.get_utc_min_date_time.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_utc_min_date_time.metadata = {"url": "/datetime/min/utc"}  # type: ignore

    @distributed_trace_async
    async def put_local_positive_offset_min_date_time(self, datetime_body: datetime.datetime, **kwargs) -> None:
        """Put min datetime value 0001-01-01T00:00:00+14:00.

        :param datetime_body: datetime body.
        :type datetime_body: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        datetime_body = self._serialize.body(datetime_body, "iso-8601")

        request = prepare_datetime_put_local_positive_offset_min_date_time_request(
            body=datetime_body, template_url=self.put_local_positive_offset_min_date_time.metadata["url"], **kwargs
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

    put_local_positive_offset_min_date_time.metadata = {"url": "/datetime/min/localpositiveoffset"}  # type: ignore

    @distributed_trace_async
    async def get_local_positive_offset_min_date_time(self, **kwargs) -> datetime.datetime:
        """Get min datetime value 0001-01-01T00:00:00+14:00.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_local_positive_offset_min_date_time_request(
            template_url=self.get_local_positive_offset_min_date_time.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_local_positive_offset_min_date_time.metadata = {"url": "/datetime/min/localpositiveoffset"}  # type: ignore

    @distributed_trace_async
    async def put_local_negative_offset_min_date_time(self, datetime_body: datetime.datetime, **kwargs) -> None:
        """Put min datetime value 0001-01-01T00:00:00-14:00.

        :param datetime_body: datetime body.
        :type datetime_body: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        datetime_body = self._serialize.body(datetime_body, "iso-8601")

        request = prepare_datetime_put_local_negative_offset_min_date_time_request(
            body=datetime_body, template_url=self.put_local_negative_offset_min_date_time.metadata["url"], **kwargs
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

    put_local_negative_offset_min_date_time.metadata = {"url": "/datetime/min/localnegativeoffset"}  # type: ignore

    @distributed_trace_async
    async def get_local_negative_offset_min_date_time(self, **kwargs) -> datetime.datetime:
        """Get min datetime value 0001-01-01T00:00:00-14:00.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_local_negative_offset_min_date_time_request(
            template_url=self.get_local_negative_offset_min_date_time.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_local_negative_offset_min_date_time.metadata = {"url": "/datetime/min/localnegativeoffset"}  # type: ignore

    @distributed_trace_async
    async def get_local_no_offset_min_date_time(self, **kwargs) -> datetime.datetime:
        """Get min datetime value 0001-01-01T00:00:00.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime, or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[datetime.datetime]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = prepare_datetime_get_local_no_offset_min_date_time_request(
            template_url=self.get_local_no_offset_min_date_time.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("iso-8601", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_local_no_offset_min_date_time.metadata = {"url": "/datetime/min/localnooffset"}  # type: ignore
