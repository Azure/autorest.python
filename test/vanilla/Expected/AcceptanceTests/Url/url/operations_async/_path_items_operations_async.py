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

from msrest.pipeline import ClientRawResponse

from .. import models


class PathItemsOperations:
    """PathItemsOperations async operations.

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

        self.config = config

    async def get_all_with_values(
            self, local_string_path, path_item_string_path, local_string_query=None, path_item_string_query=None, *, custom_headers=None, raw=False, **operation_config):
        """send globalStringPath='globalStringPath',
        pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath',
        globalStringQuery='globalStringQuery',
        pathItemStringQuery='pathItemStringQuery',
        localStringQuery='localStringQuery'.

        :param local_string_path: should contain value 'localStringPath'
        :type local_string_path: str
        :param path_item_string_path: A string value 'pathItemStringPath' that
         appears in the path
        :type path_item_string_path: str
        :param local_string_query: should contain value 'localStringQuery'
        :type local_string_query: str
        :param path_item_string_query: A string value 'pathItemStringQuery'
         that appears as a query parameter
        :type path_item_string_query: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.get_all_with_values.metadata['url']
        path_format_arguments = {
            'localStringPath': self._serialize.url("local_string_path", local_string_path, 'str'),
            'pathItemStringPath': self._serialize.url("path_item_string_path", path_item_string_path, 'str'),
            'globalStringPath': self._serialize.url("self.config.global_string_path", self.config.global_string_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if local_string_query is not None:
            query_parameters['localStringQuery'] = self._serialize.query("local_string_query", local_string_query, 'str')
        if path_item_string_query is not None:
            query_parameters['pathItemStringQuery'] = self._serialize.query("path_item_string_query", path_item_string_query, 'str')
        if self.config.global_string_query is not None:
            query_parameters['globalStringQuery'] = self._serialize.query("self.config.global_string_query", self.config.global_string_query, 'str')

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_all_with_values.metadata = {'url': '/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/pathItemStringQuery/localStringQuery'}

    async def get_global_query_null(
            self, local_string_path, path_item_string_path, local_string_query=None, path_item_string_query=None, *, custom_headers=None, raw=False, **operation_config):
        """send globalStringPath='globalStringPath',
        pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery=null,
        pathItemStringQuery='pathItemStringQuery',
        localStringQuery='localStringQuery'.

        :param local_string_path: should contain value 'localStringPath'
        :type local_string_path: str
        :param path_item_string_path: A string value 'pathItemStringPath' that
         appears in the path
        :type path_item_string_path: str
        :param local_string_query: should contain value 'localStringQuery'
        :type local_string_query: str
        :param path_item_string_query: A string value 'pathItemStringQuery'
         that appears as a query parameter
        :type path_item_string_query: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.get_global_query_null.metadata['url']
        path_format_arguments = {
            'localStringPath': self._serialize.url("local_string_path", local_string_path, 'str'),
            'pathItemStringPath': self._serialize.url("path_item_string_path", path_item_string_path, 'str'),
            'globalStringPath': self._serialize.url("self.config.global_string_path", self.config.global_string_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if local_string_query is not None:
            query_parameters['localStringQuery'] = self._serialize.query("local_string_query", local_string_query, 'str')
        if path_item_string_query is not None:
            query_parameters['pathItemStringQuery'] = self._serialize.query("path_item_string_query", path_item_string_query, 'str')
        if self.config.global_string_query is not None:
            query_parameters['globalStringQuery'] = self._serialize.query("self.config.global_string_query", self.config.global_string_query, 'str')

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_global_query_null.metadata = {'url': '/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/localStringQuery'}

    async def get_global_and_local_query_null(
            self, local_string_path, path_item_string_path, local_string_query=None, path_item_string_query=None, *, custom_headers=None, raw=False, **operation_config):
        """send globalStringPath=globalStringPath,
        pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath', globalStringQuery=null,
        pathItemStringQuery='pathItemStringQuery', localStringQuery=null.

        :param local_string_path: should contain value 'localStringPath'
        :type local_string_path: str
        :param path_item_string_path: A string value 'pathItemStringPath' that
         appears in the path
        :type path_item_string_path: str
        :param local_string_query: should contain null value
        :type local_string_query: str
        :param path_item_string_query: A string value 'pathItemStringQuery'
         that appears as a query parameter
        :type path_item_string_query: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.get_global_and_local_query_null.metadata['url']
        path_format_arguments = {
            'localStringPath': self._serialize.url("local_string_path", local_string_path, 'str'),
            'pathItemStringPath': self._serialize.url("path_item_string_path", path_item_string_path, 'str'),
            'globalStringPath': self._serialize.url("self.config.global_string_path", self.config.global_string_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if local_string_query is not None:
            query_parameters['localStringQuery'] = self._serialize.query("local_string_query", local_string_query, 'str')
        if path_item_string_query is not None:
            query_parameters['pathItemStringQuery'] = self._serialize.query("path_item_string_query", path_item_string_query, 'str')
        if self.config.global_string_query is not None:
            query_parameters['globalStringQuery'] = self._serialize.query("self.config.global_string_query", self.config.global_string_query, 'str')

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_global_and_local_query_null.metadata = {'url': '/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/null'}

    async def get_local_path_item_query_null(
            self, local_string_path, path_item_string_path, local_string_query=None, path_item_string_query=None, *, custom_headers=None, raw=False, **operation_config):
        """send globalStringPath='globalStringPath',
        pathItemStringPath='pathItemStringPath',
        localStringPath='localStringPath',
        globalStringQuery='globalStringQuery', pathItemStringQuery=null,
        localStringQuery=null.

        :param local_string_path: should contain value 'localStringPath'
        :type local_string_path: str
        :param path_item_string_path: A string value 'pathItemStringPath' that
         appears in the path
        :type path_item_string_path: str
        :param local_string_query: should contain value null
        :type local_string_query: str
        :param path_item_string_query: should contain value null
        :type path_item_string_query: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.get_local_path_item_query_null.metadata['url']
        path_format_arguments = {
            'localStringPath': self._serialize.url("local_string_path", local_string_path, 'str'),
            'pathItemStringPath': self._serialize.url("path_item_string_path", path_item_string_path, 'str'),
            'globalStringPath': self._serialize.url("self.config.global_string_path", self.config.global_string_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if local_string_query is not None:
            query_parameters['localStringQuery'] = self._serialize.query("local_string_query", local_string_query, 'str')
        if path_item_string_query is not None:
            query_parameters['pathItemStringQuery'] = self._serialize.query("path_item_string_query", path_item_string_query, 'str')
        if self.config.global_string_query is not None:
            query_parameters['globalStringQuery'] = self._serialize.query("self.config.global_string_query", self.config.global_string_query, 'str')

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_local_path_item_query_null.metadata = {'url': '/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/null/null'}
