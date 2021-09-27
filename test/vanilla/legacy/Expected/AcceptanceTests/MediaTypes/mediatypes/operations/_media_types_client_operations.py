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
from msrest import Serializer

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, IO, Optional, TypeVar, Union

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_analyze_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[Union[str, "_models.ContentType"]]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/mediatypes/analyze')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_analyze_body_no_accept_header_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[Union[str, "_models.ContentType"]]

    # Construct URL
    url = kwargs.pop("template_url", '/mediatypes/analyzeNoAccept')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_content_type_with_encoding_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/mediatypes/contentTypeWithEncoding')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class MediaTypesClientOperationsMixin(object):
    @distributed_trace
    def analyze_body(
        self,
        input=None,  # type: Optional[Union[IO, "_models.SourcePath"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> str
        """Analyze body, that could be different media types.

        :param input: Input parameter.
        :type input: IO or ~mediatypes.models.SourcePath
        :keyword str content_type: Media type of the body sent to the API. Default value is
         "application/json". Allowed values are: "application/pdf", "image/jpeg", "image/png",
         "image/tiff", "application/json."
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop(
            "content_type", "application/json"
        )  # type: Optional[Union[str, "_models.ContentType"]]

        json = None
        content = None
        if content_type.split(";")[0] in ["application/pdf", "image/jpeg", "image/png", "image/tiff"]:
            content = input
        elif content_type.split(";")[0] in ["application/json"]:
            if input is not None:
                json = self._serialize.body(input, "SourcePath")
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(content_type)
            )

        request = build_analyze_body_request(
            content_type=content_type,
            json=json,
            content=content,
            template_url=self.analyze_body.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    analyze_body.metadata = {"url": "/mediatypes/analyze"}  # type: ignore

    @distributed_trace
    def analyze_body_no_accept_header(
        self,
        input=None,  # type: Optional[Union[IO, "_models.SourcePath"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
        type.

        :param input: Input parameter.
        :type input: IO or ~mediatypes.models.SourcePath
        :keyword str content_type: Media type of the body sent to the API. Default value is
         "application/json". Allowed values are: "application/pdf", "image/jpeg", "image/png",
         "image/tiff", "application/json."
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop(
            "content_type", "application/json"
        )  # type: Optional[Union[str, "_models.ContentType"]]

        json = None
        content = None
        if content_type.split(";")[0] in ["application/pdf", "image/jpeg", "image/png", "image/tiff"]:
            content = input
        elif content_type.split(";")[0] in ["application/json"]:
            if input is not None:
                json = self._serialize.body(input, "SourcePath")
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(content_type)
            )

        request = build_analyze_body_no_accept_header_request(
            content_type=content_type,
            json=json,
            content=content,
            template_url=self.analyze_body_no_accept_header.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    analyze_body_no_accept_header.metadata = {"url": "/mediatypes/analyzeNoAccept"}  # type: ignore

    @distributed_trace
    def content_type_with_encoding(
        self,
        input=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> str
        """Pass in contentType 'text/plain; encoding=UTF-8' to pass test. Value for input does not matter.

        :param input: Input parameter.
        :type input: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "text/plain")  # type: Optional[str]

        if input is not None:
            content = self._serialize.body(input, "str")
        else:
            content = None

        request = build_content_type_with_encoding_request(
            content_type=content_type,
            content=content,
            template_url=self.content_type_with_encoding.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    content_type_with_encoding.metadata = {"url": "/mediatypes/contentTypeWithEncoding"}  # type: ignore
