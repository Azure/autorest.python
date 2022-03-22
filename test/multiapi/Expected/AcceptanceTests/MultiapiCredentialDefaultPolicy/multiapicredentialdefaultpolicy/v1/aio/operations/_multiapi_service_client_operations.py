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
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._multiapi_service_client_operations import build_test_different_calls_request, build_test_lro_and_paging_request_initial, build_test_lro_request_initial, build_test_one_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MultiapiServiceClientOperationsMixin:

    @distributed_trace_async
    async def test_one(  # pylint: disable=inconsistent-return-statements
        self,
        id: int,
        message: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """TestOne should be in an FirstVersionOperationsMixin.

        :param id: An int parameter.
        :type id: int
        :param message: An optional string parameter. Default value is None.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "1.0.0")  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_test_one_request(
            api_version=api_version,
            id=id,
            message=message,
            template_url=self.test_one.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_one.metadata = {'url': "/multiapi/testOneEndpoint"}  # type: ignore


    async def _test_lro_initial(
        self,
        product: Optional[_models.Product] = None,
        **kwargs: Any
    ) -> Optional[_models.Product]:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional[_models.Product]]

        if product is not None:
            _json = self._serialize.body(product, 'Product')
        else:
            _json = None

        request = build_test_lro_request_initial(
            content_type=content_type,
            json=_json,
            template_url=self._test_lro_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Product', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _test_lro_initial.metadata = {'url': "/multiapi/lro"}  # type: ignore


    @distributed_trace_async
    async def begin_test_lro(
        self,
        product: Optional[_models.Product] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Product]:
        """Put in whatever shape of Product you want, will return a Product with id equal to 100.

        :param product: Product to put. Default value is None.
        :type product: ~multiapicredentialdefaultpolicy.v1.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either Product or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~multiapicredentialdefaultpolicy.v1.models.Product]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.Product]
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._test_lro_initial(  # type: ignore
                product=product,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('Product', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(
                lro_delay,
                
                
                **kwargs
        ))  # type: AsyncPollingMethod
        elif polling is False: polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_test_lro.metadata = {'url': "/multiapi/lro"}  # type: ignore

    async def _test_lro_and_paging_initial(
        self,
        client_request_id: Optional[str] = None,
        test_lro_and_paging_options: Optional[_models.TestLroAndPagingOptions] = None,
        **kwargs: Any
    ) -> _models.PagingResult:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        cls = kwargs.pop('cls', None)  # type: ClsType[_models.PagingResult]

        _maxresults = None
        _timeout = None
        if test_lro_and_paging_options is not None:
            _maxresults = test_lro_and_paging_options.maxresults
            _timeout = test_lro_and_paging_options.timeout

        request = build_test_lro_and_paging_request_initial(
            client_request_id=client_request_id,
            maxresults=_maxresults,
            timeout=_timeout,
            template_url=self._test_lro_and_paging_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PagingResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _test_lro_and_paging_initial.metadata = {'url': "/multiapi/lroAndPaging"}  # type: ignore


    @distributed_trace_async
    async def begin_test_lro_and_paging(
        self,
        client_request_id: Optional[str] = None,
        test_lro_and_paging_options: Optional[_models.TestLroAndPagingOptions] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[AsyncItemPaged[_models.PagingResult]]:
        """A long-running paging operation that includes a nextLink that has 10 pages.

        :param client_request_id:  Default value is None.
        :type client_request_id: str
        :param test_lro_and_paging_options: Parameter group. Default value is None.
        :type test_lro_and_paging_options:
         ~multiapicredentialdefaultpolicy.v1.models.TestLroAndPagingOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns an iterator like instance of either
         PagingResult or the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.core.async_paging.AsyncItemPaged[~multiapicredentialdefaultpolicy.v1.models.PagingResult]]
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        cls = kwargs.pop('cls', None)  # type: ClsType[_models.PagingResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                _maxresults = None
                _timeout = None
                if test_lro_and_paging_options is not None:
                    _maxresults = test_lro_and_paging_options.maxresults
                    _timeout = test_lro_and_paging_options.timeout
                
                request = build_test_lro_and_paging_request_initial(
                    client_request_id=client_request_id,
                    maxresults=_maxresults,
                    timeout=_timeout,
                    template_url=self.begin_test_lro_and_paging.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                _maxresults = None
                _timeout = None
                if test_lro_and_paging_options is not None:
                    _maxresults = test_lro_and_paging_options.maxresults
                    _timeout = test_lro_and_paging_options.timeout
                
                request = build_test_lro_and_paging_request_initial(
                    client_request_id=client_request_id,
                    maxresults=_maxresults,
                    timeout=_timeout,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PagingResult", pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._test_lro_and_paging_initial(  # type: ignore
                client_request_id=client_request_id,
                test_lro_and_paging_options=test_lro_and_paging_options,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            async def internal_get_next(next_link=None):
                if next_link is None:
                    return pipeline_response
                return await get_next(next_link)

            return AsyncItemPaged(
                internal_get_next, extract_data
            )

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(
                lro_delay,
                
                
                **kwargs
        ))  # type: AsyncPollingMethod
        elif polling is False: polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_test_lro_and_paging.metadata = {'url': "/multiapi/lroAndPaging"}  # type: ignore


    @distributed_trace_async
    async def test_different_calls(  # pylint: disable=inconsistent-return-statements
        self,
        greeting_in_english: str,
        **kwargs: Any
    ) -> None:
        """Has added parameters across the API versions.

        :param greeting_in_english: pass in 'hello' to pass test.
        :type greeting_in_english: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "1.0.0")  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_test_different_calls_request(
            api_version=api_version,
            greeting_in_english=greeting_in_english,
            template_url=self.test_different_calls.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_different_calls.metadata = {'url': "/multiapi/testDifferentCalls"}  # type: ignore

