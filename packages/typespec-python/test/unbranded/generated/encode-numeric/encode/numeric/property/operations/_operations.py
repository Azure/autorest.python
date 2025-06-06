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
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from .. import models as _models1
from ..._configuration import NumericClientConfiguration
from ..._utils.model_base import SdkJSONEncoder, _deserialize
from ..._utils.serialization import Deserializer, Serializer

JSON = MutableMapping[str, Any]
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_property_safeint_as_string_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/encode/numeric/property/safeint"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_property_uint32_as_string_optional_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/encode/numeric/property/uint32"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_property_uint8_as_string_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/encode/numeric/property/uint8"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class PropertyOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~encode.numeric.NumericClient`'s
        :attr:`property` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: NumericClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def safeint_as_string(
        self, value: _models1.SafeintAsStringProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models1.SafeintAsStringProperty:
        """safeint_as_string.

        :param value: Required.
        :type value: ~encode.numeric.property.models.SafeintAsStringProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SafeintAsStringProperty. The SafeintAsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.property.models.SafeintAsStringProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def safeint_as_string(
        self, value: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models1.SafeintAsStringProperty:
        """safeint_as_string.

        :param value: Required.
        :type value: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SafeintAsStringProperty. The SafeintAsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.property.models.SafeintAsStringProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def safeint_as_string(
        self, value: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models1.SafeintAsStringProperty:
        """safeint_as_string.

        :param value: Required.
        :type value: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SafeintAsStringProperty. The SafeintAsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.property.models.SafeintAsStringProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def safeint_as_string(
        self, value: Union[_models1.SafeintAsStringProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models1.SafeintAsStringProperty:
        """safeint_as_string.

        :param value: Is one of the following types: SafeintAsStringProperty, JSON, IO[bytes] Required.
        :type value: ~encode.numeric.property.models.SafeintAsStringProperty or JSON or IO[bytes]
        :return: SafeintAsStringProperty. The SafeintAsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.property.models.SafeintAsStringProperty
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
        cls: ClsType[_models1.SafeintAsStringProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(value, (IOBase, bytes)):
            _content = value
        else:
            _content = json.dumps(value, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

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
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

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
            deserialized = _deserialize(_models1.SafeintAsStringProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def uint32_as_string_optional(
        self, value: _models1.Uint32AsStringProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models1.Uint32AsStringProperty:
        """uint32_as_string_optional.

        :param value: Required.
        :type value: ~encode.numeric.property.models.Uint32AsStringProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Uint32AsStringProperty. The Uint32AsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.property.models.Uint32AsStringProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def uint32_as_string_optional(
        self, value: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models1.Uint32AsStringProperty:
        """uint32_as_string_optional.

        :param value: Required.
        :type value: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Uint32AsStringProperty. The Uint32AsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.property.models.Uint32AsStringProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def uint32_as_string_optional(
        self, value: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models1.Uint32AsStringProperty:
        """uint32_as_string_optional.

        :param value: Required.
        :type value: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Uint32AsStringProperty. The Uint32AsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.property.models.Uint32AsStringProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def uint32_as_string_optional(
        self, value: Union[_models1.Uint32AsStringProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models1.Uint32AsStringProperty:
        """uint32_as_string_optional.

        :param value: Is one of the following types: Uint32AsStringProperty, JSON, IO[bytes] Required.
        :type value: ~encode.numeric.property.models.Uint32AsStringProperty or JSON or IO[bytes]
        :return: Uint32AsStringProperty. The Uint32AsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.property.models.Uint32AsStringProperty
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
        cls: ClsType[_models1.Uint32AsStringProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(value, (IOBase, bytes)):
            _content = value
        else:
            _content = json.dumps(value, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

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
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

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
            deserialized = _deserialize(_models1.Uint32AsStringProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def uint8_as_string(
        self, value: _models1.Uint8AsStringProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models1.Uint8AsStringProperty:
        """uint8_as_string.

        :param value: Required.
        :type value: ~encode.numeric.property.models.Uint8AsStringProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Uint8AsStringProperty. The Uint8AsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.property.models.Uint8AsStringProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def uint8_as_string(
        self, value: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models1.Uint8AsStringProperty:
        """uint8_as_string.

        :param value: Required.
        :type value: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Uint8AsStringProperty. The Uint8AsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.property.models.Uint8AsStringProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def uint8_as_string(
        self, value: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models1.Uint8AsStringProperty:
        """uint8_as_string.

        :param value: Required.
        :type value: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Uint8AsStringProperty. The Uint8AsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.property.models.Uint8AsStringProperty
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def uint8_as_string(
        self, value: Union[_models1.Uint8AsStringProperty, JSON, IO[bytes]], **kwargs: Any
    ) -> _models1.Uint8AsStringProperty:
        """uint8_as_string.

        :param value: Is one of the following types: Uint8AsStringProperty, JSON, IO[bytes] Required.
        :type value: ~encode.numeric.property.models.Uint8AsStringProperty or JSON or IO[bytes]
        :return: Uint8AsStringProperty. The Uint8AsStringProperty is compatible with MutableMapping
        :rtype: ~encode.numeric.property.models.Uint8AsStringProperty
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
        cls: ClsType[_models1.Uint8AsStringProperty] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(value, (IOBase, bytes)):
            _content = value
        else:
            _content = json.dumps(value, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_property_uint8_as_string_request(
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
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

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
            deserialized = _deserialize(_models1.Uint8AsStringProperty, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
