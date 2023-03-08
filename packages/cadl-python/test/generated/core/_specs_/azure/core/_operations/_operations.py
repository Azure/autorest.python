# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import json
import sys
from typing import Any, Callable, Dict, IO, Iterable, List, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import AzureJSONEncoder, _deserialize
from .._serialization import Serializer
from .._vendor import CoreClientMixinABC, _format_url_section

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_core_create_or_update_request(id: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: Literal["2022-12-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-12-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/core/users/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


def build_core_create_or_replace_request(id: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: Literal["2022-12-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-12-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/core/users/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_core_get_request(id: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-12-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-12-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/core/users/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_core_list_request(
    *,
    top: Optional[int] = None,
    skip: Optional[int] = None,
    orderby: Optional[List[str]] = None,
    filter: Optional[str] = None,
    select: Optional[List[str]] = None,
    expand: Optional[List[str]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-12-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-12-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/core/users"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if top is not None:
        _params["top"] = _SERIALIZER.query("top", top, "int")
    if skip is not None:
        _params["skip"] = _SERIALIZER.query("skip", skip, "int")
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


def build_core_list_with_page_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-12-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-12-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/core/page"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_core_delete_request(id: int, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-12-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-12-01-preview")
    )
    # Construct URL
    _url = "/azure/core/users/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


def build_core_export_request(id: int, *, format: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-12-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-12-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/core/users/{id}:export"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "int"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["format"] = _SERIALIZER.query("format", format, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class CoreClientOperationsMixin(CoreClientMixinABC):
    @overload
    def create_or_update(
        self, id: int, resource: _models.User, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: ~_specs_.azure.core.models.User
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.models.User
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
        :rtype: ~_specs_.azure.core.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self, id: int, resource: IO, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(self, id: int, resource: Union[_models.User, JSON, IO], **kwargs: Any) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Is one of the following types: User, JSON, IO Required.
        :type resource: ~_specs_.azure.core.models.User or JSON or IO
        :keyword content_type: This request has a JSON Merge Patch body. Default value is None.
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.models.User
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
        cls: ClsType[_models.User] = kwargs.pop("cls", None)

        content_type = content_type or "application/merge-patch+json"
        _content = None
        if isinstance(resource, (IO, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=AzureJSONEncoder)  # type: ignore

        request = build_core_create_or_update_request(
            id=id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 200:
            deserialized = _deserialize(_models.User, response.json())

        if response.status_code == 201:
            deserialized = _deserialize(_models.User, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create_or_replace(
        self, id: int, resource: _models.User, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or repalces a user's fields.

        Creates or repalces a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: ~_specs_.azure.core.models.User
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_replace(
        self, id: int, resource: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or repalces a user's fields.

        Creates or repalces a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_replace(
        self, id: int, resource: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or repalces a user's fields.

        Creates or repalces a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Required.
        :type resource: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_replace(self, id: int, resource: Union[_models.User, JSON, IO], **kwargs: Any) -> _models.User:
        """Adds a user or repalces a user's fields.

        Creates or repalces a User.

        :param id: The user's id. Required.
        :type id: int
        :param resource: The resource instance. Is one of the following types: User, JSON, IO Required.
        :type resource: ~_specs_.azure.core.models.User or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.models.User
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
        cls: ClsType[_models.User] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IO, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=AzureJSONEncoder)  # type: ignore

        request = build_core_create_or_replace_request(
            id=id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 200:
            deserialized = _deserialize(_models.User, response.json())

        if response.status_code == 201:
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
        :rtype: ~_specs_.azure.core.models.User
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

        request = build_core_get_request(
            id=id,
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
        :return: An iterator like instance of User. The User is compatible with MutableMapping
        :rtype: ~azure.core.paging.ItemPaged[~_specs_.azure.core.models.User]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models._models.CustomPageUser] = kwargs.pop("cls", None)  # pylint: disable=protected-access

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_core_list_request(
                    top=top,
                    skip=skip,
                    orderby=orderby,
                    filter=filter,
                    select=select,
                    expand=expand,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                request.url = self._client.format_url(request.url)

            else:
                request = HttpRequest("GET", next_link)
                request.url = self._client.format_url(request.url)

            return request

        def extract_data(pipeline_response):
            deserialized: _models._models.CustomPageUser = _deserialize(  # pylint: disable=protected-access
                _models._models.CustomPageUser, pipeline_response  # pylint: disable=protected-access
            )
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @distributed_trace
    def list_with_page(self, **kwargs: Any) -> Iterable["_models.User"]:
        """List with Azure.Core.Page<>.

        :return: An iterator like instance of User. The User is compatible with MutableMapping
        :rtype: ~azure.core.paging.ItemPaged[~_specs_.azure.core.models.User]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models._models.PagedUser] = kwargs.pop("cls", None)  # pylint: disable=protected-access

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_core_list_with_page_request(
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                request.url = self._client.format_url(request.url)

            else:
                request = HttpRequest("GET", next_link)
                request.url = self._client.format_url(request.url)

            return request

        def extract_data(pipeline_response):
            deserialized: _models._models.PagedUser = _deserialize(  # pylint: disable=protected-access
                _models._models.PagedUser, pipeline_response  # pylint: disable=protected-access
            )
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
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

        request = build_core_delete_request(
            id=id,
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

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def export(self, id: int, *, format: str, **kwargs: Any) -> _models.User:
        """Exports a user.

        Exports a User.

        :param id: The user's id. Required.
        :type id: int
        :keyword format: The format of the data. Required.
        :paramtype format: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~_specs_.azure.core.models.User
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

        request = build_core_export_request(
            id=id,
            format=format,
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

        deserialized = _deserialize(_models.User, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
