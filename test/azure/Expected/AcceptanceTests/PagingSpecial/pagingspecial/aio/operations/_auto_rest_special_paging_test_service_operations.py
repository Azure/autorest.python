# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging_method import BasicPagingMethod
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat
from customdefinitions.aio import AsyncPagerWithMetadata

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class AutoRestSpecialPagingTestServiceOperationsMixin:

    def _next_link_in_response_headers_initial(
        self,
        next_link: str,
        **kwargs
    ) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = next_link

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        return request
    _next_link_in_response_headers_initial.metadata = {'url': '/pagingSpecial/nextLinkInResponseHeaders'}  # type: ignore

    @distributed_trace
    def next_link_in_response_headers(
        self,
        **kwargs
    ) -> AsyncIterable["_models.ProductResultValue"]:
        """A paging operation where the next link is found in the response headers, not in the response
        body.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProductResultValue or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~pagingspecial.models.ProductResultValue]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        def deserialize_output(pipeline_response):
            return self._deserialize('ProductResultValue', pipeline_response)

        _initial_request = self._next_link_in_response_headers_initial(
            next_link=self._next_link_in_response_headers_initial.metadata['url'],
        )
        _next_request_partial = functools.partial(
            self._next_link_in_response_headers_initial,
        )
        return AsyncItemPaged(
            paging_method = kwargs.pop("paging_method", BasicPagingMethod()),
            client=self._client,
            deserialize_output=deserialize_output,
            continuation_token_location=None,
            initial_request=_initial_request,
            next_request_partial=_next_request_partial,
            _cls=kwargs.pop("cls", None),
            **kwargs,
        )

    def _continuation_token_initial(
        self,
        next_link: str,
        **kwargs
    ) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = next_link

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        return request
    _continuation_token_initial.metadata = {'url': '/pagingSpecial/continuationToken'}  # type: ignore

    @distributed_trace
    def continuation_token(
        self,
        **kwargs
    ) -> AsyncIterable["_models.ProductResultValueWithToken"]:
        """A paging operation where the token in the response body needs to be passed into subsequent
        calls.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProductResultValueWithToken or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~pagingspecial.models.ProductResultValueWithToken]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        def deserialize_output(pipeline_response):
            return self._deserialize('ProductResultValueWithToken', pipeline_response)

        _initial_request = self._continuation_token_initial(
            next_link=self._continuation_token_initial.metadata['url'],
        )
        _next_request_partial = functools.partial(
            self._continuation_token_initial,
        )
        return AsyncItemPaged(
            paging_method = kwargs.pop("paging_method", BasicPagingMethod()),
            client=self._client,
            deserialize_output=deserialize_output,
            continuation_token_location='token',
            initial_request=_initial_request,
            next_request_partial=_next_request_partial,
            _cls=kwargs.pop("cls", None),
            **kwargs,
        )

    def _continuation_token_in_response_headers_initial(
        self,
        next_link: str,
        continuation_token_parameter: Optional[str] = None,
        **kwargs
    ) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = next_link

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if continuation_token_parameter is not None:
            header_parameters['continuationToken'] = self._serialize.header("continuation_token_parameter", continuation_token_parameter, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        return request
    _continuation_token_in_response_headers_initial.metadata = {'url': '/pagingSpecial/continuationTokenInResponseHeaders'}  # type: ignore

    @distributed_trace
    def continuation_token_in_response_headers(
        self,
        continuation_token_parameter: Optional[str] = None,
        **kwargs
    ) -> AsyncIterable["_models.ProductResultValueWithToken"]:
        """A paging operation where the continuation is found in the response headers, and needs to be
        passed into subsequent calls.

        :param continuation_token_parameter: Continuation token for subsequent paging.
        :type continuation_token_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProductResultValueWithToken or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~pagingspecial.models.ProductResultValueWithToken]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        def deserialize_output(pipeline_response):
            return self._deserialize('ProductResultValueWithToken', pipeline_response)

        _initial_request = self._continuation_token_in_response_headers_initial(
            next_link=self._continuation_token_in_response_headers_initial.metadata['url'],
            continuation_token_parameter=continuation_token_parameter,
        )
        _next_request_partial = functools.partial(
            self._continuation_token_in_response_headers_initial,
            continuation_token_parameter=continuation_token_parameter,
        )
        return AsyncItemPaged(
            paging_method = kwargs.pop("paging_method", BasicPagingMethod()),
            client=self._client,
            deserialize_output=deserialize_output,
            continuation_token_location=None,
            initial_request=_initial_request,
            next_request_partial=_next_request_partial,
            _cls=kwargs.pop("cls", None),
            **kwargs,
        )

    def _token_with_metadata_initial(
        self,
        next_link: str,
        **kwargs
    ) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = next_link

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        return request
    _token_with_metadata_initial.metadata = {'url': '/pagingSpecial/tokenWithMetadata'}  # type: ignore

    @distributed_trace
    def token_with_metadata(
        self,
        **kwargs
    ) -> AsyncIterable["_models.ProductResultValueWithToken"]:
        """A paging operation that returns a continuation token, and metadata about the number of total
        results. Should be able to access metadata from pager.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProductResultValueWithToken or the result of cls(response)
        :rtype: ~customdefinitions.aio.AsyncPagerWithMetadata[~pagingspecial.models.ProductResultValueWithToken]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        def deserialize_output(pipeline_response):
            return self._deserialize('ProductResultValueWithToken', pipeline_response)

        _initial_request = self._token_with_metadata_initial(
            next_link=self._token_with_metadata_initial.metadata['url'],
        )
        _next_request_partial = functools.partial(
            self._token_with_metadata_initial,
        )
        return AsyncPagerWithMetadata(
            paging_method = kwargs.pop("paging_method", BasicPagingMethod()),
            client=self._client,
            deserialize_output=deserialize_output,
            continuation_token_location='token',
            initial_request=_initial_request,
            next_request_partial=_next_request_partial,
            _cls=kwargs.pop("cls", None),
            **kwargs,
        )

    def _next_link_and_continuation_token_initial(
        self,
        next_link: str,
        continuation_token_parameter: Optional[str] = None,
        **kwargs
    ) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = next_link

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if continuation_token_parameter is not None:
            header_parameters['continuationToken'] = self._serialize.header("continuation_token_parameter", continuation_token_parameter, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        return request
    _next_link_and_continuation_token_initial.metadata = {'url': '/pagingSpecial/nextLinkAndContinuationToken'}  # type: ignore

    @distributed_trace
    def next_link_and_continuation_token(
        self,
        continuation_token_parameter: Optional[str] = None,
        **kwargs
    ) -> AsyncIterable["_models.ProductResultValueWithToken"]:
        """A paging operation that returns a continuation token. The token is part continuation token that
        needs to be passed as a header to subsequent calls, and part next link, the url for subsequent
        calls.

        :param continuation_token_parameter: Continuation token for subsequent paging.
        :type continuation_token_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProductResultValueWithToken or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~pagingspecial.models.ProductResultValueWithToken]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        def deserialize_output(pipeline_response):
            return self._deserialize('ProductResultValueWithToken', pipeline_response)

        _initial_request = self._next_link_and_continuation_token_initial(
            next_link=self._next_link_and_continuation_token_initial.metadata['url'],
            continuation_token_parameter=continuation_token_parameter,
        )
        _next_request_partial = functools.partial(
            self._next_link_and_continuation_token_initial,
            continuation_token_parameter=continuation_token_parameter,
        )
        return AsyncItemPaged(
            paging_method = kwargs.pop("paging_method", BasicPagingMethod()),
            client=self._client,
            deserialize_output=deserialize_output,
            continuation_token_location='token',
            initial_request=_initial_request,
            next_request_partial=_next_request_partial,
            _cls=kwargs.pop("cls", None),
            **kwargs,
        )

    def _continuation_token_initial_operation_initial(
        self,
        **kwargs
    ) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = self._continuation_token_initial_operation_initial.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        return request
    _continuation_token_initial_operation_initial.metadata = {'url': '/pagingSpecial/continuationTokenInitialOperation'}  # type: ignore

    def _continuation_token_initial_operation_next(
        self,
        **kwargs
    ) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = self._continuation_token_initial_operation_next.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        return request
    _continuation_token_initial_operation_next.metadata = {'url': '/pagingSpecial/continuationTokenNextOperation'}  # type: ignore

    @distributed_trace
    def continuation_token_initial_operation(
        self,
        **kwargs
    ) -> AsyncIterable["_models.ProductResultValueWithToken"]:
        """A paging operation where the token in the response body needs to be passed into a separate next
        operation. The separate next operation is not defined with the token input parameter.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProductResultValueWithToken or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~pagingspecial.models.ProductResultValueWithToken]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        def deserialize_output(pipeline_response):
            return self._deserialize('ProductResultValueWithToken', pipeline_response)

        _initial_request = self._continuation_token_initial_operation_initial(
            next_link=self._continuation_token_initial_operation_initial.metadata['url'],
        )
        _next_request_partial = functools.partial(
            self._continuation_token_initial_operation_next,
        )
        return AsyncItemPaged(
            paging_method = kwargs.pop("paging_method", BasicPagingMethod()),
            client=self._client,
            deserialize_output=deserialize_output,
            continuation_token_location='token',
            initial_request=_initial_request,
            next_request_partial=_next_request_partial,
            _cls=kwargs.pop("cls", None),
            **kwargs,
        )
