# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, IO, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MediaTypesClientOperationsMixin:

    @distributed_trace_async
    async def analyze_body(
        self,
        input: Optional[Union[IO, "models.SourcePath"]] = None,
        **kwargs
    ) -> str:
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
        cls = kwargs.pop('cls', None)  # type: ClsType[str]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.analyze_body.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

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
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    analyze_body.metadata = {'url': '/mediatypes/analyze'}  # type: ignore

    @distributed_trace_async
    async def content_type_with_encoding(
        self,
        input: str,
        **kwargs
    ) -> str:
        """Pass in contentType 'text/plain; encoding=UTF-8' to pass test. Value for input does not matter.

        :param input: Input parameter.
        :type input: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[str]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "text/plain")
        accept = "application/json"

        # Construct URL
        url = self.content_type_with_encoding.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(input, 'str')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    content_type_with_encoding.metadata = {'url': '/mediatypes/contentTypeWithEncoding'}  # type: ignore
