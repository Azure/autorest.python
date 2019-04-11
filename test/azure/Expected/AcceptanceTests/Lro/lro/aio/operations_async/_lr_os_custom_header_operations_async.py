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
from msrestazure.azure_exceptions import CloudError
from msrest.polling.async_poller import async_poller, AsyncNoPolling
from msrestazure.polling.async_arm_polling import AsyncARMPolling

from ... import models


class LROsCustomHeaderOperations:
    """LROsCustomHeaderOperations async operations.

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


    async def _put_async_retry_succeeded_initial(
            self, product=None, *, cls=None, **operation_config):
        # Construct URL
        url = self.put_async_retry_succeeded.metadata['url']

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
        response = await self._client.pipeline.run(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)
            header_dict = {
                'Azure-AsyncOperation': self._deserialize('str', response.headers.get('Azure-AsyncOperation')),
                'Location': self._deserialize('str', response.headers.get('Location')),
                'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            header_dict
            return client_raw_response

        return deserialized

    async def put_async_retry_succeeded(
            self, product=None, *, cls=None, polling=True, **operation_config):
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is
        required message header for all requests. Long running put request,
        service returns a 200 to the initial request, with an entity that
        contains ProvisioningState=’Creating’. Poll the endpoint indicated in
        the Azure-AsyncOperation header for operation status.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of Product or ClientRawResponse<Product> if
         raw==True
        :rtype: ~~lro.models.Product or
         ~msrest.pipeline.ClientRawResponse[~lro.models.Product]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = await self._put_async_retry_succeeded_initial(
            product=product,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            header_dict = {
                'Azure-AsyncOperation': self._deserialize('str', response.headers.get('Azure-AsyncOperation')),
                'Location': self._deserialize('str', response.headers.get('Location')),
                'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
            }
            deserialized = self._deserialize('Product', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                header_dict
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self._config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    put_async_retry_succeeded.metadata = {'url': '/lro/customheader/putasync/retry/succeeded'}


    async def _put201_creating_succeeded200_initial(
            self, product=None, *, cls=None, **operation_config):
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
        response = await self._client.pipeline.run(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)
        if response.status_code == 201:
            deserialized = self._deserialize('Product', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    async def put201_creating_succeeded200(
            self, product=None, *, cls=None, polling=True, **operation_config):
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is
        required message header for all requests. Long running put request,
        service returns a 201 to the initial request, with an entity that
        contains ProvisioningState=’Creating’.  Polls return this value until
        the last poll returns a ‘200’ with ProvisioningState=’Succeeded’.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of Product or ClientRawResponse<Product> if
         raw==True
        :rtype: ~~lro.models.Product or
         ~msrest.pipeline.ClientRawResponse[~lro.models.Product]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = await self._put201_creating_succeeded200_initial(
            product=product,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('Product', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                None
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self._config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    put201_creating_succeeded200.metadata = {'url': '/lro/customheader/put/201/creating/succeeded/200'}


    async def _post202_retry200_initial(
            self, product=None, *, cls=None, **operation_config):
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
        response = await self._client.pipeline.run(request, stream=False, **operation_config)

        if response.status_code not in [202]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            header_dict = {
                'Location': self._deserialize('str', response.headers.get('Location')),
                'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
            }
            header_dict
            return client_raw_response

    async def post202_retry200(
            self, product=None, *, cls=None, polling=True, **operation_config):
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is
        required message header for all requests. Long running post request,
        service returns a 202 to the initial request, with 'Location' and
        'Retry-After' headers, Polls return a 200 with a response body after
        success.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of None or ClientRawResponse<None> if raw==True
        :rtype: ~None or ~msrest.pipeline.ClientRawResponse[None]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = await self._post202_retry200_initial(
            product=product,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if cls:
                response_headers = {
                    'Location': self._deserialize('str', response.headers.get('Location')),
                    'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
                }
                return cls(response, None, response_headers)

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self._config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    post202_retry200.metadata = {'url': '/lro/customheader/post/202/retry/200'}


    async def _post_async_retry_succeeded_initial(
            self, product=None, *, cls=None, **operation_config):
        # Construct URL
        url = self.post_async_retry_succeeded.metadata['url']

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
        response = await self._client.pipeline.run(request, stream=False, **operation_config)

        if response.status_code not in [202]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            header_dict = {
                'Azure-AsyncOperation': self._deserialize('str', response.headers.get('Azure-AsyncOperation')),
                'Location': self._deserialize('str', response.headers.get('Location')),
                'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
            }
            header_dict
            return client_raw_response

    async def post_async_retry_succeeded(
            self, product=None, *, cls=None, polling=True, **operation_config):
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is
        required message header for all requests. Long running post request,
        service returns a 202 to the initial request, with an entity that
        contains ProvisioningState=’Creating’. Poll the endpoint indicated in
        the Azure-AsyncOperation header for operation status.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of None or ClientRawResponse<None> if raw==True
        :rtype: ~None or ~msrest.pipeline.ClientRawResponse[None]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = await self._post_async_retry_succeeded_initial(
            product=product,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if cls:
                response_headers = {
                    'Azure-AsyncOperation': self._deserialize('str', response.headers.get('Azure-AsyncOperation')),
                    'Location': self._deserialize('str', response.headers.get('Location')),
                    'Retry-After': self._deserialize('int', response.headers.get('Retry-After')),
                }
                return cls(response, None, response_headers)

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self._config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    post_async_retry_succeeded.metadata = {'url': '/lro/customheader/postasync/retry/succeeded'}
