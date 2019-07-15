# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from azure.core.exceptions import map_error
from azure.mgmt.core.exceptions import ARMError
from azure.core.polling import LROPoller, NoPolling
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models


class LRORetrysOperations(object):
    """LRORetrysOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

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
            self, product=None, cls=None, **kwargs):
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put201_creating_succeeded200.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())

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


        if response.status_code == 200:
            self._deserialize('Product', response)
        if response.status_code == 201:
            self._deserialize('Product', response)

        return response

    def put201_creating_succeeded200(
            self, product=None, cls=None, polling=True, **kwargs):
        """Long running put request, service returns a 500, then a 201 to the
        initial request, with an entity that contains
        ProvisioningState=’Creating’.  Polls return this value until the last
        poll returns a ‘200’ with ProvisioningState=’Succeeded’.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns Product
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~lro.models.Product]
        :raises: :class:`ARMError<azure.mgmt.core.ARMError>`
        """
        raw_result = self._put201_creating_succeeded200_initial(
            product=product,
            **kwargs
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('Product', response)

            return deserialized

        lro_delay = kwargs.get(
            'polling_interval ',
            self._config.polling_interval)
        if polling is True: polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    put201_creating_succeeded200.metadata = {'url': '/lro/retryerror/put/201/creating/succeeded/200'}


    def _put_async_relative_retry_succeeded_initial(
            self, product=None, cls=None, **kwargs):
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_async_relative_retry_succeeded.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())

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

        header_dict = {}

        if response.status_code == 200:
            self._deserialize('Product', response)
            header_dict = {
                'Azure-AsyncOperation': self._deserialize('str', response.headers.get('Azure-AsyncOperation')),
                'Location': self._deserialize('str', response.headers.get('Location')),
                'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
            }

        return response

    def put_async_relative_retry_succeeded(
            self, product=None, cls=None, polling=True, **kwargs):
        """Long running put request, service returns a 500, then a 200 to the
        initial request, with an entity that contains
        ProvisioningState=’Creating’. Poll the endpoint indicated in the
        Azure-AsyncOperation header for operation status.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns Product
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~lro.models.Product]
        :raises: :class:`ARMError<azure.mgmt.core.ARMError>`
        """
        raw_result = self._put_async_relative_retry_succeeded_initial(
            product=product,
            **kwargs
        )

        def get_long_running_output(response):
            header_dict = {
                'Azure-AsyncOperation': self._deserialize('str', response.headers.get('Azure-AsyncOperation')),
                'Location': self._deserialize('str', response.headers.get('Location')),
                'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
            }
            deserialized = self._deserialize('Product', response)

            return deserialized

        lro_delay = kwargs.get(
            'polling_interval ',
            self._config.polling_interval)
        if polling is True: polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    put_async_relative_retry_succeeded.metadata = {'url': '/lro/retryerror/putasync/retry/succeeded'}


    def _delete_provisioning202_accepted200_succeeded_initial(
            self, cls=None, **kwargs):
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.delete_provisioning202_accepted200_succeeded.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        header_dict = {}

        if response.status_code == 200:
            self._deserialize('Product', response)
            header_dict = {
                'Location': self._deserialize('str', response.headers.get('Location')),
                'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
            }
        if response.status_code == 202:
            self._deserialize('Product', response)
            header_dict = {
                'Location': self._deserialize('str', response.headers.get('Location')),
                'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
            }

        return response

    def delete_provisioning202_accepted200_succeeded(
            self, cls=None, polling=True, **kwargs):
        """Long running delete request, service returns a 500, then a  202 to the
        initial request, with an entity that contains
        ProvisioningState=’Accepted’.  Polls return this value until the last
        poll returns a ‘200’ with ProvisioningState=’Succeeded’.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns Product
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~lro.models.Product]
        :raises: :class:`ARMError<azure.mgmt.core.ARMError>`
        """
        raw_result = self._delete_provisioning202_accepted200_succeeded_initial(
            **kwargs
        )

        def get_long_running_output(response):
            header_dict = {
                'Location': self._deserialize('str', response.headers.get('Location')),
                'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
            }
            deserialized = self._deserialize('Product', response)

            return deserialized

        lro_delay = kwargs.get(
            'polling_interval ',
            self._config.polling_interval)
        if polling is True: polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    delete_provisioning202_accepted200_succeeded.metadata = {'url': '/lro/retryerror/delete/provisioning/202/accepted/200/succeeded'}


    def _delete202_retry200_initial(
            self, cls=None, **kwargs):
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.delete202_retry200.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        return response

    def delete202_retry200(
            self, cls=None, polling=True, **kwargs):
        """Long running delete request, service returns a 500, then a 202 to the
        initial request. Polls return this value until the last poll returns a
        ‘200’ with ProvisioningState=’Succeeded’.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None]
        :raises: :class:`ARMError<azure.mgmt.core.ARMError>`
        """
        raw_result = self._delete202_retry200_initial(
            **kwargs
        )

        def get_long_running_output(response):
            if cls:
                response_headers = {
                    'Location': self._deserialize('str', response.headers.get('Location')),
                    'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
                }
                return cls(response, None, response_headers)

        lro_delay = kwargs.get(
            'polling_interval ',
            self._config.polling_interval)
        if polling is True: polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    delete202_retry200.metadata = {'url': '/lro/retryerror/delete/202/retry/200'}


    def _delete_async_relative_retry_succeeded_initial(
            self, cls=None, **kwargs):
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.delete_async_relative_retry_succeeded.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        return response

    def delete_async_relative_retry_succeeded(
            self, cls=None, polling=True, **kwargs):
        """Long running delete request, service returns a 500, then a 202 to the
        initial request. Poll the endpoint indicated in the
        Azure-AsyncOperation header for operation status.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None]
        :raises: :class:`ARMError<azure.mgmt.core.ARMError>`
        """
        raw_result = self._delete_async_relative_retry_succeeded_initial(
            **kwargs
        )

        def get_long_running_output(response):
            if cls:
                response_headers = {
                    'Azure-AsyncOperation': self._deserialize('str', response.headers.get('Azure-AsyncOperation')),
                    'Location': self._deserialize('str', response.headers.get('Location')),
                    'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
                }
                return cls(response, None, response_headers)

        lro_delay = kwargs.get(
            'polling_interval ',
            self._config.polling_interval)
        if polling is True: polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    delete_async_relative_retry_succeeded.metadata = {'url': '/lro/retryerror/deleteasync/retry/succeeded'}


    def _post202_retry200_initial(
            self, product=None, cls=None, **kwargs):
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.post202_retry200.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())

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

        return response

    def post202_retry200(
            self, product=None, cls=None, polling=True, **kwargs):
        """Long running post request, service returns a 500, then a 202 to the
        initial request, with 'Location' and 'Retry-After' headers, Polls
        return a 200 with a response body after success.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None]
        :raises: :class:`ARMError<azure.mgmt.core.ARMError>`
        """
        raw_result = self._post202_retry200_initial(
            product=product,
            **kwargs
        )

        def get_long_running_output(response):
            if cls:
                response_headers = {
                    'Location': self._deserialize('str', response.headers.get('Location')),
                    'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
                }
                return cls(response, None, response_headers)

        lro_delay = kwargs.get(
            'polling_interval ',
            self._config.polling_interval)
        if polling is True: polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    post202_retry200.metadata = {'url': '/lro/retryerror/post/202/retry/200'}


    def _post_async_relative_retry_succeeded_initial(
            self, product=None, cls=None, **kwargs):
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.post_async_relative_retry_succeeded.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())

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

        return response

    def post_async_relative_retry_succeeded(
            self, product=None, cls=None, polling=True, **kwargs):
        """Long running post request, service returns a 500, then a 202 to the
        initial request, with an entity that contains
        ProvisioningState=’Creating’. Poll the endpoint indicated in the
        Azure-AsyncOperation header for operation status.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None]
        :raises: :class:`ARMError<azure.mgmt.core.ARMError>`
        """
        raw_result = self._post_async_relative_retry_succeeded_initial(
            product=product,
            **kwargs
        )

        def get_long_running_output(response):
            if cls:
                response_headers = {
                    'Azure-AsyncOperation': self._deserialize('str', response.headers.get('Azure-AsyncOperation')),
                    'Location': self._deserialize('str', response.headers.get('Location')),
                    'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
                }
                return cls(response, None, response_headers)

        lro_delay = kwargs.get(
            'polling_interval ',
            self._config.polling_interval)
        if polling is True: polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    post_async_relative_retry_succeeded.metadata = {'url': '/lro/retryerror/postasync/retry/succeeded'}
