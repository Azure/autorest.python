# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import map_error
from azure.core.polling import AsyncNoPolling, async_poller
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMError
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling
from msrest.serialization import Model

from ... import models


class PagingOperations:
    """PagingOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~paging.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    async def get_no_item_name_pages(
        self,
        cls=None,
        **kwargs
    ) -> "ProductResultValue":
        """A paging operation that must return result of the default 'value' node..

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: ProductResultValue or the result of cls(response)
        :rtype: ~paging.models.ProductResultValue
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_no_item_name_pages.metadata['url']
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('ProductResultValue', response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_no_item_name_pages.metadata = {'url': '/paging/noitemname'}


    @distributed_trace
    async def get_null_next_link_name_pages(
        self,
        cls=None,
        **kwargs
    ) -> "ProductResult":
        """A paging operation that must ignore any kind of nextLink, and stop after page 1..

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_null_next_link_name_pages.metadata['url']
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('ProductResult', response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_null_next_link_name_pages.metadata = {'url': '/paging/nullnextlink'}


    @distributed_trace
    async def get_single_pages(
        self,
        cls=None,
        **kwargs
    ) -> "ProductResult":
        """A paging operation that finishes on the first call without a nextlink.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_single_pages.metadata['url']
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('ProductResult', response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_single_pages.metadata = {'url': '/paging/single'}


    @distributed_trace
    async def get_multiple_pages(
        self,
        client_request_id: Optional[str] = None,
        maxresults: Optional[int] = None,
        timeout: Optional[int] = None,
        *,
        cls=None,
        **kwargs
    ) -> "ProductResult":
        """A paging operation that includes a nextLink that has 10 pages.

        FIXME: add operation.summary


        :param client_request_id: MISSING·PARAMETER-DESCRIPTION
        :type client_request_id: str
        :param maxresults: Sets the maximum number of items to return in the response.
        :type maxresults: int
        :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages.metadata['url']
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}


            # Construct headers
            header_parameters = {}
            if client_request_id is not None:
                header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
            if maxresults is not None:
                header_parameters['maxresults'] = self._serialize.header("maxresults", maxresults, 'int')
            if timeout is not None:
                header_parameters['timeout'] = self._serialize.header("timeout", timeout, 'int')
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('ProductResult', response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_multiple_pages.metadata = {'url': '/paging/multiple'}


    @distributed_trace
    async def get_odata_multiple_pages(
        self,
        client_request_id: Optional[str] = None,
        maxresults: Optional[int] = None,
        timeout: Optional[int] = None,
        *,
        cls=None,
        **kwargs
    ) -> "OdataProductResult":
        """A paging operation that includes a nextLink in odata format that has 10 pages.

        FIXME: add operation.summary


        :param client_request_id: MISSING·PARAMETER-DESCRIPTION
        :type client_request_id: str
        :param maxresults: Sets the maximum number of items to return in the response.
        :type maxresults: int
        :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: OdataProductResult or the result of cls(response)
        :rtype: ~paging.models.OdataProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_odata_multiple_pages.metadata['url']
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}


            # Construct headers
            header_parameters = {}
            if client_request_id is not None:
                header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
            if maxresults is not None:
                header_parameters['maxresults'] = self._serialize.header("maxresults", maxresults, 'int')
            if timeout is not None:
                header_parameters['timeout'] = self._serialize.header("timeout", timeout, 'int')
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('OdataProductResult', response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_odata_multiple_pages.metadata = {'url': '/paging/multiple/odata'}


    @distributed_trace
    async def get_multiple_pages_with_offset(
        self,
        offset: int,
        client_request_id: Optional[str] = None,
        maxresults: Optional[int] = None,
        timeout: Optional[int] = None,
        *,
        cls=None,
        **kwargs
    ) -> "ProductResult":
        """A paging operation that includes a nextLink that has 10 pages.

        FIXME: add operation.summary


        :param offset: Offset of return value
        :type offset: int
        :param client_request_id: MISSING·PARAMETER-DESCRIPTION
        :type client_request_id: str
        :param maxresults: Sets the maximum number of items to return in the response.
        :type maxresults: int
        :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_with_offset.metadata['url']
                path_format_arguments = {
                    'offset': self._serialize.url("offset", offset, 'int'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}


            # Construct headers
            header_parameters = {}
            if client_request_id is not None:
                header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
            if maxresults is not None:
                header_parameters['maxresults'] = self._serialize.header("maxresults", maxresults, 'int')
            if timeout is not None:
                header_parameters['timeout'] = self._serialize.header("timeout", timeout, 'int')
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('ProductResult', response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_with_offset.metadata = {'url': '/paging/multiple/withpath/{offset}'}


    @distributed_trace
    async def get_multiple_pages_retry_first(
        self,
        cls=None,
        **kwargs
    ) -> "ProductResult":
        """A paging operation that fails on the first call with 500 and then retries and then get a response including a nextLink that has 10 pages.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_retry_first.metadata['url']
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('ProductResult', response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_retry_first.metadata = {'url': '/paging/multiple/retryfirst'}


    @distributed_trace
    async def get_multiple_pages_retry_second(
        self,
        cls=None,
        **kwargs
    ) -> "ProductResult":
        """A paging operation that includes a nextLink that has 10 pages, of which the 2nd call fails first with 500. The client should retry and finish all 10 pages eventually..

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_retry_second.metadata['url']
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('ProductResult', response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_retry_second.metadata = {'url': '/paging/multiple/retrysecond'}


    @distributed_trace
    async def get_single_pages_failure(
        self,
        cls=None,
        **kwargs
    ) -> "ProductResult":
        """A paging operation that receives a 400 on the first call.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_single_pages_failure.metadata['url']
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('ProductResult', response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_single_pages_failure.metadata = {'url': '/paging/single/failure'}


    @distributed_trace
    async def get_multiple_pages_failure(
        self,
        cls=None,
        **kwargs
    ) -> "ProductResult":
        """A paging operation that receives a 400 on the second call.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_failure.metadata['url']
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('ProductResult', response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_failure.metadata = {'url': '/paging/multiple/failure'}


    @distributed_trace
    async def get_multiple_pages_failure_uri(
        self,
        cls=None,
        **kwargs
    ) -> "ProductResult":
        """A paging operation that receives an invalid nextLink.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_failure_uri.metadata['url']
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('ProductResult', response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_failure_uri.metadata = {'url': '/paging/multiple/failureuri'}


    @distributed_trace
    async def get_multiple_pages_fragment_next_link(
        self,
        api_version: str,
        tenant: str,
        *,
        cls=None,
        **kwargs
    ) -> "OdataProductResult":
        """A paging operation that doesn't return a full URL, just a fragment.

        FIXME: add operation.summary


        :param api_version: Sets the api version to use.
        :type api_version: str
        :param tenant: Sets the tenant to use.
        :type tenant: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: OdataProductResult or the result of cls(response)
        :rtype: ~paging.models.OdataProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_fragment_next_link.metadata['url']
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", tenant, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = '/paging/multiple/fragment/{tenant}/{nextLink}'
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", tenant, 'str'),
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)

            # Construct parameters
            query_parameters = {}
            query_parameters['api_version'] = self._serialize.query("api_version", api_version, 'str')


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('OdataProductResult', response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_fragment_next_link.metadata = {'url': '/paging/multiple/fragment/{tenant}'}


    @distributed_trace
    async def get_multiple_pages_fragment_with_grouping_next_link(
        self,
        api_version: str,
        tenant: str,
        *,
        cls=None,
        **kwargs
    ) -> "OdataProductResult":
        """A paging operation that doesn't return a full URL, just a fragment with parameters grouped.

        FIXME: add operation.summary


        :param api_version: Sets the api version to use.
        :type api_version: str
        :param tenant: Sets the tenant to use.
        :type tenant: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: OdataProductResult or the result of cls(response)
        :rtype: ~paging.models.OdataProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_fragment_with_grouping_next_link.metadata['url']
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", tenant, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = '/paging/multiple/fragmentwithgrouping/{tenant}/{nextLink}'
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", tenant, 'str'),
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)

            # Construct parameters
            query_parameters = {}
            query_parameters['api_version'] = self._serialize.query("api_version", api_version, 'str')


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('OdataProductResult', response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_fragment_with_grouping_next_link.metadata = {'url': '/paging/multiple/fragmentwithgrouping/{tenant}'}


    
    async def _get_multiple_pages_lro_initial(
        self,
        client_request_id: Optional[str] = None,
        maxresults: Optional[int] = None,
        timeout: Optional[int] = None,
        *,
        cls=None,
        **kwargs
    ) -> "ProductResult":
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self._get_multiple_pages_lro_initial.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        if client_request_id is not None:
            header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
        if maxresults is not None:
            header_parameters['maxresults'] = self._serialize.header("maxresults", maxresults, 'int')
        if timeout is not None:
            header_parameters['timeout'] = self._serialize.header("timeout", timeout, 'int')
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = self._deserialize('ProductResult', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    _get_multiple_pages_lro_initial.metadata = {'url': '/paging/multiple/lro'}

    @distributed_trace_async
    async def get_multiple_pages_lro(
        self,
        client_request_id: Optional[str] = None,
        maxresults: Optional[int] = None,
        timeout: Optional[int] = None,
        *,
        cls=None,
        polling: Optional[bool] = True,
        **kwargs
    ) -> "ProductResult":
        """A long-running paging operation that includes a nextLink that has 10 pages.

        FIXME: add operation.summary


        :param client_request_id: MISSING·PARAMETER-DESCRIPTION
        :type client_request_id: str
        :param maxresults: Sets the maximum number of items to return in the response.
        :type maxresults: int
        :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns ProductResult
        :rtype: ~azure.core.polling.LROPoller[~paging.models.ProductResult]

        :raises ~azure.mgmt.core.ARMError:
        """
        raw_result = await self._get_multiple_pages_lro_initial(
            client_request_id=client_request_id,
            maxresults=maxresults,
            timeout=timeout,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('ProductResult', response)

            if cls:
                return cls(response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    get_multiple_pages_lro.metadata = {'url': '/paging/multiple/lro'}

