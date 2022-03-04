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
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_post_method_local_valid_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/azurespecials/subscriptionId/method/string/none/path/local/1234-5678-9012-3456/{subscriptionId}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_post_method_local_null_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/azurespecials/subscriptionId/method/string/none/path/local/null/{subscriptionId}")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_post_path_local_valid_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/azurespecials/subscriptionId/path/string/none/path/local/1234-5678-9012-3456/{subscriptionId}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_post_swagger_local_valid_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/azurespecials/subscriptionId/swagger/string/none/path/local/1234-5678-9012-3456/{subscriptionId}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class SubscriptionInMethodOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through :class:`~azurespecialproperties.AutoRestAzureSpecialParametersTestClient`'s
        :attr:`~azurespecialproperties.AutoRestAzureSpecialParametersTestClient.subscription_in_method` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")

    @distributed_trace
    def post_method_local_valid(  # pylint: disable=inconsistent-return-statements
        self,
        subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in the method.  pass in subscription id =
        '1234-5678-9012-3456' to succeed.

        :param subscription_id: This should appear as a method parameter, use value
         '1234-5678-9012-3456'.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_post_method_local_valid_request(
            subscription_id=subscription_id,
            template_url=self.post_method_local_valid.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post_method_local_valid.metadata = {"url": "/azurespecials/subscriptionId/method/string/none/path/local/1234-5678-9012-3456/{subscriptionId}"}  # type: ignore

    @distributed_trace
    def post_method_local_null(  # pylint: disable=inconsistent-return-statements
        self,
        subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in the method.  pass in subscription id = null,
        client-side validation should prevent you from making this call.

        :param subscription_id: This should appear as a method parameter, use value null, client-side
         validation should prvenet the call.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_post_method_local_null_request(
            subscription_id=subscription_id,
            template_url=self.post_method_local_null.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post_method_local_null.metadata = {"url": "/azurespecials/subscriptionId/method/string/none/path/local/null/{subscriptionId}"}  # type: ignore

    @distributed_trace
    def post_path_local_valid(  # pylint: disable=inconsistent-return-statements
        self,
        subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in the method.  pass in subscription id =
        '1234-5678-9012-3456' to succeed.

        :param subscription_id: Should appear as a method parameter -use value '1234-5678-9012-3456'.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_post_path_local_valid_request(
            subscription_id=subscription_id,
            template_url=self.post_path_local_valid.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post_path_local_valid.metadata = {"url": "/azurespecials/subscriptionId/path/string/none/path/local/1234-5678-9012-3456/{subscriptionId}"}  # type: ignore

    @distributed_trace
    def post_swagger_local_valid(  # pylint: disable=inconsistent-return-statements
        self,
        subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in the method.  pass in subscription id =
        '1234-5678-9012-3456' to succeed.

        :param subscription_id: The subscriptionId, which appears in the path, the value is always
         '1234-5678-9012-3456'.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_post_swagger_local_valid_request(
            subscription_id=subscription_id,
            template_url=self.post_swagger_local_valid.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post_swagger_local_valid.metadata = {"url": "/azurespecials/subscriptionId/swagger/string/none/path/local/1234-5678-9012-3456/{subscriptionId}"}  # type: ignore
