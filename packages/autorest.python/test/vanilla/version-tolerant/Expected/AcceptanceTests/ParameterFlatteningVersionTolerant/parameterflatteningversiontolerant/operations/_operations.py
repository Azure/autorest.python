# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core import PipelineClient
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .._configuration import AutoRestParameterFlatteningConfiguration
from .._utils.serialization import Deserializer, Serializer

JSON = MutableMapping[str, Any]
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_availability_sets_update_request(resource_group_name: str, avset: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/parameterFlattening/{resourceGroupName}/{availabilitySetName}"
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "availabilitySetName": _SERIALIZER.url("avset", avset, "str", max_length=80),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PATCH", url=_url, headers=_headers, **kwargs)


class AvailabilitySetsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~parameterflatteningversiontolerant.AutoRestParameterFlattening`'s
        :attr:`availability_sets` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: AutoRestParameterFlatteningConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def update(
        self, resource_group_name: str, avset: str, tags: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Updates the tags for an availability set.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param avset: The name of the storage availability set. Required.
        :type avset: str
        :param tags: The tags. Required.
        :type tags: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                tags = {
                    "tags": {
                        "str": "str"
                    }
                }
        """

    @overload
    def update(
        self,
        resource_group_name: str,
        avset: str,
        tags: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Updates the tags for an availability set.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param avset: The name of the storage availability set. Required.
        :type avset: str
        :param tags: The tags. Required.
        :type tags: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def update(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, avset: str, tags: Union[JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """Updates the tags for an availability set.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param avset: The name of the storage availability set. Required.
        :type avset: str
        :param tags: The tags. Is either a JSON type or a IO[bytes] type. Required.
        :type tags: JSON or IO[bytes]
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                tags = {
                    "tags": {
                        "str": "str"
                    }
                }
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(tags, (IOBase, bytes)):
            _content = tags
        else:
            _json = tags

        _request = build_availability_sets_update_request(
            resource_group_name=resource_group_name,
            avset=avset,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
