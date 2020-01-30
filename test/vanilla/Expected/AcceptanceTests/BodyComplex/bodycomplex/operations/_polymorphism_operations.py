# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from msrest.serialization import Model

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class PolymorphismOperations(object):
    """PolymorphismOperations operations.

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
        cls=None,  # type: ClsType["Fish"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "Fish"
        """Get complex types that are polymorphic.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: Fish or the result of cls(response)
        :rtype: ~bodycomplex.models.Fish
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

        deserialized = self._deserialize('Fish', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_valid.metadata = {'url': '/complex/polymorphism/valid'}

    @distributed_trace
    def put_valid(
        self,
        complex_body,  # type: "Fish"
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types that are polymorphic.

        FIXME: add operation.summary

        :param complex_body: Please put a salmon that looks like this:
    {
            'fishtype':'Salmon',
            'location':'alaska',
            'iswild':true,
            'species':'king',
            'length':1.0,
            'siblings':[
              {
                'fishtype':'Shark',
                'age':6,
                'birthday': '2012-01-05T01:00:00Z',
                'length':20.0,
                'species':'predator',
              },
              {
                'fishtype':'Sawshark',
                'age':105,
                'birthday': '1900-01-05T01:00:00Z',
                'length':10.0,
                'picture': new Buffer([255, 255, 255, 255, 254]).toString('base64'),
                'species':'dangerous',
              },
              {
                'fishtype': 'goblin',
                'age': 1,
                'birthday': '2015-08-08T00:00:00Z',
                'length': 30.0,
                'species': 'scary',
                'jawsize': 5
              }
            ]
          };.
        :type complex_body: ~bodycomplex.models.Fish
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(complex_body, 'Fish')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_valid.metadata = {'url': '/complex/polymorphism/valid'}

    @distributed_trace
    def get_dot_syntax(
        self,
        cls=None,  # type: ClsType["DotFish"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "DotFish"
        """Get complex types that are polymorphic, JSON key contains a dot.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: DotFish or the result of cls(response)
        :rtype: ~bodycomplex.models.DotFish
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_dot_syntax.metadata['url']

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

        deserialized = self._deserialize('DotFish', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_dot_syntax.metadata = {'url': '/complex/polymorphism/dotsyntax'}

    @distributed_trace
    def get_composed_with_discriminator(
        self,
        cls=None,  # type: ClsType["DotFishMarket"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "DotFishMarket"
        """Get complex object composing a polymorphic scalar property and array property with polymorphic element type, with discriminator specified. Deserialization must NOT fail and use the discriminator type specified on the wire.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: DotFishMarket or the result of cls(response)
        :rtype: ~bodycomplex.models.DotFishMarket
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_composed_with_discriminator.metadata['url']

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

        deserialized = self._deserialize('DotFishMarket', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_composed_with_discriminator.metadata = {'url': '/complex/polymorphism/composedWithDiscriminator'}

    @distributed_trace
    def get_composed_without_discriminator(
        self,
        cls=None,  # type: ClsType["DotFishMarket"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "DotFishMarket"
        """Get complex object composing a polymorphic scalar property and array property with polymorphic element type, without discriminator specified on wire. Deserialization must NOT fail and use the explicit type of the property.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: DotFishMarket or the result of cls(response)
        :rtype: ~bodycomplex.models.DotFishMarket
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_composed_without_discriminator.metadata['url']

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

        deserialized = self._deserialize('DotFishMarket', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_composed_without_discriminator.metadata = {'url': '/complex/polymorphism/composedWithoutDiscriminator'}

    @distributed_trace
    def get_complicated(
        self,
        cls=None,  # type: ClsType["Salmon"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "Salmon"
        """Get complex types that are polymorphic, but not at the root of the hierarchy; also have additional properties.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: Salmon or the result of cls(response)
        :rtype: ~bodycomplex.models.Salmon
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_complicated.metadata['url']

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

        deserialized = self._deserialize('Salmon', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_complicated.metadata = {'url': '/complex/polymorphism/complicated'}

    @distributed_trace
    def put_complicated(
        self,
        complex_body,  # type: "Salmon"
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types that are polymorphic, but not at the root of the hierarchy; also have additional properties.

        FIXME: add operation.summary

        :param complex_body: 
        :type complex_body: ~bodycomplex.models.Salmon
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_complicated.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(complex_body, 'Salmon')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_complicated.metadata = {'url': '/complex/polymorphism/complicated'}

    @distributed_trace
    def put_missing_discriminator(
        self,
        complex_body,  # type: "Salmon"
        cls=None,  # type: ClsType["Salmon"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "Salmon"
        """Put complex types that are polymorphic, omitting the discriminator.

        FIXME: add operation.summary

        :param complex_body: 
        :type complex_body: ~bodycomplex.models.Salmon
        :param callable cls: A custom type or function that will be passed the direct response
        :return: Salmon or the result of cls(response)
        :rtype: ~bodycomplex.models.Salmon
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_missing_discriminator.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(complex_body, 'Salmon')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('Salmon', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    put_missing_discriminator.metadata = {'url': '/complex/polymorphism/missingdiscriminator'}

    @distributed_trace
    def put_valid_missing_required(
        self,
        complex_body,  # type: "Fish"
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types that are polymorphic, attempting to omit required 'birthday' field - the request should not be allowed from the client.

        FIXME: add operation.summary

        :param complex_body: Please put a salmon that looks like this:
    {
            'fishtype':'Salmon',
            'location':'alaska',
            'iswild':true,
            'species':'king',
            'length':1.0,
            'siblings':[
              {
                'fishtype':'Shark',
                'age':6,
                'birthday': '2012-01-05T01:00:00Z',
                'length':20.0,
                'species':'predator',
              },
              {
                'fishtype':'Sawshark',
                'age':105,
                'birthday': '1900-01-05T01:00:00Z',
                'length':10.0,
                'picture': new Buffer([255, 255, 255, 255, 254]).toString('base64'),
                'species':'dangerous',
              },
              {
                'fishtype': 'goblin',
                'age': 1,
                'birthday': '2015-08-08T00:00:00Z',
                'length': 30.0,
                'species': 'scary',
                'jawsize': 5
              }
            ]
          };.
        :type complex_body: ~bodycomplex.models.Fish
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_valid_missing_required.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(complex_body, 'Fish')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_valid_missing_required.metadata = {'url': '/complex/polymorphism/missingrequired/invalid'}
