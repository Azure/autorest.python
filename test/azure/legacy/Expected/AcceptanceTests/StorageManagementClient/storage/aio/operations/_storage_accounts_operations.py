# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar, Union, cast

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._storage_accounts_operations import (
    build_check_name_availability_request,
    build_create_request_initial,
    build_delete_request,
    build_get_properties_request,
    build_list_by_resource_group_request,
    build_list_keys_request,
    build_list_request,
    build_regenerate_key_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class StorageAccountsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~storage.aio.StorageManagementClient`'s
        :attr:`storage_accounts` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def check_name_availability(
        self,
        account_name: _models.StorageAccountCheckNameAvailabilityParameters,
        *,
        content_type: Optional[str] = "application/json",
        **kwargs: Any
    ) -> _models.CheckNameAvailabilityResult:
        """Checks that account name is valid and is not in use.

        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: ~storage.models.StorageAccountCheckNameAvailabilityParameters
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "text/json". Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityResult, or the result of cls(response)
        :rtype: ~storage.models.CheckNameAvailabilityResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        api_version = kwargs.pop("api_version", "2015-05-01-preview")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CheckNameAvailabilityResult]

        _json = self._serialize.body(account_name, "StorageAccountCheckNameAvailabilityParameters")

        request = build_check_name_availability_request(
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.check_name_availability.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CheckNameAvailabilityResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_name_availability.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/checkNameAvailability"}  # type: ignore

    async def _create_initial(
        self,
        resource_group_name: str,
        account_name: str,
        parameters: _models.StorageAccountCreateParameters,
        *,
        content_type: Optional[str] = "application/json",
        **kwargs: Any
    ) -> Optional[_models.StorageAccount]:
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        api_version = kwargs.pop("api_version", "2015-05-01-preview")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[_models.StorageAccount]]

        _json = self._serialize.body(parameters, "StorageAccountCreateParameters")

        request = build_create_request_initial(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._create_initial.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("StorageAccount", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}"}  # type: ignore

    @distributed_trace_async
    async def begin_create(
        self,
        resource_group_name: str,
        account_name: str,
        parameters: _models.StorageAccountCreateParameters,
        *,
        content_type: Optional[str] = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.StorageAccount]:
        """Asynchronously creates a new storage account with the specified parameters. Existing accounts
        cannot be updated with this API and should instead use the Update Storage Account API. If an
        account is already created and subsequent PUT request is issued with exact same set of
        properties, then HTTP 200 would be returned.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param parameters: The parameters to provide for the created account.
        :type parameters: ~storage.models.StorageAccountCreateParameters
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "text/json". Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either StorageAccount or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~storage.models.StorageAccount]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop("api_version", "2015-05-01-preview")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.StorageAccount]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_initial(  # type: ignore
                resource_group_name=resource_group_name,
                account_name=account_name,
                parameters=parameters,
                content_type=content_type,
                api_version=api_version,
                cls=lambda x, y, z: x,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("StorageAccount", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, account_name: str, **kwargs: Any
    ) -> None:
        """Deletes a storage account in Microsoft Azure.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        api_version = kwargs.pop("api_version", "2015-05-01-preview")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}"}  # type: ignore

    @distributed_trace_async
    async def get_properties(
        self, resource_group_name: str, account_name: str, **kwargs: Any
    ) -> _models.StorageAccount:
        """Returns the properties for the specified storage account including but not limited to name,
        account type, location, and account status. The ListKeys operation should be used to retrieve
        storage keys.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccount, or the result of cls(response)
        :rtype: ~storage.models.StorageAccount
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        api_version = kwargs.pop("api_version", "2015-05-01-preview")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.StorageAccount]

        request = build_get_properties_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_properties.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("StorageAccount", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_properties.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}"}  # type: ignore

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        account_name: str,
        parameters: _models.StorageAccountUpdateParameters,
        *,
        content_type: Optional[str] = "application/json",
        **kwargs: Any
    ) -> _models.StorageAccount:
        """Updates the account type or tags for a storage account. It can also be used to add a custom
        domain (note that custom domains cannot be added via the Create operation). Only one custom
        domain is supported per storage account. This API can only be used to update one of tags,
        accountType, or customDomain per call. To update multiple of these properties, call the API
        multiple times with one change per call. This call does not change the storage keys for the
        account. If you want to change storage account keys, use the RegenerateKey operation. The
        location and name of the storage account cannot be changed after creation.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param parameters: The parameters to update on the account. Note that only one property can be
         changed at a time using this API.
        :type parameters: ~storage.models.StorageAccountUpdateParameters
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "text/json". Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccount, or the result of cls(response)
        :rtype: ~storage.models.StorageAccount
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        api_version = kwargs.pop("api_version", "2015-05-01-preview")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.StorageAccount]

        _json = self._serialize.body(parameters, "StorageAccountUpdateParameters")

        request = build_update_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("StorageAccount", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}"}  # type: ignore

    @distributed_trace_async
    async def list_keys(self, resource_group_name: str, account_name: str, **kwargs: Any) -> _models.StorageAccountKeys:
        """Lists the access keys for the specified storage account.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccountKeys, or the result of cls(response)
        :rtype: ~storage.models.StorageAccountKeys
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        api_version = kwargs.pop("api_version", "2015-05-01-preview")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.StorageAccountKeys]

        request = build_list_keys_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_keys.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("StorageAccountKeys", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_keys.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/listKeys"}  # type: ignore

    @distributed_trace
    def list(self, **kwargs: Any) -> AsyncIterable[_models.StorageAccountListResult]:
        """Lists all the storage accounts available under the subscription. Note that storage keys are not
        returned; use the ListKeys operation for this.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either StorageAccountListResult or the result of
         cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~storage.models.StorageAccountListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop("api_version", "2015-05-01-preview")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.StorageAccountListResult]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:

                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("StorageAccountListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/storageAccounts"}  # type: ignore

    @distributed_trace
    def list_by_resource_group(
        self, resource_group_name: str, **kwargs: Any
    ) -> AsyncIterable[_models.StorageAccountListResult]:
        """Lists all the storage accounts available under the given resource group. Note that storage keys
        are not returned; use the ListKeys operation for this.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either StorageAccountListResult or the result of
         cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~storage.models.StorageAccountListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop("api_version", "2015-05-01-preview")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.StorageAccountListResult]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_by_resource_group.metadata["url"],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:

                request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("StorageAccountListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_resource_group.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts"}  # type: ignore

    @distributed_trace_async
    async def regenerate_key(
        self,
        resource_group_name: str,
        account_name: str,
        key_name: Optional[Union[str, "_models.KeyName"]] = None,
        *,
        content_type: Optional[str] = "application/json",
        **kwargs: Any
    ) -> _models.StorageAccountKeys:
        """Regenerates the access keys for the specified storage account.

        :param resource_group_name: The name of the resource group within the user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param key_name:  Default value is None.
        :type key_name: str or ~storage.models.KeyName
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/json" or "text/json". Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageAccountKeys, or the result of cls(response)
        :rtype: ~storage.models.StorageAccountKeys
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        api_version = kwargs.pop("api_version", "2015-05-01-preview")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.StorageAccountKeys]

        _regenerate_key = _models.StorageAccountRegenerateKeyParameters(key_name=key_name)
        _json = self._serialize.body(_regenerate_key, "StorageAccountRegenerateKeyParameters")

        request = build_regenerate_key_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.regenerate_key.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("StorageAccountKeys", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    regenerate_key.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/regenerateKey"}  # type: ignore
