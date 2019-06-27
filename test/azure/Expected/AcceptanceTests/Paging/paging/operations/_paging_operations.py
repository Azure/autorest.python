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
from azure.core.polling import LROPoller, NoPolling
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models


class PagingOperations(object):
    """PagingOperations operations.

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

    def get_single_pages(
            self, cls=None, **kwargs):
        """A paging operation that finishes on the first call without a nextlink.

        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises:
         :class:`CloudErrorException<paging.models.CloudErrorException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_single_pages.metadata['url']

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self._config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if self._config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            error_map = kwargs.pop('error_map', None)
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException(response, self._deserialize)

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize)

        return deserialized
    get_single_pages.metadata = {'url': '/paging/single'}

    def get_multiple_pages(
            self, client_request_id=None, paging_get_multiple_pages_options=None, cls=None, **kwargs):
        """A paging operation that includes a nextLink that has 10 pages.

        :param client_request_id:
        :type client_request_id: str
        :param paging_get_multiple_pages_options: Additional parameters for
         the operation
        :type paging_get_multiple_pages_options:
         ~paging.models.PagingGetMultiplePagesOptions
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises:
         :class:`CloudErrorException<paging.models.CloudErrorException>`
        """
        maxresults = None
        if paging_get_multiple_pages_options is not None:
            maxresults = paging_get_multiple_pages_options.maxresults
        timeout = None
        if paging_get_multiple_pages_options is not None:
            timeout = paging_get_multiple_pages_options.timeout

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages.metadata['url']

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self._config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if client_request_id is not None:
                header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
            if self._config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
            if maxresults is not None:
                header_parameters['maxresults'] = self._serialize.header("maxresults", maxresults, 'int')
            if timeout is not None:
                header_parameters['timeout'] = self._serialize.header("timeout", timeout, 'int')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            error_map = kwargs.pop('error_map', None)
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException(response, self._deserialize)

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize)

        return deserialized
    get_multiple_pages.metadata = {'url': '/paging/multiple'}

    def get_odata_multiple_pages(
            self, client_request_id=None, paging_get_odata_multiple_pages_options=None, cls=None, **kwargs):
        """A paging operation that includes a nextLink in odata format that has 10
        pages.

        :param client_request_id:
        :type client_request_id: str
        :param paging_get_odata_multiple_pages_options: Additional parameters
         for the operation
        :type paging_get_odata_multiple_pages_options:
         ~paging.models.PagingGetOdataMultiplePagesOptions
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged1[~paging.models.Product]
        :raises:
         :class:`CloudErrorException<paging.models.CloudErrorException>`
        """
        maxresults = None
        if paging_get_odata_multiple_pages_options is not None:
            maxresults = paging_get_odata_multiple_pages_options.maxresults
        timeout = None
        if paging_get_odata_multiple_pages_options is not None:
            timeout = paging_get_odata_multiple_pages_options.timeout

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_odata_multiple_pages.metadata['url']

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self._config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if client_request_id is not None:
                header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
            if self._config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
            if maxresults is not None:
                header_parameters['maxresults'] = self._serialize.header("maxresults", maxresults, 'int')
            if timeout is not None:
                header_parameters['timeout'] = self._serialize.header("timeout", timeout, 'int')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            error_map = kwargs.pop('error_map', None)
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException(response, self._deserialize)

            return response

        # Deserialize response
        deserialized = models.ProductPaged1(internal_paging, self._deserialize)

        return deserialized
    get_odata_multiple_pages.metadata = {'url': '/paging/multiple/odata'}

    def get_multiple_pages_with_offset(
            self, paging_get_multiple_pages_with_offset_options, client_request_id=None, cls=None, **kwargs):
        """A paging operation that includes a nextLink that has 10 pages.

        :param paging_get_multiple_pages_with_offset_options: Additional
         parameters for the operation
        :type paging_get_multiple_pages_with_offset_options:
         ~paging.models.PagingGetMultiplePagesWithOffsetOptions
        :param client_request_id:
        :type client_request_id: str
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises:
         :class:`CloudErrorException<paging.models.CloudErrorException>`
        """
        maxresults = None
        if paging_get_multiple_pages_with_offset_options is not None:
            maxresults = paging_get_multiple_pages_with_offset_options.maxresults
        offset = None
        if paging_get_multiple_pages_with_offset_options is not None:
            offset = paging_get_multiple_pages_with_offset_options.offset
        timeout = None
        if paging_get_multiple_pages_with_offset_options is not None:
            timeout = paging_get_multiple_pages_with_offset_options.timeout

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_with_offset.metadata['url']
                path_format_arguments = {
                    'offset': self._serialize.url("offset", offset, 'int')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self._config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if client_request_id is not None:
                header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
            if self._config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
            if maxresults is not None:
                header_parameters['maxresults'] = self._serialize.header("maxresults", maxresults, 'int')
            if timeout is not None:
                header_parameters['timeout'] = self._serialize.header("timeout", timeout, 'int')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            error_map = kwargs.pop('error_map', None)
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException(response, self._deserialize)

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize)

        return deserialized
    get_multiple_pages_with_offset.metadata = {'url': '/paging/multiple/withpath/{offset}'}

    def get_multiple_pages_retry_first(
            self, cls=None, **kwargs):
        """A paging operation that fails on the first call with 500 and then
        retries and then get a response including a nextLink that has 10 pages.

        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises:
         :class:`CloudErrorException<paging.models.CloudErrorException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_retry_first.metadata['url']

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self._config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if self._config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            error_map = kwargs.pop('error_map', None)
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException(response, self._deserialize)

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize)

        return deserialized
    get_multiple_pages_retry_first.metadata = {'url': '/paging/multiple/retryfirst'}

    def get_multiple_pages_retry_second(
            self, cls=None, **kwargs):
        """A paging operation that includes a nextLink that has 10 pages, of which
        the 2nd call fails first with 500. The client should retry and finish
        all 10 pages eventually.

        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises:
         :class:`CloudErrorException<paging.models.CloudErrorException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_retry_second.metadata['url']

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self._config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if self._config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            error_map = kwargs.pop('error_map', None)
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException(response, self._deserialize)

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize)

        return deserialized
    get_multiple_pages_retry_second.metadata = {'url': '/paging/multiple/retrysecond'}

    def get_single_pages_failure(
            self, cls=None, **kwargs):
        """A paging operation that receives a 400 on the first call.

        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises:
         :class:`CloudErrorException<paging.models.CloudErrorException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_single_pages_failure.metadata['url']

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self._config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if self._config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            error_map = kwargs.pop('error_map', None)
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException(response, self._deserialize)

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize)

        return deserialized
    get_single_pages_failure.metadata = {'url': '/paging/single/failure'}

    def get_multiple_pages_failure(
            self, cls=None, **kwargs):
        """A paging operation that receives a 400 on the second call.

        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises:
         :class:`CloudErrorException<paging.models.CloudErrorException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_failure.metadata['url']

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self._config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if self._config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            error_map = kwargs.pop('error_map', None)
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException(response, self._deserialize)

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize)

        return deserialized
    get_multiple_pages_failure.metadata = {'url': '/paging/multiple/failure'}

    def get_multiple_pages_failure_uri(
            self, cls=None, **kwargs):
        """A paging operation that receives an invalid nextLink.

        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises:
         :class:`CloudErrorException<paging.models.CloudErrorException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_failure_uri.metadata['url']

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self._config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if self._config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            error_map = kwargs.pop('error_map', None)
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException(response, self._deserialize)

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize)

        return deserialized
    get_multiple_pages_failure_uri.metadata = {'url': '/paging/multiple/failureuri'}

    def get_multiple_pages_fragment_next_link(
            self, api_version, tenant, cls=None, **kwargs):
        """A paging operation that doesn't return a full URL, just a fragment.

        :param api_version: Sets the api version to use.
        :type api_version: str
        :param tenant: Sets the tenant to use.
        :type tenant: str
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged1[~paging.models.Product]
        :raises:
         :class:`CloudErrorException<paging.models.CloudErrorException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_fragment_next_link.metadata['url']
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", tenant, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api_version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = '/paging/multiple/fragment/{tenant}/{nextLink}'
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", tenant, 'str'),
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True)
                }
                url = self._client.format_url(url, **path_format_arguments)
                query_parameters = {}
                query_parameters['api_version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self._config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if self._config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            error_map = kwargs.pop('error_map', None)
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException(response, self._deserialize)

            return response

        # Deserialize response
        deserialized = models.ProductPaged1(internal_paging, self._deserialize)

        return deserialized
    get_multiple_pages_fragment_next_link.metadata = {'url': '/paging/multiple/fragment/{tenant}'}

    def get_multiple_pages_fragment_with_grouping_next_link(
            self, custom_parameter_group, cls=None, **kwargs):
        """A paging operation that doesn't return a full URL, just a fragment with
        parameters grouped.

        :param custom_parameter_group: Additional parameters for the operation
        :type custom_parameter_group: ~paging.models.CustomParameterGroup
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged1[~paging.models.Product]
        :raises:
         :class:`CloudErrorException<paging.models.CloudErrorException>`
        """
        api_version = None
        if custom_parameter_group is not None:
            api_version = custom_parameter_group.api_version
        tenant = None
        if custom_parameter_group is not None:
            tenant = custom_parameter_group.tenant

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_multiple_pages_fragment_with_grouping_next_link.metadata['url']
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", tenant, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api_version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = '/paging/multiple/fragmentwithgrouping/{tenant}/{nextLink}'
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", tenant, 'str'),
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True)
                }
                url = self._client.format_url(url, **path_format_arguments)
                query_parameters = {}
                query_parameters['api_version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self._config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if self._config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            error_map = kwargs.pop('error_map', None)
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException(response, self._deserialize)

            return response

        # Deserialize response
        deserialized = models.ProductPaged1(internal_paging, self._deserialize)

        return deserialized
    get_multiple_pages_fragment_with_grouping_next_link.metadata = {'url': '/paging/multiple/fragmentwithgrouping/{tenant}'}


    def _get_multiple_pages_lro_initial(
            self, client_request_id=None, paging_get_multiple_pages_lro_options=None, cls=None, **kwargs):
        error_map = kwargs.pop('error_map', None)
        maxresults = None
        if paging_get_multiple_pages_lro_options is not None:
            maxresults = paging_get_multiple_pages_lro_options.maxresults
        timeout = None
        if paging_get_multiple_pages_lro_options is not None:
            timeout = paging_get_multiple_pages_lro_options.timeout

        # Construct URL
        url = self.get_multiple_pages_lro.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if client_request_id is not None:
            header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
        if maxresults is not None:
            header_parameters['maxresults'] = self._serialize.header("maxresults", maxresults, 'int')
        if timeout is not None:
            header_parameters['timeout'] = self._serialize.header("timeout", timeout, 'int')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException(response, self._deserialize)

        deserialized = None

        if response.status_code == 202:
            deserialized = self._deserialize('ProductResult', response)

        return deserialized

    def get_multiple_pages_lro(
            self, client_request_id=None, paging_get_multiple_pages_lro_options=None, cls=None, polling=True, **kwargs):
        """A long-running paging operation that includes a nextLink that has 10
        pages.

        :param client_request_id:
        :type client_request_id: str
        :param paging_get_multiple_pages_lro_options: Additional parameters
         for the operation
        :type paging_get_multiple_pages_lro_options:
         ~paging.models.PagingGetMultiplePagesLroOptions
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns ProductResult
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~paging.models.ProductResult]
        :raises:
         :class:`CloudErrorException<paging.models.CloudErrorException>`
        """
        raw_result = self._get_multiple_pages_lro_initial(
            client_request_id=client_request_id,
            paging_get_multiple_pages_lro_options=paging_get_multiple_pages_lro_options,
            **kwargs
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('ProductResult', response)

            return deserialized

        lro_delay = kwargs.get(
            'long_running_operation_timeout',
            self._config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    get_multiple_pages_lro.metadata = {'url': '/paging/multiple/lro'}
