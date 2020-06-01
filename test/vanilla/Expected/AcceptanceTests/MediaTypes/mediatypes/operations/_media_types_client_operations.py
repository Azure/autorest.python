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

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, IO, Optional, TypeVar, Union

    from azure.core import PipelineClient
    from msrest import Deserializer, Serializer

    from .._configuration import MediaTypesClientConfiguration


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
            # type: () -> MediaTypesClientConfiguration
            """Configuration of service client
            :rtype: MediaTypesClientConfiguration
            """

        @_config.setter
        def _config(self, value):
            # type: (MediaTypesClientConfiguration) -> None
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


class MediaTypesClientOperationsMixin(_MIXIN_BASE):

    @distributed_trace
    def analyze_body(
        self,
        input=None,  # type: Optional[Union[IO, "models.SourcePath"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Union[str, ClsReturnType]
        """Analyze body, that could be different media types.

        :param input: Input parameter.
        :type input: IO or ~mediatypes.models.SourcePath
        :keyword str content_type: Media type of the body sent to the API. Default value is "application/json".
         Allowed values are: "application/pdf", "image/jpeg", "image/png", "image/tiff", "application/json".
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[str, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.analyze_body.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        if header_parameters['Content-Type'].split(";")[0] in ['application/pdf', 'image/jpeg', 'image/png', 'image/tiff']:
            body_content_kwargs['stream_content'] = input
        elif header_parameters['Content-Type'].split(";")[0] in ['application/json']:
            if input is not None:
                body_content = self._serialize.body(input, 'SourcePath')
            else:
                body_content = None
            body_content_kwargs['content'] = body_content
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(header_parameters['Content-Type'])
            )
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    analyze_body.metadata = {'url': '/mediatypes/analyze'}  # type: ignore

    @distributed_trace
    def content_type_with_encoding(
        self,
        input,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Union[str, ClsReturnType]
        """Pass in contentType 'text/plain; encoding=UTF-8' to pass test. Value for input does not matter.

        :param input: Input parameter.
        :type input: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[str, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "text/plain")

        # Construct URL
        url = self.content_type_with_encoding.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(input, 'str')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    content_type_with_encoding.metadata = {'url': '/mediatypes/contentTypeWithEncoding'}  # type: ignore
