# coding=utf-8
from collections.abc import MutableMapping
import datetime
from typing import Any, Callable, Dict, Optional, TypeVar

from corehttp import MatchConditions
from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceModifiedError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from .._configuration import ConditionalRequestClientConfiguration
from .._utils.serialization import Serializer
from .._utils.utils import ClientMixinABC, prep_if_match, prep_if_none_match

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_conditional_request_post_if_match_request(  # pylint: disable=name-too-long
    *, etag: Optional[str] = None, match_condition: Optional[MatchConditions] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/special-headers/conditional-request/if-match"

    # Construct headers
    if_match = prep_if_match(etag, match_condition)
    if if_match is not None:
        _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if_none_match = prep_if_none_match(etag, match_condition)
    if if_none_match is not None:
        _headers["If-None-Match"] = _SERIALIZER.header("if_none_match", if_none_match, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_conditional_request_post_if_none_match_request(  # pylint: disable=name-too-long
    *, etag: Optional[str] = None, match_condition: Optional[MatchConditions] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/special-headers/conditional-request/if-none-match"

    # Construct headers
    if_match = prep_if_match(etag, match_condition)
    if if_match is not None:
        _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if_none_match = prep_if_none_match(etag, match_condition)
    if if_none_match is not None:
        _headers["If-None-Match"] = _SERIALIZER.header("if_none_match", if_none_match, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_conditional_request_head_if_modified_since_request(  # pylint: disable=name-too-long
    *, if_modified_since: Optional[datetime.datetime] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/special-headers/conditional-request/if-modified-since"

    # Construct headers
    if if_modified_since is not None:
        _headers["If-Modified-Since"] = _SERIALIZER.header("if_modified_since", if_modified_since, "rfc-1123")

    return HttpRequest(method="HEAD", url=_url, headers=_headers, **kwargs)


def build_conditional_request_post_if_unmodified_since_request(  # pylint: disable=name-too-long
    *, if_unmodified_since: Optional[datetime.datetime] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/special-headers/conditional-request/if-unmodified-since"

    # Construct headers
    if if_unmodified_since is not None:
        _headers["If-Unmodified-Since"] = _SERIALIZER.header("if_unmodified_since", if_unmodified_since, "rfc-1123")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class _ConditionalRequestClientOperationsMixin(
    ClientMixinABC[PipelineClient[HttpRequest, HttpResponse], ConditionalRequestClientConfiguration]
):

    def post_if_match(  # pylint: disable=inconsistent-return-statements
        self, *, etag: Optional[str] = None, match_condition: Optional[MatchConditions] = None, **kwargs: Any
    ) -> None:
        """Check when only If-Match in header is defined.

        :keyword etag: check if resource is changed. Set None to skip checking etag. Default value is
         None.
        :paramtype etag: str
        :keyword match_condition: The match condition to use upon the etag. Default value is None.
        :paramtype match_condition: ~corehttp.MatchConditions
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
        if match_condition == MatchConditions.IfNotModified:
            error_map[412] = ResourceModifiedError
        elif match_condition == MatchConditions.IfPresent:
            error_map[412] = ResourceNotFoundError
        elif match_condition == MatchConditions.IfMissing:
            error_map[412] = ResourceExistsError
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_conditional_request_post_if_match_request(
            etag=etag,
            match_condition=match_condition,
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

    def post_if_none_match(  # pylint: disable=inconsistent-return-statements
        self, *, etag: Optional[str] = None, match_condition: Optional[MatchConditions] = None, **kwargs: Any
    ) -> None:
        """Check when only If-None-Match in header is defined.

        :keyword etag: check if resource is changed. Set None to skip checking etag. Default value is
         None.
        :paramtype etag: str
        :keyword match_condition: The match condition to use upon the etag. Default value is None.
        :paramtype match_condition: ~corehttp.MatchConditions
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
        if match_condition == MatchConditions.IfNotModified:
            error_map[412] = ResourceModifiedError
        elif match_condition == MatchConditions.IfPresent:
            error_map[412] = ResourceNotFoundError
        elif match_condition == MatchConditions.IfMissing:
            error_map[412] = ResourceExistsError
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_conditional_request_post_if_none_match_request(
            etag=etag,
            match_condition=match_condition,
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

    def head_if_modified_since(self, *, if_modified_since: Optional[datetime.datetime] = None, **kwargs: Any) -> bool:
        """Check when only If-Modified-Since in header is defined.

        :keyword if_modified_since: A timestamp indicating the last modified time of the resource known
         to the
         client. The operation will be performed only if the resource on the service has
         been modified since the specified time. Default value is None.
        :paramtype if_modified_since: ~datetime.datetime
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

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_conditional_request_head_if_modified_since_request(
            if_modified_since=if_modified_since,
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
        return 200 <= response.status_code <= 299

    def post_if_unmodified_since(  # pylint: disable=inconsistent-return-statements
        self, *, if_unmodified_since: Optional[datetime.datetime] = None, **kwargs: Any
    ) -> None:
        """Check when only If-Unmodified-Since in header is defined.

        :keyword if_unmodified_since: A timestamp indicating the last modified time of the resource
         known to the
         client. The operation will be performed only if the resource on the service has
         not been modified since the specified time. Default value is None.
        :paramtype if_unmodified_since: ~datetime.datetime
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

        _request = build_conditional_request_post_if_unmodified_since_request(
            if_unmodified_since=if_unmodified_since,
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
