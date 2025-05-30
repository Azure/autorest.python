# coding=utf-8
from collections.abc import MutableMapping
from io import IOBase
import json
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
from corehttp.runtime import PipelineClient
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from ..._configuration import SpreadClientConfiguration
from ..._utils.model_base import SdkJSONEncoder
from ..._utils.serialization import Deserializer, Serializer

JSON = MutableMapping[str, Any]
_Unset: Any = object()
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_alias_spread_as_request_body_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/parameters/spread/alias/request-body"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_alias_spread_parameter_with_inner_model_request(  # pylint: disable=name-too-long
    id: str, *, x_ms_test_header: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/parameters/spread/alias/inner-model-parameter/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct headers
    _headers["x-ms-test-header"] = _SERIALIZER.header("x_ms_test_header", x_ms_test_header, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_alias_spread_as_request_parameter_request(  # pylint: disable=name-too-long
    id: str, *, x_ms_test_header: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/parameters/spread/alias/request-parameter/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct headers
    _headers["x-ms-test-header"] = _SERIALIZER.header("x_ms_test_header", x_ms_test_header, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_alias_spread_with_multiple_parameters_request(  # pylint: disable=name-too-long
    id: str, *, x_ms_test_header: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/parameters/spread/alias/multiple-parameters/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct headers
    _headers["x-ms-test-header"] = _SERIALIZER.header("x_ms_test_header", x_ms_test_header, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_alias_spread_parameter_with_inner_alias_request(  # pylint: disable=name-too-long
    id: str, *, x_ms_test_header: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/parameters/spread/alias/inner-alias-parameter/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct headers
    _headers["x-ms-test-header"] = _SERIALIZER.header("x_ms_test_header", x_ms_test_header, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class AliasOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~parameters.spread.SpreadClient`'s
        :attr:`alias` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: SpreadClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def spread_as_request_body(self, *, name: str, content_type: str = "application/json", **kwargs: Any) -> None:
        """spread_as_request_body.

        :keyword name: Required.
        :paramtype name: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def spread_as_request_body(self, body: JSON, *, content_type: str = "application/json", **kwargs: Any) -> None:
        """spread_as_request_body.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def spread_as_request_body(self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> None:
        """spread_as_request_body.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def spread_as_request_body(  # pylint: disable=inconsistent-return-statements
        self, body: Union[JSON, IO[bytes]] = _Unset, *, name: str = _Unset, **kwargs: Any
    ) -> None:
        """spread_as_request_body.

        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword name: Required.
        :paramtype name: str
        :return: None
        :rtype: None
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
        cls: ClsType[None] = kwargs.pop("cls", None)

        if body is _Unset:
            if name is _Unset:
                raise TypeError("missing required argument: name")
            body = {"name": name}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_alias_spread_as_request_body_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def spread_parameter_with_inner_model(
        self, id: str, *, x_ms_test_header: str, name: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_parameter_with_inner_model.

        :param id: Required.
        :type id: str
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword name: Required.
        :paramtype name: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def spread_parameter_with_inner_model(
        self, id: str, body: JSON, *, x_ms_test_header: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_parameter_with_inner_model.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: JSON
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def spread_parameter_with_inner_model(
        self, id: str, body: IO[bytes], *, x_ms_test_header: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_parameter_with_inner_model.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: IO[bytes]
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def spread_parameter_with_inner_model(  # pylint: disable=inconsistent-return-statements
        self,
        id: str,
        body: Union[JSON, IO[bytes]] = _Unset,
        *,
        x_ms_test_header: str,
        name: str = _Unset,
        **kwargs: Any
    ) -> None:
        """spread_parameter_with_inner_model.

        :param id: Required.
        :type id: str
        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword name: Required.
        :paramtype name: str
        :return: None
        :rtype: None
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
        cls: ClsType[None] = kwargs.pop("cls", None)

        if body is _Unset:
            if name is _Unset:
                raise TypeError("missing required argument: name")
            body = {"name": name}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_alias_spread_parameter_with_inner_model_request(
            id=id,
            x_ms_test_header=x_ms_test_header,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def spread_as_request_parameter(
        self, id: str, *, x_ms_test_header: str, name: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_as_request_parameter.

        :param id: Required.
        :type id: str
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword name: Required.
        :paramtype name: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def spread_as_request_parameter(
        self, id: str, body: JSON, *, x_ms_test_header: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_as_request_parameter.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: JSON
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def spread_as_request_parameter(
        self, id: str, body: IO[bytes], *, x_ms_test_header: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_as_request_parameter.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: IO[bytes]
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def spread_as_request_parameter(  # pylint: disable=inconsistent-return-statements
        self,
        id: str,
        body: Union[JSON, IO[bytes]] = _Unset,
        *,
        x_ms_test_header: str,
        name: str = _Unset,
        **kwargs: Any
    ) -> None:
        """spread_as_request_parameter.

        :param id: Required.
        :type id: str
        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword name: Required.
        :paramtype name: str
        :return: None
        :rtype: None
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
        cls: ClsType[None] = kwargs.pop("cls", None)

        if body is _Unset:
            if name is _Unset:
                raise TypeError("missing required argument: name")
            body = {"name": name}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_alias_spread_as_request_parameter_request(
            id=id,
            x_ms_test_header=x_ms_test_header,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def spread_with_multiple_parameters(
        self,
        id: str,
        *,
        x_ms_test_header: str,
        required_string: str,
        required_int_list: List[int],
        content_type: str = "application/json",
        optional_int: Optional[int] = None,
        optional_string_list: Optional[List[str]] = None,
        **kwargs: Any
    ) -> None:
        """spread_with_multiple_parameters.

        :param id: Required.
        :type id: str
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword required_string: required string. Required.
        :paramtype required_string: str
        :keyword required_int_list: required int. Required.
        :paramtype required_int_list: list[int]
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword optional_int: optional int. Default value is None.
        :paramtype optional_int: int
        :keyword optional_string_list: optional string. Default value is None.
        :paramtype optional_string_list: list[str]
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def spread_with_multiple_parameters(
        self, id: str, body: JSON, *, x_ms_test_header: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_with_multiple_parameters.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: JSON
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def spread_with_multiple_parameters(
        self, id: str, body: IO[bytes], *, x_ms_test_header: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_with_multiple_parameters.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: IO[bytes]
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def spread_with_multiple_parameters(  # pylint: disable=inconsistent-return-statements
        self,
        id: str,
        body: Union[JSON, IO[bytes]] = _Unset,
        *,
        x_ms_test_header: str,
        required_string: str = _Unset,
        required_int_list: List[int] = _Unset,
        optional_int: Optional[int] = None,
        optional_string_list: Optional[List[str]] = None,
        **kwargs: Any
    ) -> None:
        """spread_with_multiple_parameters.

        :param id: Required.
        :type id: str
        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword required_string: required string. Required.
        :paramtype required_string: str
        :keyword required_int_list: required int. Required.
        :paramtype required_int_list: list[int]
        :keyword optional_int: optional int. Default value is None.
        :paramtype optional_int: int
        :keyword optional_string_list: optional string. Default value is None.
        :paramtype optional_string_list: list[str]
        :return: None
        :rtype: None
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
        cls: ClsType[None] = kwargs.pop("cls", None)

        if body is _Unset:
            if required_string is _Unset:
                raise TypeError("missing required argument: required_string")
            if required_int_list is _Unset:
                raise TypeError("missing required argument: required_int_list")
            body = {
                "optionalInt": optional_int,
                "optionalStringList": optional_string_list,
                "requiredIntList": required_int_list,
                "requiredString": required_string,
            }
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_alias_spread_with_multiple_parameters_request(
            id=id,
            x_ms_test_header=x_ms_test_header,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def spread_parameter_with_inner_alias(
        self,
        id: str,
        *,
        x_ms_test_header: str,
        name: str,
        age: int,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """spread an alias with contains another alias property as body.

        :param id: Required.
        :type id: str
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword name: name of the Thing. Required.
        :paramtype name: str
        :keyword age: age of the Thing. Required.
        :paramtype age: int
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def spread_parameter_with_inner_alias(
        self, id: str, body: JSON, *, x_ms_test_header: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread an alias with contains another alias property as body.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: JSON
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def spread_parameter_with_inner_alias(
        self, id: str, body: IO[bytes], *, x_ms_test_header: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread an alias with contains another alias property as body.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: IO[bytes]
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def spread_parameter_with_inner_alias(  # pylint: disable=inconsistent-return-statements
        self,
        id: str,
        body: Union[JSON, IO[bytes]] = _Unset,
        *,
        x_ms_test_header: str,
        name: str = _Unset,
        age: int = _Unset,
        **kwargs: Any
    ) -> None:
        """spread an alias with contains another alias property as body.

        :param id: Required.
        :type id: str
        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword name: name of the Thing. Required.
        :paramtype name: str
        :keyword age: age of the Thing. Required.
        :paramtype age: int
        :return: None
        :rtype: None
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
        cls: ClsType[None] = kwargs.pop("cls", None)

        if body is _Unset:
            if name is _Unset:
                raise TypeError("missing required argument: name")
            if age is _Unset:
                raise TypeError("missing required argument: age")
            body = {"age": age, "name": name}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_alias_spread_parameter_with_inner_alias_request(
            id=id,
            x_ms_test_header=x_ms_test_header,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
