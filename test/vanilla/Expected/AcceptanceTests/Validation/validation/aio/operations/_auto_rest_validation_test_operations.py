# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ...protocol import *

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AutoRestValidationTestOperationsMixin:
    @distributed_trace_async
    async def validation_of_method_parameters(self, resource_group_name: str, id: int, **kwargs) -> "_models.Product":
        """Validates input parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product, or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Product"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = _validation_of_method_parameters_request(
            resource_group_name=resource_group_name,
            id=id,
            template_url=self.validation_of_method_parameters.metadata["url"],
            **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    validation_of_method_parameters.metadata = {"url": "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"}  # type: ignore

    @distributed_trace_async
    async def validation_of_body(
        self, resource_group_name: str, id: int, body: Optional["_models.Product"] = None, **kwargs
    ) -> "_models.Product":
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :param body:
        :type body: ~validation.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product, or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Product"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        if body is not None:
            body = self._serialize.body(body, "Product")

        request = _validation_of_body_request(
            resource_group_name=resource_group_name,
            id=id,
            body=body,
            template_url=self.validation_of_body.metadata["url"],
            **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    validation_of_body.metadata = {"url": "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"}  # type: ignore

    @distributed_trace_async
    async def get_with_constant_in_path(self, **kwargs) -> None:
        """get_with_constant_in_path.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = _get_with_constant_in_path_request(
            template_url=self.get_with_constant_in_path.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    get_with_constant_in_path.metadata = {"url": "/validation/constantsInPath/{constantParam}/value"}  # type: ignore

    @distributed_trace_async
    async def post_with_constant_in_body(self, body: Optional["_models.Product"] = None, **kwargs) -> "_models.Product":
        """post_with_constant_in_body.

        :param body:
        :type body: ~validation.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product, or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Product"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        if body is not None:
            body = self._serialize.body(body, "Product")

        request = _post_with_constant_in_body_request(
            body=body, template_url=self.post_with_constant_in_body.metadata["url"], **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    post_with_constant_in_body.metadata = {"url": "/validation/constantsInPath/{constantParam}/value"}  # type: ignore
