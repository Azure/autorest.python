# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import json
import sys
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

from .... import models as _models3
from ...._model_base import SdkJSONEncoder, _deserialize
from ...._serialization import Deserializer, Serializer
from ....aio._configuration import DatetimeClientConfiguration
from ...operations._operations import (
    build_property_default_request,
    build_property_rfc3339_request,
    build_property_rfc7231_request,
    build_property_unix_timestamp_array_request,
    build_property_unix_timestamp_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PropertyOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.datetime.aio.DatetimeClient`'s
        :attr:`property` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: DatetimeClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def default(
        self, body: _models3.DefaultDatetimeProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.DefaultDatetimeProperty:
        """default.

        :param body: Required.
        :type body: ~encode.datetime.models.DefaultDatetimeProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DefaultDatetimeProperty. The DefaultDatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.DefaultDatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def default(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.DefaultDatetimeProperty:
        """default.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DefaultDatetimeProperty. The DefaultDatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.DefaultDatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def default(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.DefaultDatetimeProperty:
        """default.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DefaultDatetimeProperty. The DefaultDatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.DefaultDatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def default(
        self, body: Union[_models3.DefaultDatetimeProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models3.DefaultDatetimeProperty:
        """default.

        :param body: Is one of the following types: DefaultDatetimeProperty, JSON, IO[bytes] Required.
        :type body: ~encode.datetime.models.DefaultDatetimeProperty or JSON or IO[bytes]
        :return: DefaultDatetimeProperty. The DefaultDatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.DefaultDatetimeProperty
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
        cls: ClsType[_models3.DefaultDatetimeProperty] = kwargs.pop("cls", None)

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
            deserialized = _deserialize(_models3.DefaultDatetimeProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def rfc3339(
        self, body: _models3.Rfc3339DatetimeProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Rfc3339DatetimeProperty:
        """rfc3339.

        :param body: Required.
        :type body: ~encode.datetime.models.Rfc3339DatetimeProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Rfc3339DatetimeProperty. The Rfc3339DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc3339DatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def rfc3339(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Rfc3339DatetimeProperty:
        """rfc3339.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Rfc3339DatetimeProperty. The Rfc3339DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc3339DatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def rfc3339(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Rfc3339DatetimeProperty:
        """rfc3339.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Rfc3339DatetimeProperty. The Rfc3339DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc3339DatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def rfc3339(
        self, body: Union[_models3.Rfc3339DatetimeProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models3.Rfc3339DatetimeProperty:
        """rfc3339.

        :param body: Is one of the following types: Rfc3339DatetimeProperty, JSON, IO[bytes] Required.
        :type body: ~encode.datetime.models.Rfc3339DatetimeProperty or JSON or IO[bytes]
        :return: Rfc3339DatetimeProperty. The Rfc3339DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc3339DatetimeProperty
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
        cls: ClsType[_models3.Rfc3339DatetimeProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_rfc3339_request(
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
            deserialized = _deserialize(_models3.Rfc3339DatetimeProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def rfc7231(
        self, body: _models3.Rfc7231DatetimeProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Rfc7231DatetimeProperty:
        """rfc7231.

        :param body: Required.
        :type body: ~encode.datetime.models.Rfc7231DatetimeProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Rfc7231DatetimeProperty. The Rfc7231DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc7231DatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def rfc7231(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Rfc7231DatetimeProperty:
        """rfc7231.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Rfc7231DatetimeProperty. The Rfc7231DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc7231DatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def rfc7231(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Rfc7231DatetimeProperty:
        """rfc7231.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Rfc7231DatetimeProperty. The Rfc7231DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc7231DatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def rfc7231(
        self, body: Union[_models3.Rfc7231DatetimeProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models3.Rfc7231DatetimeProperty:
        """rfc7231.

        :param body: Is one of the following types: Rfc7231DatetimeProperty, JSON, IO[bytes] Required.
        :type body: ~encode.datetime.models.Rfc7231DatetimeProperty or JSON or IO[bytes]
        :return: Rfc7231DatetimeProperty. The Rfc7231DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc7231DatetimeProperty
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
        cls: ClsType[_models3.Rfc7231DatetimeProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_rfc7231_request(
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
            deserialized = _deserialize(_models3.Rfc7231DatetimeProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def unix_timestamp(
        self, body: _models3.UnixTimestampDatetimeProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.UnixTimestampDatetimeProperty:
        """unix_timestamp.

        :param body: Required.
        :type body: ~encode.datetime.models.UnixTimestampDatetimeProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: UnixTimestampDatetimeProperty. The UnixTimestampDatetimeProperty is compatible with
         MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampDatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def unix_timestamp(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.UnixTimestampDatetimeProperty:
        """unix_timestamp.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: UnixTimestampDatetimeProperty. The UnixTimestampDatetimeProperty is compatible with
         MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampDatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def unix_timestamp(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.UnixTimestampDatetimeProperty:
        """unix_timestamp.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: UnixTimestampDatetimeProperty. The UnixTimestampDatetimeProperty is compatible with
         MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampDatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def unix_timestamp(
        self, body: Union[_models3.UnixTimestampDatetimeProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models3.UnixTimestampDatetimeProperty:
        """unix_timestamp.

        :param body: Is one of the following types: UnixTimestampDatetimeProperty, JSON, IO[bytes]
         Required.
        :type body: ~encode.datetime.models.UnixTimestampDatetimeProperty or JSON or IO[bytes]
        :return: UnixTimestampDatetimeProperty. The UnixTimestampDatetimeProperty is compatible with
         MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampDatetimeProperty
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
        cls: ClsType[_models3.UnixTimestampDatetimeProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_unix_timestamp_request(
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
            deserialized = _deserialize(_models3.UnixTimestampDatetimeProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def unix_timestamp_array(
        self,
        body: _models3.UnixTimestampArrayDatetimeProperty,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models3.UnixTimestampArrayDatetimeProperty:
        """unix_timestamp_array.

        :param body: Required.
        :type body: ~encode.datetime.models.UnixTimestampArrayDatetimeProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: UnixTimestampArrayDatetimeProperty. The UnixTimestampArrayDatetimeProperty is
         compatible with MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampArrayDatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def unix_timestamp_array(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.UnixTimestampArrayDatetimeProperty:
        """unix_timestamp_array.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: UnixTimestampArrayDatetimeProperty. The UnixTimestampArrayDatetimeProperty is
         compatible with MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampArrayDatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def unix_timestamp_array(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.UnixTimestampArrayDatetimeProperty:
        """unix_timestamp_array.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: UnixTimestampArrayDatetimeProperty. The UnixTimestampArrayDatetimeProperty is
         compatible with MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampArrayDatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def unix_timestamp_array(
        self, body: Union[_models3.UnixTimestampArrayDatetimeProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models3.UnixTimestampArrayDatetimeProperty:
        """unix_timestamp_array.

        :param body: Is one of the following types: UnixTimestampArrayDatetimeProperty, JSON, IO[bytes]
         Required.
        :type body: ~encode.datetime.models.UnixTimestampArrayDatetimeProperty or JSON or IO[bytes]
        :return: UnixTimestampArrayDatetimeProperty. The UnixTimestampArrayDatetimeProperty is
         compatible with MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampArrayDatetimeProperty
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
        cls: ClsType[_models3.UnixTimestampArrayDatetimeProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_unix_timestamp_array_request(
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
            deserialized = _deserialize(_models3.UnixTimestampArrayDatetimeProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore