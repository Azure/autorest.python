# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from msrest import Serializer

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()


def build_get_valid_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/complex/polymorphism/valid")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_put_valid_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/complex/polymorphism/valid")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_get_dot_syntax_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/complex/polymorphism/dotsyntax")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_get_composed_with_discriminator_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/complex/polymorphism/composedWithDiscriminator")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_get_composed_without_discriminator_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/complex/polymorphism/composedWithoutDiscriminator")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_get_complicated_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/complex/polymorphism/complicated")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_put_complicated_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/complex/polymorphism/complicated")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_put_missing_discriminator_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/complex/polymorphism/missingdiscriminator")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_put_valid_missing_required_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/complex/polymorphism/missingrequired/invalid")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


class PolymorphismOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodycomplex.AutoRestComplexTestService`'s
        :attr:`polymorphism` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_valid(self, **kwargs: Any) -> _models.Fish:
        """Get complex types that are polymorphic.

        :return: Fish or the result of cls(response)
        :rtype: ~bodycomplex.models.Fish
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.Fish] = kwargs.pop("cls", None)

        _request = build_get_valid_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Fish", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: _models.Fish, *, content_type: str = "application/json", **kwargs: Any
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
               };. Required.
        :type complex_body: ~bodycomplex.models.Fish
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
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
               };. Required.
        :type complex_body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: Union[_models.Fish, IO[bytes]], **kwargs: Any
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
               };. Is either a Fish type or a IO[bytes] type. Required.
        :type complex_body: ~bodycomplex.models.Fish or IO[bytes]
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(complex_body, (IOBase, bytes)):
            _content = complex_body
        else:
            _json = self._serialize.body(complex_body, "Fish")

        _request = build_put_valid_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def get_dot_syntax(self, **kwargs: Any) -> _models.DotFish:
        """Get complex types that are polymorphic, JSON key contains a dot.

        :return: DotFish or the result of cls(response)
        :rtype: ~bodycomplex.models.DotFish
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.DotFish] = kwargs.pop("cls", None)

        _request = build_get_dot_syntax_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DotFish", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def get_composed_with_discriminator(self, **kwargs: Any) -> _models.DotFishMarket:
        """Get complex object composing a polymorphic scalar property and array property with polymorphic
        element type, with discriminator specified. Deserialization must NOT fail and use the
        discriminator type specified on the wire.

        :return: DotFishMarket or the result of cls(response)
        :rtype: ~bodycomplex.models.DotFishMarket
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.DotFishMarket] = kwargs.pop("cls", None)

        _request = build_get_composed_with_discriminator_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DotFishMarket", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def get_composed_without_discriminator(self, **kwargs: Any) -> _models.DotFishMarket:
        """Get complex object composing a polymorphic scalar property and array property with polymorphic
        element type, without discriminator specified on wire. Deserialization must NOT fail and use
        the explicit type of the property.

        :return: DotFishMarket or the result of cls(response)
        :rtype: ~bodycomplex.models.DotFishMarket
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.DotFishMarket] = kwargs.pop("cls", None)

        _request = build_get_composed_without_discriminator_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DotFishMarket", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def get_complicated(self, **kwargs: Any) -> _models.Salmon:
        """Get complex types that are polymorphic, but not at the root of the hierarchy; also have
        additional properties.

        :return: Salmon or the result of cls(response)
        :rtype: ~bodycomplex.models.Salmon
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.Salmon] = kwargs.pop("cls", None)

        _request = build_get_complicated_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Salmon", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def put_complicated(  # pylint: disable=inconsistent-return-statements
        self, complex_body: _models.Salmon, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Put complex types that are polymorphic, but not at the root of the hierarchy; also have
        additional properties.

        :param complex_body: Required.
        :type complex_body: ~bodycomplex.models.Salmon
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def put_complicated(  # pylint: disable=inconsistent-return-statements
        self, complex_body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Put complex types that are polymorphic, but not at the root of the hierarchy; also have
        additional properties.

        :param complex_body: Required.
        :type complex_body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def put_complicated(  # pylint: disable=inconsistent-return-statements
        self, complex_body: Union[_models.Salmon, IO[bytes]], **kwargs: Any
    ) -> None:
        """Put complex types that are polymorphic, but not at the root of the hierarchy; also have
        additional properties.

        :param complex_body: Is either a Salmon type or a IO[bytes] type. Required.
        :type complex_body: ~bodycomplex.models.Salmon or IO[bytes]
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(complex_body, (IOBase, bytes)):
            _content = complex_body
        else:
            _json = self._serialize.body(complex_body, "Salmon")

        _request = build_put_complicated_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def put_missing_discriminator(
        self, complex_body: _models.Salmon, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Salmon:
        """Put complex types that are polymorphic, omitting the discriminator.

        :param complex_body: Required.
        :type complex_body: ~bodycomplex.models.Salmon
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Salmon or the result of cls(response)
        :rtype: ~bodycomplex.models.Salmon
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def put_missing_discriminator(
        self, complex_body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Salmon:
        """Put complex types that are polymorphic, omitting the discriminator.

        :param complex_body: Required.
        :type complex_body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Salmon or the result of cls(response)
        :rtype: ~bodycomplex.models.Salmon
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def put_missing_discriminator(
        self, complex_body: Union[_models.Salmon, IO[bytes]], **kwargs: Any
    ) -> _models.Salmon:
        """Put complex types that are polymorphic, omitting the discriminator.

        :param complex_body: Is either a Salmon type or a IO[bytes] type. Required.
        :type complex_body: ~bodycomplex.models.Salmon or IO[bytes]
        :return: Salmon or the result of cls(response)
        :rtype: ~bodycomplex.models.Salmon
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Salmon] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(complex_body, (IOBase, bytes)):
            _content = complex_body
        else:
            _json = self._serialize.body(complex_body, "Salmon")

        _request = build_put_missing_discriminator_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Salmon", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def put_valid_missing_required(  # pylint: disable=inconsistent-return-statements
        self, complex_body: _models.Fish, *, content_type: str = "application/json", **kwargs: Any
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
         }. Required.
        :type complex_body: ~bodycomplex.models.Fish
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def put_valid_missing_required(  # pylint: disable=inconsistent-return-statements
        self, complex_body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
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
         }. Required.
        :type complex_body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def put_valid_missing_required(  # pylint: disable=inconsistent-return-statements
        self, complex_body: Union[_models.Fish, IO[bytes]], **kwargs: Any
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
         }. Is either a Fish type or a IO[bytes] type. Required.
        :type complex_body: ~bodycomplex.models.Fish or IO[bytes]
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(complex_body, (IOBase, bytes)):
            _content = complex_body
        else:
            _json = self._serialize.body(complex_body, "Fish")

        _request = build_put_valid_missing_required_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
