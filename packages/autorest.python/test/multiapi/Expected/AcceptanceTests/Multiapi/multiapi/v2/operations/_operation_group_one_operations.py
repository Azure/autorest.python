# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import _serialization, models as _models
from ..._serialization import Serializer
from .._vendor import MultiapiServiceClientMixinABC, _convert_request

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_test_two_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2.0.0"] = kwargs.pop("api_version", _params.pop("api-version", "2.0.0"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/multiapi/one/testTwoEndpoint")

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_test_three_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2.0.0"] = kwargs.pop("api_version", _params.pop("api-version", "2.0.0"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/multiapi/one/testThreeEndpoint")

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


class OperationGroupOneOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~multiapi.v2.MultiapiServiceClient`'s
        :attr:`operation_group_one` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def test_two(
        self, parameter_one: Optional[_models.ModelTwo] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ModelTwo:
        """TestTwo should be in OperationGroupOneOperations. Takes in ModelTwo and ouputs ModelTwo.

        :param parameter_one: A ModelTwo parameter. Default value is None.
        :type parameter_one: ~multiapi.v2.models.ModelTwo
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ModelTwo or the result of cls(response)
        :rtype: ~multiapi.v2.models.ModelTwo
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def test_two(
        self, parameter_one: Optional[IO] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ModelTwo:
        """TestTwo should be in OperationGroupOneOperations. Takes in ModelTwo and ouputs ModelTwo.

        :param parameter_one: A ModelTwo parameter. Default value is None.
        :type parameter_one: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ModelTwo or the result of cls(response)
        :rtype: ~multiapi.v2.models.ModelTwo
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def test_two(self, parameter_one: Optional[Union[_models.ModelTwo, IO]] = None, **kwargs: Any) -> _models.ModelTwo:
        """TestTwo should be in OperationGroupOneOperations. Takes in ModelTwo and ouputs ModelTwo.

        :param parameter_one: A ModelTwo parameter. Is either a ModelTwo type or a IO type. Default
         value is None.
        :type parameter_one: ~multiapi.v2.models.ModelTwo or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ModelTwo or the result of cls(response)
        :rtype: ~multiapi.v2.models.ModelTwo
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2.0.0"] = kwargs.pop("api_version", _params.pop("api-version", "2.0.0"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ModelTwo] = kwargs.pop("cls", None)

        _json: Any = None
        _content: Any = None
        if isinstance(parameter_one, (_serialization.Model, dict)):
            if parameter_one is not None:
                _json = self._serialize.body(parameter_one, "ModelTwo")
            else:
                _json = None
            content_type = content_type or "application/json"
        elif isinstance(parameter_one, (IO, bytes)):
            if parameter_one is not None:
                _content = parameter_one
            else:
                _content = None
            content_type = content_type or "application/json"
        else:
            raise TypeError("unrecognized type for parameter_one")

        request = build_test_two_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.test_two.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ModelTwo", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    test_two.metadata = {"url": "/multiapi/one/testTwoEndpoint"}

    @distributed_trace
    def test_three(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """TestThree should be in OperationGroupOneOperations. Takes in ModelTwo.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2.0.0"] = kwargs.pop("api_version", _params.pop("api-version", "2.0.0"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_test_three_request(
            api_version=api_version,
            template_url=self.test_three.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_three.metadata = {"url": "/multiapi/one/testThreeEndpoint"}
