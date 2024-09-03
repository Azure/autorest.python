# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, AsyncIterator, Callable, Dict, IO, Optional, Type, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ...operations._lr_os_custom_header_operations import (
    build_post202_retry200_request,
    build_post_async_retry_succeeded_request,
    build_put201_creating_succeeded200_request,
    build_put_async_retry_succeeded_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class LROsCustomHeaderOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~lro.aio.AutoRestLongRunningOperationTestService`'s
        :attr:`lr_os_custom_header` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def _put_async_retry_succeeded_initial(
        self, product: Optional[Union[_models.Product, IO[bytes]]] = None, **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(product, (IOBase, bytes)):
            _content = product
        else:
            if product is not None:
                _json = self._serialize.body(product, "Product")
            else:
                _json = None

        _request = build_put_async_retry_succeeded_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _decompress = kwargs.pop("decompress", True)
        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Azure-AsyncOperation"] = self._deserialize(
            "str", response.headers.get("Azure-AsyncOperation")
        )
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
        response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.stream_download(self._client._pipeline, decompress=_decompress)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_put_async_retry_succeeded(
        self, product: Optional[_models.Product] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.Product]:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running put request, service returns a 200 to the initial request, with an
        entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
        Azure-AsyncOperation header for operation status.

        :param product: Product to put. Default value is None.
        :type product: ~lro.models.Product
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Product or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~lro.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_put_async_retry_succeeded(
        self, product: Optional[IO[bytes]] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.Product]:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running put request, service returns a 200 to the initial request, with an
        entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
        Azure-AsyncOperation header for operation status.

        :param product: Product to put. Default value is None.
        :type product: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Product or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~lro.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_put_async_retry_succeeded(
        self, product: Optional[Union[_models.Product, IO[bytes]]] = None, **kwargs: Any
    ) -> AsyncLROPoller[_models.Product]:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running put request, service returns a 200 to the initial request, with an
        entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
        Azure-AsyncOperation header for operation status.

        :param product: Product to put. Is either a Product type or a IO[bytes] type. Default value is
         None.
        :type product: ~lro.models.Product or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either Product or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~lro.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Product] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._put_async_retry_succeeded_initial(
                product=product,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

            deserialized = self._deserialize("Product", pipeline_response.http_response)
            if cls:
                return cls(pipeline_response, deserialized, response_headers)  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.Product].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.Product](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _put201_creating_succeeded200_initial(
        self, product: Optional[Union[_models.Product, IO[bytes]]] = None, **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(product, (IOBase, bytes)):
            _content = product
        else:
            if product is not None:
                _json = self._serialize.body(product, "Product")
            else:
                _json = None

        _request = build_put201_creating_succeeded200_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _decompress = kwargs.pop("decompress", True)
        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = response.stream_download(self._client._pipeline, decompress=_decompress)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_put201_creating_succeeded200(
        self, product: Optional[_models.Product] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.Product]:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running put request, service returns a 201 to the initial request, with an
        entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll
        returns a ‘200’ with ProvisioningState=’Succeeded’.

        :param product: Product to put. Default value is None.
        :type product: ~lro.models.Product
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Product or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~lro.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_put201_creating_succeeded200(
        self, product: Optional[IO[bytes]] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.Product]:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running put request, service returns a 201 to the initial request, with an
        entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll
        returns a ‘200’ with ProvisioningState=’Succeeded’.

        :param product: Product to put. Default value is None.
        :type product: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Product or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~lro.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_put201_creating_succeeded200(
        self, product: Optional[Union[_models.Product, IO[bytes]]] = None, **kwargs: Any
    ) -> AsyncLROPoller[_models.Product]:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running put request, service returns a 201 to the initial request, with an
        entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll
        returns a ‘200’ with ProvisioningState=’Succeeded’.

        :param product: Product to put. Is either a Product type or a IO[bytes] type. Default value is
         None.
        :type product: ~lro.models.Product or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either Product or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~lro.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Product] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._put201_creating_succeeded200_initial(
                product=product,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("Product", pipeline_response.http_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.Product].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.Product](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _post202_retry200_initial(
        self, product: Optional[Union[_models.Product, IO[bytes]]] = None, **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(product, (IOBase, bytes)):
            _content = product
        else:
            if product is not None:
                _json = self._serialize.body(product, "Product")
            else:
                _json = None

        _request = build_post202_retry200_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _decompress = kwargs.pop("decompress", True)
        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
        response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.stream_download(self._client._pipeline, decompress=_decompress)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_post202_retry200(
        self, product: Optional[_models.Product] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running post request, service returns a 202 to the initial request, with
        'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

        :param product: Product to put. Default value is None.
        :type product: ~lro.models.Product
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_post202_retry200(
        self, product: Optional[IO[bytes]] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running post request, service returns a 202 to the initial request, with
        'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

        :param product: Product to put. Default value is None.
        :type product: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_post202_retry200(
        self, product: Optional[Union[_models.Product, IO[bytes]]] = None, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running post request, service returns a 202 to the initial request, with
        'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

        :param product: Product to put. Is either a Product type or a IO[bytes] type. Default value is
         None.
        :type product: ~lro.models.Product or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._post202_retry200_initial(
                product=product,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    async def _post_async_retry_succeeded_initial(
        self, product: Optional[Union[_models.Product, IO[bytes]]] = None, **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(product, (IOBase, bytes)):
            _content = product
        else:
            if product is not None:
                _json = self._serialize.body(product, "Product")
            else:
                _json = None

        _request = build_post_async_retry_succeeded_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _decompress = kwargs.pop("decompress", True)
        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Azure-AsyncOperation"] = self._deserialize(
            "str", response.headers.get("Azure-AsyncOperation")
        )
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
        response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.stream_download(self._client._pipeline, decompress=_decompress)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_post_async_retry_succeeded(
        self, product: Optional[_models.Product] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running post request, service returns a 202 to the initial request, with an
        entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
        Azure-AsyncOperation header for operation status.

        :param product: Product to put. Default value is None.
        :type product: ~lro.models.Product
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_post_async_retry_succeeded(
        self, product: Optional[IO[bytes]] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running post request, service returns a 202 to the initial request, with an
        entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
        Azure-AsyncOperation header for operation status.

        :param product: Product to put. Default value is None.
        :type product: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_post_async_retry_succeeded(
        self, product: Optional[Union[_models.Product, IO[bytes]]] = None, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running post request, service returns a 202 to the initial request, with an
        entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
        Azure-AsyncOperation header for operation status.

        :param product: Product to put. Is either a Product type or a IO[bytes] type. Default value is
         None.
        :type product: ~lro.models.Product or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._post_async_retry_succeeded_initial(
                product=product,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore
