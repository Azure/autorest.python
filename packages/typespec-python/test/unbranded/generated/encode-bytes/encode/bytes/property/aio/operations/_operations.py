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

from .... import models as _models3
from ...._utils.model_base import SdkJSONEncoder, _deserialize
from ...._utils.serialization import Deserializer, Serializer
from ....aio._configuration import BytesClientConfiguration
from ...operations._operations import (
    build_property_base64_request,
    build_property_base64_url_array_request,
    build_property_base64_url_request,
    build_property_default_request,
)

JSON = MutableMapping[str, Any]
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PropertyOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.bytes.aio.BytesClient`'s
        :attr:`property` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: BytesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def default(
        self, body: _models3.DefaultBytesProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.DefaultBytesProperty:
        """default.

        :param body: Required.
        :type body: ~encode.bytes.models.DefaultBytesProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DefaultBytesProperty. The DefaultBytesProperty is compatible with MutableMapping
        :rtype: ~encode.bytes.models.DefaultBytesProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def default(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.DefaultBytesProperty:
        """default.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DefaultBytesProperty. The DefaultBytesProperty is compatible with MutableMapping
        :rtype: ~encode.bytes.models.DefaultBytesProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def default(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.DefaultBytesProperty:
        """default.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DefaultBytesProperty. The DefaultBytesProperty is compatible with MutableMapping
        :rtype: ~encode.bytes.models.DefaultBytesProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def default(
        self, body: Union[_models3.DefaultBytesProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models3.DefaultBytesProperty:
        """default.

        :param body: Is one of the following types: DefaultBytesProperty, JSON, IO[bytes] Required.
        :type body: ~encode.bytes.models.DefaultBytesProperty or JSON or IO[bytes]
        :return: DefaultBytesProperty. The DefaultBytesProperty is compatible with MutableMapping
        :rtype: ~encode.bytes.models.DefaultBytesProperty
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
        cls: ClsType[_models3.DefaultBytesProperty] = kwargs.pop("cls", None)

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
            deserialized = _deserialize(_models3.DefaultBytesProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def base64(
        self, body: _models3.Base64BytesProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Base64BytesProperty:
        """base64.

        :param body: Required.
        :type body: ~encode.bytes.models.Base64BytesProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Base64BytesProperty. The Base64BytesProperty is compatible with MutableMapping
        :rtype: ~encode.bytes.models.Base64BytesProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def base64(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Base64BytesProperty:
        """base64.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Base64BytesProperty. The Base64BytesProperty is compatible with MutableMapping
        :rtype: ~encode.bytes.models.Base64BytesProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def base64(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Base64BytesProperty:
        """base64.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Base64BytesProperty. The Base64BytesProperty is compatible with MutableMapping
        :rtype: ~encode.bytes.models.Base64BytesProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def base64(
        self, body: Union[_models3.Base64BytesProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models3.Base64BytesProperty:
        """base64.

        :param body: Is one of the following types: Base64BytesProperty, JSON, IO[bytes] Required.
        :type body: ~encode.bytes.models.Base64BytesProperty or JSON or IO[bytes]
        :return: Base64BytesProperty. The Base64BytesProperty is compatible with MutableMapping
        :rtype: ~encode.bytes.models.Base64BytesProperty
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
        cls: ClsType[_models3.Base64BytesProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_base64_request(
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
            deserialized = _deserialize(_models3.Base64BytesProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def base64_url(
        self, body: _models3.Base64urlBytesProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Base64urlBytesProperty:
        """base64_url.

        :param body: Required.
        :type body: ~encode.bytes.models.Base64urlBytesProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Base64urlBytesProperty. The Base64urlBytesProperty is compatible with MutableMapping
        :rtype: ~encode.bytes.models.Base64urlBytesProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def base64_url(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Base64urlBytesProperty:
        """base64_url.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Base64urlBytesProperty. The Base64urlBytesProperty is compatible with MutableMapping
        :rtype: ~encode.bytes.models.Base64urlBytesProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def base64_url(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Base64urlBytesProperty:
        """base64_url.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Base64urlBytesProperty. The Base64urlBytesProperty is compatible with MutableMapping
        :rtype: ~encode.bytes.models.Base64urlBytesProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def base64_url(
        self, body: Union[_models3.Base64urlBytesProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models3.Base64urlBytesProperty:
        """base64_url.

        :param body: Is one of the following types: Base64urlBytesProperty, JSON, IO[bytes] Required.
        :type body: ~encode.bytes.models.Base64urlBytesProperty or JSON or IO[bytes]
        :return: Base64urlBytesProperty. The Base64urlBytesProperty is compatible with MutableMapping
        :rtype: ~encode.bytes.models.Base64urlBytesProperty
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
        cls: ClsType[_models3.Base64urlBytesProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_base64_url_request(
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
            deserialized = _deserialize(_models3.Base64urlBytesProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def base64_url_array(
        self, body: _models3.Base64urlArrayBytesProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Base64urlArrayBytesProperty:
        """base64_url_array.

        :param body: Required.
        :type body: ~encode.bytes.models.Base64urlArrayBytesProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Base64urlArrayBytesProperty. The Base64urlArrayBytesProperty is compatible with
         MutableMapping
        :rtype: ~encode.bytes.models.Base64urlArrayBytesProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def base64_url_array(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Base64urlArrayBytesProperty:
        """base64_url_array.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Base64urlArrayBytesProperty. The Base64urlArrayBytesProperty is compatible with
         MutableMapping
        :rtype: ~encode.bytes.models.Base64urlArrayBytesProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def base64_url_array(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models3.Base64urlArrayBytesProperty:
        """base64_url_array.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Base64urlArrayBytesProperty. The Base64urlArrayBytesProperty is compatible with
         MutableMapping
        :rtype: ~encode.bytes.models.Base64urlArrayBytesProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def base64_url_array(
        self, body: Union[_models3.Base64urlArrayBytesProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models3.Base64urlArrayBytesProperty:
        """base64_url_array.

        :param body: Is one of the following types: Base64urlArrayBytesProperty, JSON, IO[bytes]
         Required.
        :type body: ~encode.bytes.models.Base64urlArrayBytesProperty or JSON or IO[bytes]
        :return: Base64urlArrayBytesProperty. The Base64urlArrayBytesProperty is compatible with
         MutableMapping
        :rtype: ~encode.bytes.models.Base64urlArrayBytesProperty
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
        cls: ClsType[_models3.Base64urlArrayBytesProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_base64_url_array_request(
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
            deserialized = _deserialize(_models3.Base64urlArrayBytesProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
