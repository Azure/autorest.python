# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import Any, Dict, List, cast

from azure.core.exceptions import (
    ClientAuthenticationError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
    HttpResponseError,
)
from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict
from azure.core.tracing.decorator import distributed_trace
from azure.core.pipeline import PipelineResponse

from ._operations import FormdataurlencodedOperations as _FormdataurlencodedOperations
from .._vendor import _format_url_section


class Helpers:
    def _update_pet_with_form_request(self, pet_id: int, *, data: Dict[str, Any], **kwargs: Any) -> HttpRequest:
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/x-www-form-urlencoded"))
        # Construct URL
        _url = "/formsdataurlencoded/pet/add/{petId}"
        path_format_arguments = {
            "petId": pet_id,
        }

        _url = _format_url_section(_url, **path_format_arguments)

        if content_type is not None:
            _headers["Content-Type"] = content_type
        return HttpRequest(
            method="POST", url=cast(str, _url), headers=_headers, data=data, params=kwargs.pop("params", {})
        )

    def _update_pet_with_form_deserialize(self, pipeline_response: PipelineResponse, **kwargs: Any) -> None:
        cls = kwargs.pop("cls", None)

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})
        response = pipeline_response.http_response
        if response.status_code not in [200, 405]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    def _partial_constant_body_request(self, *, data: Dict[str, Any], **kwargs: Any) -> HttpRequest:
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/x-www-form-urlencoded"))
        # Construct URL
        _url = "/formsdataurlencoded/partialConstantBody"

        # Construct headers
        if content_type is not None:
            _headers["Content-Type"] = content_type

        return HttpRequest(method="POST", url=_url, headers=_headers, data=data, params=_params)

    def _partial_constant_body_deserialize(self, pipeline_response: PipelineResponse, **kwargs: Any) -> None:
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        cls = kwargs.pop("cls", None)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})


class FormdataurlencodedOperations(_FormdataurlencodedOperations, Helpers):
    def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> PipelineResponse:
        return self._client._pipeline.run(request, stream=stream, **kwargs)

    @distributed_trace
    def update_pet_with_form(  # pylint: disable=inconsistent-return-statements
        self, pet_id: int, data: Dict[str, Any], **kwargs: Any
    ) -> None:
        """Updates a pet in the store with form data.

        Updates a pet in the store with form data.
        :param pet_id: ID of pet that needs to be updated.
        :type pet_id: int
        :param data: Form-encoded input for data. See the template in our example to find the input
         shape.
        :type data: dict[str, any]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python
                # form-encoded input template you can fill out and use as your `data` input.
                data = {
                    "name": "str",  # Optional. Updated name of the pet. Default value is None.
                    "pet_age": 0,  # How many years is it old?.
                    "pet_food": "str",  # Can take a value of meat, or fish, or plant. Known
                      values are: "meat", "fish", and "plant".
                    "pet_type": "str",  # Can take a value of dog, or cat, or fish. Known values
                      are: "dog", "cat", and "fish".
                    "status": "str"  # Optional. Updated status of the pet. Default value is
                      None.
                }
        """
        request = self._update_pet_with_form_request(pet_id=pet_id, data=data, **kwargs)
        request.url = self._client.format_url(request.url)
        return self._update_pet_with_form_deserialize(self._send_request(request, **kwargs))

    @distributed_trace
    def partial_constant_body(  # pylint: disable=inconsistent-return-statements
        self, data: Dict[str, Any], **kwargs: Any
    ) -> None:
        """Test a partially constant formdata body. Pass in { grant_type: 'access_token', access_token:
        'foo', service: 'bar' } to pass the test.

        :param data: Form-encoded input for data. See the template in our example to find the input
         shape.
        :type data: dict[str, any]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python
                # form-encoded input template you can fill out and use as your `data` input.
                data = {
                    "access_token": "str",  # AAD access token, mandatory when grant_type is
                      access_token_refresh_token or access_token.
                    "grant_type": "access_token",  # Default value is "access_token". Constant
                      part of a formdata body. Default value is "access_token". Note that overriding
                      this default value may result in unsupported behavior.
                    "service": "str"  # Indicates the name of your Azure container registry.
                }
        """
        request = self._partial_constant_body_request(data=data, **kwargs)
        request.url = self._client.format_url(request.url)
        return self._partial_constant_body_deserialize(self._send_request(request, **kwargs))


__all__: List[str] = [
    "FormdataurlencodedOperations"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
