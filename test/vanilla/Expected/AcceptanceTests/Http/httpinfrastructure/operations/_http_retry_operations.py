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


class HttpRetryOperations(object):
    """HttpRetryOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~httpinfrastructure.models
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
    def head408(
        self,
        cls=None,  # type: Callable[[HttpResponse, None, Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Return 408 status code, then 200 after retry.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~httpinfrastructure.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.head408.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    head408.metadata = {'url': '/http/retry/408'}

    @distributed_trace
    def put500(
        self,
        cls=None,  # type: Callable[[HttpResponse, None, Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Return 500 status code, then 200 after retry.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~httpinfrastructure.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.put500.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
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
          return cls(response, None, {})

    put500.metadata = {'url': '/http/retry/500'}

    @distributed_trace
    def patch500(
        self,
        cls=None,  # type: Callable[[HttpResponse, None, Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Return 500 status code, then 200 after retry.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~httpinfrastructure.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.patch500.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    patch500.metadata = {'url': '/http/retry/500'}

    @distributed_trace
    def get502(
        self,
        cls=None,  # type: Callable[[HttpResponse, None, Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Return 502 status code, then 200 after retry.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~httpinfrastructure.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get502.metadata['url']

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
          return cls(response, None, {})

    get502.metadata = {'url': '/http/retry/502'}

    @distributed_trace
    def options502(
        self,
        cls=None,  # type: Callable[[HttpResponse, bool, Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> bool
        """Return 502 status code, then 200 after retry.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: ~httpinfrastructure.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.options502.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.options(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('bool', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    options502.metadata = {'url': '/http/retry/502'}

    @distributed_trace
    def post503(
        self,
        cls=None,  # type: Callable[[HttpResponse, None, Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Return 503 status code, then 200 after retry.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~httpinfrastructure.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.post503.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post503.metadata = {'url': '/http/retry/503'}

    @distributed_trace
    def delete503(
        self,
        cls=None,  # type: Callable[[HttpResponse, None, Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Return 503 status code, then 200 after retry.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~httpinfrastructure.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.delete503.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    delete503.metadata = {'url': '/http/retry/503'}

    @distributed_trace
    def put504(
        self,
        cls=None,  # type: Callable[[HttpResponse, None, Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Return 504 status code, then 200 after retry.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~httpinfrastructure.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.put504.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
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
          return cls(response, None, {})

    put504.metadata = {'url': '/http/retry/504'}

    @distributed_trace
    def patch504(
        self,
        cls=None,  # type: Callable[[HttpResponse, None, Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Return 504 status code, then 200 after retry.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~httpinfrastructure.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.patch504.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    patch504.metadata = {'url': '/http/retry/504'}
