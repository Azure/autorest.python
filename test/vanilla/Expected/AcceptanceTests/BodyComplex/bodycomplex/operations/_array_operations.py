# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
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
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

    from azure.core.pipeline.transport import HttpRequest

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class ArrayOperations(object):
    """ArrayOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodycomplex.models
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
        # type: (...) -> "_models.ArrayWrapper"
        """Get complex types with array property.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ArrayWrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.ArrayWrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ArrayWrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_valid_request(template_url=self.get_valid.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("ArrayWrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_valid.metadata = {"url": "/complex/array/valid"}  # type: ignore

    @distributed_trace
    def put_valid(
        self,
        array=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types with array property.

        :param array:
        :type array: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _complex_body = _models.ArrayWrapper(array=array)
        _complex_body = self._serialize.body(_complex_body, "ArrayWrapper")

        request = self._put_valid_request(body=_complex_body, template_url=self.put_valid.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_valid.metadata = {"url": "/complex/array/valid"}  # type: ignore

    @distributed_trace
    def get_empty(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ArrayWrapper"
        """Get complex types with array property which is empty.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ArrayWrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.ArrayWrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ArrayWrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_empty_request(template_url=self.get_empty.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("ArrayWrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_empty.metadata = {"url": "/complex/array/empty"}  # type: ignore

    @distributed_trace
    def put_empty(
        self,
        array=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types with array property which is empty.

        :param array:
        :type array: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _complex_body = _models.ArrayWrapper(array=array)
        _complex_body = self._serialize.body(_complex_body, "ArrayWrapper")

        request = self._put_empty_request(body=_complex_body, template_url=self.put_empty.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_empty.metadata = {"url": "/complex/array/empty"}  # type: ignore

    @distributed_trace
    def get_not_provided(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ArrayWrapper"
        """Get complex types with array property while server doesn't provide a response payload.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ArrayWrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.ArrayWrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ArrayWrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_not_provided_request(template_url=self.get_not_provided.metadata["url"], **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("ArrayWrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_not_provided.metadata = {"url": "/complex/array/notprovided"}  # type: ignore
