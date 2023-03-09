# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
import sys
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import _deserialize
from .._serialization import Serializer
from .._vendor import TraitsClientMixinABC, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_traits_get_request(
    id: int,
    *,
    foo: str,
    if_match: Optional[str] = None,
    if_none_match: Optional[str] = None,
    if_unmodified_since: Optional[datetime.datetime] = None,
    if_modified_since: Optional[datetime.datetime] = None,
    client_request_id: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-12-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-12-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/traits/user/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["foo"] = _SERIALIZER.header("foo", foo, "str")
    if if_match is not None:
        _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if if_none_match is not None:
        _headers["If-None-Match"] = _SERIALIZER.header("if_none_match", if_none_match, "str")
    if if_unmodified_since is not None:
        _headers["If-Unmodified-Since"] = _SERIALIZER.header("if_unmodified_since", if_unmodified_since, "rfc-1123")
    if if_modified_since is not None:
        _headers["If-Modified-Since"] = _SERIALIZER.header("if_modified_since", if_modified_since, "rfc-1123")
    if client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_traits_delete_request(
    id: int,
    *,
    repeatability_request_id: Optional[str] = None,
    repeatability_first_sent: Optional[datetime.datetime] = None,
    client_request_id: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    api_version: Literal["2022-12-01-preview"] = kwargs.pop("api_version", "2022-12-01-preview")
    # Construct URL
    _url = "/azure/traits/api/{apiVersion}/user/{id}"
    path_format_arguments = {
        "apiVersion": _SERIALIZER.url("api_version", api_version, "str"),
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct headers
    if repeatability_request_id is not None:
        _headers["Repeatability-Request-ID"] = _SERIALIZER.header(
            "repeatability_request_id", repeatability_request_id, "str"
        )
    if repeatability_first_sent is not None:
        _headers["Repeatability-First-Sent"] = _SERIALIZER.header(
            "repeatability_first_sent", repeatability_first_sent, "rfc-1123"
        )
    if client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")

    return HttpRequest(method="DELETE", url=_url, headers=_headers, **kwargs)


class TraitsClientOperationsMixin(TraitsClientMixinABC):
    @distributed_trace
    def get(
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
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.traits.models.User
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

        request = build_traits_get_request(
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

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
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

        deserialized = _deserialize(_models.User, response.json())

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self,
        id: int,
        *,
        repeatability_request_id: Optional[str] = None,
        repeatability_first_sent: Optional[datetime.datetime] = None,
        client_request_id: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Delete resource with api-version path parameter.

        :param id: The user's id. Required.
        :type id: int
        :keyword repeatability_request_id: An opaque, globally-unique, client-generated string
         identifier for the request. Default value is None.
        :paramtype repeatability_request_id: str
        :keyword repeatability_first_sent: Specifies the date and time at which the request was first
         created. Default value is None.
        :paramtype repeatability_first_sent: ~datetime.datetime
        :keyword client_request_id: An opaque, globally-unique, client-generated string identifier for
         the request. Default value is None.
        :paramtype client_request_id: str
        :return: None
        :rtype: None
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

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_traits_delete_request(
            id=id,
            repeatability_request_id=repeatability_request_id,
            repeatability_first_sent=repeatability_first_sent,
            client_request_id=client_request_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["Repeatability-Result"] = self._deserialize(
            "str", response.headers.get("Repeatability-Result")
        )
        response_headers["x-ms-client-request-id"] = self._deserialize(
            "str", response.headers.get("x-ms-client-request-id")
        )

        if cls:
            return cls(pipeline_response, None, response_headers)
