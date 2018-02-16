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
from msrest.pipeline import ClientRawResponse

from .. import models


class ParameterGroupingOperations(object):
    """ParameterGroupingOperations operations.

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

        self.config = config

    def post_required(
            self, parameter_grouping_post_required_parameters, custom_headers=None, raw=False, **operation_config):
        """Post a bunch of required parameters grouped.

        :param parameter_grouping_post_required_parameters: Additional
         parameters for the operation
        :type parameter_grouping_post_required_parameters:
         ~azureparametergrouping.models.ParameterGroupingPostRequiredParameters
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azureparametergrouping.models.ErrorException>`
        """
        body = None
        if parameter_grouping_post_required_parameters is not None:
            body = parameter_grouping_post_required_parameters.body
        custom_header = None
        if parameter_grouping_post_required_parameters is not None:
            custom_header = parameter_grouping_post_required_parameters.custom_header
        query = None
        if parameter_grouping_post_required_parameters is not None:
            query = parameter_grouping_post_required_parameters.query
        path = None
        if parameter_grouping_post_required_parameters is not None:
            path = parameter_grouping_post_required_parameters.path

        # Construct URL
        url = self.post_required.metadata['url']
        path_format_arguments = {
            'path': self._serialize.url("path", path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if query is not None:
            query_parameters['query'] = self._serialize.query("query", query, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if custom_header is not None:
            header_parameters['customHeader'] = self._serialize.header("custom_header", custom_header, 'str')

        # Construct body
        body_content = self._serialize.body(body, 'int')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    post_required.metadata = {'url': '/parameterGrouping/postRequired/{path}'}

    def post_optional(
            self, parameter_grouping_post_optional_parameters=None, custom_headers=None, raw=False, **operation_config):
        """Post a bunch of optional parameters grouped.

        :param parameter_grouping_post_optional_parameters: Additional
         parameters for the operation
        :type parameter_grouping_post_optional_parameters:
         ~azureparametergrouping.models.ParameterGroupingPostOptionalParameters
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azureparametergrouping.models.ErrorException>`
        """
        custom_header = None
        if parameter_grouping_post_optional_parameters is not None:
            custom_header = parameter_grouping_post_optional_parameters.custom_header
        query = None
        if parameter_grouping_post_optional_parameters is not None:
            query = parameter_grouping_post_optional_parameters.query

        # Construct URL
        url = self.post_optional.metadata['url']

        # Construct parameters
        query_parameters = {}
        if query is not None:
            query_parameters['query'] = self._serialize.query("query", query, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if custom_header is not None:
            header_parameters['customHeader'] = self._serialize.header("custom_header", custom_header, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    post_optional.metadata = {'url': '/parameterGrouping/postOptional'}

    def post_multi_param_groups(
            self, first_parameter_group=None, parameter_grouping_post_multi_param_groups_second_param_group=None, custom_headers=None, raw=False, **operation_config):
        """Post parameters from multiple different parameter groups.

        :param first_parameter_group: Additional parameters for the operation
        :type first_parameter_group:
         ~azureparametergrouping.models.FirstParameterGroup
        :param parameter_grouping_post_multi_param_groups_second_param_group:
         Additional parameters for the operation
        :type parameter_grouping_post_multi_param_groups_second_param_group:
         ~azureparametergrouping.models.ParameterGroupingPostMultiParamGroupsSecondParamGroup
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azureparametergrouping.models.ErrorException>`
        """
        header_one = None
        if first_parameter_group is not None:
            header_one = first_parameter_group.header_one
        query_one = None
        if first_parameter_group is not None:
            query_one = first_parameter_group.query_one
        header_two = None
        if parameter_grouping_post_multi_param_groups_second_param_group is not None:
            header_two = parameter_grouping_post_multi_param_groups_second_param_group.header_two
        query_two = None
        if parameter_grouping_post_multi_param_groups_second_param_group is not None:
            query_two = parameter_grouping_post_multi_param_groups_second_param_group.query_two

        # Construct URL
        url = self.post_multi_param_groups.metadata['url']

        # Construct parameters
        query_parameters = {}
        if query_one is not None:
            query_parameters['query-one'] = self._serialize.query("query_one", query_one, 'int')
        if query_two is not None:
            query_parameters['query-two'] = self._serialize.query("query_two", query_two, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if header_one is not None:
            header_parameters['header-one'] = self._serialize.header("header_one", header_one, 'str')
        if header_two is not None:
            header_parameters['header-two'] = self._serialize.header("header_two", header_two, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    post_multi_param_groups.metadata = {'url': '/parameterGrouping/postMultipleParameterGroups'}

    def post_shared_parameter_group_object(
            self, first_parameter_group=None, custom_headers=None, raw=False, **operation_config):
        """Post parameters with a shared parameter group object.

        :param first_parameter_group: Additional parameters for the operation
        :type first_parameter_group:
         ~azureparametergrouping.models.FirstParameterGroup
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azureparametergrouping.models.ErrorException>`
        """
        header_one = None
        if first_parameter_group is not None:
            header_one = first_parameter_group.header_one
        query_one = None
        if first_parameter_group is not None:
            query_one = first_parameter_group.query_one

        # Construct URL
        url = self.post_shared_parameter_group_object.metadata['url']

        # Construct parameters
        query_parameters = {}
        if query_one is not None:
            query_parameters['query-one'] = self._serialize.query("query_one", query_one, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if header_one is not None:
            header_parameters['header-one'] = self._serialize.header("header_one", header_one, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    post_shared_parameter_group_object.metadata = {'url': '/parameterGrouping/sharedParameterGroupObject'}
