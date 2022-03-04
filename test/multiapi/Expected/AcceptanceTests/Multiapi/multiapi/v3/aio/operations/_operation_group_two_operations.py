# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._operation_group_two_operations import build_test_five_request, build_test_four_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class OperationGroupTwoOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through :class:`~multiapi.v3.aio.MultiapiServiceClient`'s
        :attr:`~multiapi.v3.aio.MultiapiServiceClient.operation_group_two` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")


    @distributed_trace_async
    async def test_four(  # pylint: disable=inconsistent-return-statements
        self,
        input: Optional[Union[IO, "_models.SourcePath"]] = None,
        *,
        content_type: Optional[Union[str, "_models.ContentType"]] = "application/json",
        **kwargs: Any
    ) -> None:
        """TestFour should be in OperationGroupTwoOperations.

        :param input: Input parameter. Default value is None.
        :type input: IO or ~multiapi.v3.models.SourcePath
        :keyword content_type: Media type of the body sent to the API. Possible values are:
         "application/pdf", "image/jpeg", "image/png", "image/tiff", and "application/json". Default
         value is "application/json".
        :paramtype content_type: str or ~multiapi.v3.models.ContentType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "3.0.0")  # type: str

        _json = None
        _content = None
        if content_type.split(";")[0] in ['application/json']:
            if input is not None:
                _json = self._serialize.body(input, 'SourcePath')
        elif content_type.split(";")[0] in ['application/pdf', 'image/jpeg', 'image/png', 'image/tiff']:
            _content = input
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(content_type)
            )

        request = build_test_four_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.test_four.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_four.metadata = {'url': "/multiapi/two/testFourEndpoint"}  # type: ignore


    @distributed_trace_async
    async def test_five(  # pylint: disable=inconsistent-return-statements
        self,
        **kwargs: Any
    ) -> None:
        """TestFive should be in OperationGroupTwoOperations.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "3.0.0")  # type: str

        
        request = build_test_five_request(
            api_version=api_version,
            template_url=self.test_five.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_five.metadata = {'url': "/multiapi/two/testFiveEndpoint"}  # type: ignore

