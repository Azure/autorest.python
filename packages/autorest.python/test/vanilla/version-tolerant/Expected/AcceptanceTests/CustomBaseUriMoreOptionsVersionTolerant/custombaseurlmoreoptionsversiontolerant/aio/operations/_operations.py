# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core import AsyncPipelineClient
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ..._utils.serialization import Deserializer, Serializer
from ...operations._operations import build_paths_get_empty_request
from .._configuration import AutoRestParameterizedCustomHostTestClientConfiguration

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PathsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~custombaseurlmoreoptionsversiontolerant.aio.AutoRestParameterizedCustomHostTestClient`'s
        :attr:`paths` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: AutoRestParameterizedCustomHostTestClientConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_empty(
        self, vault: str, secret: str, key_name: str, *, key_version: str = "v1", **kwargs: Any
    ) -> None:
        """Get a 200 to test a valid base uri.

        :param vault: The vault name, e.g. https://myvault. Required.
        :type vault: str
        :param secret: Secret value. Required.
        :type secret: str
        :param key_name: The key name with value 'key1'. Required.
        :type key_name: str
        :keyword key_version: The key version. Default value 'v1'. Default value is "v1".
        :paramtype key_version: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_paths_get_empty_request(
            key_name=key_name,
            subscription_id=self._config.subscription_id,
            key_version=key_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "vault": self._serialize.url("vault", vault, "str", skip_quote=True),
            "secret": self._serialize.url("secret", secret, "str", skip_quote=True),
            "dnsSuffix": self._serialize.url(
                "self._config.dns_suffix", self._config.dns_suffix, "str", skip_quote=True
            ),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
