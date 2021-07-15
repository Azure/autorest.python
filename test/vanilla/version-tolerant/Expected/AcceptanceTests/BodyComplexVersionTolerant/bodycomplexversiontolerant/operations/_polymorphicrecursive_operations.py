# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

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

from .. import models as _models
from .._rest import polymorphicrecursive as rest_polymorphicrecursive

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class PolymorphicrecursiveOperations(object):
    """PolymorphicrecursiveOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodycomplexversiontolerant.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_valid(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> "_models.Fish"
        """Get complex types that are polymorphic and have recursive references.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Fish, or the result of cls(response)
        :rtype: ~bodycomplexversiontolerant.models.Fish
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Fish"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_polymorphicrecursive.build_get_valid_request(
            template_url=self.get_valid.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Fish", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_valid.metadata = {"url": "/complex/polymorphicrecursive/valid"}  # type: ignore

    @distributed_trace
    def put_valid(
        self,
        complex_body,  # type: "_models.Fish"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
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
         }.
        :type complex_body: ~bodycomplexversiontolerant.models.Fish
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(complex_body, "Fish")

        request = rest_polymorphicrecursive.build_put_valid_request(
            content_type=content_type,
            json=json,
            template_url=self.put_valid.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_valid.metadata = {"url": "/complex/polymorphicrecursive/valid"}  # type: ignore
