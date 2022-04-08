# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import Any, Dict, List, IO

from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.rest import HttpRequest
from azure.core.pipeline import PipelineResponse

from ._operations import FormdataOperations as _FormdataOperations
from ...operations._patch import (
    _upload_file_request,
    _upload_file_deserialize,
    _upload_files_request,
    _upload_files_deserialize,
)


class FormdataOperations(_FormdataOperations):
    async def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs) -> PipelineResponse:
        kwargs.pop("cls", None)
        request.url = self._client.format_url(request.url)
        return await self._client._pipeline.run(request, stream=stream, **kwargs)  # pylint: disable=protected-access

    @distributed_trace_async
    async def upload_file(self, files: Dict[str, Any], **kwargs: Any) -> IO:  # type: ignore # pylint: disable=arguments-differ
        """Upload file.

        :param files: Multipart input for files. See the template in our example to find the input
         shape.
        :type files: dict[str, any]
        :return: IO
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python
                # multipart input template you can fill out and use as your `files` input.
                files = {
                    "file_content": b'bytes',  # File to upload.
                    "file_name": "str"  # File name to upload. Name has to be spelled exactly as
                      written here.
                }
        """
        request = _upload_file_request(files=files, **kwargs)
        request.url = self._client.format_url(request.url)
        return _upload_file_deserialize(await self._send_request(request, stream=True, **kwargs), **kwargs)

    @distributed_trace_async
    async def upload_files(self, files: Dict[str, Any], **kwargs: Any) -> IO:  # type: ignore # pylint: disable=arguments-differ
        """Upload multiple files.

        :param files: Multipart input for files. See the template in our example to find the input
         shape.
        :type files: dict[str, any]
        :return: IO
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python
                # multipart input template you can fill out and use as your `files` input.
                files = {
                    "file_content": [
                        b'bytes'  # Files to upload.
                    ]
                }
        """
        request = _upload_files_request(files=files, **kwargs)
        request.url = self._client.format_url(request.url)
        return _upload_files_deserialize(await self._send_request(request, stream=True, **kwargs), **kwargs)


__all__: List[str] = [
    "FormdataOperations"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
