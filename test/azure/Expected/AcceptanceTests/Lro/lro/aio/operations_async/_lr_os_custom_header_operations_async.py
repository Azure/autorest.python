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
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncNoPolling, async_poller
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMError
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling
from msrest.serialization import Model

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

def _cls_type_annotation(return_type):
    return Optional[Callable[[AsyncHttpResponse, return_type, Dict[str, Any]], Any]]


class LROsCustomHeaderOperations:
    """LROsCustomHeaderOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~lro.models
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

    
    async def _put_async_retry_succeeded_initial(
        self,
        product: Optional["Product"] = None,
        *,
        cls: ClsType["Product"] = None,
        **kwargs: Any
    ) -> "Product":
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self._put_async_retry_succeeded_initial.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if product is not None:
            body_content = self._serialize.body(product, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
        deserialized = self._deserialize('Product', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    _put_async_retry_succeeded_initial.metadata = {'url': '/lro/customheader/putasync/retry/succeeded'}

    @distributed_trace_async
    async def put_async_retry_succeeded(
        self,
        product: Optional["Product"] = None,
        *,
        cls: _cls_type_annotation("Product") = None,
        polling: Optional[bool] = True,
        **kwargs
    ) -> "Product":
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for all requests. Long running put request, service returns a 200 to the initial request, with an entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the Azure-AsyncOperation header for operation status.

        FIXME: add operation.summary


        :param product: Product to put
        :type product: ~lro.models.Product
        :param callable cls: A custom type or function that will be passed the direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns Product
        :rtype: ~azure.core.polling.LROPoller[~lro.models.Product]

        :raises ~azure.mgmt.core.ARMError:
        """
        raw_result = await self._put_async_retry_succeeded_initial(
            product=product,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
            deserialized = self._deserialize('Product', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, response_headers)
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    put_async_retry_succeeded.metadata = {'url': '/lro/customheader/putasync/retry/succeeded'}


    
    async def _put201_creating_succeeded200_initial(
        self,
        product: Optional["Product"] = None,
        *,
        cls: ClsType["Product"] = None,
        **kwargs: Any
    ) -> "Product":
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self._put201_creating_succeeded200_initial.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if product is not None:
            body_content = self._serialize.body(product, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Product', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Product', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _put201_creating_succeeded200_initial.metadata = {'url': '/lro/customheader/put/201/creating/succeeded/200'}

    @distributed_trace_async
    async def put201_creating_succeeded200(
        self,
        product: Optional["Product"] = None,
        *,
        cls: _cls_type_annotation("Product") = None,
        polling: Optional[bool] = True,
        **kwargs
    ) -> "Product":
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for all requests. Long running put request, service returns a 201 to the initial request, with an entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll returns a ‘200’ with ProvisioningState=’Succeeded’.

        FIXME: add operation.summary


        :param product: Product to put
        :type product: ~lro.models.Product
        :param callable cls: A custom type or function that will be passed the direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns Product
        :rtype: ~azure.core.polling.LROPoller[~lro.models.Product]

        :raises ~azure.mgmt.core.ARMError:
        """
        raw_result = await self._put201_creating_succeeded200_initial(
            product=product,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('Product', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    put201_creating_succeeded200.metadata = {'url': '/lro/customheader/put/201/creating/succeeded/200'}


    
    async def _post202_retry200_initial(
        self,
        product: Optional["Product"] = None,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self._post202_retry200_initial.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if product is not None:
            body_content = self._serialize.body(product, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    _post202_retry200_initial.metadata = {'url': '/lro/customheader/post/202/retry/200'}

    @distributed_trace_async
    async def post202_retry200(
        self,
        product: Optional["Product"] = None,
        *,
        cls: _cls_type_annotation(None) = None,
        polling: Optional[bool] = True,
        **kwargs
    ) -> None:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for all requests. Long running post request, service returns a 202 to the initial request, with 'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

        FIXME: add operation.summary


        :param product: Product to put
        :type product: ~lro.models.Product
        :param callable cls: A custom type or function that will be passed the direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]

        :raises ~azure.mgmt.core.ARMError:
        """
        raw_result = await self._post202_retry200_initial(
            product=product,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    post202_retry200.metadata = {'url': '/lro/customheader/post/202/retry/200'}


    
    async def _post_async_retry_succeeded_initial(
        self,
        product: Optional["Product"] = None,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self._post_async_retry_succeeded_initial.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if product is not None:
            body_content = self._serialize.body(product, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    _post_async_retry_succeeded_initial.metadata = {'url': '/lro/customheader/postasync/retry/succeeded'}

    @distributed_trace_async
    async def post_async_retry_succeeded(
        self,
        product: Optional["Product"] = None,
        *,
        cls: _cls_type_annotation(None) = None,
        polling: Optional[bool] = True,
        **kwargs
    ) -> None:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for all requests. Long running post request, service returns a 202 to the initial request, with an entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the Azure-AsyncOperation header for operation status.

        FIXME: add operation.summary


        :param product: Product to put
        :type product: ~lro.models.Product
        :param callable cls: A custom type or function that will be passed the direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]

        :raises ~azure.mgmt.core.ARMError:
        """
        raw_result = await self._post_async_retry_succeeded_initial(
            product=product,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    post_async_retry_succeeded.metadata = {'url': '/lro/customheader/postasync/retry/succeeded'}

