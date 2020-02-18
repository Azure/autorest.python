# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMError
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class PagingOperations(object):
    """PagingOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~paging.models
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
    def get_no_item_name_pages(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResultValue"
        """A paging operation that must return result of the default 'value' node.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProductResultValue or the result of cls(response)
        :rtype: ~paging.models.ProductResultValue
        :raises: ~azure.mgmt.core.ARMError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ProductResultValue"]
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProductResultValue', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_no_item_name_pages.metadata = {'url': '/paging/noitemname'}

    @distributed_trace
    def get_null_next_link_name_pages(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResult"
        """A paging operation that must ignore any kind of nextLink, and stop after page 1.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ProductResult"]
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_null_next_link_name_pages.metadata = {'url': '/paging/nullnextlink'}

    @distributed_trace
    def get_single_pages(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResult"
        """A paging operation that finishes on the first call without a nextlink.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ProductResult"]
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_single_pages.metadata = {'url': '/paging/single'}

    @distributed_trace
    def get_multiple_pages(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResult"
        """A paging operation that includes a nextLink that has 10 pages.

        :param client_request_id:
        :type client_request_id: str
        :param paging_get_multiple_pages_options: Parameter group.
        :type paging_get_multiple_pages_options: ~paging.models.PagingGetMultiplePagesOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ProductResult"]
        error_map = kwargs.pop('error_map', {})
        
        _maxresults = None
        _timeout = None
        if paging_get_multiple_pages_options is not None:
            _maxresults = paging_get_multiple_pages_options.maxresults
            _timeout = paging_get_multiple_pages_options.timeout

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
            if _maxresults is not None:
                header_parameters['maxresults'] = self._serialize.header("maxresults", _maxresults, 'int')
            if _timeout is not None:
                header_parameters['timeout'] = self._serialize.header("timeout", _timeout, 'int')
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_multiple_pages.metadata = {'url': '/paging/multiple'}

    @distributed_trace
    def get_odata_multiple_pages(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.OdataProductResult"
        """A paging operation that includes a nextLink in odata format that has 10 pages.

        :param client_request_id:
        :type client_request_id: str
        :param paging_get_odata_multiple_pages_options: Parameter group.
        :type paging_get_odata_multiple_pages_options: ~paging.models.PagingGetOdataMultiplePagesOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OdataProductResult or the result of cls(response)
        :rtype: ~paging.models.OdataProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.OdataProductResult"]
        error_map = kwargs.pop('error_map', {})
        
        _maxresults = None
        _timeout = None
        if paging_get_odata_multiple_pages_options is not None:
            _maxresults = paging_get_odata_multiple_pages_options.maxresults
            _timeout = paging_get_odata_multiple_pages_options.timeout

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
            if _maxresults is not None:
                header_parameters['maxresults'] = self._serialize.header("maxresults", _maxresults, 'int')
            if _timeout is not None:
                header_parameters['timeout'] = self._serialize.header("timeout", _timeout, 'int')
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('OdataProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_odata_multiple_pages.metadata = {'url': '/paging/multiple/odata'}

    @distributed_trace
    def get_multiple_pages_with_offset(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResult"
        """A paging operation that includes a nextLink that has 10 pages.

        :param paging_get_multiple_pages_with_offset_options: Parameter group.
        :type paging_get_multiple_pages_with_offset_options: ~paging.models.PagingGetMultiplePagesWithOffsetOptions
        :param client_request_id:
        :type client_request_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ProductResult"]
        error_map = kwargs.pop('error_map', {})
        
        _maxresults = None
        _offset = None
        _timeout = None
        if paging_get_multiple_pages_with_offset_options is not None:
            _maxresults = paging_get_multiple_pages_with_offset_options.maxresults
            _offset = paging_get_multiple_pages_with_offset_options.offset
            _timeout = paging_get_multiple_pages_with_offset_options.timeout

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_with_offset.metadata['url']
                path_format_arguments = {
                    'offset': self._serialize.url("offset", _offset, 'int'),
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
            if _maxresults is not None:
                header_parameters['maxresults'] = self._serialize.header("maxresults", _maxresults, 'int')
            if _timeout is not None:
                header_parameters['timeout'] = self._serialize.header("timeout", _timeout, 'int')
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_with_offset.metadata = {'url': '/paging/multiple/withpath/{offset}'}

    @distributed_trace
    def get_multiple_pages_retry_first(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResult"
        """A paging operation that fails on the first call with 500 and then retries and then get a response including a nextLink that has 10 pages.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ProductResult"]
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_retry_first.metadata = {'url': '/paging/multiple/retryfirst'}

    @distributed_trace
    def get_multiple_pages_retry_second(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResult"
        """A paging operation that includes a nextLink that has 10 pages, of which the 2nd call fails first with 500. The client should retry and finish all 10 pages eventually.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ProductResult"]
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_retry_second.metadata = {'url': '/paging/multiple/retrysecond'}

    @distributed_trace
    def get_single_pages_failure(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResult"
        """A paging operation that receives a 400 on the first call.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ProductResult"]
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_single_pages_failure.metadata = {'url': '/paging/single/failure'}

    @distributed_trace
    def get_multiple_pages_failure(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResult"
        """A paging operation that receives a 400 on the second call.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ProductResult"]
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_failure.metadata = {'url': '/paging/multiple/failure'}

    @distributed_trace
    def get_multiple_pages_failure_uri(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResult"
        """A paging operation that receives an invalid nextLink.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProductResult or the result of cls(response)
        :rtype: ~paging.models.ProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ProductResult"]
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_failure_uri.metadata = {'url': '/paging/multiple/failureuri'}

    @distributed_trace
    def get_multiple_pages_fragment_next_link(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.OdataProductResult"
        """A paging operation that doesn't return a full URL, just a fragment.

        :param api_version: Sets the api version to use.
        :type api_version: str
        :param tenant: Sets the tenant to use.
        :type tenant: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OdataProductResult or the result of cls(response)
        :rtype: ~paging.models.OdataProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.OdataProductResult"]
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('OdataProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_fragment_next_link.metadata = {'url': '/paging/multiple/fragment/{tenant}'}

    @distributed_trace
    def get_multiple_pages_fragment_with_grouping_next_link(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.OdataProductResult"
        """A paging operation that doesn't return a full URL, just a fragment with parameters grouped.

        :param custom_parameter_group: Parameter group.
        :type custom_parameter_group: ~paging.models.CustomParameterGroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OdataProductResult or the result of cls(response)
        :rtype: ~paging.models.OdataProductResult
        :raises: ~azure.mgmt.core.ARMError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.OdataProductResult"]
        error_map = kwargs.pop('error_map', {})
        
        _api_version = None
        _tenant = None
        if custom_parameter_group is not None:
            _api_version = custom_parameter_group.api_version
            _tenant = custom_parameter_group.tenant

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_fragment_with_grouping_next_link.metadata['url']
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", _tenant, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = '/paging/multiple/fragmentwithgrouping/{tenant}/{nextLink}'
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", _tenant, 'str'),
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)

            # Construct parameters
            query_parameters = {}
            query_parameters['api_version'] = self._serialize.query("api_version", _api_version, 'str')

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('OdataProductResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_multiple_pages_fragment_with_grouping_next_link.metadata = {'url': '/paging/multiple/fragmentwithgrouping/{tenant}'}

    def _get_multiple_pages_lro_initial(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResult"
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ProductResult"]
        error_map = kwargs.pop('error_map', {})
        
        _maxresults = None
        _timeout = None
        if paging_get_multiple_pages_lro_options is not None:
            _maxresults = paging_get_multiple_pages_lro_options.maxresults
            _timeout = paging_get_multiple_pages_lro_options.timeout

        # Construct URL
        url = self._get_multiple_pages_lro_initial.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if client_request_id is not None:
            header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
        if _maxresults is not None:
            header_parameters['maxresults'] = self._serialize.header("maxresults", _maxresults, 'int')
        if _timeout is not None:
            header_parameters['timeout'] = self._serialize.header("timeout", _timeout, 'int')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = self._deserialize('ProductResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _get_multiple_pages_lro_initial.metadata = {'url': '/paging/multiple/lro'}

    @distributed_trace
    def begin_get_multiple_pages_lro(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProductResult"
        """A long-running paging operation that includes a nextLink that has 10 pages.

        :param client_request_id:
        :type client_request_id: str
        :param paging_get_multiple_pages_lro_options: Parameter group.
        :type paging_get_multiple_pages_lro_options: ~paging.models.PagingGetMultiplePagesLroOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :return: An instance of LROPoller that returns ProductResult
        :rtype: ~azure.core.polling.LROPoller[~paging.models.ProductResult]

        :raises ~azure.mgmt.core.ARMError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ProductResult"]
        raw_result = self._get_multiple_pages_lro_initial(
            client_request_id=client_request_id,
            paging_get_multiple_pages_lro_options=paging_get_multiple_pages_lro_options,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('ProductResult', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_get_multiple_pages_lro.metadata = {'url': '/paging/multiple/lro'}
