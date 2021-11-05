# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer
from my.library import CustomDefaultPollingMethod, CustomPager, CustomPoller

from .. import models as _models
from .._vendor import _convert_request

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_basic_polling_request_initial(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/basic/polling')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_basic_paging_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/basic/paging')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class PollingPagingExampleOperationsMixin(object):

    def _basic_polling_initial(
        self,
        product=None,  # type: Optional["_models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.Product"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.Product"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if product is not None:
            json = self._serialize.body(product, 'Product')
        else:
            json = None

        request = build_basic_polling_request_initial(
            content_type=content_type,
            json=json,
            template_url=self._basic_polling_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Product', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _basic_polling_initial.metadata = {'url': '/basic/polling'}  # type: ignore


    @distributed_trace
    def begin_basic_polling(
        self,
        product=None,  # type: Optional["_models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> CustomPoller["_models.Product"]
        """A simple polling operation.

        :param product: Product to put.
        :type product: ~azure.directives.sample.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be CustomDefaultPollingMethod. Pass in
         False for this operation to not poll, or pass in your own initialized polling object for a
         personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of CustomPoller that returns either Product or the result of cls(response)
        :rtype: ~my.library.CustomPoller[~azure.directives.sample.models.Product]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Product"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._basic_polling_initial(
                product=product,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('Product', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = CustomDefaultPollingMethod(lro_delay, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return CustomPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return CustomPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_basic_polling.metadata = {'url': '/basic/polling'}  # type: ignore

    @distributed_trace
    def basic_paging(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.ProductResult"]
        """A simple paging operation.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProductResult or the result of cls(response)
        :rtype: ~my.library.CustomPager[~azure.directives.sample.models.ProductResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ProductResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_basic_paging_request(
                    template_url=self.basic_paging.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_basic_paging_request(
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ProductResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response


        return CustomPager(
            get_next, extract_data
        )
    basic_paging.metadata = {'url': '/basic/paging'}  # type: ignore
