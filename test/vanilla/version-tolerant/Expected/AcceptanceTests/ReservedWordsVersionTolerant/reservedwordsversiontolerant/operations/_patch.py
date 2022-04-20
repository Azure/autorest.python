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
    ResourceNotFoundError,
    ResourceExistsError,
    HttpResponseError,
    map_error,
)
from azure.core.utils import case_insensitive_dict
from azure.core.tracing.decorator import distributed_trace
from azure.core.rest import HttpRequest
from azure.core.pipeline import PipelineResponse

from ._operations import ReservedWordsClientOperationsMixin as _ReservedWordsClientOperationsMixin


class Helpers:
    @staticmethod
    def _operation_with_data_param_request(data: Dict[str, Any], **kwargs: Any) -> HttpRequest:
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/x-www-form-urlencoded"))
        accept = _headers.pop("Accept", "application/json")

        # Construct URL
        _url = "/reservedWords/operation/data"

        # Construct headers
        if content_type is not None:
            _headers["Content-Type"] = content_type
        _headers["Accept"] = accept

        return HttpRequest(method="PUT", url=_url, headers=_headers, data=data, params=_params)

    @staticmethod
    def _operation_with_data_param_deserialize(pipeline_response: PipelineResponse, **kwargs) -> Any:
        cls = kwargs.pop("cls", None)
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)
        if response.content:
            deserialized = response.json()
        else:
            deserialized = None
        if cls:
            return cls(pipeline_response, cast(Any, deserialized), {})
        return cast(Any, deserialized)

    @staticmethod
    def _operation_with_files_param_request(*, files: Dict[str, Any], **kwargs: Any) -> HttpRequest:
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        accept = _headers.pop("Accept", "application/json")

        # Construct URL
        _url = "/reservedWords/operation/files"

        # Construct headers
        if content_type is not None:
            _headers["Content-Type"] = content_type
        _headers["Accept"] = accept

        return HttpRequest(method="PUT", url=_url, headers=_headers, files=files, params=_params)

    @staticmethod
    def _operation_with_files_param_deserialize(pipeline_response: PipelineResponse, **kwargs) -> Any:
        cls = kwargs.pop("cls", None)

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)
        if response.content:
            deserialized = response.json()
        else:
            deserialized = None
        if cls:
            return cls(pipeline_response, cast(Any, deserialized), {})
        return cast(Any, deserialized)


class ReservedWordsClientOperationsMixin(_ReservedWordsClientOperationsMixin, Helpers):
    def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs) -> PipelineResponse:
        return self._client._pipeline.run(request, stream=stream, **kwargs)  # pylint: disable=protected-access

    @distributed_trace
    def operation_with_data_param(self, data: Dict[str, Any], **kwargs: Any) -> Any:  # type: ignore # pylint: disable=arguments-differ
        """Operation with urlencoded body param called 'data'.

        :param data: Form-encoded input for data. See the template in our example to find the input
         shape.
        :type data: dict[str, any]
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python
                # form-encoded input template you can fill out and use as your `data` input.
                data = {
                    "data": "str",  # Pass in 'hello'.
                    "world": "str"  # Pass in 'world'.
                }
        """
        request = self._operation_with_data_param_request(data=data, **kwargs)
        request.url = self._client.format_url(request.url)
        return self._operation_with_data_param_deserialize(self._send_request(request), **kwargs)

    @distributed_trace
    def operation_with_files_param(  # type: ignore # pylint: disable=arguments-differ
        self, files: Dict[str, Any], **kwargs: Any
    ) -> Any:
        """Operation with multipart body param called 'files'.

        :param files: Multipart input for files. See the template in our example to find the input
         shape.
        :type files: dict[str, any]
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python
                # multipart input template you can fill out and use as your `files` input.
                files = {
                    "file_name": "str",  # File name to upload. Pass in 'my.txt'.
                    "files": b'bytes'  # Files to upload. Pass in list of input streams.
                }
        """
        request = self._operation_with_files_param_request(files=files, **kwargs)
        request.url = self._client.format_url(request.url)
        return self._operation_with_files_param_deserialize(self._send_request(request), **kwargs)


__all__: List[str] = [
    "ReservedWordsClientOperationsMixin"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
