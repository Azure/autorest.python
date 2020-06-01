# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    from azure.core import PipelineClient
    from msrest import Deserializer, Serializer

    from .._configuration import ObjectTypeClientConfiguration


    T = TypeVar('T')
    ClsReturnType = TypeVar('ClsReturnType')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], ClsReturnType]]

    class AbstractServiceClient(object):
        """Abstract class of a service client to help with type hints for the following mixin class"""

        def __init__(self):
            # type: () -> None
            """
            Init for abstract service client class
            """

        @property
        def _client(self):
            # type: () -> PipelineClient
            """Pipeline client
            :rtype: PipelineClient
            """

        @_client.setter
        def _client(self, value):
            # type: (PipelineClient) -> None
            """Set the pipeline client"""

        @property
        def _config(self):
            # type: () -> ObjectTypeClientConfiguration
            """Configuration of service client
            :rtype: ObjectTypeClientConfiguration
            """

        @_config.setter
        def _config(self, value):
            # type: (ObjectTypeClientConfiguration) -> None
            """Set the configuration"""

        @property
        def _serialize(self):
            # type: () -> Serializer
            """Serializer
            :rtype: Serializer
            """

        @_serialize.setter
        def _serialize(self, value):
            # type: (Serializer) -> None
            """Set the serializer"""

        @property
        def _deserialize(self):
            # type: () -> Deserializer
            """Deserializer
            :rtype: Deserializer
            """

        @_deserialize.setter
        def _deserialize(self, value):
            # type: (Deserializer) -> None
            """Set the deserializer"""

    # https://github.com/python/mypy/issues/5837
    _MIXIN_BASE = AbstractServiceClient
else:
    _MIXIN_BASE = object


class ObjectTypeClientOperationsMixin(_MIXIN_BASE):

    @distributed_trace
    def get(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Union[object, ClsReturnType]
        """Basic get that returns an object. Returns object { 'message': 'An object was successfully
        returned' }.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: object, or the result of cls(response)
        :rtype: object
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[object, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize('object', response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('object', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/objectType/get'}  # type: ignore

    @distributed_trace
    def put(
        self,
        put_object,  # type: object
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional[ClsReturnType]
        """Basic put that puts an object. Pass in {'foo': 'bar'} to get a 200 and anything else to get an
        object error.

        :param put_object: Pass in {'foo': 'bar'} for a 200, anything else for an object error.
        :type put_object: object
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.put.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(put_object, 'object')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize('object', response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

        return None
    put.metadata = {'url': '/objectType/put'}  # type: ignore
