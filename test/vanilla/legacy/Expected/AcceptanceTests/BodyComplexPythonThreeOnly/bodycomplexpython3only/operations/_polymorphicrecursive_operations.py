# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from msrest import Serializer

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._vendor import _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_valid_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/complex/polymorphicrecursive/valid")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_put_valid_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/complex/polymorphicrecursive/valid")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


class PolymorphicrecursiveOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodycomplexpython3only.AutoRestComplexTestService`'s
        :attr:`polymorphicrecursive` attribute.
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
        """Get complex types that are polymorphic and have recursive references.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Fish or the result of cls(response)
        :rtype: ~bodycomplexpython3only.models.Fish
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Fish]

        request = build_get_valid_request(
            template_url=self.get_valid.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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

    get_valid.metadata = {"url": "/complex/polymorphicrecursive/valid"}  # type: ignore

    @overload
    def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: _models.Fish, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Put complex types that are polymorphic and have recursive references.

        :param complex_body: Please put a salmon that looks like this:
         {
             "fishtype": "salmon",
             "species": "king",
             "length": 1,
             "age": 1,
             "location": "alaska",
             "iswild": true,
             "siblings": [
                 {
                     "fishtype": "shark",
                     "species": "predator",
                     "length": 20,
                     "age": 6,
                     "siblings": [
                         {
                             "fishtype": "salmon",
                             "species": "coho",
                             "length": 2,
                             "age": 2,
                             "location": "atlantic",
                             "iswild": true,
                             "siblings": [
                                 {
                                     "fishtype": "shark",
                                     "species": "predator",
                                     "length": 20,
                                     "age": 6
                                 },
                                 {
                                     "fishtype": "sawshark",
                                     "species": "dangerous",
                                     "length": 10,
                                     "age": 105
                                 }
                             ]
                         },
                         {
                             "fishtype": "sawshark",
                             "species": "dangerous",
                             "length": 10,
                             "age": 105
                         }
                     ]
                 },
                 {
                     "fishtype": "sawshark",
                     "species": "dangerous",
                     "length": 10,
                     "age": 105
                 }
             ]
         }. Required.
        :type complex_body: ~bodycomplexpython3only.models.Fish
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """

    @overload
    def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Put complex types that are polymorphic and have recursive references.

        :param complex_body: Please put a salmon that looks like this:
         {
             "fishtype": "salmon",
             "species": "king",
             "length": 1,
             "age": 1,
             "location": "alaska",
             "iswild": true,
             "siblings": [
                 {
                     "fishtype": "shark",
                     "species": "predator",
                     "length": 20,
                     "age": 6,
                     "siblings": [
                         {
                             "fishtype": "salmon",
                             "species": "coho",
                             "length": 2,
                             "age": 2,
                             "location": "atlantic",
                             "iswild": true,
                             "siblings": [
                                 {
                                     "fishtype": "shark",
                                     "species": "predator",
                                     "length": 20,
                                     "age": 6
                                 },
                                 {
                                     "fishtype": "sawshark",
                                     "species": "dangerous",
                                     "length": 10,
                                     "age": 105
                                 }
                             ]
                         },
                         {
                             "fishtype": "sawshark",
                             "species": "dangerous",
                             "length": 10,
                             "age": 105
                         }
                     ]
                 },
                 {
                     "fishtype": "sawshark",
                     "species": "dangerous",
                     "length": 10,
                     "age": 105
                 }
             ]
         }. Required.
        :type complex_body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """

    @distributed_trace
    def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: Union[_models.Fish, IO], **kwargs: Any
    ) -> None:
        """Put complex types that are polymorphic and have recursive references.

        :param complex_body: Please put a salmon that looks like this:
         {
             "fishtype": "salmon",
             "species": "king",
             "length": 1,
             "age": 1,
             "location": "alaska",
             "iswild": true,
             "siblings": [
                 {
                     "fishtype": "shark",
                     "species": "predator",
                     "length": 20,
                     "age": 6,
                     "siblings": [
                         {
                             "fishtype": "salmon",
                             "species": "coho",
                             "length": 2,
                             "age": 2,
                             "location": "atlantic",
                             "iswild": true,
                             "siblings": [
                                 {
                                     "fishtype": "shark",
                                     "species": "predator",
                                     "length": 20,
                                     "age": 6
                                 },
                                 {
                                     "fishtype": "sawshark",
                                     "species": "dangerous",
                                     "length": 10,
                                     "age": 105
                                 }
                             ]
                         },
                         {
                             "fishtype": "sawshark",
                             "species": "dangerous",
                             "length": 10,
                             "age": 105
                         }
                     ]
                 },
                 {
                     "fishtype": "sawshark",
                     "species": "dangerous",
                     "length": 10,
                     "age": 105
                 }
             ]
         }. Is either a model type or a IO type. Required.
        :type complex_body: ~bodycomplexpython3only.models.Fish or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(complex_body, (IO, bytes)):
            _content = complex_body
        else:
            _json = self._serialize.body(complex_body, "Fish")

        request = build_put_valid_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.put_valid.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_valid.metadata = {"url": "/complex/polymorphicrecursive/valid"}  # type: ignore
