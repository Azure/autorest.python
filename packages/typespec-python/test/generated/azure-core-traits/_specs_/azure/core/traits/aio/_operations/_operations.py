# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload
import uuid

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import AzureJSONEncoder, _deserialize
from ..._operations._operations import build_traits_repeatable_action_request, build_traits_smoke_test_request
from .._vendor import TraitsClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
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
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        if_unmodified_since: Optional[datetime.datetime] = None,
        if_modified_since: Optional[datetime.datetime] = None,
        client_request_id: Optional[str] = None,
        **kwargs: Any
    ) -> _models.User:
        """Get a resource, sending and receiving headers.

        :param id: The user's id. Required.
        :type id: int
        :keyword foo: header in request. Required.
        :paramtype foo: str
        :keyword if_match: The request should only proceed if an entity matches this string. Default
         value is None.
        :paramtype if_match: str
        :keyword if_none_match: The request should only proceed if no entity matches this string.
         Default value is None.
        :paramtype if_none_match: str
        :keyword if_unmodified_since: The request should only proceed if the entity was not modified
         after this time. Default value is None.
        :paramtype if_unmodified_since: ~datetime.datetime
        :keyword if_modified_since: The request should only proceed if the entity was modified after
         this time. Default value is None.
        :paramtype if_modified_since: ~datetime.datetime
        :keyword client_request_id: An opaque, globally-unique, client-generated string identifier for
         the request. Default value is None.
        :paramtype client_request_id: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.traits.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
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

        cls: ClsType[_models.User] = kwargs.pop("cls", None)

        request = build_traits_smoke_test_request(
            id=id,
            foo=foo,
            if_match=if_match,
            if_none_match=if_none_match,
            if_unmodified_since=if_unmodified_since,
            if_modified_since=if_modified_since,
            client_request_id=client_request_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
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
        :param body: Required.
        :type body: ~_specs_.azure.core.traits.models.UserActionParam
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: UserActionResponse. The UserActionResponse is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.traits.models.UserActionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def repeatable_action(
        self, id: int, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.UserActionResponse:
        """Test for repeatable requests.

        :param id: The user's id. Required.
        :type id: int
        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: UserActionResponse. The UserActionResponse is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.traits.models.UserActionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def repeatable_action(
        self, id: int, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.UserActionResponse:
        """Test for repeatable requests.

        :param id: The user's id. Required.
        :type id: int
        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: UserActionResponse. The UserActionResponse is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.traits.models.UserActionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def repeatable_action(
        self, id: int, body: Union[_models.UserActionParam, JSON, IO], **kwargs: Any
    ) -> _models.UserActionResponse:
        """Test for repeatable requests.

        :param id: The user's id. Required.
        :type id: int
        :param body: Is one of the following types: UserActionParam, JSON, IO Required.
        :type body: ~_specs_.azure.core.traits.models.UserActionParam or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: UserActionResponse. The UserActionResponse is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.traits.models.UserActionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
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
        cls: ClsType[_models.UserActionResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore

        request = build_traits_repeatable_action_request(
            id=id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
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
