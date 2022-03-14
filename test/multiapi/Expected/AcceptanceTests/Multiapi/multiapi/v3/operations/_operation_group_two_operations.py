# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_test_four_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    api_version = kwargs.pop('api_version', case_insensitive_dict(_params).pop('api-version', "3.0.0"))  # type: str
    content_type = kwargs.pop('content_type', case_insensitive_dict(_headers).pop('Content-Type', None))  # type: Optional[Union[str, "_models.ContentType"]]
    accept = case_insensitive_dict(_headers).pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/multiapi/two/testFourEndpoint")

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_test_five_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    api_version = kwargs.pop('api_version', case_insensitive_dict(_params).pop('api-version', "3.0.0"))  # type: str
    accept = case_insensitive_dict(_headers).pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/multiapi/two/testFiveEndpoint")

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )

# fmt: on
class OperationGroupTwoOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~multiapi.v3.MultiapiServiceClient`'s
        :attr:`operation_group_two` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def test_four(  # pylint: disable=inconsistent-return-statements
        self,
        input=None,  # type: Optional[Union[IO, "_models.SourcePath"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
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
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        api_version = kwargs.pop('api_version', case_insensitive_dict(_params).pop('api-version', "3.0.0"))  # type: str
        content_type = kwargs.pop('content_type', case_insensitive_dict(_headers).pop('Content-Type', "application/json"))  # type: Optional[Union[str, "_models.ContentType"]]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        _json = None
        _content = None
        content_type = content_type or ""
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
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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


    @distributed_trace
    def test_five(  # pylint: disable=inconsistent-return-statements
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """TestFive should be in OperationGroupTwoOperations.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
        _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

        api_version = kwargs.pop('api_version', case_insensitive_dict(_params).pop('api-version', "3.0.0"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_test_five_request(
            api_version=api_version,
            template_url=self.test_five.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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

