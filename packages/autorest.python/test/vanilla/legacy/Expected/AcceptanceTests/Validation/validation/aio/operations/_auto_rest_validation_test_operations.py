# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
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
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._auto_rest_validation_test_operations import (
    build_get_with_constant_in_path_request,
    build_post_with_constant_in_body_request,
    build_validation_of_body_request,
    build_validation_of_method_parameters_request,
)
from .._vendor import AutoRestValidationTestMixinABC

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AutoRestValidationTestOperationsMixin(AutoRestValidationTestMixinABC):
    @distributed_trace_async
    async def validation_of_method_parameters(
        self, resource_group_name: str, id: int, **kwargs: Any
    ) -> _models.Product:
        """Validates input parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
         Required.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000. Required.
        :type id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~validation.models.Product
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
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("apiVersion", self._config.api_version))
        cls: ClsType[_models.Product] = kwargs.pop("cls", None)

        request = build_validation_of_method_parameters_request(
            resource_group_name=resource_group_name,
            id=id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.validation_of_method_parameters.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    validation_of_method_parameters.metadata = {"url": "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"}

    @overload
    async def validation_of_body(
        self,
        resource_group_name: str,
        id: int,
        body: Optional[_models.Product] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Product:
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
         Required.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000. Required.
        :type id: int
        :param body: Default value is None.
        :type body: ~validation.models.Product
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def validation_of_body(
        self,
        resource_group_name: str,
        id: int,
        body: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Product:
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
         Required.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000. Required.
        :type id: int
        :param body: Default value is None.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def validation_of_body(
        self, resource_group_name: str, id: int, body: Optional[Union[_models.Product, IO]] = None, **kwargs: Any
    ) -> _models.Product:
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
         Required.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000. Required.
        :type id: int
        :param body: Is either a Product type or a IO type. Default value is None.
        :type body: ~validation.models.Product or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~validation.models.Product
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
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("apiVersion", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Product] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            if body is not None:
                _json = self._serialize.body(body, "Product")
            else:
                _json = None

        request = build_validation_of_body_request(
            resource_group_name=resource_group_name,
            id=id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.validation_of_body.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    validation_of_body.metadata = {"url": "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"}

    @distributed_trace_async
    async def get_with_constant_in_path(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """get_with_constant_in_path.

        :keyword constant_param: Default value is "constant". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype constant_param: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
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

        constant_param: Literal["constant"] = kwargs.pop("constant_param", "constant")
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_get_with_constant_in_path_request(
            constant_param=constant_param,
            template_url=self.get_with_constant_in_path.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    get_with_constant_in_path.metadata = {"url": "/validation/constantsInPath/{constantParam}/value"}

    @overload
    async def post_with_constant_in_body(
        self, body: Optional[_models.Product] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Product:
        """post_with_constant_in_body.

        :param body: Default value is None.
        :type body: ~validation.models.Product
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword constant_param: Default value is "constant". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype constant_param: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def post_with_constant_in_body(
        self, body: Optional[IO] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Product:
        """post_with_constant_in_body.

        :param body: Default value is None.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword constant_param: Default value is "constant". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype constant_param: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def post_with_constant_in_body(
        self, body: Optional[Union[_models.Product, IO]] = None, **kwargs: Any
    ) -> _models.Product:
        """post_with_constant_in_body.

        :param body: Is either a Product type or a IO type. Default value is None.
        :type body: ~validation.models.Product or IO
        :keyword constant_param: Default value is "constant". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype constant_param: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~validation.models.Product
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

        constant_param: Literal["constant"] = kwargs.pop("constant_param", "constant")
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Product] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            if body is not None:
                _json = self._serialize.body(body, "Product")
            else:
                _json = None

        request = build_post_with_constant_in_body_request(
            constant_param=constant_param,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.post_with_constant_in_body.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    post_with_constant_in_body.metadata = {"url": "/validation/constantsInPath/{constantParam}/value"}
