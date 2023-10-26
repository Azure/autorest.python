# pylint: disable=too-many-lines
# coding=utf-8

import datetime
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar, Union, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import AzureJSONEncoder, _deserialize
from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_query_default_request(*, input: datetime.timedelta, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/encode/duration/query/default"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "duration")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


def build_query_iso8601_request(*, input: datetime.timedelta, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/encode/duration/query/iso8601"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "duration")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


def build_query_int32_seconds_request(*, input: int, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/encode/duration/query/int32-seconds"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "int")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


def build_query_float_seconds_request(*, input: float, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/encode/duration/query/float-seconds"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "float")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


def build_query_int32_seconds_array_request(*, input: List[int], **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/encode/duration/query/int32-seconds-array"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "[int]", div=",")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


def build_property_default_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/encode/duration/property/default"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_property_iso8601_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/encode/duration/property/iso8601"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_property_int32_seconds_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/encode/duration/property/int32-seconds"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_property_float_seconds_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/encode/duration/property/float-seconds"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_property_float_seconds_array_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/encode/duration/property/float-seconds-array"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_header_default_request(*, duration: datetime.timedelta, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/encode/duration/header/default"

    # Construct headers
    _headers["duration"] = _SERIALIZER.header("duration", duration, "duration")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_header_iso8601_request(*, duration: datetime.timedelta, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/encode/duration/header/iso8601"

    # Construct headers
    _headers["duration"] = _SERIALIZER.header("duration", duration, "duration")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_header_iso8601_array_request(*, duration: List[datetime.timedelta], **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/encode/duration/header/iso8601-array"

    # Construct headers
    _headers["duration"] = _SERIALIZER.header("duration", duration, "[duration]", div=",")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_header_int32_seconds_request(*, duration: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/encode/duration/header/int32-seconds"

    # Construct headers
    _headers["duration"] = _SERIALIZER.header("duration", duration, "int")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_header_float_seconds_request(*, duration: float, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/encode/duration/header/float-seconds"

    # Construct headers
    _headers["duration"] = _SERIALIZER.header("duration", duration, "float")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


class QueryOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.duration.DurationClient`'s
        :attr:`query` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def default(  # pylint: disable=inconsistent-return-statements
        self, *, input: datetime.timedelta, **kwargs: Any
    ) -> None:
        """default.

        :keyword input: Required.
        :paramtype input: ~datetime.timedelta
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map = {
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
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    def iso8601(  # pylint: disable=inconsistent-return-statements
        self, *, input: datetime.timedelta, **kwargs: Any
    ) -> None:
        """iso8601.

        :keyword input: Required.
        :paramtype input: ~datetime.timedelta
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map = {
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
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    def int32_seconds(self, *, input: int, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """int32_seconds.

        :keyword input: Required.
        :paramtype input: int
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map = {
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
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    def float_seconds(self, *, input: float, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """float_seconds.

        :keyword input: Required.
        :paramtype input: float
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map = {
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
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    def int32_seconds_array(  # pylint: disable=inconsistent-return-statements
        self, *, input: List[int], **kwargs: Any
    ) -> None:
        """int32_seconds_array.

        :keyword input: Required.
        :paramtype input: list[int]
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map = {
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
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore


class PropertyOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.duration.DurationClient`'s
        :attr:`property` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def default(
        self, body: _models.DefaultDurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DefaultDurationProperty:
        """default.

        :param body: Required.
        :type body: ~encode.duration.models.DefaultDurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: DefaultDurationProperty. The DefaultDurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.DefaultDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def default(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DefaultDurationProperty:
        """default.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: DefaultDurationProperty. The DefaultDurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.DefaultDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def default(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DefaultDurationProperty:
        """default.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: DefaultDurationProperty. The DefaultDurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.DefaultDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def default(
        self, body: Union[_models.DefaultDurationProperty, JSON, IO], **kwargs: Any
    ) -> _models.DefaultDurationProperty:
        """default.

        :param body: Is one of the following types: DefaultDurationProperty, JSON, IO Required.
        :type body: ~encode.duration.models.DefaultDurationProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: DefaultDurationProperty. The DefaultDurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.DefaultDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DefaultDurationProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_default_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
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
    def iso8601(
        self, body: _models.ISO8601DurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ISO8601DurationProperty:
        """iso8601.

        :param body: Required.
        :type body: ~encode.duration.models.ISO8601DurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: ISO8601DurationProperty. The ISO8601DurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.ISO8601DurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def iso8601(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ISO8601DurationProperty:
        """iso8601.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: ISO8601DurationProperty. The ISO8601DurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.ISO8601DurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def iso8601(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ISO8601DurationProperty:
        """iso8601.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: ISO8601DurationProperty. The ISO8601DurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.ISO8601DurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def iso8601(
        self, body: Union[_models.ISO8601DurationProperty, JSON, IO], **kwargs: Any
    ) -> _models.ISO8601DurationProperty:
        """iso8601.

        :param body: Is one of the following types: ISO8601DurationProperty, JSON, IO Required.
        :type body: ~encode.duration.models.ISO8601DurationProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: ISO8601DurationProperty. The ISO8601DurationProperty is compatible with MutableMapping
        :rtype: ~encode.duration.models.ISO8601DurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ISO8601DurationProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_iso8601_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
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
    def int32_seconds(
        self, body: _models.Int32SecondsDurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Int32SecondsDurationProperty:
        """int32_seconds.

        :param body: Required.
        :type body: ~encode.duration.models.Int32SecondsDurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Int32SecondsDurationProperty. The Int32SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.Int32SecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def int32_seconds(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Int32SecondsDurationProperty:
        """int32_seconds.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Int32SecondsDurationProperty. The Int32SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.Int32SecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def int32_seconds(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Int32SecondsDurationProperty:
        """int32_seconds.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Int32SecondsDurationProperty. The Int32SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.Int32SecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def int32_seconds(
        self, body: Union[_models.Int32SecondsDurationProperty, JSON, IO], **kwargs: Any
    ) -> _models.Int32SecondsDurationProperty:
        """int32_seconds.

        :param body: Is one of the following types: Int32SecondsDurationProperty, JSON, IO Required.
        :type body: ~encode.duration.models.Int32SecondsDurationProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Int32SecondsDurationProperty. The Int32SecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.Int32SecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Int32SecondsDurationProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_int32_seconds_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
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
    def float_seconds(
        self, body: _models.FloatSecondsDurationProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FloatSecondsDurationProperty:
        """float_seconds.

        :param body: Required.
        :type body: ~encode.duration.models.FloatSecondsDurationProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: FloatSecondsDurationProperty. The FloatSecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def float_seconds(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FloatSecondsDurationProperty:
        """float_seconds.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: FloatSecondsDurationProperty. The FloatSecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def float_seconds(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FloatSecondsDurationProperty:
        """float_seconds.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: FloatSecondsDurationProperty. The FloatSecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def float_seconds(
        self, body: Union[_models.FloatSecondsDurationProperty, JSON, IO], **kwargs: Any
    ) -> _models.FloatSecondsDurationProperty:
        """float_seconds.

        :param body: Is one of the following types: FloatSecondsDurationProperty, JSON, IO Required.
        :type body: ~encode.duration.models.FloatSecondsDurationProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: FloatSecondsDurationProperty. The FloatSecondsDurationProperty is compatible with
         MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationProperty
        :raises ~corehttp.exceptions.HttpResponseError:
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.FloatSecondsDurationProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_float_seconds_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
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
    def float_seconds_array(
        self, body: _models.FloatSecondsDurationArrayProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FloatSecondsDurationArrayProperty:
        """float_seconds_array.

        :param body: Required.
        :type body: ~encode.duration.models.FloatSecondsDurationArrayProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: FloatSecondsDurationArrayProperty. The FloatSecondsDurationArrayProperty is compatible
         with MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationArrayProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def float_seconds_array(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FloatSecondsDurationArrayProperty:
        """float_seconds_array.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: FloatSecondsDurationArrayProperty. The FloatSecondsDurationArrayProperty is compatible
         with MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationArrayProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def float_seconds_array(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FloatSecondsDurationArrayProperty:
        """float_seconds_array.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: FloatSecondsDurationArrayProperty. The FloatSecondsDurationArrayProperty is compatible
         with MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationArrayProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def float_seconds_array(
        self, body: Union[_models.FloatSecondsDurationArrayProperty, JSON, IO], **kwargs: Any
    ) -> _models.FloatSecondsDurationArrayProperty:
        """float_seconds_array.

        :param body: Is one of the following types: FloatSecondsDurationArrayProperty, JSON, IO
         Required.
        :type body: ~encode.duration.models.FloatSecondsDurationArrayProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: FloatSecondsDurationArrayProperty. The FloatSecondsDurationArrayProperty is compatible
         with MutableMapping
        :rtype: ~encode.duration.models.FloatSecondsDurationArrayProperty
        :raises ~corehttp.exceptions.HttpResponseError:
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.FloatSecondsDurationArrayProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_float_seconds_array_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
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
        :class:`~encode.duration.DurationClient`'s
        :attr:`header` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def default(  # pylint: disable=inconsistent-return-statements
        self, *, duration: datetime.timedelta, **kwargs: Any
    ) -> None:
        """default.

        :keyword duration: Required.
        :paramtype duration: ~datetime.timedelta
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map = {
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
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    def iso8601(  # pylint: disable=inconsistent-return-statements
        self, *, duration: datetime.timedelta, **kwargs: Any
    ) -> None:
        """iso8601.

        :keyword duration: Required.
        :paramtype duration: ~datetime.timedelta
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map = {
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
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    def iso8601_array(  # pylint: disable=inconsistent-return-statements
        self, *, duration: List[datetime.timedelta], **kwargs: Any
    ) -> None:
        """iso8601_array.

        :keyword duration: Required.
        :paramtype duration: list[~datetime.timedelta]
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map = {
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
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    def int32_seconds(self, *, duration: int, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """int32_seconds.

        :keyword duration: Required.
        :paramtype duration: int
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map = {
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
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    def float_seconds(  # pylint: disable=inconsistent-return-statements
        self, *, duration: float, **kwargs: Any
    ) -> None:
        """float_seconds.

        :keyword duration: Required.
        :paramtype duration: float
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map = {
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
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
