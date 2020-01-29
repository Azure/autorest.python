# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional, Union
import warnings

from azure.core.exceptions import map_error
from azure.core.polling import LROPoller, NoPolling
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMError
from azure.mgmt.core.polling.arm_polling import ARMPolling
from msrest.serialization import Model

from .. import models


class LRORetrysOperations(object):
    """LRORetrysOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~lro.models
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

    
    def _put201_creating_succeeded200_initial(
        self,
        product=None,  # type: Optional["Product"]
        cls=None,  # type: Optional[Callable[[HttpResponse, "Product", Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> "Product"
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)

        if response.status_code == 201:
            deserialized = self._deserialize('Product', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    _put201_creating_succeeded200_initial.metadata = {'url': '/lro/retryerror/put/201/creating/succeeded/200'}

    @distributed_trace
    def begin_put201_creating_succeeded200(
        self,
        product=None,  # type: Optional["Product"]
        cls=None,  # type: Callable[[HTTPResponse, "Product", Dict[str, Any]], Any]
        polling=True,  # type: Optional[bool]
        **kwargs  # type: **Any
    ):
        # type: (...) -> "Product"
        """Long running put request, service returns a 500, then a 201 to the initial request, with an entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll returns a ‘200’ with ProvisioningState=’Succeeded’.

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
        raw_result = self._put201_creating_succeeded200_initial(
            product=product,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('Product', response)

            if cls:
                return cls(response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_put201_creating_succeeded200.metadata = {'url': '/lro/retryerror/put/201/creating/succeeded/200'}


    
    def _put_async_relative_retry_succeeded_initial(
        self,
        product=None,  # type: Optional["Product"]
        cls=None,  # type: Optional[Callable[[HttpResponse, "Product", Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> "Product"
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self._put_async_relative_retry_succeeded_initial.metadata['url']

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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
        deserialized = self._deserialize('Product', response)

        if cls:
          return cls(response, deserialized, response_headers)

        return deserialized
    _put_async_relative_retry_succeeded_initial.metadata = {'url': '/lro/retryerror/putasync/retry/succeeded'}

    @distributed_trace
    def begin_put_async_relative_retry_succeeded(
        self,
        product=None,  # type: Optional["Product"]
        cls=None,  # type: Callable[[HTTPResponse, "Product", Dict[str, Any]], Any]
        polling=True,  # type: Optional[bool]
        **kwargs  # type: **Any
    ):
        # type: (...) -> "Product"
        """Long running put request, service returns a 500, then a 200 to the initial request, with an entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the Azure-AsyncOperation header for operation status.

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
        raw_result = self._put_async_relative_retry_succeeded_initial(
            product=product,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(response):
            response_headers = {}
            response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
            deserialized = self._deserialize('Product', response)

            if cls:
                return cls(response, deserialized, response_headers)
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_put_async_relative_retry_succeeded.metadata = {'url': '/lro/retryerror/putasync/retry/succeeded'}


    
    def _delete_provisioning202_accepted200_succeeded_initial(
        self,
        cls=None,  # type: Optional[Callable[[HttpResponse, "Product", Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> "Product"
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self._delete_provisioning202_accepted200_succeeded_initial.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)

        if response.status_code == 202:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
            deserialized = self._deserialize('Product', response)

        if cls:
          return cls(response, deserialized, response_headers)

        return deserialized
    _delete_provisioning202_accepted200_succeeded_initial.metadata = {'url': '/lro/retryerror/delete/provisioning/202/accepted/200/succeeded'}

    @distributed_trace
    def begin_delete_provisioning202_accepted200_succeeded(
        self,
        cls=None,  # type: Callable[[HTTPResponse, "Product", Dict[str, Any]], Any]
        polling=True,  # type: Optional[bool]
        **kwargs  # type: **Any
    ):
        # type: (...) -> "Product"
        """Long running delete request, service returns a 500, then a  202 to the initial request, with an entity that contains ProvisioningState=’Accepted’.  Polls return this value until the last poll returns a ‘200’ with ProvisioningState=’Succeeded’.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns Product
        :rtype: ~azure.core.polling.LROPoller[~lro.models.Product]

        :raises ~azure.mgmt.core.ARMError:
        """
        raw_result = self._delete_provisioning202_accepted200_succeeded_initial(
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(response):
            response_headers = {}
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
            deserialized = self._deserialize('Product', response)

            if cls:
                return cls(response, deserialized, response_headers)
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_delete_provisioning202_accepted200_succeeded.metadata = {'url': '/lro/retryerror/delete/provisioning/202/accepted/200/succeeded'}


    
    def _delete202_retry200_initial(
        self,
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self._delete202_retry200_initial.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))

        if cls:
          return cls(response, None, response_headers)

    _delete202_retry200_initial.metadata = {'url': '/lro/retryerror/delete/202/retry/200'}

    @distributed_trace
    def begin_delete202_retry200(
        self,
        cls=None,  # type: Callable[[HTTPResponse, None, Dict[str, Any]], Any]
        polling=True,  # type: Optional[bool]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Long running delete request, service returns a 500, then a 202 to the initial request. Polls return this value until the last poll returns a ‘200’ with ProvisioningState=’Succeeded’.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]

        :raises ~azure.mgmt.core.ARMError:
        """
        raw_result = self._delete202_retry200_initial(
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(response):
            if cls:
                return cls(response, None, {})

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_delete202_retry200.metadata = {'url': '/lro/retryerror/delete/202/retry/200'}


    
    def _delete_async_relative_retry_succeeded_initial(
        self,
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self._delete_async_relative_retry_succeeded_initial.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))

        if cls:
          return cls(response, None, response_headers)

    _delete_async_relative_retry_succeeded_initial.metadata = {'url': '/lro/retryerror/deleteasync/retry/succeeded'}

    @distributed_trace
    def begin_delete_async_relative_retry_succeeded(
        self,
        cls=None,  # type: Callable[[HTTPResponse, None, Dict[str, Any]], Any]
        polling=True,  # type: Optional[bool]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Long running delete request, service returns a 500, then a 202 to the initial request. Poll the endpoint indicated in the Azure-AsyncOperation header for operation status.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]

        :raises ~azure.mgmt.core.ARMError:
        """
        raw_result = self._delete_async_relative_retry_succeeded_initial(
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(response):
            if cls:
                return cls(response, None, {})

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_delete_async_relative_retry_succeeded.metadata = {'url': '/lro/retryerror/deleteasync/retry/succeeded'}


    
    def _post202_retry200_initial(
        self,
        product=None,  # type: Optional["Product"]
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))

        if cls:
          return cls(response, None, response_headers)

    _post202_retry200_initial.metadata = {'url': '/lro/retryerror/post/202/retry/200'}

    @distributed_trace
    def begin_post202_retry200(
        self,
        product=None,  # type: Optional["Product"]
        cls=None,  # type: Callable[[HTTPResponse, None, Dict[str, Any]], Any]
        polling=True,  # type: Optional[bool]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Long running post request, service returns a 500, then a 202 to the initial request, with 'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

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
        raw_result = self._post202_retry200_initial(
            product=product,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(response):
            if cls:
                return cls(response, None, {})

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_post202_retry200.metadata = {'url': '/lro/retryerror/post/202/retry/200'}


    
    def _post_async_relative_retry_succeeded_initial(
        self,
        product=None,  # type: Optional["Product"]
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self._post_async_relative_retry_succeeded_initial.metadata['url']

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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        response_headers = {}
        response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))

        if cls:
          return cls(response, None, response_headers)

    _post_async_relative_retry_succeeded_initial.metadata = {'url': '/lro/retryerror/postasync/retry/succeeded'}

    @distributed_trace
    def begin_post_async_relative_retry_succeeded(
        self,
        product=None,  # type: Optional["Product"]
        cls=None,  # type: Callable[[HTTPResponse, None, Dict[str, Any]], Any]
        polling=True,  # type: Optional[bool]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Long running post request, service returns a 500, then a 202 to the initial request, with an entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the Azure-AsyncOperation header for operation status.

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
        raw_result = self._post_async_relative_retry_succeeded_initial(
            product=product,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(response):
            if cls:
                return cls(response, None, {})

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_post_async_relative_retry_succeeded.metadata = {'url': '/lro/retryerror/postasync/retry/succeeded'}

