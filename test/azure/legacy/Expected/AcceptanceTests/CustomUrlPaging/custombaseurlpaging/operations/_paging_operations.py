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
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Iterable, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_get_pages_partial_url_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/paging/customurl/partialnextlink")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_get_pages_partial_url_operation_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/paging/customurl/partialnextlinkop")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_get_pages_partial_url_operation_next_request(
    next_link,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/paging/customurl/{nextLink}")
    path_format_arguments = {
        "nextLink": _SERIALIZER.url("next_link", next_link, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class PagingOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through :class:`~custombaseurlpaging.AutoRestParameterizedHostTestPagingClient`'s
        :attr:`~custombaseurlpaging.AutoRestParameterizedHostTestPagingClient.paging` attribute.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_pages_partial_url(
        self,
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.ProductResult"]
        """A paging operation that combines custom url, paging and partial URL and expect to concat after
        host.

        :param account_name: Account Name.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProductResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~custombaseurlpaging.models.ProductResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ProductResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_get_pages_partial_url_request(
                    template_url=self.get_pages_partial_url.metadata["url"],
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:

                request = build_get_pages_partial_url_request(
                    template_url=next_link,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ProductResult", pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    get_pages_partial_url.metadata = {"url": "/paging/customurl/partialnextlink"}  # type: ignore

    @distributed_trace
    def get_pages_partial_url_operation(
        self,
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.ProductResult"]
        """A paging operation that combines custom url, paging and partial URL with next operation.

        :param account_name: Account Name.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProductResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~custombaseurlpaging.models.ProductResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ProductResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_get_pages_partial_url_operation_request(
                    template_url=self.get_pages_partial_url_operation.metadata["url"],
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:

                request = build_get_pages_partial_url_operation_next_request(
                    next_link=next_link,
                    template_url="/paging/customurl/{nextLink}",
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ProductResult", pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    get_pages_partial_url_operation.metadata = {"url": "/paging/customurl/partialnextlinkop"}  # type: ignore
