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
from typing import Any, AsyncIterable, Callable, Dict, IO, List, Optional, TypeVar, Union, overload

from azure.core.async_paging import AsyncItemPaged, AsyncList
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
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import AzureJSONEncoder, _deserialize
from ..._operations._operations import (
    build_dev_driven_get_model_request,
    build_dev_driven_get_pages_request,
    build_dev_driven_lro_request,
    build_dev_driven_post_model_request,
)
from .._vendor import DevDrivenClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class DevDrivenClientOperationsMixin(DevDrivenClientMixinABC):
    @distributed_trace_async
    async def get_model(self, mode: Union[str, _models.Mode], **kwargs: Any) -> _models.Product:
        """Get models that you will either return to end users as a raw body, or with a model added during
        grow up.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Product. The Product is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.Product
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

        cls: ClsType[_models.Product] = kwargs.pop("cls", None)

        request = build_dev_driven_get_model_request(
            mode=mode,
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

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Product, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def post_model(self, mode: Union[str, _models.Mode], input: IO, **kwargs: Any) -> _models.Product:
        """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
        take a model instead, and put in 'model' as mode.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :param input: Please put {'hello': 'world!'}. Required.
        :type input: IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Product. The Product is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def post_model(self, mode: Union[str, _models.Mode], input: JSON, **kwargs: Any) -> _models.Product:
        """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
        take a model instead, and put in 'model' as mode.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :param input: Please put {'hello': 'world!'}. Required.
        :type input: JSON
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Product. The Product is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def post_model(
        self, mode: Union[str, _models.Mode], input: Union[_models.Input, IO, JSON], **kwargs: Any
    ) -> _models.Product:
        """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
        take a model instead, and put in 'model' as mode.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :param input: Please put {'hello': 'world!'}. Is one of the following types: Input, IO, JSON
         Required.
        :type input: ~resiliency.devdriven.models.Input or IO or JSON
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Product. The Product is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.Product
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

        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[_models.Product] = kwargs.pop("cls", None)

        _content: Any = None
        if isinstance(input, (IO, bytes)):
            _content = json.dumps(input, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        elif isinstance(input, MutableMapping):
            _content = json.dumps(input, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        else:
            raise TypeError("unrecognized type for input")

        request = build_dev_driven_post_model_request(
            mode=mode,
            content_type=content_type,
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

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Product, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def get_pages(self, **kwargs: Any) -> AsyncIterable["_models.Product"]:
        """Get pages that you will either return to users in pages of raw bodies, or pages of models
        following group.

        :return: An iterator like instance of Product. The Product is compatible with MutableMapping
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~resiliency.devdriven.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models._models.CustomPageProduct] = kwargs.pop("cls", None)  # pylint: disable=protected-access

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_dev_driven_get_pages_request(
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                request.url = self._client.format_url(request.url)

            else:
                request = HttpRequest("GET", next_link)
                request.url = self._client.format_url(request.url)

            return request

        async def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.Product], deserialized["value"])
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def lro(self, mode: Union[str, _models.Mode], **kwargs: Any) -> _models.LroProduct:
        """Long running put request that will either return to end users a final payload of a raw body, or
        a final payload of a model after the SDK has grown up.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: LroProduct. The LroProduct is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.LroProduct
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

        cls: ClsType[_models.LroProduct] = kwargs.pop("cls", None)

        request = build_dev_driven_lro_request(
            mode=mode,
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

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.LroProduct, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
