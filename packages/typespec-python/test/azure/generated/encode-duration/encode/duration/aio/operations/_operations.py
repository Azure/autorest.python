# pylint: disable=too-many-lines
# coding=utf-8
import datetime
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar, Union, overload

from azure.core import AsyncPipelineClient
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import SdkJSONEncoder, _deserialize
from ..._serialization import Deserializer, Serializer
from ...operations._operations import (
    build_header_default_request,
    build_header_float64_seconds_request,
    build_header_float_seconds_request,
    build_header_int32_seconds_request,
    build_header_iso8601_array_request,
    build_header_iso8601_request,
    build_property_default_request,
    build_property_float64_seconds_request,
    build_property_float_seconds_array_request,
    build_property_float_seconds_request,
    build_property_int32_seconds_request,
    build_property_iso8601_request,
    build_query_default_request,
    build_query_float64_seconds_request,
    build_query_float_seconds_request,
    build_query_int32_seconds_array_request,
    build_query_int32_seconds_request,
    build_query_iso8601_request,
)
from .._configuration import DurationClientConfiguration

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class QueryOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.duration.aio.DurationClient`'s
        :attr:`query` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: DurationClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def default(self, *, input: datetime.timedelta, **kwargs: Any) -> None:
        """default.

        :keyword input: Required.
        :paramtype input: ~datetime.timedelta
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_query_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def iso8601(self, *, input: datetime.timedelta, **kwargs: Any) -> None:
        """iso8601.

        :keyword input: Required.
        :paramtype input: ~datetime.timedelta
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_query_iso8601_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def int32_seconds(self, *, input: int, **kwargs: Any) -> None:
        """int32_seconds.

        :keyword input: Required.
        :paramtype input: int
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_query_int32_seconds_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def float_seconds(self, *, input: float, **kwargs: Any) -> None:
        """float_seconds.

        :keyword input: Required.
        :paramtype input: float
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_query_float_seconds_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def float64_seconds(self, *, input: float, **kwargs: Any) -> None:
        """float64_seconds.

        :keyword input: Required.
        :paramtype input: float
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_query_float64_seconds_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def int32_seconds_array(self, *, input: List[int], **kwargs: Any) -> None:
        """int32_seconds_array.

        :keyword input: Required.
        :paramtype input: list[int]
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_query_int32_seconds_array_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore


class PropertyOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.duration.aio.DurationClient`'s
        :attr:`property` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: DurationClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def default(
        self, body: _models.DefaultDurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DefaultDurationProperty:
        """default.

        :param body: Required.
        :type body: ~encode.duration.models.DefaultDurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DefaultDurationProperty. The DefaultDurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.DefaultDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def default(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DefaultDurationProperty:
        """default.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DefaultDurationProperty. The DefaultDurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.DefaultDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def default(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DefaultDurationProperty:
        """default.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DefaultDurationProperty. The DefaultDurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.DefaultDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def default(
        self, body: Union[_models.DefaultDurationProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.DefaultDurationProperty:
        """default.

        :param body: Is one of the following types: DefaultDurationProperty, JSON, IO[bytes] Required.
        :type body: ~encode.duration.models.DefaultDurationProperty or JSON or IO[bytes]
        :return: DefaultDurationProperty. The DefaultDurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.DefaultDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DefaultDurationProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_default_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.DefaultDurationProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def iso8601(
        self, body: _models.ISO8601DurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ISO8601DurationProperty:
        """iso8601.

        :param body: Required.
        :type body: ~encode.duration.models.ISO8601DurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ISO8601DurationProperty. The ISO8601DurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.ISO8601DurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def iso8601(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ISO8601DurationProperty:
        """iso8601.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ISO8601DurationProperty. The ISO8601DurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.ISO8601DurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def iso8601(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ISO8601DurationProperty:
        """iso8601.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ISO8601DurationProperty. The ISO8601DurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.ISO8601DurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def iso8601(
        self, body: Union[_models.ISO8601DurationProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.ISO8601DurationProperty:
        """iso8601.

        :param body: Is one of the following types: ISO8601DurationProperty, JSON, IO[bytes] Required.
        :type body: ~encode.duration.models.ISO8601DurationProperty or JSON or IO[bytes]
        :return: ISO8601DurationProperty. The ISO8601DurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.ISO8601DurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ISO8601DurationProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_iso8601_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ISO8601DurationProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def int32_seconds(
        self, body: _models.Int32SecondsDurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Int32SecondsDurationProperty:
        """int32_seconds.

        :param body: Required.
        :type body: ~encode.duration.models.Int32SecondsDurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Int32SecondsDurationProperty. The Int32SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.Int32SecondsDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def int32_seconds(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Int32SecondsDurationProperty:
        """int32_seconds.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Int32SecondsDurationProperty. The Int32SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.Int32SecondsDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def int32_seconds(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Int32SecondsDurationProperty:
        """int32_seconds.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Int32SecondsDurationProperty. The Int32SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.Int32SecondsDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def int32_seconds(
        self, body: Union[_models.Int32SecondsDurationProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Int32SecondsDurationProperty:
        """int32_seconds.

        :param body: Is one of the following types: Int32SecondsDurationProperty, JSON, IO[bytes]
         Required.
        :type body: ~encode.duration.models.Int32SecondsDurationProperty or JSON or IO[bytes]
        :return: Int32SecondsDurationProperty. The Int32SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.Int32SecondsDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Int32SecondsDurationProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_int32_seconds_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Int32SecondsDurationProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def float_seconds(
        self, body: _models.FloatSecondsDurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FloatSecondsDurationProperty:
        """float_seconds.

        :param body: Required.
        :type body: ~encode.duration.models.FloatSecondsDurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FloatSecondsDurationProperty. The FloatSecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def float_seconds(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FloatSecondsDurationProperty:
        """float_seconds.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FloatSecondsDurationProperty. The FloatSecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def float_seconds(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FloatSecondsDurationProperty:
        """float_seconds.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FloatSecondsDurationProperty. The FloatSecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def float_seconds(
        self, body: Union[_models.FloatSecondsDurationProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.FloatSecondsDurationProperty:
        """float_seconds.

        :param body: Is one of the following types: FloatSecondsDurationProperty, JSON, IO[bytes]
         Required.
        :type body: ~encode.duration.models.FloatSecondsDurationProperty or JSON or IO[bytes]
        :return: FloatSecondsDurationProperty. The FloatSecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.FloatSecondsDurationProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_float_seconds_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.FloatSecondsDurationProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def float64_seconds(
        self, body: _models.Float64SecondsDurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Float64SecondsDurationProperty:
        """float64_seconds.

        :param body: Required.
        :type body: ~encode.duration.models.Float64SecondsDurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Float64SecondsDurationProperty. The Float64SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.Float64SecondsDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def float64_seconds(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Float64SecondsDurationProperty:
        """float64_seconds.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Float64SecondsDurationProperty. The Float64SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.Float64SecondsDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def float64_seconds(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Float64SecondsDurationProperty:
        """float64_seconds.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Float64SecondsDurationProperty. The Float64SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.Float64SecondsDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def float64_seconds(
        self, body: Union[_models.Float64SecondsDurationProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Float64SecondsDurationProperty:
        """float64_seconds.

        :param body: Is one of the following types: Float64SecondsDurationProperty, JSON, IO[bytes]
         Required.
        :type body: ~encode.duration.models.Float64SecondsDurationProperty or JSON or IO[bytes]
        :return: Float64SecondsDurationProperty. The Float64SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.Float64SecondsDurationProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Float64SecondsDurationProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_float64_seconds_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Float64SecondsDurationProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def float_seconds_array(
        self, body: _models.FloatSecondsDurationArrayProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FloatSecondsDurationArrayProperty:
        """float_seconds_array.

        :param body: Required.
        :type body: ~encode.duration.models.FloatSecondsDurationArrayProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FloatSecondsDurationArrayProperty. The FloatSecondsDurationArrayProperty is compatible
         with MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationArrayProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def float_seconds_array(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FloatSecondsDurationArrayProperty:
        """float_seconds_array.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FloatSecondsDurationArrayProperty. The FloatSecondsDurationArrayProperty is compatible
         with MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationArrayProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def float_seconds_array(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FloatSecondsDurationArrayProperty:
        """float_seconds_array.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FloatSecondsDurationArrayProperty. The FloatSecondsDurationArrayProperty is compatible
         with MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationArrayProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def float_seconds_array(
        self, body: Union[_models.FloatSecondsDurationArrayProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.FloatSecondsDurationArrayProperty:
        """float_seconds_array.

        :param body: Is one of the following types: FloatSecondsDurationArrayProperty, JSON, IO[bytes]
         Required.
        :type body: ~encode.duration.models.FloatSecondsDurationArrayProperty or JSON or IO[bytes]
        :return: FloatSecondsDurationArrayProperty. The FloatSecondsDurationArrayProperty is compatible
         with MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationArrayProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.FloatSecondsDurationArrayProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_float_seconds_array_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.FloatSecondsDurationArrayProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class HeaderOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.duration.aio.DurationClient`'s
        :attr:`header` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: DurationClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def default(self, *, duration: datetime.timedelta, **kwargs: Any) -> None:
        """default.

        :keyword duration: Required.
        :paramtype duration: ~datetime.timedelta
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_header_default_request(
            duration=duration,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def iso8601(self, *, duration: datetime.timedelta, **kwargs: Any) -> None:
        """iso8601.

        :keyword duration: Required.
        :paramtype duration: ~datetime.timedelta
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_header_iso8601_request(
            duration=duration,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def iso8601_array(self, *, duration: List[datetime.timedelta], **kwargs: Any) -> None:
        """iso8601_array.

        :keyword duration: Required.
        :paramtype duration: list[~datetime.timedelta]
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_header_iso8601_array_request(
            duration=duration,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def int32_seconds(self, *, duration: int, **kwargs: Any) -> None:
        """int32_seconds.

        :keyword duration: Required.
        :paramtype duration: int
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_header_int32_seconds_request(
            duration=duration,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def float_seconds(self, *, duration: float, **kwargs: Any) -> None:
        """float_seconds.

        :keyword duration: Required.
        :paramtype duration: float
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_header_float_seconds_request(
            duration=duration,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def float64_seconds(self, *, duration: float, **kwargs: Any) -> None:
        """float64_seconds.

        :keyword duration: Required.
        :paramtype duration: float
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_header_float64_seconds_request(
            duration=duration,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
