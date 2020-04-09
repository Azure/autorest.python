# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class PagingOperations(object):
    """PagingOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~custombaseurlpaging.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_pages_partial_url(
        self,
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResult"
        """A paging operation that combines custom url, paging and partial URL and expect to concat after host.

        :param account_name: Account Name.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~custombaseurlpaging.models.ProductResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProductResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

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
            query_parameters = {}  # type: Dict[str, Any]

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_pages_partial_url.metadata = {'url': '/paging/customurl/partialnextlink'}

    @distributed_trace
    def get_pages_partial_url_operation(
        self,
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResult"
        """A paging operation that combines custom url, paging and partial URL with next operation.

        :param account_name: Account Name.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~custombaseurlpaging.models.ProductResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProductResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

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
            query_parameters = {}  # type: Dict[str, Any]

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_pages_partial_url_operation.metadata = {'url': '/paging/customurl/partialnextlinkop'}
