# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar, Union, cast

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
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._lro_with_paramaterized_endpoints_operations import (
    build_poll_with_constant_parameterized_endpoints_request,
    build_poll_with_parameterized_endpoints_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class LROWithParamaterizedEndpointsOperationsMixin:
    async def _poll_with_parameterized_endpoints_initial(self, account_name: str, **kwargs: Any) -> Optional[str]:
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[str]]

        request = build_poll_with_parameterized_endpoints_request(
            template_url=self._poll_with_parameterized_endpoints_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("str", pipeline_response)

        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _poll_with_parameterized_endpoints_initial.metadata = {"url": "/lroParameterizedEndpoints"}  # type: ignore

    @distributed_trace_async
    async def begin_poll_with_parameterized_endpoints(self, account_name: str, **kwargs: Any) -> AsyncLROPoller[str]:
        """Poll with method and client level parameters in endpoint.

        :param account_name: Account Name. Pass in 'local' to pass test.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either str or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._poll_with_parameterized_endpoints_initial(  # type: ignore
                account_name=account_name, cls=lambda x, y, z: x, headers=_headers, params=_params, **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("str", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }

        if polling is True:
            polling_method = cast(
                AsyncPollingMethod,
                AsyncLROBasePolling(
                    lro_delay,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=path_format_arguments,
                    **kwargs
                ),
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

    begin_poll_with_parameterized_endpoints.metadata = {"url": "/lroParameterizedEndpoints"}  # type: ignore

    async def _poll_with_constant_parameterized_endpoints_initial(
        self, account_name: str, **kwargs: Any
    ) -> Optional[str]:
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        constant_parameter = kwargs.pop("constant_parameter", "iAmConstant")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[str]]

        request = build_poll_with_constant_parameterized_endpoints_request(
            constant_parameter=constant_parameter,
            template_url=self._poll_with_constant_parameterized_endpoints_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("str", pipeline_response)

        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _poll_with_constant_parameterized_endpoints_initial.metadata = {"url": "/lroConstantParameterizedEndpoints/{constantParameter}"}  # type: ignore

    @distributed_trace_async
    async def begin_poll_with_constant_parameterized_endpoints(
        self, account_name: str, **kwargs: Any
    ) -> AsyncLROPoller[str]:
        """Poll with method and client level parameters in endpoint, with a constant value.

        :param account_name: Account Name. Pass in 'local' to pass test.
        :type account_name: str
        :keyword constant_parameter: Next link for the list operation. Default value is "iAmConstant".
         Note that overriding this default value may result in unsupported behavior.
        :paramtype constant_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either str or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        constant_parameter = kwargs.pop("constant_parameter", "iAmConstant")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._poll_with_constant_parameterized_endpoints_initial(  # type: ignore
                account_name=account_name,
                constant_parameter=constant_parameter,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("str", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }

        if polling is True:
            polling_method = cast(
                AsyncPollingMethod,
                AsyncLROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs),
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

    begin_poll_with_constant_parameterized_endpoints.metadata = {"url": "/lroConstantParameterizedEndpoints/{constantParameter}"}  # type: ignore
