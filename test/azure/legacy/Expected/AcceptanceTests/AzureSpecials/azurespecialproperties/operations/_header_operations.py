# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

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
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_custom_named_request_id_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    foo_client_request_id = kwargs.pop('foo_client_request_id')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/azurespecials/customNamedRequestId")

    # Construct headers
    _headers['foo-client-request-id'] = _SERIALIZER.header("foo_client_request_id", foo_client_request_id, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_custom_named_request_id_param_grouping_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    foo_client_request_id = kwargs.pop('foo_client_request_id')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/azurespecials/customNamedRequestIdParamGrouping")

    # Construct headers
    _headers['foo-client-request-id'] = _SERIALIZER.header("foo_client_request_id", foo_client_request_id, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_custom_named_request_id_head_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    foo_client_request_id = kwargs.pop('foo_client_request_id')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/azurespecials/customNamedRequestIdHead")

    # Construct headers
    _headers['foo-client-request-id'] = _SERIALIZER.header("foo_client_request_id", foo_client_request_id, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="HEAD",
        url=_url,
        headers=_headers,
        **kwargs
    )

# fmt: on
class HeaderOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azurespecialproperties.AutoRestAzureSpecialParametersTestClient`'s
        :attr:`header` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def custom_named_request_id(  # pylint: disable=inconsistent-return-statements
        self,
        foo_client_request_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request.

        :param foo_client_request_id: The fooRequestId. Required.
        :type foo_client_request_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_custom_named_request_id_request(
            foo_client_request_id=foo_client_request_id,
            template_url=self.custom_named_request_id.metadata["url"],
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
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["foo-request-id"] = self._deserialize("str", response.headers.get("foo-request-id"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    custom_named_request_id.metadata = {"url": "/azurespecials/customNamedRequestId"}  # type: ignore

    @distributed_trace
    def custom_named_request_id_param_grouping(  # pylint: disable=inconsistent-return-statements
        self,
        header_custom_named_request_id_param_grouping_parameters,  # type: _models.HeaderCustomNamedRequestIdParamGroupingParameters
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request,
        via a parameter group.

        :param header_custom_named_request_id_param_grouping_parameters: Parameter group. Required.
        :type header_custom_named_request_id_param_grouping_parameters:
         ~azurespecialproperties.models.HeaderCustomNamedRequestIdParamGroupingParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _foo_client_request_id = None
        if header_custom_named_request_id_param_grouping_parameters is not None:
            _foo_client_request_id = header_custom_named_request_id_param_grouping_parameters.foo_client_request_id

        request = build_custom_named_request_id_param_grouping_request(
            foo_client_request_id=_foo_client_request_id,
            template_url=self.custom_named_request_id_param_grouping.metadata["url"],
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
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["foo-request-id"] = self._deserialize("str", response.headers.get("foo-request-id"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    custom_named_request_id_param_grouping.metadata = {"url": "/azurespecials/customNamedRequestIdParamGrouping"}  # type: ignore

    @distributed_trace
    def custom_named_request_id_head(
        self,
        foo_client_request_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> bool
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request.

        :param foo_client_request_id: The fooRequestId. Required.
        :type foo_client_request_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_custom_named_request_id_head_request(
            foo_client_request_id=foo_client_request_id,
            template_url=self.custom_named_request_id_head.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers["foo-request-id"] = self._deserialize("str", response.headers.get("foo-request-id"))

        if cls:
            return cls(pipeline_response, None, response_headers)
        return 200 <= response.status_code <= 299

    custom_named_request_id_head.metadata = {"url": "/azurespecials/customNamedRequestIdHead"}  # type: ignore
