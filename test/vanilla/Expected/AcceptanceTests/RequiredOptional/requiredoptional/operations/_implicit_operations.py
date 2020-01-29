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


class ImplicitOperations(object):
    """ImplicitOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~requiredoptional.models
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
    def get_required_path(
        self,
        path_parameter,  # type: str
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Test implicitly required path parameter.

        FIXME: add operation.summary

        :param path_parameter: MISSING·PARAMETER-DESCRIPTION
        :type path_parameter: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_required_path.metadata['url']
        path_format_arguments = {
            'pathParameter': self._serialize.url("path_parameter", path_parameter, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


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
          return cls(pipeline_response, None, {})

    get_required_path.metadata = {'url': '/reqopt/implicit/required/path/{pathParameter}'}

    @distributed_trace
    def put_optional_query(
        self,
        query_parameter=None,  # type: Optional[str]
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Test implicitly optional query parameter.

        FIXME: add operation.summary

        :param query_parameter: MISSING·PARAMETER-DESCRIPTION
        :type query_parameter: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_optional_query.metadata['url']

        # Construct parameters
        query_parameters = {}
        if query_parameter is not None:
            query_parameters['queryParameter'] = self._serialize.query("query_parameter", query_parameter, 'str')


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_optional_query.metadata = {'url': '/reqopt/implicit/optional/query'}

    @distributed_trace
    def put_optional_header(
        self,
        query_parameter=None,  # type: Optional[str]
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Test implicitly optional header parameter.

        FIXME: add operation.summary

        :param query_parameter: MISSING·PARAMETER-DESCRIPTION
        :type query_parameter: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_optional_header.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        if query_parameter is not None:
            header_parameters['queryParameter'] = self._serialize.header("query_parameter", query_parameter, 'str')


        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_optional_header.metadata = {'url': '/reqopt/implicit/optional/header'}

    @distributed_trace
    def put_optional_body(
        self,
        body_parameter=None,  # type: Optional[str]
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Test implicitly optional body parameter.

        FIXME: add operation.summary

        :param body_parameter: 
        :type body_parameter: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_optional_body.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if body_parameter is not None:
            body_content = self._serialize.body(body_parameter, 'str')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_optional_body.metadata = {'url': '/reqopt/implicit/optional/body'}

    @distributed_trace
    def get_required_global_path(
        self,
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Test implicitly required path parameter.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_required_global_path.metadata['url']
        path_format_arguments = {
            'required-global-path': self._serialize.url("self._config.required_global_path", self._config.required_global_path, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


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
          return cls(pipeline_response, None, {})

    get_required_global_path.metadata = {'url': '/reqopt/global/required/path/{required-global-path}'}

    @distributed_trace
    def get_required_global_query(
        self,
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Test implicitly required query parameter.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_required_global_query.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['required-global-query'] = self._serialize.query("self._config.required_global_query", self._config.required_global_query, 'str')


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
          return cls(pipeline_response, None, {})

    get_required_global_query.metadata = {'url': '/reqopt/global/required/query'}

    @distributed_trace
    def get_optional_global_query(
        self,
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Test implicitly optional query parameter.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_optional_global_query.metadata['url']

        # Construct parameters
        query_parameters = {}
        if self._config.optional_global_query is not None:
            query_parameters['optional-global-query'] = self._serialize.query("self._config.optional_global_query", self._config.optional_global_query, 'int')


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
          return cls(pipeline_response, None, {})

    get_optional_global_query.metadata = {'url': '/reqopt/global/optional/query'}
