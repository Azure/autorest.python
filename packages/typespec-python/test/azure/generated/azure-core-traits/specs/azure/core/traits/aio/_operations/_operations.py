# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
import datetime
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core import MatchConditions
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceModifiedError,
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
from ..._operations._operations import build_traits_repeatable_action_request, build_traits_smoke_test_request
from .._vendor import TraitsClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class TraitsClientOperationsMixin(TraitsClientMixinABC):

    @distributed_trace_async
    async def smoke_test(
        self,
        id: int,
        *,
        foo: str,
        if_unmodified_since: Optional[datetime.datetime] = None,
        if_modified_since: Optional[datetime.datetime] = None,
        etag: Optional[str] = None,
        match_condition: Optional[MatchConditions] = None,
        **kwargs: Any
    ) -> _models.User:
        """Get a resource, sending and receiving headers.

        :param id: The user's id. Required.
        :type id: int
        :keyword foo: header in request. Required.
        :paramtype foo: str
        :keyword if_unmodified_since: The request should only proceed if the entity was not modified
         after this time. Default value is None.
        :paramtype if_unmodified_since: ~datetime.datetime
        :keyword if_modified_since: The request should only proceed if the entity was modified after
         this time. Default value is None.
        :paramtype if_modified_since: ~datetime.datetime
        :keyword etag: check if resource is changed. Set None to skip checking etag. Default value is
         None.
        :paramtype etag: str
        :keyword match_condition: The match condition to use upon the etag. Default value is None.
        :paramtype match_condition: ~azure.core.MatchConditions
        :return: User. The User is compatible with MutableMapping
        :rtype: ~specs.azure.core.traits.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
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

        cls: ClsType[_models.User] = kwargs.pop("cls", None)

        _request = build_traits_smoke_test_request(
            id=id,
            foo=foo,
            if_unmodified_since=if_unmodified_since,
            if_modified_since=if_modified_since,
            etag=etag,
            match_condition=match_condition,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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

        response_headers = {}
        response_headers["bar"] = self._deserialize("str", response.headers.get("bar"))
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))
        response_headers["x-ms-client-request-id"] = self._deserialize(
            "str", response.headers.get("x-ms-client-request-id")
        )

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.User, response.json())

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def repeatable_action(
        self, id: int, body: _models.UserActionParam, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.UserActionResponse:
        """Test for repeatable requests.

        :param id: The user's id. Required.
        :type id: int
        :param body: The body parameter. Required.
        :type body: ~specs.azure.core.traits.models.UserActionParam
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: UserActionResponse. The UserActionResponse is compatible with MutableMapping
        :rtype: ~specs.azure.core.traits.models.UserActionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def repeatable_action(
        self, id: int, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.UserActionResponse:
        """Test for repeatable requests.

        :param id: The user's id. Required.
        :type id: int
        :param body: The body parameter. Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: UserActionResponse. The UserActionResponse is compatible with MutableMapping
        :rtype: ~specs.azure.core.traits.models.UserActionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def repeatable_action(
        self, id: int, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.UserActionResponse:
        """Test for repeatable requests.

        :param id: The user's id. Required.
        :type id: int
        :param body: The body parameter. Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: UserActionResponse. The UserActionResponse is compatible with MutableMapping
        :rtype: ~specs.azure.core.traits.models.UserActionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def repeatable_action(
        self, id: int, body: Union[_models.UserActionParam, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.UserActionResponse:
        """Test for repeatable requests.

        :param id: The user's id. Required.
        :type id: int
        :param body: The body parameter. Is one of the following types: UserActionParam, JSON,
         IO[bytes] Required.
        :type body: ~specs.azure.core.traits.models.UserActionParam or JSON or IO[bytes]
        :return: UserActionResponse. The UserActionResponse is compatible with MutableMapping
        :rtype: ~specs.azure.core.traits.models.UserActionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
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
        cls: ClsType[_models.UserActionResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_traits_repeatable_action_request(
            id=id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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

        response_headers = {}
        response_headers["Repeatability-Result"] = self._deserialize(
            "str", response.headers.get("Repeatability-Result")
        )

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.UserActionResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore
