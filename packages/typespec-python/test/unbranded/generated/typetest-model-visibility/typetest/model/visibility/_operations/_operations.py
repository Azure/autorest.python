# coding=utf-8
from collections.abc import MutableMapping
from io import IOBase
import json
from typing import Any, Callable, IO, Optional, TypeVar, Union, overload

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

from .. import models as _models
from .._configuration import VisibilityClientConfiguration
from .._utils.model_base import SdkJSONEncoder, _deserialize
from .._utils.serialization import Serializer
from .._utils.utils import ClientMixinABC

JSON = MutableMapping[str, Any]
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_visibility_get_model_request(*, query_prop: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/visibility"

    # Construct parameters
    _params["queryProp"] = _SERIALIZER.query("query_prop", query_prop, "int")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_visibility_head_model_request(*, query_prop: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/type/model/visibility"

    # Construct parameters
    _params["queryProp"] = _SERIALIZER.query("query_prop", query_prop, "int")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="HEAD", url=_url, params=_params, headers=_headers, **kwargs)


def build_visibility_put_model_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/type/model/visibility"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_visibility_patch_model_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/type/model/visibility"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PATCH", url=_url, headers=_headers, **kwargs)


def build_visibility_post_model_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/type/model/visibility"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_visibility_delete_model_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/type/model/visibility"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="DELETE", url=_url, headers=_headers, **kwargs)


def build_visibility_put_read_only_model_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/visibility/readonlyroundtrip"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


class _VisibilityClientOperationsMixin(
    ClientMixinABC[PipelineClient[HttpRequest, HttpResponse], VisibilityClientConfiguration]
):

    @overload
    def get_model(
        self, input: _models.VisibilityModel, *, query_prop: int, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.VisibilityModel
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def get_model(
        self, input: JSON, *, query_prop: int, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Required.
        :type input: JSON
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.VisibilityModel
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def get_model(
        self, input: IO[bytes], *, query_prop: int, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.VisibilityModel
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def get_model(
        self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], *, query_prop: int, **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.VisibilityModel
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
        cls: ClsType[_models.VisibilityModel] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_get_model_request(
            query_prop=query_prop,
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
            deserialized = _deserialize(_models.VisibilityModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def head_model(
        self, input: _models.VisibilityModel, *, query_prop: int, content_type: str = "application/json", **kwargs: Any
    ) -> bool:
        """head_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: bool
        :rtype: bool
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def head_model(
        self, input: JSON, *, query_prop: int, content_type: str = "application/json", **kwargs: Any
    ) -> bool:
        """head_model.

        :param input: Required.
        :type input: JSON
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: bool
        :rtype: bool
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def head_model(
        self, input: IO[bytes], *, query_prop: int, content_type: str = "application/json", **kwargs: Any
    ) -> bool:
        """head_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: bool
        :rtype: bool
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def head_model(
        self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], *, query_prop: int, **kwargs: Any
    ) -> bool:
        """head_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :return: bool
        :rtype: bool
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

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_head_model_request(
            query_prop=query_prop,
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

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
        return 200 <= response.status_code <= 299

    @overload
    def put_model(
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def put_model(self, input: JSON, *, content_type: str = "application/json", **kwargs: Any) -> None:
        """put_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def put_model(self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> None:
        """put_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
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

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_put_model_request(
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
    def patch_model(
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """patch_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def patch_model(self, input: JSON, *, content_type: str = "application/json", **kwargs: Any) -> None:
        """patch_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def patch_model(self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> None:
        """patch_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def patch_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """patch_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
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

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_patch_model_request(
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
    def post_model(
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """post_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def post_model(self, input: JSON, *, content_type: str = "application/json", **kwargs: Any) -> None:
        """post_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def post_model(self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> None:
        """post_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def post_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """post_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
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

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_post_model_request(
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
    def delete_model(
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """delete_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def delete_model(self, input: JSON, *, content_type: str = "application/json", **kwargs: Any) -> None:
        """delete_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def delete_model(self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> None:
        """delete_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def delete_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """delete_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
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

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_delete_model_request(
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
    def put_read_only_model(
        self, input: _models.ReadOnlyModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ReadOnlyModel:
        """put_read_only_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.ReadOnlyModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ReadOnlyModel. The ReadOnlyModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.ReadOnlyModel
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def put_read_only_model(
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ReadOnlyModel:
        """put_read_only_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ReadOnlyModel. The ReadOnlyModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.ReadOnlyModel
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def put_read_only_model(
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ReadOnlyModel:
        """put_read_only_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ReadOnlyModel. The ReadOnlyModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.ReadOnlyModel
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def put_read_only_model(
        self, input: Union[_models.ReadOnlyModel, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.ReadOnlyModel:
        """put_read_only_model.

        :param input: Is one of the following types: ReadOnlyModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.ReadOnlyModel or JSON or IO[bytes]
        :return: ReadOnlyModel. The ReadOnlyModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.ReadOnlyModel
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
        cls: ClsType[_models.ReadOnlyModel] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_put_read_only_model_request(
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
            deserialized = _deserialize(_models.ReadOnlyModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
,line-too-long,useless-suppression