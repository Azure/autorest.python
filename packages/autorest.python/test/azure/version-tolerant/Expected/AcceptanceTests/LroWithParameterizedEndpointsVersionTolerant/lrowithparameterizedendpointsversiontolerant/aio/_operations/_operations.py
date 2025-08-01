# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
from typing import Any, AsyncIterator, Callable, Dict, Literal, Optional, TypeVar, Union, cast

from azure.core import AsyncPipelineClient
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
from azure.core.pipeline import PipelineResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.polling.async_base_polling import AsyncLROBasePolling
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ..._operations._operations import (
    build_lro_with_paramaterized_endpoints_poll_with_constant_parameterized_endpoints_request,
    build_lro_with_paramaterized_endpoints_poll_with_parameterized_endpoints_request,
)
from ..._utils.utils import ClientMixinABC
from .._configuration import LROWithParamaterizedEndpointsConfiguration

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class _LROWithParamaterizedEndpointsOperationsMixin(
    ClientMixinABC[AsyncPipelineClient[HttpRequest, AsyncHttpResponse], LROWithParamaterizedEndpointsConfiguration]
):

    async def _poll_with_parameterized_endpoints_initial(  # pylint: disable=name-too-long
        self, account_name: str, **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        _request = build_lro_with_paramaterized_endpoints_poll_with_parameterized_endpoints_request(
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, cast(AsyncIterator[bytes], deserialized), response_headers)  # type: ignore

        return cast(AsyncIterator[bytes], deserialized)  # type: ignore

    @distributed_trace_async
    async def begin_poll_with_parameterized_endpoints(self, account_name: str, **kwargs: Any) -> AsyncLROPoller[str]:
        """Poll with method and client level parameters in endpoint.

        :param account_name: Account Name. Pass in 'local' to pass test. Required.
        :type account_name: str
        :return: An instance of AsyncLROPoller that returns str
        :rtype: ~azure.core.polling.AsyncLROPoller[str]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[str] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._poll_with_parameterized_endpoints_initial(
                account_name=account_name, cls=lambda x, y, z: x, headers=_headers, params=_params, **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncLROBasePolling(
                    lro_delay,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=path_format_arguments,
                    **kwargs
                ),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[str].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[str](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    async def _poll_with_constant_parameterized_endpoints_initial(  # pylint: disable=name-too-long
        self, account_name: str, **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        constant_parameter: Literal["iAmConstant"] = kwargs.pop("constant_parameter", "iAmConstant")
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        _request = build_lro_with_paramaterized_endpoints_poll_with_constant_parameterized_endpoints_request(
            constant_parameter=constant_parameter,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, cast(AsyncIterator[bytes], deserialized), response_headers)  # type: ignore

        return cast(AsyncIterator[bytes], deserialized)  # type: ignore

    @distributed_trace_async
    async def begin_poll_with_constant_parameterized_endpoints(  # pylint: disable=name-too-long
        self, account_name: str, **kwargs: Any
    ) -> AsyncLROPoller[str]:
        """Poll with method and client level parameters in endpoint, with a constant value.

        :param account_name: Account Name. Pass in 'local' to pass test. Required.
        :type account_name: str
        :return: An instance of AsyncLROPoller that returns str
        :rtype: ~azure.core.polling.AsyncLROPoller[str]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        constant_parameter: Literal["iAmConstant"] = kwargs.pop("constant_parameter", "iAmConstant")
        cls: ClsType[str] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._poll_with_constant_parameterized_endpoints_initial(
                account_name=account_name,
                constant_parameter=constant_parameter,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncLROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[str].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[str](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore
