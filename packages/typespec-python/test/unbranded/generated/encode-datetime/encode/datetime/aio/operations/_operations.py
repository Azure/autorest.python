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
from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import AzureJSONEncoder, _deserialize
from ...operations._operations import (
    build_header_default_request,
    build_header_rfc3339_request,
    build_header_rfc7231_request,
    build_header_unix_timestamp_array_request,
    build_header_unix_timestamp_request,
    build_property_default_request,
    build_property_rfc3339_request,
    build_property_rfc7231_request,
    build_property_unix_timestamp_array_request,
    build_property_unix_timestamp_request,
    build_query_default_request,
    build_query_rfc3339_request,
    build_query_rfc7231_request,
    build_query_unix_timestamp_array_request,
    build_query_unix_timestamp_request,
    build_response_header_default_request,
    build_response_header_rfc3339_request,
    build_response_header_rfc7231_request,
    build_response_header_unix_timestamp_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class QueryOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.datetime.aio.DatetimeClient`'s
        :attr:`query` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def default(  # pylint: disable=inconsistent-return-statements
        self, *, value: datetime.datetime, **kwargs: Any
    ) -> None:
        """default.

        :keyword value: Required.
        :paramtype value: ~datetime.datetime
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
            value=value,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def rfc3339(  # pylint: disable=inconsistent-return-statements
        self, *, value: datetime.datetime, **kwargs: Any
    ) -> None:
        """rfc3339.

        :keyword value: Required.
        :paramtype value: ~datetime.datetime
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

        _request = build_query_rfc3339_request(
            value=value,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def rfc7231(  # pylint: disable=inconsistent-return-statements
        self, *, value: datetime.datetime, **kwargs: Any
    ) -> None:
        """rfc7231.

        :keyword value: Required.
        :paramtype value: ~datetime.datetime
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

        _request = build_query_rfc7231_request(
            value=value,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def unix_timestamp(  # pylint: disable=inconsistent-return-statements
        self, *, value: datetime.datetime, **kwargs: Any
    ) -> None:
        """unix_timestamp.

        :keyword value: Required.
        :paramtype value: ~datetime.datetime
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

        _request = build_query_unix_timestamp_request(
            value=value,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def unix_timestamp_array(  # pylint: disable=inconsistent-return-statements
        self, *, value: List[datetime.datetime], **kwargs: Any
    ) -> None:
        """unix_timestamp_array.

        :keyword value: Required.
        :paramtype value: list[~datetime.datetime]
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

        _request = build_query_unix_timestamp_array_request(
            value=value,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore


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
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def default(
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
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def default(
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
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def default(
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
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def default(
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
        cls: ClsType[_models.DefaultDatetimeProperty] = kwargs.pop("cls", None)

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
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
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
    async def rfc3339(
        self, body: _models.Rfc3339DatetimeProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Rfc3339DatetimeProperty:
        """rfc3339.

        :param body: Required.
        :type body: ~encode.datetime.models.Rfc3339DatetimeProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Rfc3339DatetimeProperty. The Rfc3339DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc3339DatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def rfc3339(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Rfc3339DatetimeProperty:
        """rfc3339.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Rfc3339DatetimeProperty. The Rfc3339DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc3339DatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def rfc3339(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Rfc3339DatetimeProperty:
        """rfc3339.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Rfc3339DatetimeProperty. The Rfc3339DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc3339DatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def rfc3339(
        self, body: Union[_models.Rfc3339DatetimeProperty, JSON, IO], **kwargs: Any
    ) -> _models.Rfc3339DatetimeProperty:
        """rfc3339.

        :param body: Is one of the following types: Rfc3339DatetimeProperty, JSON, IO Required.
        :type body: ~encode.datetime.models.Rfc3339DatetimeProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Rfc3339DatetimeProperty. The Rfc3339DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc3339DatetimeProperty
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
        cls: ClsType[_models.Rfc3339DatetimeProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_rfc3339_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Rfc3339DatetimeProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def rfc7231(
        self, body: _models.Rfc7231DatetimeProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Rfc7231DatetimeProperty:
        """rfc7231.

        :param body: Required.
        :type body: ~encode.datetime.models.Rfc7231DatetimeProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Rfc7231DatetimeProperty. The Rfc7231DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc7231DatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def rfc7231(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Rfc7231DatetimeProperty:
        """rfc7231.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Rfc7231DatetimeProperty. The Rfc7231DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc7231DatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def rfc7231(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Rfc7231DatetimeProperty:
        """rfc7231.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Rfc7231DatetimeProperty. The Rfc7231DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc7231DatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def rfc7231(
        self, body: Union[_models.Rfc7231DatetimeProperty, JSON, IO], **kwargs: Any
    ) -> _models.Rfc7231DatetimeProperty:
        """rfc7231.

        :param body: Is one of the following types: Rfc7231DatetimeProperty, JSON, IO Required.
        :type body: ~encode.datetime.models.Rfc7231DatetimeProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Rfc7231DatetimeProperty. The Rfc7231DatetimeProperty is compatible with MutableMapping
        :rtype: ~encode.datetime.models.Rfc7231DatetimeProperty
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
        cls: ClsType[_models.Rfc7231DatetimeProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_rfc7231_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Rfc7231DatetimeProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def unix_timestamp(
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
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def unix_timestamp(
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
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def unix_timestamp(
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
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def unix_timestamp(
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
        cls: ClsType[_models.UnixTimestampDatetimeProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_unix_timestamp_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.UnixTimestampDatetimeProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def unix_timestamp_array(
        self, body: _models.UnixTimestampArrayDatetimeProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.UnixTimestampArrayDatetimeProperty:
        """unix_timestamp_array.

        :param body: Required.
        :type body: ~encode.datetime.models.UnixTimestampArrayDatetimeProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: UnixTimestampArrayDatetimeProperty. The UnixTimestampArrayDatetimeProperty is
         compatible with MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampArrayDatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def unix_timestamp_array(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.UnixTimestampArrayDatetimeProperty:
        """unix_timestamp_array.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: UnixTimestampArrayDatetimeProperty. The UnixTimestampArrayDatetimeProperty is
         compatible with MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampArrayDatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def unix_timestamp_array(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.UnixTimestampArrayDatetimeProperty:
        """unix_timestamp_array.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: UnixTimestampArrayDatetimeProperty. The UnixTimestampArrayDatetimeProperty is
         compatible with MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampArrayDatetimeProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def unix_timestamp_array(
        self, body: Union[_models.UnixTimestampArrayDatetimeProperty, JSON, IO], **kwargs: Any
    ) -> _models.UnixTimestampArrayDatetimeProperty:
        """unix_timestamp_array.

        :param body: Is one of the following types: UnixTimestampArrayDatetimeProperty, JSON, IO
         Required.
        :type body: ~encode.datetime.models.UnixTimestampArrayDatetimeProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: UnixTimestampArrayDatetimeProperty. The UnixTimestampArrayDatetimeProperty is
         compatible with MutableMapping
        :rtype: ~encode.datetime.models.UnixTimestampArrayDatetimeProperty
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
        cls: ClsType[_models.UnixTimestampArrayDatetimeProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_unix_timestamp_array_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.UnixTimestampArrayDatetimeProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class HeaderOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.datetime.aio.DatetimeClient`'s
        :attr:`header` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def default(  # pylint: disable=inconsistent-return-statements
        self, *, value: datetime.datetime, **kwargs: Any
    ) -> None:
        """default.

        :keyword value: Required.
        :paramtype value: ~datetime.datetime
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
            value=value,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def rfc3339(  # pylint: disable=inconsistent-return-statements
        self, *, value: datetime.datetime, **kwargs: Any
    ) -> None:
        """rfc3339.

        :keyword value: Required.
        :paramtype value: ~datetime.datetime
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

        _request = build_header_rfc3339_request(
            value=value,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def rfc7231(  # pylint: disable=inconsistent-return-statements
        self, *, value: datetime.datetime, **kwargs: Any
    ) -> None:
        """rfc7231.

        :keyword value: Required.
        :paramtype value: ~datetime.datetime
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

        _request = build_header_rfc7231_request(
            value=value,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def unix_timestamp(  # pylint: disable=inconsistent-return-statements
        self, *, value: datetime.datetime, **kwargs: Any
    ) -> None:
        """unix_timestamp.

        :keyword value: Required.
        :paramtype value: ~datetime.datetime
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

        _request = build_header_unix_timestamp_request(
            value=value,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def unix_timestamp_array(  # pylint: disable=inconsistent-return-statements
        self, *, value: List[datetime.datetime], **kwargs: Any
    ) -> None:
        """unix_timestamp_array.

        :keyword value: Required.
        :paramtype value: list[~datetime.datetime]
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

        _request = build_header_unix_timestamp_array_request(
            value=value,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore


class ResponseHeaderOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.datetime.aio.DatetimeClient`'s
        :attr:`response_header` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def default(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """default.

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

        _request = build_response_header_default_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["value"] = self._deserialize("rfc-1123", response.headers.get("value"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    async def rfc3339(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """rfc3339.

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

        _request = build_response_header_rfc3339_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["value"] = self._deserialize("iso-8601", response.headers.get("value"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    async def rfc7231(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """rfc7231.

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

        _request = build_response_header_rfc7231_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["value"] = self._deserialize("rfc-1123", response.headers.get("value"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    async def unix_timestamp(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """unix_timestamp.

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

        _request = build_response_header_unix_timestamp_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["value"] = self._deserialize("unix-time", response.headers.get("value"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore
