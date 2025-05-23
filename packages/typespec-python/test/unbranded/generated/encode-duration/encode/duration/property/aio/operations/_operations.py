# coding=utf-8
from collections.abc import MutableMapping
from io import IOBase
import json
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from ... import models as _models2
from ...._utils.model_base import SdkJSONEncoder, _deserialize
from ...._utils.serialization import Deserializer, Serializer
from ....aio._configuration import DurationClientConfiguration
from ...operations._operations import (
    build_property_default_request,
    build_property_float64_seconds_request,
    build_property_float_seconds_array_request,
    build_property_float_seconds_request,
    build_property_int32_seconds_request,
    build_property_iso8601_request,
)

JSON = MutableMapping[str, Any]
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


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
        self, body: _models2.DefaultDurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.DefaultDurationProperty:
        """default.

        :param body: Required.
        :type body: ~encode.duration.property.models.DefaultDurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DefaultDurationProperty. The DefaultDurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.property.models.DefaultDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def default(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.DefaultDurationProperty:
        """default.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DefaultDurationProperty. The DefaultDurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.property.models.DefaultDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def default(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.DefaultDurationProperty:
        """default.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DefaultDurationProperty. The DefaultDurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.property.models.DefaultDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def default(
        self, body: Union[_models2.DefaultDurationProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models2.DefaultDurationProperty:
        """default.

        :param body: Is one of the following types: DefaultDurationProperty, JSON, IO[bytes] Required.
        :type body: ~encode.duration.property.models.DefaultDurationProperty or JSON or IO[bytes]
        :return: DefaultDurationProperty. The DefaultDurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.property.models.DefaultDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
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
        cls: ClsType[_models2.DefaultDurationProperty] = kwargs.pop("cls", None)

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
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

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
            deserialized = _deserialize(_models2.DefaultDurationProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def iso8601(
        self, body: _models2.ISO8601DurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.ISO8601DurationProperty:
        """iso8601.

        :param body: Required.
        :type body: ~encode.duration.property.models.ISO8601DurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ISO8601DurationProperty. The ISO8601DurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.property.models.ISO8601DurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def iso8601(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.ISO8601DurationProperty:
        """iso8601.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ISO8601DurationProperty. The ISO8601DurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.property.models.ISO8601DurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def iso8601(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.ISO8601DurationProperty:
        """iso8601.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ISO8601DurationProperty. The ISO8601DurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.property.models.ISO8601DurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def iso8601(
        self, body: Union[_models2.ISO8601DurationProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models2.ISO8601DurationProperty:
        """iso8601.

        :param body: Is one of the following types: ISO8601DurationProperty, JSON, IO[bytes] Required.
        :type body: ~encode.duration.property.models.ISO8601DurationProperty or JSON or IO[bytes]
        :return: ISO8601DurationProperty. The ISO8601DurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.property.models.ISO8601DurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
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
        cls: ClsType[_models2.ISO8601DurationProperty] = kwargs.pop("cls", None)

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
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

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
            deserialized = _deserialize(_models2.ISO8601DurationProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def int32_seconds(
        self, body: _models2.Int32SecondsDurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.Int32SecondsDurationProperty:
        """int32_seconds.

        :param body: Required.
        :type body: ~encode.duration.property.models.Int32SecondsDurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Int32SecondsDurationProperty. The Int32SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.property.models.Int32SecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def int32_seconds(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.Int32SecondsDurationProperty:
        """int32_seconds.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Int32SecondsDurationProperty. The Int32SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.property.models.Int32SecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def int32_seconds(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.Int32SecondsDurationProperty:
        """int32_seconds.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Int32SecondsDurationProperty. The Int32SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.property.models.Int32SecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def int32_seconds(
        self, body: Union[_models2.Int32SecondsDurationProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models2.Int32SecondsDurationProperty:
        """int32_seconds.

        :param body: Is one of the following types: Int32SecondsDurationProperty, JSON, IO[bytes]
         Required.
        :type body: ~encode.duration.property.models.Int32SecondsDurationProperty or JSON or IO[bytes]
        :return: Int32SecondsDurationProperty. The Int32SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.property.models.Int32SecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
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
        cls: ClsType[_models2.Int32SecondsDurationProperty] = kwargs.pop("cls", None)

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
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

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
            deserialized = _deserialize(_models2.Int32SecondsDurationProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def float_seconds(
        self, body: _models2.FloatSecondsDurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.FloatSecondsDurationProperty:
        """float_seconds.

        :param body: Required.
        :type body: ~encode.duration.property.models.FloatSecondsDurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FloatSecondsDurationProperty. The FloatSecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.property.models.FloatSecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def float_seconds(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.FloatSecondsDurationProperty:
        """float_seconds.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FloatSecondsDurationProperty. The FloatSecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.property.models.FloatSecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def float_seconds(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.FloatSecondsDurationProperty:
        """float_seconds.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FloatSecondsDurationProperty. The FloatSecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.property.models.FloatSecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def float_seconds(
        self, body: Union[_models2.FloatSecondsDurationProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models2.FloatSecondsDurationProperty:
        """float_seconds.

        :param body: Is one of the following types: FloatSecondsDurationProperty, JSON, IO[bytes]
         Required.
        :type body: ~encode.duration.property.models.FloatSecondsDurationProperty or JSON or IO[bytes]
        :return: FloatSecondsDurationProperty. The FloatSecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.property.models.FloatSecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
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
        cls: ClsType[_models2.FloatSecondsDurationProperty] = kwargs.pop("cls", None)

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
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

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
            deserialized = _deserialize(_models2.FloatSecondsDurationProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def float64_seconds(
        self, body: _models2.Float64SecondsDurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.Float64SecondsDurationProperty:
        """float64_seconds.

        :param body: Required.
        :type body: ~encode.duration.property.models.Float64SecondsDurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Float64SecondsDurationProperty. The Float64SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.property.models.Float64SecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def float64_seconds(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.Float64SecondsDurationProperty:
        """float64_seconds.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Float64SecondsDurationProperty. The Float64SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.property.models.Float64SecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def float64_seconds(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.Float64SecondsDurationProperty:
        """float64_seconds.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Float64SecondsDurationProperty. The Float64SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.property.models.Float64SecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def float64_seconds(
        self, body: Union[_models2.Float64SecondsDurationProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models2.Float64SecondsDurationProperty:
        """float64_seconds.

        :param body: Is one of the following types: Float64SecondsDurationProperty, JSON, IO[bytes]
         Required.
        :type body: ~encode.duration.property.models.Float64SecondsDurationProperty or JSON or
         IO[bytes]
        :return: Float64SecondsDurationProperty. The Float64SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.property.models.Float64SecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
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
        cls: ClsType[_models2.Float64SecondsDurationProperty] = kwargs.pop("cls", None)

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
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

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
            deserialized = _deserialize(_models2.Float64SecondsDurationProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def float_seconds_array(
        self, body: _models2.FloatSecondsDurationArrayProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.FloatSecondsDurationArrayProperty:
        """float_seconds_array.

        :param body: Required.
        :type body: ~encode.duration.property.models.FloatSecondsDurationArrayProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FloatSecondsDurationArrayProperty. The FloatSecondsDurationArrayProperty is compatible
         with MutableMapping
        :rtype: ~encode.duration.property.models.FloatSecondsDurationArrayProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def float_seconds_array(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.FloatSecondsDurationArrayProperty:
        """float_seconds_array.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FloatSecondsDurationArrayProperty. The FloatSecondsDurationArrayProperty is compatible
         with MutableMapping
        :rtype: ~encode.duration.property.models.FloatSecondsDurationArrayProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def float_seconds_array(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.FloatSecondsDurationArrayProperty:
        """float_seconds_array.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FloatSecondsDurationArrayProperty. The FloatSecondsDurationArrayProperty is compatible
         with MutableMapping
        :rtype: ~encode.duration.property.models.FloatSecondsDurationArrayProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def float_seconds_array(
        self, body: Union[_models2.FloatSecondsDurationArrayProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models2.FloatSecondsDurationArrayProperty:
        """float_seconds_array.

        :param body: Is one of the following types: FloatSecondsDurationArrayProperty, JSON, IO[bytes]
         Required.
        :type body: ~encode.duration.property.models.FloatSecondsDurationArrayProperty or JSON or
         IO[bytes]
        :return: FloatSecondsDurationArrayProperty. The FloatSecondsDurationArrayProperty is compatible
         with MutableMapping
        :rtype: ~encode.duration.property.models.FloatSecondsDurationArrayProperty
        :raises ~corehttp.exceptions.HttpResponseError:
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
        cls: ClsType[_models2.FloatSecondsDurationArrayProperty] = kwargs.pop("cls", None)

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
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

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
            deserialized = _deserialize(_models2.FloatSecondsDurationArrayProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
