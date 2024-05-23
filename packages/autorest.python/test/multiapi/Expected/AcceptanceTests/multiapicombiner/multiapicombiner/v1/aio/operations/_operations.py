# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, Type, TypeVar, Union, cast, overload
import urllib.parse

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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._operations import (
    build_multiapi_service_test_different_calls_request,
    build_multiapi_service_test_lro_and_paging_request,
    build_multiapi_service_test_lro_request,
    build_multiapi_service_test_one_request,
    build_operation_group_one_test_two_request,
)
from .._vendor import MultiapiServiceClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class MultiapiServiceClientOperationsMixin(MultiapiServiceClientMixinABC):
    def _api_version(self, op_name: str) -> str:  # pylint: disable=unused-argument
        try:
            return self._config.api_version
        except:  # pylint: disable=bare-except
            return ""

    @distributed_trace_async
    async def test_one(  # pylint: disable=inconsistent-return-statements
        self, *, id: int, message: Optional[str] = None, **kwargs: Any
    ) -> None:
        """TestOne should be in an FirstVersionOperationsMixin.

        :keyword id: An int parameter. Required.
        :paramtype id: int
        :keyword message: An optional string parameter. Default value is None.
        :paramtype message: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version("test_one") or "1.0.0")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_multiapi_service_test_one_request(
            id=id,
            message=message,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def _test_lro_initial(
        self, product: Optional[Union[_models.Product, IO[bytes]]] = None, **kwargs: Any
    ) -> Optional[_models.Product]:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.Product]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(product, (IOBase, bytes)):
            _content = product
        else:
            if product is not None:
                _json = self._serialize.body(product, "Product")
            else:
                _json = None

        _request = build_multiapi_service_test_lro_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            if _stream:
                await response.load_body()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            if _stream:
                deserialized = (await response.load_body()) or response._content  # pylint: disable=protected-access
            else:
                deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_test_lro(
        self, product: Optional[_models.Product] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.Product]:
        """Put in whatever shape of Product you want, will return a Product with id equal to 100.

        :param product: Product to put. Default value is None.
        :type product: ~multiapicombiner.v1.models.Product
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Product or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~multiapicombiner.v1.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_test_lro(
        self, product: Optional[IO[bytes]] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.Product]:
        """Put in whatever shape of Product you want, will return a Product with id equal to 100.

        :param product: Product to put. Default value is None.
        :type product: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Product or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~multiapicombiner.v1.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_test_lro(
        self, product: Optional[Union[_models.Product, IO[bytes]]] = None, **kwargs: Any
    ) -> AsyncLROPoller[_models.Product]:
        """Put in whatever shape of Product you want, will return a Product with id equal to 100.

        :param product: Product to put. Is either a Product type or a IO[bytes] type. Default value is
         None.
        :type product: ~multiapicombiner.v1.models.Product or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either Product or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~multiapicombiner.v1.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Product] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._test_lro_initial(
                product=product,
                content_type=content_type,
                cls=lambda x, y, z: x,
                stream=True,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("Product", pipeline_response.http_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.Product].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.Product](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _test_lro_and_paging_initial(
        self,
        test_lro_and_paging_options: Optional[_models.TestLroAndPagingOptions] = None,
        *,
        client_request_id: Optional[str] = None,
        **kwargs: Any
    ) -> _models.PagingResult:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.PagingResult] = kwargs.pop("cls", None)

        _maxresults = None
        _timeout = None
        if test_lro_and_paging_options is not None:
            _maxresults = test_lro_and_paging_options.maxresults
            _timeout = test_lro_and_paging_options.timeout

        _request = build_multiapi_service_test_lro_and_paging_request(
            client_request_id=client_request_id,
            maxresults=_maxresults,
            timeout=_timeout,  # type: ignore
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.load_body()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if _stream:
            deserialized = (await response.load_body()) or response._content  # pylint: disable=protected-access
        else:
            deserialized = self._deserialize("PagingResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def begin_test_lro_and_paging(
        self,
        test_lro_and_paging_options: Optional[_models.TestLroAndPagingOptions] = None,
        *,
        client_request_id: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[AsyncIterable["_models.Product"]]:
        """A long-running paging operation that includes a nextLink that has 10 pages.

        :param test_lro_and_paging_options: Parameter group. Default value is None.
        :type test_lro_and_paging_options: ~multiapicombiner.v1.models.TestLroAndPagingOptions
        :keyword client_request_id: Default value is None.
        :paramtype client_request_id: str
        :return: An instance of LROPoller that returns an iterator like instance of either PagingResult
         or the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.core.async_paging.AsyncItemPaged[~multiapicombiner.v1.models.Product]]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.PagingResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:
                _maxresults = None
                _timeout = None
                if test_lro_and_paging_options is not None:
                    _maxresults = test_lro_and_paging_options.maxresults
                    _timeout = test_lro_and_paging_options.timeout

                _request = build_multiapi_service_test_lro_and_paging_request(
                    client_request_id=client_request_id,
                    maxresults=_maxresults,
                    timeout=_timeout,  # type: ignore
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PagingResult", pipeline_response.http_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._test_lro_and_paging_initial(
                test_lro_and_paging_options=test_lro_and_paging_options,
                client_request_id=client_request_id,
                cls=lambda x, y, z: x,
                stream=True,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            async def internal_get_next(next_link=None):
                if next_link is None:
                    return pipeline_response
                return await get_next(next_link)

            return AsyncItemPaged(internal_get_next, extract_data)

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[AsyncIterable["_models.Product"]].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[AsyncIterable["_models.Product"]](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @distributed_trace_async
    async def test_different_calls(  # pylint: disable=inconsistent-return-statements
        self, *, greeting_in_english: str, **kwargs: Any
    ) -> None:
        """Has added parameters across the API versions.

        :keyword greeting_in_english: pass in 'hello' to pass test. Required.
        :paramtype greeting_in_english: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version("test_different_calls") or "1.0.0")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_multiapi_service_test_different_calls_request(
            greeting_in_english=greeting_in_english,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore


class OperationGroupOneOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~multiapicombiner.v1.aio.MultiapiServiceClient`'s
        :attr:`operation_group_one` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace_async
    async def test_two(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """TestTwo should be in OperationGroupOneOperations.

        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "1.0.0"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_operation_group_one_test_two_request(
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
