# pyright: reportUnnecessaryTypeIgnoreComment=false
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import List, Any, overload, IO, Optional, Union

from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.exceptions import (
    ClientAuthenticationError,
    ResourceExistsError,
    ResourceNotFoundError,
)

from ._operations import MediaTypesClientOperationsMixin as _MediaTypesClientOperationsMixin
from ..._operations._patch import MediaTypesSharedMixin


class MediaTypesClientOperationsMixin(_MediaTypesClientOperationsMixin, MediaTypesSharedMixin):
    @overload
    async def body_three_types(self, message: Any, *, content_type: str = "application/json", **kwargs: Any) -> str:
        """Body with three types. Can be stream, string, or JSON. Pass in string 'hello, world' with
        content type 'text/plain', {'hello': world'} with content type 'application/json' and a byte
        string for 'application/octet-stream'.

        :param message: The payload body. Required.
        :type message: any
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def body_three_types(  # type: ignore
        self, message: IO, *, content_type: str = "application/octet-stream", **kwargs: Any
    ) -> str:
        """Body with three types. Can be stream, string, or JSON. Pass in string 'hello, world' with
        content type 'text/plain', {'hello': world'} with content type 'application/json' and a byte
        string for 'application/octet-stream'.

        :param message: The payload body. Required.
        :type message: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Known values are: 'application/json', 'application/octet-stream', 'text/plain'. Default value
         is "application/octet-stream".
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def body_three_types(self, message: str, *, content_type: Optional[str] = None, **kwargs: Any) -> str:
        """Body with three types. Can be stream, string, or JSON. Pass in string 'hello, world' with
        content type 'text/plain', {'hello': world'} with content type 'application/json' and a byte
        string for 'application/octet-stream'.

        :param message: The payload body. Required.
        :type message: str
        :keyword content_type: Body Parameter content-type. Content type parameter for string body.
         Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def body_three_types(self, message: Union[Any, IO, str], **kwargs: Any) -> str:
        """Body with three types. Can be stream, string, or JSON. Pass in string 'hello, world' with
        content type 'text/plain', {'hello': world'} with content type 'application/json' and a byte
        string for 'application/octet-stream'.

        :param message: The payload body. Is one of the following types: any, IO, string Required.
        :type message: any or IO or str
        :return: str
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        cls = kwargs.pop("cls", None)
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})
        request, kwargs = self._prepare_body_three_types(message, **kwargs)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        return self._handle_body_three_types_response(pipeline_response, cls=cls, error_map=error_map)  # type: ignore


__all__: List[str] = [
    "MediaTypesClientOperationsMixin"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
