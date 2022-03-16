# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._header_operations import (
    build_custom_named_request_id_head_request,
    build_custom_named_request_id_param_grouping_request,
    build_custom_named_request_id_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class HeaderOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azurespecialproperties.aio.AutoRestAzureSpecialParametersTestClient`'s
        :attr:`header` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def custom_named_request_id(  # pylint: disable=inconsistent-return-statements
        self, foo_client_request_id: str, **kwargs: Any
    ) -> None:
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request.

        :param foo_client_request_id: The fooRequestId.
        :type foo_client_request_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_custom_named_request_id_request(
            foo_client_request_id=foo_client_request_id,
            template_url=self.custom_named_request_id.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["foo-request-id"] = self._deserialize("str", response.headers.get("foo-request-id"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    custom_named_request_id.metadata = {"url": "/azurespecials/customNamedRequestId"}  # type: ignore

    @distributed_trace_async
    async def custom_named_request_id_param_grouping(  # pylint: disable=inconsistent-return-statements
        self,
        header_custom_named_request_id_param_grouping_parameters: "_models.HeaderCustomNamedRequestIdParamGroupingParameters",
        **kwargs: Any
    ) -> None:
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request,
        via a parameter group.

        :param header_custom_named_request_id_param_grouping_parameters: Parameter group.
        :type header_custom_named_request_id_param_grouping_parameters:
         ~azurespecialproperties.models.HeaderCustomNamedRequestIdParamGroupingParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _foo_client_request_id = None
        if header_custom_named_request_id_param_grouping_parameters is not None:
            _foo_client_request_id = header_custom_named_request_id_param_grouping_parameters.foo_client_request_id

        request = build_custom_named_request_id_param_grouping_request(
            foo_client_request_id=_foo_client_request_id,
            template_url=self.custom_named_request_id_param_grouping.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["foo-request-id"] = self._deserialize("str", response.headers.get("foo-request-id"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    custom_named_request_id_param_grouping.metadata = {"url": "/azurespecials/customNamedRequestIdParamGrouping"}  # type: ignore

    @distributed_trace_async
    async def custom_named_request_id_head(self, foo_client_request_id: str, **kwargs: Any) -> bool:
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request.

        :param foo_client_request_id: The fooRequestId.
        :type foo_client_request_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool, or the result of cls(response)
        :rtype: bool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_custom_named_request_id_head_request(
            foo_client_request_id=foo_client_request_id,
            template_url=self.custom_named_request_id_head.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers["foo-request-id"] = self._deserialize("str", response.headers.get("foo-request-id"))

        if cls:
            return cls(pipeline_response, None, response_headers)
        return 200 <= response.status_code <= 299

    custom_named_request_id_head.metadata = {"url": "/azurespecials/customNamedRequestIdHead"}  # type: ignore
