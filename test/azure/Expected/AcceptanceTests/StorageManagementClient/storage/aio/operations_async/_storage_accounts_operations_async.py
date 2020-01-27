# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional, Union
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


class StorageAccountsOperations:
    """StorageAccountsOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~storage.models
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

    @distributed_trace_async
    async def check_name_availability(
        self,
        account_name: "StorageAccountCheckNameAvailabilityParameters",
        *,
        cls=None,
        **kwargs
    ) -> "CheckNameAvailabilityResult":
        """Checks that account name is valid and is not in use..

        FIXME: add operation.summary

        :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :type account_name: ~storage.models.StorageAccountCheckNameAvailabilityParameters
        :param callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityResult or the result of cls(response)
        :rtype: ~storage.models.CheckNameAvailabilityResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.check_name_availability.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(account_name, 'StorageAccountCheckNameAvailabilityParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = self._deserialize('CheckNameAvailabilityResult', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    check_name_availability.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Storage/checkNameAvailability'}

    
    async def _create_initial(
        self,
        resource_group_name: str,
        account_name: str,
        parameters: "StorageAccountCreateParameters",
        *,
        cls=None,
        **kwargs
    ) -> "StorageAccount":
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self._create_initial.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(parameters, 'StorageAccountCreateParameters')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('StorageAccount', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    _create_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}'}

    @distributed_trace_async
    async def create(
        self,
        resource_group_name: str,
        account_name: str,
        parameters: "StorageAccountCreateParameters",
        *,
        cls=None,
        polling: Optional[bool] = True,
        **kwargs
    ) -> "StorageAccount":
        """Asynchronously creates a new storage account with the specified parameters. Existing accounts cannot be updated with this API and should instead use the Update Storage Account API. If an account is already created and subsequent PUT request is issued with exact same set of properties, then HTTP 200 would be returned..

        FIXME: add operation.summary


        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param parameters: The parameters to provide for the created account.
        :type parameters: ~storage.models.StorageAccountCreateParameters
        :param callable cls: A custom type or function that will be passed the direct response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns StorageAccount
        :rtype: ~azure.core.polling.LROPoller[~storage.models.StorageAccount]

        :raises ~azure.mgmt.core.ARMError:
        """
        raw_result = await self._create_initial(
            resource_group_name=resource_group_name,
            account_name=account_name,
            parameters=parameters,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('StorageAccount', response)

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
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}'}


    @distributed_trace_async
    async def delete(
        self,
        resource_group_name: str,
        account_name: str,
        *,
        cls=None,
        **kwargs
    ) -> None:
        """Deletes a storage account in Microsoft Azure..

        FIXME: add operation.summary

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        if cls:
          return cls(response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}'}

    @distributed_trace_async
    async def get_properties(
        self,
        resource_group_name: str,
        account_name: str,
        *,
        cls=None,
        **kwargs
    ) -> "StorageAccount":
        """Returns the properties for the specified storage account including but not limited to name, account type, location, and account status. The ListKeys operation should be used to retrieve storage keys..

        FIXME: add operation.summary

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccount or the result of cls(response)
        :rtype: ~storage.models.StorageAccount
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_properties.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = self._deserialize('StorageAccount', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_properties.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}'}

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        account_name: str,
        parameters: "StorageAccountUpdateParameters",
        *,
        cls=None,
        **kwargs
    ) -> "StorageAccount":
        """Updates the account type or tags for a storage account. It can also be used to add a custom domain (note that custom domains cannot be added via the Create operation). Only one custom domain is supported per storage account. This API can only be used to update one of tags, accountType, or customDomain per call. To update multiple of these properties, call the API multiple times with one change per call. This call does not change the storage keys for the account. If you want to change storage account keys, use the RegenerateKey operation. The location and name of the storage account cannot be changed after creation..

        FIXME: add operation.summary

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param parameters: The parameters to update on the account. Note that only one property can be changed at a time using this API.
        :type parameters: ~storage.models.StorageAccountUpdateParameters
        :param callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccount or the result of cls(response)
        :rtype: ~storage.models.StorageAccount
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(parameters, 'StorageAccountUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = self._deserialize('StorageAccount', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}'}

    @distributed_trace_async
    async def list_keys(
        self,
        resource_group_name: str,
        account_name: str,
        *,
        cls=None,
        **kwargs
    ) -> "StorageAccountKeys":
        """Lists the access keys for the specified storage account..

        FIXME: add operation.summary

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccountKeys or the result of cls(response)
        :rtype: ~storage.models.StorageAccountKeys
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.list_keys.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = self._deserialize('StorageAccountKeys', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    list_keys.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/listKeys'}

    @distributed_trace
    async def list(
        self,
        cls=None,
        **kwargs
    ) -> "StorageAccountListResult":
        """Lists all the storage accounts available under the subscription. Note that storage keys are not returned; use the ListKeys operation for this..

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccountListResult or the result of cls(response)
        :rtype: ~storage.models.StorageAccountListResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
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
            deserialized = self._deserialize('StorageAccountListResult', response)
            list_of_elem = deserialized.value
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
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Storage/storageAccounts'}


    @distributed_trace
    async def list_by_resource_group(
        self,
        resource_group_name: str,
        *,
        cls=None,
        **kwargs
    ) -> "StorageAccountListResult":
        """Lists all the storage accounts available under the given resource group. Note that storage keys are not returned; use the ListKeys operation for this..

        FIXME: add operation.summary


        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccountListResult or the result of cls(response)
        :rtype: ~storage.models.StorageAccountListResult
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
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
            deserialized = self._deserialize('StorageAccountListResult', response)
            list_of_elem = deserialized.value
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
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts'}


    @distributed_trace_async
    async def regenerate_key(
        self,
        resource_group_name: str,
        account_name: str,
        key_name: Optional[Union[str, "KeyName"]] = None,
        *,
        cls=None,
        **kwargs
    ) -> "StorageAccountKeys":
        """Regenerates the access keys for the specified storage account..

        FIXME: add operation.summary

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param key_name: MISSING·SCHEMA-DESCRIPTION-CHOICE
        :type key_name: str or ~storage.models.KeyName
        :param callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccountKeys or the result of cls(response)
        :rtype: ~storage.models.StorageAccountKeys
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})
        regenerate_key = models.StorageAccountRegenerateKeyParameters(key_name=key_name)

        # Construct URL
        url = self.regenerate_key.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(regenerate_key, 'StorageAccountRegenerateKeyParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = self._deserialize('StorageAccountKeys', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    regenerate_key.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/regenerateKey'}
