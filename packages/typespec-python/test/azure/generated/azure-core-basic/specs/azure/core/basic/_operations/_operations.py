# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Iterable, List, Optional, Type, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import SdkJSONEncoder, _deserialize
from .._serialization import Serializer
from .._vendor import BasicClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_basic_create_or_update_request(id: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/core/basic/users/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


def build_basic_create_or_replace_request(id: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/core/basic/users/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_basic_get_request(id: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/core/basic/users/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_basic_list_request(
    *,
    top: Optional[int] = None,
    skip: Optional[int] = None,
    maxpagesize: Optional[int] = None,
    orderby: Optional[List[str]] = None,
    filter: Optional[str] = None,
    select: Optional[List[str]] = None,
    expand: Optional[List[str]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/core/basic/users"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if top is not None:
        _params["top"] = _SERIALIZER.query("top", top, "int")
    if skip is not None:
        _params["skip"] = _SERIALIZER.query("skip", skip, "int")
    if maxpagesize is not None:
        _params["maxpagesize"] = _SERIALIZER.query("maxpagesize", maxpagesize, "int")
    if orderby is not None:
        _params["orderby"] = [_SERIALIZER.query("orderby", q, "str") if q is not None else "" for q in orderby]
    if filter is not None:
        _params["filter"] = _SERIALIZER.query("filter", filter, "str")
    if select is not None:
        _params["select"] = [_SERIALIZER.query("select", q, "str") if q is not None else "" for q in select]
    if expand is not None:
        _params["expand"] = [_SERIALIZER.query("expand", q, "str") if q is not None else "" for q in expand]

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_basic_delete_request(id: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/core/basic/users/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_basic_export_request(id: int, *, format: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/core/basic/users/{id}:export"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["format"] = _SERIALIZER.query("format", format, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class BasicClientOperationsMixin(BasicClientMixinABC):

    @overload
    def create_or_update(
        self, id: int, resource: _models.User, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: ~specs.azure.core.basic.models.User
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~specs.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self, id: int, resource: JSON, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~specs.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self, id: int, resource: IO[bytes], *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~specs.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(self, id: int, resource: Union[_models.User, JSON, IO[bytes]], **kwargs: Any) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Is one of the following types: User, JSON, IO[bytes]
         Required.
        :type resource: ~specs.azure.core.basic.models.User or JSON or IO[bytes]
        :return: User. The User is compatible with MutableMapping
        :rtype: ~specs.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.User] = kwargs.pop("cls", None)

        content_type = content_type or "application/merge-patch+json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_basic_create_or_update_request(
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
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
            deserialized = _deserialize(_models.User, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create_or_replace(
        self, id: int, resource: _models.User, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or replaces a user's fields.

        Creates or replaces a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: ~specs.azure.core.basic.models.User
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~specs.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_replace(
        self, id: int, resource: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or replaces a user's fields.

        Creates or replaces a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~specs.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_replace(
        self, id: int, resource: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or replaces a user's fields.

        Creates or replaces a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~specs.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_replace(self, id: int, resource: Union[_models.User, JSON, IO[bytes]], **kwargs: Any) -> _models.User:
        """Adds a user or replaces a user's fields.

        Creates or replaces a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Is one of the following types: User, JSON, IO[bytes]
         Required.
        :type resource: ~specs.azure.core.basic.models.User or JSON or IO[bytes]
        :return: User. The User is compatible with MutableMapping
        :rtype: ~specs.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.User] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_basic_create_or_replace_request(
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
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
            deserialized = _deserialize(_models.User, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def get(self, id: int, **kwargs: Any) -> _models.User:
        """Gets a user.

        Gets a User.

        :param id: The user's id. Required.
        :type id: int
        :return: User. The User is compatible with MutableMapping
        :rtype: ~specs.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.User] = kwargs.pop("cls", None)

        _request = build_basic_get_request(
            id=id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.User, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list(
        self,
        *,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        orderby: Optional[List[str]] = None,
        filter: Optional[str] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
        **kwargs: Any
    ) -> Iterable["_models.User"]:
        """Lists all users.

        Lists all Users.

        :keyword top: The number of result items to return. Default value is None.
        :paramtype top: int
        :keyword skip: The number of result items to skip. Default value is None.
        :paramtype skip: int
        :keyword orderby: Expressions that specify the order of returned results. Default value is
         None.
        :paramtype orderby: list[str]
        :keyword filter: Filter the result list using the given expression. Default value is None.
        :paramtype filter: str
        :keyword select: Select the specified fields to be included in the response. Default value is
         None.
        :paramtype select: list[str]
        :keyword expand: Expand the indicated resources into the response. Default value is None.
        :paramtype expand: list[str]
        :return: An iterator like instance of User
        :rtype: ~azure.core.paging.ItemPaged[~specs.azure.core.basic.models.User]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        maxpagesize = kwargs.pop("maxpagesize", None)
        cls: ClsType[List[_models.User]] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_basic_list_request(
                    top=top,
                    skip=skip,
                    maxpagesize=maxpagesize,
                    orderby=orderby,
                    filter=filter,
                    select=select,
                    expand=expand,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.User], deserialized["value"])
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @distributed_trace
    def delete(self, id: int, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Deletes a user.

        Deletes a User.

        :param id: The user's id. Required.
        :type id: int
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_basic_delete_request(
            id=id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def export(self, id: int, *, format: str, **kwargs: Any) -> _models.User:
        """Exports a user.

        Exports a User.

        :param id: The user's id. Required.
        :type id: int
        :keyword format: The format of the data. Required.
        :paramtype format: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~specs.azure.core.basic.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.User] = kwargs.pop("cls", None)

        _request = build_basic_export_request(
            id=id,
            format=format,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.User, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
