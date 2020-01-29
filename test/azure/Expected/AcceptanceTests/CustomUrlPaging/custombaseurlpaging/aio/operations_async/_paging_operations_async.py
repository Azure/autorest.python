# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import map_error
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMError
from msrest.serialization import Model

from ... import models


def _cls_type_annotation(return_type):
    return Optional[Callable[[AsyncHttpResponse, return_type, Dict[str, Any]], Any]]


class PagingOperations:
    """PagingOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~custombaseurlpaging.models
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
    def get_pages_partial_url(
        self,
        account_name: str,
        *,
        cls: _cls_type_annotation("ProductResult") = None,
        **kwargs
    ) -> "ProductResult":
        """A paging operation that combines custom url, paging and partial URL and expect to concat after host.

        FIXME: add operation.summary


        :param account_name: Account Name
        :type account_name: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~custombaseurlpaging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_pages_partial_url.metadata['url']
                path_format_arguments = {
                    'accountName': self._serialize.url("account_name", account_name, 'str', skip_quote=True),
                    'host': self._serialize.url("self._config.host", self._config.host, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link
                path_format_arguments = {
                    'accountName': self._serialize.url("account_name", account_name, 'str', skip_quote=True),
                    'host': self._serialize.url("self._config.host", self._config.host, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)

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
    get_pages_partial_url.metadata = {'url': '/paging/customurl/partialnextlink'}


    @distributed_trace
    def get_pages_partial_url_operation(
        self,
        account_name: str,
        *,
        cls: _cls_type_annotation("ProductResult") = None,
        **kwargs
    ) -> "ProductResult":
        """A paging operation that combines custom url, paging and partial URL with next operation.

        FIXME: add operation.summary


        :param account_name: Account Name
        :type account_name: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~custombaseurlpaging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_pages_partial_url_operation.metadata['url']
                path_format_arguments = {
                    'accountName': self._serialize.url("account_name", account_name, 'str', skip_quote=True),
                    'host': self._serialize.url("self._config.host", self._config.host, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = '/paging/customurl/{nextLink}'
                path_format_arguments = {
                    'accountName': self._serialize.url("account_name", account_name, 'str', skip_quote=True),
                    'host': self._serialize.url("self._config.host", self._config.host, 'str', skip_quote=True),
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)

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
    get_pages_partial_url_operation.metadata = {'url': '/paging/customurl/partialnextlinkop'}

