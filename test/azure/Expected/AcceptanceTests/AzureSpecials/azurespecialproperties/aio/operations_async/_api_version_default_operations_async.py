# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models


class ApiVersionDefaultOperations:
    """ApiVersionDefaultOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azurespecialproperties.models
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
    async def get_method_global_valid(self, cls=None, **kwargs) -> None:

        """GET method with api-version modeled in global settings..

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_method_global_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    get_method_global_valid.metadata = {'url': '/azurespecials/apiVersion/method/string/none/query/global/2015-07-01-preview'}

    @distributed_trace_async
    async def get_method_global_not_provided_valid(self, cls=None, **kwargs) -> None:

        """GET method with api-version modeled in global settings..

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_method_global_not_provided_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    get_method_global_not_provided_valid.metadata = {'url': '/azurespecials/apiVersion/method/string/none/query/globalNotProvided/2015-07-01-preview'}

    @distributed_trace_async
    async def get_path_global_valid(self, cls=None, **kwargs) -> None:

        """GET method with api-version modeled in global settings..

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_path_global_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    get_path_global_valid.metadata = {'url': '/azurespecials/apiVersion/path/string/none/query/global/2015-07-01-preview'}

    @distributed_trace_async
    async def get_swagger_global_valid(self, cls=None, **kwargs) -> None:

        """GET method with api-version modeled in global settings..

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_swagger_global_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    get_swagger_global_valid.metadata = {'url': '/azurespecials/apiVersion/swagger/string/none/query/global/2015-07-01-preview'}
