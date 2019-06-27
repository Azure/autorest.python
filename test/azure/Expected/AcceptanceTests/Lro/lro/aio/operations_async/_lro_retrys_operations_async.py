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
from azure.core.polling.async_poller import async_poller, AsyncNoPolling
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models


class LRORetrysOperations:
    """LRORetrysOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

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


    async def _put201_creating_succeeded200_initial(
            self, product=None, *, cls=None, **kwargs):
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
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if product is not None:
            body_content = self._serialize.body(product, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException(response, self._deserialize)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)
        if response.status_code == 201:
            deserialized = self._deserialize('Product', response)

        return deserialized

    async def put201_creating_succeeded200(
            self, product=None, *, cls=None, polling=True, **kwargs):
        """Long running put request, service returns a 500, then a 201 to the
        initial request, with an entity that contains
        ProvisioningState=’Creating’.  Polls return this value until the last
        poll returns a ‘200’ with ProvisioningState=’Succeeded’.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of Product
        :rtype: ~~lro.models.Product
        :raises: :class:`CloudErrorException<lro.models.CloudErrorException>`
        """
        raw_result = await self._put201_creating_succeeded200_initial(
            product=product,
            **kwargs
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('Product', response)

            return deserialized

        lro_delay = kwargs.get(
            'long_running_operation_timeout',
            self._config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    put201_creating_succeeded200.metadata = {'url': '/lro/retryerror/put/201/creating/succeeded/200'}


    async def _put_async_relative_retry_succeeded_initial(
            self, product=None, *, cls=None, **kwargs):
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
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if product is not None:
            body_content = self._serialize.body(product, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException(response, self._deserialize)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)
            header_dict = {
                'Azure-AsyncOperation': self._deserialize('str', response.headers.get('Azure-AsyncOperation')),
                'Location': self._deserialize('str', response.headers.get('Location')),
                'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
            }

        return deserialized

    async def put_async_relative_retry_succeeded(
            self, product=None, *, cls=None, polling=True, **kwargs):
        """Long running put request, service returns a 500, then a 200 to the
        initial request, with an entity that contains
        ProvisioningState=’Creating’. Poll the endpoint indicated in the
        Azure-AsyncOperation header for operation status.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of Product
        :rtype: ~~lro.models.Product
        :raises: :class:`CloudErrorException<lro.models.CloudErrorException>`
        """
        raw_result = await self._put_async_relative_retry_succeeded_initial(
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
            'long_running_operation_timeout',
            self._config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    put_async_relative_retry_succeeded.metadata = {'url': '/lro/retryerror/putasync/retry/succeeded'}


    async def _delete_provisioning202_accepted200_succeeded_initial(
            self, *, cls=None, **kwargs):
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
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException(response, self._deserialize)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)
            header_dict = {
                'Location': self._deserialize('str', response.headers.get('Location')),
                'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
            }
        if response.status_code == 202:
            deserialized = self._deserialize('Product', response)
            header_dict = {
                'Location': self._deserialize('str', response.headers.get('Location')),
                'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
            }

        return deserialized

    async def delete_provisioning202_accepted200_succeeded(
            self, *, cls=None, polling=True, **kwargs):
        """Long running delete request, service returns a 500, then a  202 to the
        initial request, with an entity that contains
        ProvisioningState=’Accepted’.  Polls return this value until the last
        poll returns a ‘200’ with ProvisioningState=’Succeeded’.

        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of Product
        :rtype: ~~lro.models.Product
        :raises: :class:`CloudErrorException<lro.models.CloudErrorException>`
        """
        raw_result = await self._delete_provisioning202_accepted200_succeeded_initial(
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
            'long_running_operation_timeout',
            self._config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    delete_provisioning202_accepted200_succeeded.metadata = {'url': '/lro/retryerror/delete/provisioning/202/accepted/200/succeeded'}


    async def _delete202_retry200_initial(
            self, *, cls=None, **kwargs):
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.delete202_retry200.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException(response, self._deserialize)

            return ''

    async def delete202_retry200(
            self, *, cls=None, polling=True, **kwargs):
        """Long running delete request, service returns a 500, then a 202 to the
        initial request. Polls return this value until the last poll returns a
        ‘200’ with ProvisioningState=’Succeeded’.

        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of None
        :rtype: ~None
        :raises: :class:`CloudErrorException<lro.models.CloudErrorException>`
        """
        raw_result = await self._delete202_retry200_initial(
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
            'long_running_operation_timeout',
            self._config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    delete202_retry200.metadata = {'url': '/lro/retryerror/delete/202/retry/200'}


    async def _delete_async_relative_retry_succeeded_initial(
            self, *, cls=None, **kwargs):
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.delete_async_relative_retry_succeeded.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException(response, self._deserialize)

            return ''

    async def delete_async_relative_retry_succeeded(
            self, *, cls=None, polling=True, **kwargs):
        """Long running delete request, service returns a 500, then a 202 to the
        initial request. Poll the endpoint indicated in the
        Azure-AsyncOperation header for operation status.

        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of None
        :rtype: ~None
        :raises: :class:`CloudErrorException<lro.models.CloudErrorException>`
        """
        raw_result = await self._delete_async_relative_retry_succeeded_initial(
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
            'long_running_operation_timeout',
            self._config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    delete_async_relative_retry_succeeded.metadata = {'url': '/lro/retryerror/deleteasync/retry/succeeded'}


    async def _post202_retry200_initial(
            self, product=None, *, cls=None, **kwargs):
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
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if product is not None:
            body_content = self._serialize.body(product, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException(response, self._deserialize)

            return ''

    async def post202_retry200(
            self, product=None, *, cls=None, polling=True, **kwargs):
        """Long running post request, service returns a 500, then a 202 to the
        initial request, with 'Location' and 'Retry-After' headers, Polls
        return a 200 with a response body after success.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of None
        :rtype: ~None
        :raises: :class:`CloudErrorException<lro.models.CloudErrorException>`
        """
        raw_result = await self._post202_retry200_initial(
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
            'long_running_operation_timeout',
            self._config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    post202_retry200.metadata = {'url': '/lro/retryerror/post/202/retry/200'}


    async def _post_async_relative_retry_succeeded_initial(
            self, product=None, *, cls=None, **kwargs):
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
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if product is not None:
            body_content = self._serialize.body(product, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException(response, self._deserialize)

            return ''

    async def post_async_relative_retry_succeeded(
            self, product=None, *, cls=None, polling=True, **kwargs):
        """Long running post request, service returns a 500, then a 202 to the
        initial request, with an entity that contains
        ProvisioningState=’Creating’. Poll the endpoint indicated in the
        Azure-AsyncOperation header for operation status.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of None
        :rtype: ~None
        :raises: :class:`CloudErrorException<lro.models.CloudErrorException>`
        """
        raw_result = await self._post_async_relative_retry_succeeded_initial(
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
            'long_running_operation_timeout',
            self._config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    post_async_relative_retry_succeeded.metadata = {'url': '/lro/retryerror/postasync/retry/succeeded'}
