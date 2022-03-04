# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

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

from .._vendor import _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_paths_get_empty_request(
    key_name: str, subscription_id: str, *, key_version: Optional[str] = "v1", **kwargs: Any
) -> HttpRequest:
    accept = "application/json"
    # Construct URL
    _url = "/customuri/{subscriptionId}/{keyName}"
    path_format_arguments = {
        "keyName": _SERIALIZER.url("key_name", key_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if key_version is not None:
        _query_parameters["keyVersion"] = _SERIALIZER.query("key_version", key_version, "str")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_query_parameters, headers=_header_parameters, **kwargs)


class PathsOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through :class:`~custombaseurlmoreoptionsversiontolerant.AutoRestParameterizedCustomHostTestClient`'s
        :attr:`~custombaseurlmoreoptionsversiontolerant.AutoRestParameterizedCustomHostTestClient.paths` attribute.
    """

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_empty(  # pylint: disable=inconsistent-return-statements
        self, vault: str, secret: str, key_name: str, *, key_version: Optional[str] = "v1", **kwargs: Any
    ) -> None:
        """Get a 200 to test a valid base uri.

        :param vault: The vault name, e.g. https://myvault.
        :type vault: str
        :param secret: Secret value.
        :type secret: str
        :param key_name: The key name with value 'key1'.
        :type key_name: str
        :keyword key_version: The key version. Default value 'v1'. Default value is "v1".
        :paramtype key_version: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_paths_get_empty_request(
            key_name=key_name,
            subscription_id=self._config.subscription_id,
            key_version=key_version,
        )
        path_format_arguments = {
            "vault": self._serialize.url("vault", vault, "str", skip_quote=True),
            "secret": self._serialize.url("secret", secret, "str", skip_quote=True),
            "dnsSuffix": self._serialize.url(
                "self._config.dns_suffix", self._config.dns_suffix, "str", skip_quote=True
            ),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
