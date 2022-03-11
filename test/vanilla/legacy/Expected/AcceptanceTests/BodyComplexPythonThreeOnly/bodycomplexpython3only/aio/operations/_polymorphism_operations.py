# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._polymorphism_operations import (
    build_get_complicated_request,
    build_get_composed_with_discriminator_request,
    build_get_composed_without_discriminator_request,
    build_get_dot_syntax_request,
    build_get_valid_request,
    build_put_complicated_request,
    build_put_missing_discriminator_request,
    build_put_valid_missing_required_request,
    build_put_valid_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PolymorphismOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodycomplexpython3only.aio.AutoRestComplexTestService`'s
        :attr:`polymorphism` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_valid(self, **kwargs: Any) -> "_models.Fish":
        """Get complex types that are polymorphic.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Fish, or the result of cls(response)
        :rtype: ~bodycomplexpython3only.models.Fish
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Fish"]

        request = build_get_valid_request(
            template_url=self.get_valid.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Fish", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_valid.metadata = {"url": "/complex/polymorphism/valid"}  # type: ignore

    @distributed_trace_async
    async def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: "_models.Fish", **kwargs: Any
    ) -> None:
        """Put complex types that are polymorphic.

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
        :type complex_body: ~bodycomplexpython3only.models.Fish
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = self._serialize.body(complex_body, "Fish")

        request = build_put_valid_request(
            content_type=content_type,
            json=_json,
            template_url=self.put_valid.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_valid.metadata = {"url": "/complex/polymorphism/valid"}  # type: ignore

    @distributed_trace_async
    async def get_dot_syntax(self, **kwargs: Any) -> "_models.DotFish":
        """Get complex types that are polymorphic, JSON key contains a dot.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DotFish, or the result of cls(response)
        :rtype: ~bodycomplexpython3only.models.DotFish
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DotFish"]

        request = build_get_dot_syntax_request(
            template_url=self.get_dot_syntax.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DotFish", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_dot_syntax.metadata = {"url": "/complex/polymorphism/dotsyntax"}  # type: ignore

    @distributed_trace_async
    async def get_composed_with_discriminator(self, **kwargs: Any) -> "_models.DotFishMarket":
        """Get complex object composing a polymorphic scalar property and array property with polymorphic
        element type, with discriminator specified. Deserialization must NOT fail and use the
        discriminator type specified on the wire.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DotFishMarket, or the result of cls(response)
        :rtype: ~bodycomplexpython3only.models.DotFishMarket
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DotFishMarket"]

        request = build_get_composed_with_discriminator_request(
            template_url=self.get_composed_with_discriminator.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DotFishMarket", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_composed_with_discriminator.metadata = {"url": "/complex/polymorphism/composedWithDiscriminator"}  # type: ignore

    @distributed_trace_async
    async def get_composed_without_discriminator(self, **kwargs: Any) -> "_models.DotFishMarket":
        """Get complex object composing a polymorphic scalar property and array property with polymorphic
        element type, without discriminator specified on wire. Deserialization must NOT fail and use
        the explicit type of the property.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DotFishMarket, or the result of cls(response)
        :rtype: ~bodycomplexpython3only.models.DotFishMarket
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DotFishMarket"]

        request = build_get_composed_without_discriminator_request(
            template_url=self.get_composed_without_discriminator.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DotFishMarket", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_composed_without_discriminator.metadata = {"url": "/complex/polymorphism/composedWithoutDiscriminator"}  # type: ignore

    @distributed_trace_async
    async def get_complicated(self, **kwargs: Any) -> "_models.Salmon":
        """Get complex types that are polymorphic, but not at the root of the hierarchy; also have
        additional properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Salmon, or the result of cls(response)
        :rtype: ~bodycomplexpython3only.models.Salmon
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Salmon"]

        request = build_get_complicated_request(
            template_url=self.get_complicated.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Salmon", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_complicated.metadata = {"url": "/complex/polymorphism/complicated"}  # type: ignore

    @distributed_trace_async
    async def put_complicated(  # pylint: disable=inconsistent-return-statements
        self, complex_body: "_models.Salmon", **kwargs: Any
    ) -> None:
        """Put complex types that are polymorphic, but not at the root of the hierarchy; also have
        additional properties.

        :param complex_body:
        :type complex_body: ~bodycomplexpython3only.models.Salmon
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = self._serialize.body(complex_body, "Salmon")

        request = build_put_complicated_request(
            content_type=content_type,
            json=_json,
            template_url=self.put_complicated.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_complicated.metadata = {"url": "/complex/polymorphism/complicated"}  # type: ignore

    @distributed_trace_async
    async def put_missing_discriminator(self, complex_body: "_models.Salmon", **kwargs: Any) -> "_models.Salmon":
        """Put complex types that are polymorphic, omitting the discriminator.

        :param complex_body:
        :type complex_body: ~bodycomplexpython3only.models.Salmon
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Salmon, or the result of cls(response)
        :rtype: ~bodycomplexpython3only.models.Salmon
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Salmon"]

        _json = self._serialize.body(complex_body, "Salmon")

        request = build_put_missing_discriminator_request(
            content_type=content_type,
            json=_json,
            template_url=self.put_missing_discriminator.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Salmon", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_missing_discriminator.metadata = {"url": "/complex/polymorphism/missingdiscriminator"}  # type: ignore

    @distributed_trace_async
    async def put_valid_missing_required(  # pylint: disable=inconsistent-return-statements
        self, complex_body: "_models.Fish", **kwargs: Any
    ) -> None:
        """Put complex types that are polymorphic, attempting to omit required 'birthday' field - the
        request should not be allowed from the client.

        :param complex_body: Please attempt put a sawshark that looks like this, the client should not
         allow this data to be sent:
         {
             "fishtype": "sawshark",
             "species": "snaggle toothed",
             "length": 18.5,
             "age": 2,
             "birthday": "2013-06-01T01:00:00Z",
             "location": "alaska",
             "picture": base64(FF FF FF FF FE),
             "siblings": [
                 {
                     "fishtype": "shark",
                     "species": "predator",
                     "birthday": "2012-01-05T01:00:00Z",
                     "length": 20,
                     "age": 6
                 },
                 {
                     "fishtype": "sawshark",
                     "species": "dangerous",
                     "picture": base64(FF FF FF FF FE),
                     "length": 10,
                     "age": 105
                 }
             ]
         }.
        :type complex_body: ~bodycomplexpython3only.models.Fish
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = self._serialize.body(complex_body, "Fish")

        request = build_put_valid_missing_required_request(
            content_type=content_type,
            json=_json,
            template_url=self.put_valid_missing_required.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_valid_missing_required.metadata = {"url": "/complex/polymorphism/missingrequired/invalid"}  # type: ignore
