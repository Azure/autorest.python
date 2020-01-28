# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator import distributed_trace
from msrest.serialization import Model

from .. import models


class PetsOperations(object):
    """PetsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~additionalproperties.models
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
    def create_ap_true(
        self,
        create_parameters,  # type: "PetAPTrue"
        cls=None,  # type: Callable[[HttpResponse, "PetAPTrue", Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> "PetAPTrue"
        """Create a Pet which contains more properties than what is defined..

        FIXME: add operation.summary

        :param create_parameters: 
        :type create_parameters: ~additionalproperties.models.PetAPTrue
        :param callable cls: A custom type or function that will be passed the direct response
        :return: PetAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPTrue
        :raises: ~additionalproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.create_ap_true.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(create_parameters, 'PetAPTrue')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('PetAPTrue', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    create_ap_true.metadata = {'url': '/additionalProperties/true'}

    @distributed_trace
    def create_cat_ap_true(
        self,
        create_parameters,  # type: "CatAPTrue"
        cls=None,  # type: Callable[[HttpResponse, "CatAPTrue", Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> "CatAPTrue"
        """Create a CatAPTrue which contains more properties than what is defined..

        FIXME: add operation.summary

        :param create_parameters: 
        :type create_parameters: ~additionalproperties.models.CatAPTrue
        :param callable cls: A custom type or function that will be passed the direct response
        :return: CatAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.CatAPTrue
        :raises: ~additionalproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.create_cat_ap_true.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(create_parameters, 'CatAPTrue')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('CatAPTrue', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    create_cat_ap_true.metadata = {'url': '/additionalProperties/true-subclass'}

    @distributed_trace
    def create_ap_object(
        self,
        create_parameters,  # type: "PetAPObject"
        cls=None,  # type: Callable[[HttpResponse, "PetAPObject", Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> "PetAPObject"
        """Create a Pet which contains more properties than what is defined..

        FIXME: add operation.summary

        :param create_parameters: 
        :type create_parameters: ~additionalproperties.models.PetAPObject
        :param callable cls: A custom type or function that will be passed the direct response
        :return: PetAPObject or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPObject
        :raises: ~additionalproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.create_ap_object.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(create_parameters, 'PetAPObject')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('PetAPObject', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    create_ap_object.metadata = {'url': '/additionalProperties/type/object'}

    @distributed_trace
    def create_ap_string(
        self,
        create_parameters,  # type: "PetAPString"
        cls=None,  # type: Callable[[HttpResponse, "PetAPString", Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> "PetAPString"
        """Create a Pet which contains more properties than what is defined..

        FIXME: add operation.summary

        :param create_parameters: 
        :type create_parameters: ~additionalproperties.models.PetAPString
        :param callable cls: A custom type or function that will be passed the direct response
        :return: PetAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPString
        :raises: ~additionalproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.create_ap_string.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(create_parameters, 'PetAPString')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('PetAPString', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    create_ap_string.metadata = {'url': '/additionalProperties/type/string'}

    @distributed_trace
    def create_ap_in_properties(
        self,
        create_parameters,  # type: "PetAPInProperties"
        cls=None,  # type: Callable[[HttpResponse, "PetAPInProperties", Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> "PetAPInProperties"
        """Create a Pet which contains more properties than what is defined..

        FIXME: add operation.summary

        :param create_parameters: 
        :type create_parameters: ~additionalproperties.models.PetAPInProperties
        :param callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInProperties or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInProperties
        :raises: ~additionalproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.create_ap_in_properties.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(create_parameters, 'PetAPInProperties')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('PetAPInProperties', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    create_ap_in_properties.metadata = {'url': '/additionalProperties/in/properties'}

    @distributed_trace
    def create_ap_in_properties_with_ap_string(
        self,
        create_parameters,  # type: "PetAPInPropertiesWithAPString"
        cls=None,  # type: Callable[[HttpResponse, "PetAPInPropertiesWithAPString", Dict[str, Any]], Any]
        **kwargs  # type: **Any
    ):
        # type: (...) -> "PetAPInPropertiesWithAPString"
        """Create a Pet which contains more properties than what is defined..

        FIXME: add operation.summary

        :param create_parameters: 
        :type create_parameters: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :param callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInPropertiesWithAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :raises: ~additionalproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.create_ap_in_properties_with_ap_string.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(create_parameters, 'PetAPInPropertiesWithAPString')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('PetAPInPropertiesWithAPString', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    create_ap_in_properties_with_ap_string.metadata = {'url': '/additionalProperties/in/properties/with/additionalProperties/string'}
