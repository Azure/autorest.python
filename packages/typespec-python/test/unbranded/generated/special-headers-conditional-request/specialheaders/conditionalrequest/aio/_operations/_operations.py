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
from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient
from corehttp.runtime.pipeline import PipelineResponse

from ..._operations._operations import (
    build_conditional_request_head_if_modified_since_request,
    build_conditional_request_post_if_match_request,
    build_conditional_request_post_if_none_match_request,
    build_conditional_request_post_if_unmodified_since_request,
)
from ..._utils.utils import ClientMixinABC
from .._configuration import ConditionalRequestClientConfiguration

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class _ConditionalRequestClientOperationsMixin(
    ClientMixinABC[AsyncPipelineClient[HttpRequest, AsyncHttpResponse], ConditionalRequestClientConfiguration]
):

    async def post_if_match(
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
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def post_if_none_match(
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
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def head_if_modified_since(
        self, *, if_modified_since: Optional[datetime.datetime] = None, **kwargs: Any
    ) -> bool:
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
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
        return 200 <= response.status_code <= 299

    async def post_if_unmodified_since(
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
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
