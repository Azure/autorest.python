# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, IO, Optional, TypeVar
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class FilesOperations(object):
    """FilesOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodyfile.models
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
    def get_file(
        self,
        cls=None,  # type: ClsType[IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """Get file.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: IO or the result of cls(response)
        :rtype: IO
        :raises: ~bodyfile.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_file.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'image/png'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_file.metadata = {'url': '/files/stream/nonempty'}

    @distributed_trace
    def get_file_large(
        self,
        cls=None,  # type: ClsType[IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """Get a large file.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: IO or the result of cls(response)
        :rtype: IO
        :raises: ~bodyfile.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_file_large.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'image/png'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_file_large.metadata = {'url': '/files/stream/verylarge'}

    @distributed_trace
    def get_empty_file(
        self,
        cls=None,  # type: ClsType[IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """Get empty file.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: IO or the result of cls(response)
        :rtype: IO
        :raises: ~bodyfile.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_empty_file.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'image/png'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_empty_file.metadata = {'url': '/files/stream/empty'}
