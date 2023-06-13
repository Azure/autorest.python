# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

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


def build_query_default_request(*, input: datetime.datetime, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/encode/datetime/query/default"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "iso-8601")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


def build_query_rfc3339_request(*, input: datetime.datetime, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/encode/datetime/query/rfc3339"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "iso-8601")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


def build_query_rfc7231_request(*, input: datetime.datetime, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/encode/datetime/query/rfc7231"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "iso-8601")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


def build_query_unix_timestamp_request(*, input: datetime.datetime, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/encode/datetime/query/unixTimestamp"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "iso-8601")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


def build_property_default_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/encode/datetime/property/default"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_property_rfc3339_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/encode/datetime/property/rfc3339"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_property_rfc7231_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/encode/datetime/property/rfc7231"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_property_unix_timestamp_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/encode/datetime/property/unix-timestamp"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class QueryOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.datetime.DatetimeClient`'s
        :attr:`query` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def default(  # pylint: disable=inconsistent-return-statements
        self, *, input: datetime.datetime, **kwargs: Any
    ) -> None:
        """default.

        :keyword input: Required.
        :paramtype input: ~datetime.datetime
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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

        request = build_query_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def rfc3339(  # pylint: disable=inconsistent-return-statements
        self, *, input: datetime.datetime, **kwargs: Any
    ) -> None:
        """rfc3339.

        :keyword input: Required.
        :paramtype input: ~datetime.datetime
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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

        request = build_query_rfc3339_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def rfc7231(  # pylint: disable=inconsistent-return-statements
        self, *, input: datetime.datetime, **kwargs: Any
    ) -> None:
        """rfc7231.

        :keyword input: Required.
        :paramtype input: ~datetime.datetime
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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

        request = build_query_rfc7231_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def unix_timestamp(  # pylint: disable=inconsistent-return-statements
        self, *, input: datetime.datetime, **kwargs: Any
    ) -> None:
        """unix_timestamp.

        :keyword input: Required.
        :paramtype input: ~datetime.datetime
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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

        request = build_query_unix_timestamp_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})


class PropertyOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.datetime.DatetimeClient`'s
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
        self, body: _models.DefaultDatetimeProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DefaultDatetimeProperty:
        """default.

        :param body: Required.
        :type body: ~encode.datetime.models.DefaultDatetimeProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: DefaultDatetimeProperty. The DefaultDatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.DefaultDatetimeProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def default(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DefaultDatetimeProperty:
        """default.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: DefaultDatetimeProperty. The DefaultDatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.DefaultDatetimeProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def default(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DefaultDatetimeProperty:
        """default.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: DefaultDatetimeProperty. The DefaultDatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.DefaultDatetimeProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def default(
        self, body: Union[_models.DefaultDatetimeProperty, JSON, IO], **kwargs: Any
    ) -> _models.DefaultDatetimeProperty:
        """default.

        :param body: Is one of the following types: DefaultDatetimeProperty, JSON, IO Required.
        :type body: ~encode.datetime.models.DefaultDatetimeProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: DefaultDatetimeProperty. The DefaultDatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.DefaultDatetimeProperty
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DefaultDatetimeProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore

        request = build_property_default_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.DefaultDatetimeProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def rfc3339(
        self, body: _models.RFC3339DatetimeProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RFC3339DatetimeProperty:
        """rfc3339.

        :param body: Required.
        :type body: ~encode.datetime.models.RFC3339DatetimeProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: RFC3339DatetimeProperty. The RFC3339DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.RFC3339DatetimeProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def rfc3339(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RFC3339DatetimeProperty:
        """rfc3339.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: RFC3339DatetimeProperty. The RFC3339DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.RFC3339DatetimeProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def rfc3339(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RFC3339DatetimeProperty:
        """rfc3339.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: RFC3339DatetimeProperty. The RFC3339DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.RFC3339DatetimeProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def rfc3339(
        self, body: Union[_models.RFC3339DatetimeProperty, JSON, IO], **kwargs: Any
    ) -> _models.RFC3339DatetimeProperty:
        """rfc3339.

        :param body: Is one of the following types: RFC3339DatetimeProperty, JSON, IO Required.
        :type body: ~encode.datetime.models.RFC3339DatetimeProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: RFC3339DatetimeProperty. The RFC3339DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.RFC3339DatetimeProperty
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.RFC3339DatetimeProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore

        request = build_property_rfc3339_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.RFC3339DatetimeProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def rfc7231(
        self, body: _models.RFC7231DatetimeProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RFC7231DatetimeProperty:
        """rfc7231.

        :param body: Required.
        :type body: ~encode.datetime.models.RFC7231DatetimeProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: RFC7231DatetimeProperty. The RFC7231DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.RFC7231DatetimeProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def rfc7231(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RFC7231DatetimeProperty:
        """rfc7231.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: RFC7231DatetimeProperty. The RFC7231DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.RFC7231DatetimeProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def rfc7231(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RFC7231DatetimeProperty:
        """rfc7231.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: RFC7231DatetimeProperty. The RFC7231DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.RFC7231DatetimeProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def rfc7231(
        self, body: Union[_models.RFC7231DatetimeProperty, JSON, IO], **kwargs: Any
    ) -> _models.RFC7231DatetimeProperty:
        """rfc7231.

        :param body: Is one of the following types: RFC7231DatetimeProperty, JSON, IO Required.
        :type body: ~encode.datetime.models.RFC7231DatetimeProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: RFC7231DatetimeProperty. The RFC7231DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.RFC7231DatetimeProperty
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.RFC7231DatetimeProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore

        request = build_property_rfc7231_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.RFC7231DatetimeProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def unix_timestamp(
        self, body: _models.UnixTimestampDatetimeProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.UnixTimestampDatetimeProperty:
        """unix_timestamp.

        :param body: Required.
        :type body: ~encode.datetime.models.UnixTimestampDatetimeProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: UnixTimestampDatetimeProperty. The UnixTimestampDatetimeProperty is compatible with
         MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampDatetimeProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def unix_timestamp(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.UnixTimestampDatetimeProperty:
        """unix_timestamp.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: UnixTimestampDatetimeProperty. The UnixTimestampDatetimeProperty is compatible with
         MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampDatetimeProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def unix_timestamp(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.UnixTimestampDatetimeProperty:
        """unix_timestamp.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: UnixTimestampDatetimeProperty. The UnixTimestampDatetimeProperty is compatible with
         MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampDatetimeProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def unix_timestamp(
        self, body: Union[_models.UnixTimestampDatetimeProperty, JSON, IO], **kwargs: Any
    ) -> _models.UnixTimestampDatetimeProperty:
        """unix_timestamp.

        :param body: Is one of the following types: UnixTimestampDatetimeProperty, JSON, IO Required.
        :type body: ~encode.datetime.models.UnixTimestampDatetimeProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: UnixTimestampDatetimeProperty. The UnixTimestampDatetimeProperty is compatible with
         MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampDatetimeProperty
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.UnixTimestampDatetimeProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore

        request = build_property_unix_timestamp_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.UnixTimestampDatetimeProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
