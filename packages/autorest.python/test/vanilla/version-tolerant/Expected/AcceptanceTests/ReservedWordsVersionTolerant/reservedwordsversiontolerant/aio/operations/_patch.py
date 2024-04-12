# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import Any, Dict, List

from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.rest import HttpRequest
from azure.core.pipeline import PipelineResponse

from ._operations import (
    ReservedWordsClientOperationsMixin as _ReservedWordsClientOperationsMixin,
)
from ...operations._patch import Helpers


class ReservedWordsClientOperationsMixin(_ReservedWordsClientOperationsMixin, Helpers):
    async def _send_request(
        self, request: HttpRequest, *, stream: bool = False, **kwargs
    ) -> PipelineResponse:
        return await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=stream, **kwargs
        )

    @distributed_trace_async
    async def operation_with_data_param(
        self, data: Dict[str, Any], **kwargs: Any
    ) -> Any:
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
        return self._operation_with_data_param_deserialize(
            await self._send_request(request), **kwargs
        )

    @distributed_trace_async
    async def operation_with_files_param(
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
        return self._operation_with_files_param_deserialize(
            await self._send_request(request), **kwargs
        )


__all__: List[str] = [
    "ReservedWordsClientOperationsMixin"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
