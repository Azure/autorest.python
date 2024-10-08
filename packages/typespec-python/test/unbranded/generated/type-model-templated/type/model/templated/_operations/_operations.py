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
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import SdkJSONEncoder, _deserialize
from .._serialization import Serializer
from .._vendor import TemplatedClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_templated_numeric_type_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/templated/numericType"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_templated_float32_type_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/templated/float32ValuesType"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_templated_int32_type_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/templated/int32ValuesType"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


class TemplatedClientOperationsMixin(TemplatedClientMixinABC):

    @overload
    def numeric_type(
        self, input: _models.Int32Type, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Int32Type:
        """numeric_type.

        :param input: Required.
        :type input: ~type.model.templated.models.Int32Type
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Int32Type. The Int32Type is compatible with MutableMapping
        :rtype: ~type.model.templated.models.Int32Type
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def numeric_type(self, input: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models.Int32Type:
        """numeric_type.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Int32Type. The Int32Type is compatible with MutableMapping
        :rtype: ~type.model.templated.models.Int32Type
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def numeric_type(
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Int32Type:
        """numeric_type.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Int32Type. The Int32Type is compatible with MutableMapping
        :rtype: ~type.model.templated.models.Int32Type
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def numeric_type(self, input: Union[_models.Int32Type, JSON, IO[bytes]], **kwargs: Any) -> _models.Int32Type:
        """numeric_type.

        :param input: Is one of the following types: Int32Type, JSON, IO[bytes] Required.
        :type input: ~type.model.templated.models.Int32Type or JSON or IO[bytes]
        :return: Int32Type. The Int32Type is compatible with MutableMapping
        :rtype: ~type.model.templated.models.Int32Type
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
        cls: ClsType[_models.Int32Type] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_templated_numeric_type_request(
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
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Int32Type, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def float32_type(
        self, input: _models.Float32ValuesType, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Float32ValuesType:
        """float32_type.

        :param input: Required.
        :type input: ~type.model.templated.models.Float32ValuesType
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Float32ValuesType. The Float32ValuesType is compatible with MutableMapping
        :rtype: ~type.model.templated.models.Float32ValuesType
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def float32_type(
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Float32ValuesType:
        """float32_type.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Float32ValuesType. The Float32ValuesType is compatible with MutableMapping
        :rtype: ~type.model.templated.models.Float32ValuesType
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def float32_type(
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Float32ValuesType:
        """float32_type.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Float32ValuesType. The Float32ValuesType is compatible with MutableMapping
        :rtype: ~type.model.templated.models.Float32ValuesType
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def float32_type(
        self, input: Union[_models.Float32ValuesType, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Float32ValuesType:
        """float32_type.

        :param input: Is one of the following types: Float32ValuesType, JSON, IO[bytes] Required.
        :type input: ~type.model.templated.models.Float32ValuesType or JSON or IO[bytes]
        :return: Float32ValuesType. The Float32ValuesType is compatible with MutableMapping
        :rtype: ~type.model.templated.models.Float32ValuesType
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
        cls: ClsType[_models.Float32ValuesType] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_templated_float32_type_request(
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
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Float32ValuesType, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def int32_type(
        self, input: _models.Int32ValuesType, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Int32ValuesType:
        """int32_type.

        :param input: Required.
        :type input: ~type.model.templated.models.Int32ValuesType
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Int32ValuesType. The Int32ValuesType is compatible with MutableMapping
        :rtype: ~type.model.templated.models.Int32ValuesType
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def int32_type(
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Int32ValuesType:
        """int32_type.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Int32ValuesType. The Int32ValuesType is compatible with MutableMapping
        :rtype: ~type.model.templated.models.Int32ValuesType
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def int32_type(
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Int32ValuesType:
        """int32_type.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Int32ValuesType. The Int32ValuesType is compatible with MutableMapping
        :rtype: ~type.model.templated.models.Int32ValuesType
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def int32_type(
        self, input: Union[_models.Int32ValuesType, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Int32ValuesType:
        """int32_type.

        :param input: Is one of the following types: Int32ValuesType, JSON, IO[bytes] Required.
        :type input: ~type.model.templated.models.Int32ValuesType or JSON or IO[bytes]
        :return: Int32ValuesType. The Int32ValuesType is compatible with MutableMapping
        :rtype: ~type.model.templated.models.Int32ValuesType
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
        cls: ClsType[_models.Int32ValuesType] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_templated_int32_type_request(
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
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Int32ValuesType, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
