# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from azure.core.async_paging import AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.polling import AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from my.library.aio import AsyncCustomDefaultPollingMethod, AsyncCustomPager, AsyncCustomPoller

from ..._operations._operations import (
    build_polling_paging_example_basic_paging_request,
    build_polling_paging_example_basic_polling_request,
)
from .._vendor import PollingPagingExampleMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PollingPagingExampleOperationsMixin(PollingPagingExampleMixinABC):
    async def _basic_polling_initial(self, product: Optional[Union[JSON, IO]] = None, **kwargs: Any) -> Optional[JSON]:
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
        cls: ClsType[Optional[JSON]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(product, (IOBase, bytes)):
            _content = product
        else:
            if product is not None:
                _json = product
            else:
                _json = None

        request = build_polling_paging_example_basic_polling_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @overload
    async def begin_basic_polling(
        self, product: Optional[JSON] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncCustomPoller[JSON]:
        """A simple polling operation.

        :param product: Product to put. Default value is None.
        :type product: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncCustomDefaultPollingMethod. Pass
         in False for this operation to not poll, or pass in your own initialized polling object for a
         personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncCustomPoller that returns JSON object
        :rtype: ~my.library.aio.AsyncCustomPoller[JSON]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                product = {
                    "properties": {
                        "id": 0,  # Optional.
                        "name": "str"  # Optional.
                    }
                }

                # response body for status code(s): 200
                response == {
                    "properties": {
                        "id": 0,  # Optional.
                        "name": "str"  # Optional.
                    }
                }
        """

    @overload
    async def begin_basic_polling(
        self, product: Optional[IO] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncCustomPoller[JSON]:
        """A simple polling operation.

        :param product: Product to put. Default value is None.
        :type product: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncCustomDefaultPollingMethod. Pass
         in False for this operation to not poll, or pass in your own initialized polling object for a
         personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncCustomPoller that returns JSON object
        :rtype: ~my.library.aio.AsyncCustomPoller[JSON]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "properties": {
                        "id": 0,  # Optional.
                        "name": "str"  # Optional.
                    }
                }
        """

    @distributed_trace_async
    async def begin_basic_polling(
        self, product: Optional[Union[JSON, IO]] = None, **kwargs: Any
    ) -> AsyncCustomPoller[JSON]:
        """A simple polling operation.

        :param product: Product to put. Is either a JSON type or a IO type. Default value is None.
        :type product: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncCustomDefaultPollingMethod. Pass
         in False for this operation to not poll, or pass in your own initialized polling object for a
         personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncCustomPoller that returns JSON object
        :rtype: ~my.library.aio.AsyncCustomPoller[JSON]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                product = {
                    "properties": {
                        "id": 0,  # Optional.
                        "name": "str"  # Optional.
                    }
                }

                # response body for status code(s): 200
                response == {
                    "properties": {
                        "id": 0,  # Optional.
                        "name": "str"  # Optional.
                    }
                }
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[JSON] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._basic_polling_initial(
                product=product,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
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

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod, AsyncCustomDefaultPollingMethod(lro_delay, **kwargs)
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncCustomPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncCustomPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    @distributed_trace
    def basic_paging(self, **kwargs: Any) -> AsyncIterable[JSON]:
        """A simple paging operation.

        :return: An iterator like instance of JSON object
        :rtype: ~my.library.aio.AsyncCustomPager[JSON]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "properties": {
                        "id": 0,  # Optional.
                        "name": "str"  # Optional.
                    }
                }
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[JSON] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_polling_paging_example_basic_paging_request(
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
            list_of_elem = deserialized["value"]
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

        return AsyncCustomPager(get_next, extract_data)
