# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
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
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ..._operations._operations import (
    build_resiliency_service_driven_add_operation_request,
    build_resiliency_service_driven_from_none_request,
    build_resiliency_service_driven_from_one_optional_request,
    build_resiliency_service_driven_from_one_required_request,
)
from ..._validation import api_version_validation
from .._vendor import ResiliencyServiceDrivenClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ResiliencyServiceDrivenClientOperationsMixin(ResiliencyServiceDrivenClientMixinABC):
    @distributed_trace_async
    @api_version_validation(
        method_added_on="v2",
    )  # pylint: disable=inconsistent-return-statements
    async def add_operation(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Added operation.

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

        request = build_resiliency_service_driven_add_operation_request(
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
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    @api_version_validation(
        params_added_on={"v2": ["new_parameter"]},
    )
    async def from_none(self, *, new_parameter: Optional[str] = None, **kwargs: Any) -> bool:
        """Test that grew up from accepting no parameters to an optional input parameter.

        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
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
            new_parameter=new_parameter,
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
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
        return 200 <= response.status_code <= 299

    @distributed_trace_async
    @api_version_validation(
        params_added_on={"v2": ["new_parameter"]},
    )  # pylint: disable=inconsistent-return-statements
    async def from_one_required(  # pylint: disable=inconsistent-return-statements
        self, *, parameter: str, new_parameter: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Operation that grew up from accepting one required parameter to accepting a required parameter
        and an optional parameter.

        :keyword parameter: I am a required parameter. Required.
        :paramtype parameter: str
        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
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
            new_parameter=new_parameter,
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
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    @api_version_validation(
        params_added_on={"v2": ["new_parameter"]},
    )  # pylint: disable=inconsistent-return-statements
    async def from_one_optional(  # pylint: disable=inconsistent-return-statements
        self, *, parameter: Optional[str] = None, new_parameter: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Tests that we can grow up an operation from accepting one optional parameter to accepting two
        optional parameters.

        :keyword parameter: I am an optional parameter. Default value is None.
        :paramtype parameter: str
        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
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
            new_parameter=new_parameter,
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
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
