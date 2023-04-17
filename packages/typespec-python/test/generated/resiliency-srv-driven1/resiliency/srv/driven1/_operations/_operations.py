# pylint: disable=too-many-lines
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
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from .._model_base import AzureJSONEncoder
from .._serialization import Serializer
from .._vendor import ResiliencyServiceDrivenClientMixinABC, _format_url_section

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


def build_resiliency_service_driven_add_content_type_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type_path: Literal["json"] = kwargs.pop("content_type_path", "json")
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/add-content-type/{contentTypePath}"
    path_format_arguments = {
        "contentTypePath": _SERIALIZER.url("content_type_path", content_type_path, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_resiliency_service_driven_from_none_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    # Construct URL
    _url = "/add-optional-param/from-none"

    return HttpRequest(method="HEAD", url=_url, **kwargs)


def build_resiliency_service_driven_from_one_required_request(  # pylint: disable=name-too-long
    *, parameter: str, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/add-optional-param/from-one-required"

    # Construct parameters
    _params["parameter"] = _SERIALIZER.query("parameter", parameter, "str")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


def build_resiliency_service_driven_from_one_optional_request(  # pylint: disable=name-too-long
    *, parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/add-optional-param/from-one-optional"

    # Construct parameters
    if parameter is not None:
        _params["parameter"] = _SERIALIZER.query("parameter", parameter, "str")

    return HttpRequest(method="GET", url=_url, params=_params, **kwargs)


class ResiliencyServiceDrivenClientOperationsMixin(ResiliencyServiceDrivenClientMixinABC):
    @overload
    def add_content_type(  # pylint: disable=inconsistent-return-statements
        self, parameter: _models.PostInput, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Test that currently accepts one content type. Will be updated in next spec to accept a new
        content type as well.

        :param parameter: I am a body parameter. My only valid JSON entry is { url:
         "http://example.org/myimage.jpeg" }. Required.
        :type parameter: ~resiliency.srv.driven1.models.PostInput
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword content_type_path: Default value is "json". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype content_type_path: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def add_content_type(  # pylint: disable=inconsistent-return-statements
        self, parameter: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Test that currently accepts one content type. Will be updated in next spec to accept a new
        content type as well.

        :param parameter: I am a body parameter. My only valid JSON entry is { url:
         "http://example.org/myimage.jpeg" }. Required.
        :type parameter: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword content_type_path: Default value is "json". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype content_type_path: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def add_content_type(  # pylint: disable=inconsistent-return-statements
        self, parameter: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Test that currently accepts one content type. Will be updated in next spec to accept a new
        content type as well.

        :param parameter: I am a body parameter. My only valid JSON entry is { url:
         "http://example.org/myimage.jpeg" }. Required.
        :type parameter: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword content_type_path: Default value is "json". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype content_type_path: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def add_content_type(  # pylint: disable=inconsistent-return-statements
        self, parameter: Union[_models.PostInput, JSON, IO], **kwargs: Any
    ) -> None:
        """Test that currently accepts one content type. Will be updated in next spec to accept a new
        content type as well.

        :param parameter: I am a body parameter. My only valid JSON entry is { url:
         "http://example.org/myimage.jpeg" }. Is one of the following types: PostInput, JSON, IO
         Required.
        :type parameter: ~resiliency.srv.driven1.models.PostInput or JSON or IO
        :keyword content_type_path: Default value is "json". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype content_type_path: str
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
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

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type_path: Literal["json"] = kwargs.pop("content_type_path", "json")
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(parameter, (IOBase, bytes)):
            _content = parameter
        else:
            _content = json.dumps(parameter, cls=AzureJSONEncoder)  # type: ignore

        request = build_resiliency_service_driven_add_content_type_request(
            content_type_path=content_type_path,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "serviceDeploymentVersion": self._serialize.url(
                "self._config.service_deployment_version",
                self._config.service_deployment_version,
                "str",
                skip_quote=True,
            ),
            "apiVersion": self._serialize.url(
                "self._config.api_version", self._config.api_version, "str", skip_quote=True
            ),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def from_none(self, **kwargs: Any) -> bool:
        """Test that currently accepts no parameters, will be updated in next spec to accept a new
        optional parameter as well.

        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: bool
        :rtype: bool
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

        request = build_resiliency_service_driven_from_none_request(
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "serviceDeploymentVersion": self._serialize.url(
                "self._config.service_deployment_version",
                self._config.service_deployment_version,
                "str",
                skip_quote=True,
            ),
            "apiVersion": self._serialize.url(
                "self._config.api_version", self._config.api_version, "str", skip_quote=True
            ),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
        return 200 <= response.status_code <= 299

    @distributed_trace
    def from_one_required(  # pylint: disable=inconsistent-return-statements
        self, *, parameter: str, **kwargs: Any
    ) -> None:
        """Test that currently accepts one required parameter, will be updated in next spec to accept a
        new optional parameter as well.

        :keyword parameter: I am a required parameter. Required.
        :paramtype parameter: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
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

        request = build_resiliency_service_driven_from_one_required_request(
            parameter=parameter,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "serviceDeploymentVersion": self._serialize.url(
                "self._config.service_deployment_version",
                self._config.service_deployment_version,
                "str",
                skip_quote=True,
            ),
            "apiVersion": self._serialize.url(
                "self._config.api_version", self._config.api_version, "str", skip_quote=True
            ),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def from_one_optional(  # pylint: disable=inconsistent-return-statements
        self, *, parameter: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Test that currently accepts one optional parameter, will be updated in next spec to accept a
        new optional parameter as well.

        :keyword parameter: I am an optional parameter. Default value is None.
        :paramtype parameter: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
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

        request = build_resiliency_service_driven_from_one_optional_request(
            parameter=parameter,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "serviceDeploymentVersion": self._serialize.url(
                "self._config.service_deployment_version",
                self._config.service_deployment_version,
                "str",
                skip_quote=True,
            ),
            "apiVersion": self._serialize.url(
                "self._config.api_version", self._config.api_version, "str", skip_quote=True
            ),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
