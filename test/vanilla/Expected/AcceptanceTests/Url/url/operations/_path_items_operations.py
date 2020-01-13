# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator import distributed_trace

from .. import models


class PathItemsOperations(object):
    """PathItemsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~url.models
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
    def get_all_with_values(self, path_item_string_path, local_string_path, path_item_string_query=None, local_string_query=None, cls=None, **kwargs):
        # type: (str, str, Optional[str], Optional[str], Optional[Any], **Any) -> None
        """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath', localStringPath='localStringPath', globalStringQuery='globalStringQuery', pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

        FIXME: add operation.summary


        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'
        :type local_string_path: str
        :param path_item_string_query: A string value 'pathItemStringQuery' that appears as a query parameter
        :type path_item_string_query: str
        :param local_string_query: should contain value 'localStringQuery'
        :type local_string_query: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~url.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_all_with_values.metadata['url']
        path_format_arguments = {
            'pathItemStringPath': self._serialize.url("path_item_string_path", path_item_string_path, 'str'),
            'globalStringPath': self._serialize.url("self._config.global_string_path", self._config.global_string_path, 'str'),
            'localStringPath': self._serialize.url("local_string_path", local_string_path, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if path_item_string_query is not None:
            query_parameters['pathItemStringQuery'] = self._serialize.query("path_item_string_query", path_item_string_query, 'str')
        if self._config.global_string_query is not None:
            query_parameters['globalStringQuery'] = self._serialize.query("self._config.global_string_query", self._config.global_string_query, 'str')
        if local_string_query is not None:
            query_parameters['localStringQuery'] = self._serialize.query("local_string_query", local_string_query, 'str')


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    get_all_with_values.metadata = {'url': '/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/pathItemStringQuery/localStringQuery'}

    @distributed_trace
    def get_global_query_null(self, path_item_string_path, local_string_path, path_item_string_query=None, local_string_query=None, cls=None, **kwargs):
        # type: (str, str, Optional[str], Optional[str], Optional[Any], **Any) -> None
        """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath', localStringPath='localStringPath', globalStringQuery=null, pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

        FIXME: add operation.summary


        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'
        :type local_string_path: str
        :param path_item_string_query: A string value 'pathItemStringQuery' that appears as a query parameter
        :type path_item_string_query: str
        :param local_string_query: should contain value 'localStringQuery'
        :type local_string_query: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~url.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_global_query_null.metadata['url']
        path_format_arguments = {
            'pathItemStringPath': self._serialize.url("path_item_string_path", path_item_string_path, 'str'),
            'globalStringPath': self._serialize.url("self._config.global_string_path", self._config.global_string_path, 'str'),
            'localStringPath': self._serialize.url("local_string_path", local_string_path, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if path_item_string_query is not None:
            query_parameters['pathItemStringQuery'] = self._serialize.query("path_item_string_query", path_item_string_query, 'str')
        if self._config.global_string_query is not None:
            query_parameters['globalStringQuery'] = self._serialize.query("self._config.global_string_query", self._config.global_string_query, 'str')
        if local_string_query is not None:
            query_parameters['localStringQuery'] = self._serialize.query("local_string_query", local_string_query, 'str')


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    get_global_query_null.metadata = {'url': '/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/localStringQuery'}

    @distributed_trace
    def get_global_and_local_query_null(self, path_item_string_path, local_string_path, path_item_string_query=None, local_string_query=None, cls=None, **kwargs):
        # type: (str, str, Optional[str], Optional[str], Optional[Any], **Any) -> None
        """send globalStringPath=globalStringPath, pathItemStringPath='pathItemStringPath', localStringPath='localStringPath', globalStringQuery=null, pathItemStringQuery='pathItemStringQuery', localStringQuery=null.

        FIXME: add operation.summary


        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'
        :type local_string_path: str
        :param path_item_string_query: A string value 'pathItemStringQuery' that appears as a query parameter
        :type path_item_string_query: str
        :param local_string_query: should contain value 'localStringQuery'
        :type local_string_query: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~url.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_global_and_local_query_null.metadata['url']
        path_format_arguments = {
            'pathItemStringPath': self._serialize.url("path_item_string_path", path_item_string_path, 'str'),
            'globalStringPath': self._serialize.url("self._config.global_string_path", self._config.global_string_path, 'str'),
            'localStringPath': self._serialize.url("local_string_path", local_string_path, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if path_item_string_query is not None:
            query_parameters['pathItemStringQuery'] = self._serialize.query("path_item_string_query", path_item_string_query, 'str')
        if self._config.global_string_query is not None:
            query_parameters['globalStringQuery'] = self._serialize.query("self._config.global_string_query", self._config.global_string_query, 'str')
        if local_string_query is not None:
            query_parameters['localStringQuery'] = self._serialize.query("local_string_query", local_string_query, 'str')


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    get_global_and_local_query_null.metadata = {'url': '/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/null'}

    @distributed_trace
    def get_local_path_item_query_null(self, path_item_string_path, local_string_path, path_item_string_query=None, local_string_query=None, cls=None, **kwargs):
        # type: (str, str, Optional[str], Optional[str], Optional[Any], **Any) -> None
        """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath', localStringPath='localStringPath', globalStringQuery='globalStringQuery', pathItemStringQuery=null, localStringQuery=null.

        FIXME: add operation.summary


        :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path
        :type path_item_string_path: str
        :param local_string_path: should contain value 'localStringPath'
        :type local_string_path: str
        :param path_item_string_query: A string value 'pathItemStringQuery' that appears as a query parameter
        :type path_item_string_query: str
        :param local_string_query: should contain value 'localStringQuery'
        :type local_string_query: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~url.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_local_path_item_query_null.metadata['url']
        path_format_arguments = {
            'pathItemStringPath': self._serialize.url("path_item_string_path", path_item_string_path, 'str'),
            'globalStringPath': self._serialize.url("self._config.global_string_path", self._config.global_string_path, 'str'),
            'localStringPath': self._serialize.url("local_string_path", local_string_path, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if path_item_string_query is not None:
            query_parameters['pathItemStringQuery'] = self._serialize.query("path_item_string_query", path_item_string_query, 'str')
        if self._config.global_string_query is not None:
            query_parameters['globalStringQuery'] = self._serialize.query("self._config.global_string_query", self._config.global_string_query, 'str')
        if local_string_query is not None:
            query_parameters['localStringQuery'] = self._serialize.query("local_string_query", local_string_query, 'str')


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    get_local_path_item_query_null.metadata = {'url': '/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/null/null'}

