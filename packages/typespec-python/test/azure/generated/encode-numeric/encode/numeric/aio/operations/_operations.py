# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

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
from ...operations._operations import (
    build_property_safeint_as_string_request,
    build_property_uint32_as_string_optional_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PropertyOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.numeric.aio.NumericClient`'s
        :attr:`property` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def safeint_as_string(
        self, body: _models.SafeintAsStringProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.SafeintAsStringProperty:
        """safeint_as_string.

        :param body: Required.
        :type body: ~encode.numeric.models.SafeintAsStringProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SafeintAsStringProperty. The SafeintAsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.models.SafeintAsStringProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def safeint_as_string(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.SafeintAsStringProperty:
        """safeint_as_string.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SafeintAsStringProperty. The SafeintAsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.models.SafeintAsStringProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def safeint_as_string(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.SafeintAsStringProperty:
        """safeint_as_string.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SafeintAsStringProperty. The SafeintAsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.models.SafeintAsStringProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def safeint_as_string(
        self, body: Union[_models.SafeintAsStringProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.SafeintAsStringProperty:
        """safeint_as_string.

        :param body: Is one of the following types: SafeintAsStringProperty, JSON, IO[bytes] Required.
        :type body: ~encode.numeric.models.SafeintAsStringProperty or JSON or IO[bytes]
        :return: SafeintAsStringProperty. The SafeintAsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.models.SafeintAsStringProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SafeintAsStringProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_safeint_as_string_request(
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
            deserialized = _deserialize(_models.SafeintAsStringProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def uint32_as_string_optional(
        self, body: _models.Uint32AsStringProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Uint32AsStringProperty:
        """uint32_as_string_optional.

        :param body: Required.
        :type body: ~encode.numeric.models.Uint32AsStringProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Uint32AsStringProperty. The Uint32AsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.models.Uint32AsStringProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def uint32_as_string_optional(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Uint32AsStringProperty:
        """uint32_as_string_optional.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Uint32AsStringProperty. The Uint32AsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.models.Uint32AsStringProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def uint32_as_string_optional(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Uint32AsStringProperty:
        """uint32_as_string_optional.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Uint32AsStringProperty. The Uint32AsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.models.Uint32AsStringProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def uint32_as_string_optional(
        self, body: Union[_models.Uint32AsStringProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Uint32AsStringProperty:
        """uint32_as_string_optional.

        :param body: Is one of the following types: Uint32AsStringProperty, JSON, IO[bytes] Required.
        :type body: ~encode.numeric.models.Uint32AsStringProperty or JSON or IO[bytes]
        :return: Uint32AsStringProperty. The Uint32AsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.models.Uint32AsStringProperty
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Uint32AsStringProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_uint32_as_string_optional_request(
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
            deserialized = _deserialize(_models.Uint32AsStringProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
