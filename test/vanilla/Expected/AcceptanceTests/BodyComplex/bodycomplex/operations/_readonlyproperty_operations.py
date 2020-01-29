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
from msrest.serialization import Model

from .. import models


class ReadonlypropertyOperations(object):
    """ReadonlypropertyOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodycomplex.models
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
    def get_valid(
        self,
        cls=None,  # type: Optional[Callable[[HttpResponse, "ReadonlyObj", Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> "ReadonlyObj"
        """Get complex types that have readonly properties.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: ReadonlyObj or the result of cls(response)
        :rtype: ~bodycomplex.models.ReadonlyObj
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('ReadonlyObj', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_valid.metadata = {'url': '/complex/readonlyproperty/valid'}

    @distributed_trace
    def put_valid(
        self,
        size=None,  # type: Optional[int]
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Put complex types that have readonly properties.

        FIXME: add operation.summary

        :param size: MISSING·SCHEMA-DESCRIPTION-INTEGER
        :type size: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        complex_body = models.ReadonlyObj(size=size)

        # Construct URL
        url = self.put_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(complex_body, 'ReadonlyObj')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_valid.metadata = {'url': '/complex/readonlyproperty/valid'}
