# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models

T = TypeVar('T')
ClsReturnType = TypeVar('ClsReturnType')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], ClsReturnType]]

class PetsOperations:
    """PetsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~additionalproperties.models
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
        self._config = config

    @distributed_trace_async
    async def create_ap_true(
        self,
        create_parameters: "models.PetAPTrue",
        **kwargs
    ) -> Union["models.PetAPTrue", ClsReturnType]:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPTrue
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPTrue, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPTrue
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PetAPTrue", ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_ap_true.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(create_parameters, 'PetAPTrue')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PetAPTrue', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_ap_true.metadata = {'url': '/additionalProperties/true'}  # type: ignore

    @distributed_trace_async
    async def create_cat_ap_true(
        self,
        create_parameters: "models.CatAPTrue",
        **kwargs
    ) -> Union["models.CatAPTrue", ClsReturnType]:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.CatAPTrue
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CatAPTrue, or the result of cls(response)
        :rtype: ~additionalproperties.models.CatAPTrue
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CatAPTrue", ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_cat_ap_true.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(create_parameters, 'CatAPTrue')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('CatAPTrue', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_cat_ap_true.metadata = {'url': '/additionalProperties/true-subclass'}  # type: ignore

    @distributed_trace_async
    async def create_ap_object(
        self,
        create_parameters: "models.PetAPObject",
        **kwargs
    ) -> Union["models.PetAPObject", ClsReturnType]:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPObject
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPObject, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPObject
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PetAPObject", ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_ap_object.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(create_parameters, 'PetAPObject')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PetAPObject', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_ap_object.metadata = {'url': '/additionalProperties/type/object'}  # type: ignore

    @distributed_trace_async
    async def create_ap_string(
        self,
        create_parameters: "models.PetAPString",
        **kwargs
    ) -> Union["models.PetAPString", ClsReturnType]:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPString
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPString, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPString
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PetAPString", ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_ap_string.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(create_parameters, 'PetAPString')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PetAPString', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_ap_string.metadata = {'url': '/additionalProperties/type/string'}  # type: ignore

    @distributed_trace_async
    async def create_ap_in_properties(
        self,
        create_parameters: "models.PetAPInProperties",
        **kwargs
    ) -> Union["models.PetAPInProperties", ClsReturnType]:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPInProperties
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInProperties, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInProperties
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PetAPInProperties", ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_ap_in_properties.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(create_parameters, 'PetAPInProperties')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PetAPInProperties', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_ap_in_properties.metadata = {'url': '/additionalProperties/in/properties'}  # type: ignore

    @distributed_trace_async
    async def create_ap_in_properties_with_ap_string(
        self,
        create_parameters: "models.PetAPInPropertiesWithAPString",
        **kwargs
    ) -> Union["models.PetAPInPropertiesWithAPString", ClsReturnType]:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInPropertiesWithAPString, or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PetAPInPropertiesWithAPString", ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_ap_in_properties_with_ap_string.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(create_parameters, 'PetAPInPropertiesWithAPString')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PetAPInPropertiesWithAPString', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_ap_in_properties_with_ap_string.metadata = {'url': '/additionalProperties/in/properties/with/additionalProperties/string'}  # type: ignore
