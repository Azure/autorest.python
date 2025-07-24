# coding=utf-8
from collections.abc import MutableMapping
from typing import Any, Callable, Dict, Optional, TypeVar

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

from .._configuration import PathClientConfiguration
from .._utils.serialization import Serializer
from .._utils.utils import ClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_path_normal_request(name: str, **kwargs: Any) -> HttpRequest:
    # Construct URL
    _url = "/parameters/path/normal/{name}"
    path_format_arguments = {
        "name": _SERIALIZER.url("name", name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    return HttpRequest(method="GET", url=_url, **kwargs)


def build_path_optional_request(*, name: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    # Construct URL
    _url = "/parameters/path/optional{name}"
    path_format_arguments = {
        "name": "" if name is None else "/" + _SERIALIZER.url("name", name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    return HttpRequest(method="GET", url=_url, **kwargs)


class _PathClientOperationsMixin(ClientMixinABC[PipelineClient[HttpRequest, HttpResponse], PathClientConfiguration]):

    def normal(self, name: str, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """normal.

        :param name: Required.
        :type name: str
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

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_path_normal_request(
            name=name,
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

    def optional(  # pylint: disable=inconsistent-return-statements
        self, *, name: Optional[str] = None, **kwargs: Any
    ) -> None:
        """optional.

        :keyword name: Default value is None.
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

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_path_optional_request(
            name=name,
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
