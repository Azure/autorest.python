# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar, Union, cast

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.polling.async_base_polling import AsyncLROBasePolling
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._dpg_client_operations import (
    build_get_model_request,
    build_get_pages_request,
    build_lro_request,
    build_post_model_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class DPGClientOperationsMixin:
    @distributed_trace_async
    async def get_model(self, mode: str, **kwargs: Any) -> _models.Product:
        """Get models that you will either return to end users as a raw body, or with a model added during
        grow up.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Required.
        :type mode: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~dpgcustomizationinitial.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Product]

        request = build_get_model_request(
            mode=mode,
            template_url=self.get_model.metadata["url"],
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
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_model.metadata = {"url": "/customization/model/{mode}"}  # type: ignore

    @distributed_trace_async
    async def post_model(self, mode: str, hello: str, **kwargs: Any) -> _models.Product:
        """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
        take a model instead, and put in 'model' as mode.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Required.
        :type mode: str
        :param hello: Required.
        :type hello: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~dpgcustomizationinitial.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Product]

        _input = _models.Input(hello=hello)
        _json = self._serialize.body(_input, "Input")

        request = build_post_model_request(
            mode=mode,
            content_type=content_type,
            json=_json,
            template_url=self.post_model.metadata["url"],
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
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    post_model.metadata = {"url": "/customization/model/{mode}"}  # type: ignore

    @distributed_trace
    def get_pages(self, mode: str, **kwargs: Any) -> AsyncIterable["_models.Product"]:
        """Get pages that you will either return to users in pages of raw bodies, or pages of models
        following growup.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Required.
        :type mode: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Product or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~dpgcustomizationinitial.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ProductResult]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_get_pages_request(
                    mode=mode,
                    template_url=self.get_pages.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:

                request = build_get_pages_request(
                    mode=mode,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ProductResult", pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    get_pages.metadata = {"url": "/customization/paging/{mode}"}  # type: ignore

    async def _lro_initial(self, mode: str, **kwargs: Any) -> _models.LROProduct:
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[_models.LROProduct]

        request = build_lro_request(
            mode=mode,
            template_url=self._lro_initial.metadata["url"],
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
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("LROProduct", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _lro_initial.metadata = {"url": "/customization/lro/{mode}"}  # type: ignore

    @distributed_trace_async
    async def begin_lro(self, mode: str, **kwargs: Any) -> AsyncLROPoller[_models.LROProduct]:
        """Long running put request that will either return to end users a final payload of a raw body, or
        a final payload of a model after the SDK has grown up.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Required.
        :type mode: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either LROProduct or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~dpgcustomizationinitial.models.LROProduct]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[_models.LROProduct]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._lro_initial(  # type: ignore
                mode=mode, cls=lambda x, y, z: x, headers=_headers, params=_params, **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("LROProduct", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = cast(
                AsyncPollingMethod, AsyncLROBasePolling(lro_delay, **kwargs)
            )  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_lro.metadata = {"url": "/customization/lro/{mode}"}  # type: ignore
