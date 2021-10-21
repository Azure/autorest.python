# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ...operations._operations import (
    build_number_get_big_decimal_negative_decimal_request,
    build_number_get_big_decimal_positive_decimal_request,
    build_number_get_big_decimal_request,
    build_number_get_big_double_negative_decimal_request,
    build_number_get_big_double_positive_decimal_request,
    build_number_get_big_double_request,
    build_number_get_big_float_request,
    build_number_get_invalid_decimal_request,
    build_number_get_invalid_double_request,
    build_number_get_invalid_float_request,
    build_number_get_null_request,
    build_number_get_small_decimal_request,
    build_number_get_small_double_request,
    build_number_get_small_float_request,
    build_number_put_big_decimal_negative_decimal_request,
    build_number_put_big_decimal_positive_decimal_request,
    build_number_put_big_decimal_request,
    build_number_put_big_double_negative_decimal_request,
    build_number_put_big_double_positive_decimal_request,
    build_number_put_big_double_request,
    build_number_put_big_float_request,
    build_number_put_small_decimal_request,
    build_number_put_small_double_request,
    build_number_put_small_float_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class NumberOperations:
    """NumberOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_null(self, **kwargs: Any) -> Optional[float]:
        """Get null Number value.

        :return: float or None
        :rtype: float or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[float]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_null_request(
            template_url=self.get_null.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null.metadata = {"url": "/number/null"}  # type: ignore

    @distributed_trace_async
    async def get_invalid_float(self, **kwargs: Any) -> float:
        """Get invalid float Number value.

        :return: float
        :rtype: float
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[float]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_invalid_float_request(
            template_url=self.get_invalid_float.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_invalid_float.metadata = {"url": "/number/invalidfloat"}  # type: ignore

    @distributed_trace_async
    async def get_invalid_double(self, **kwargs: Any) -> float:
        """Get invalid double Number value.

        :return: float
        :rtype: float
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[float]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_invalid_double_request(
            template_url=self.get_invalid_double.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_invalid_double.metadata = {"url": "/number/invaliddouble"}  # type: ignore

    @distributed_trace_async
    async def get_invalid_decimal(self, **kwargs: Any) -> float:
        """Get invalid decimal Number value.

        :return: float
        :rtype: float
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[float]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_invalid_decimal_request(
            template_url=self.get_invalid_decimal.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_invalid_decimal.metadata = {"url": "/number/invaliddecimal"}  # type: ignore

    @distributed_trace_async
    async def put_big_float(self, number_body: float, **kwargs: Any) -> None:
        """Put big float value 3.402823e+20.

        :param number_body: number body.
        :type number_body: float
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = number_body

        request = build_number_put_big_float_request(
            content_type=content_type,
            json=json,
            template_url=self.put_big_float.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_big_float.metadata = {"url": "/number/big/float/3.402823e+20"}  # type: ignore

    @distributed_trace_async
    async def get_big_float(self, **kwargs: Any) -> float:
        """Get big float value 3.402823e+20.

        :return: float
        :rtype: float
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[float]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_big_float_request(
            template_url=self.get_big_float.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_big_float.metadata = {"url": "/number/big/float/3.402823e+20"}  # type: ignore

    @distributed_trace_async
    async def put_big_double(self, number_body: float, **kwargs: Any) -> None:
        """Put big double value 2.5976931e+101.

        :param number_body: number body.
        :type number_body: float
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = number_body

        request = build_number_put_big_double_request(
            content_type=content_type,
            json=json,
            template_url=self.put_big_double.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_big_double.metadata = {"url": "/number/big/double/2.5976931e+101"}  # type: ignore

    @distributed_trace_async
    async def get_big_double(self, **kwargs: Any) -> float:
        """Get big double value 2.5976931e+101.

        :return: float
        :rtype: float
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[float]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_big_double_request(
            template_url=self.get_big_double.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_big_double.metadata = {"url": "/number/big/double/2.5976931e+101"}  # type: ignore

    @distributed_trace_async
    async def put_big_double_positive_decimal(self, **kwargs: Any) -> None:
        """Put big double value 99999999.99.

        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        request = build_number_put_big_double_positive_decimal_request(
            content_type=content_type,
            template_url=self.put_big_double_positive_decimal.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_big_double_positive_decimal.metadata = {"url": "/number/big/double/99999999.99"}  # type: ignore

    @distributed_trace_async
    async def get_big_double_positive_decimal(self, **kwargs: Any) -> float:
        """Get big double value 99999999.99.

        :return: float
        :rtype: float
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[float]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_big_double_positive_decimal_request(
            template_url=self.get_big_double_positive_decimal.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_big_double_positive_decimal.metadata = {"url": "/number/big/double/99999999.99"}  # type: ignore

    @distributed_trace_async
    async def put_big_double_negative_decimal(self, **kwargs: Any) -> None:
        """Put big double value -99999999.99.

        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        request = build_number_put_big_double_negative_decimal_request(
            content_type=content_type,
            template_url=self.put_big_double_negative_decimal.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_big_double_negative_decimal.metadata = {"url": "/number/big/double/-99999999.99"}  # type: ignore

    @distributed_trace_async
    async def get_big_double_negative_decimal(self, **kwargs: Any) -> float:
        """Get big double value -99999999.99.

        :return: float
        :rtype: float
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[float]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_big_double_negative_decimal_request(
            template_url=self.get_big_double_negative_decimal.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_big_double_negative_decimal.metadata = {"url": "/number/big/double/-99999999.99"}  # type: ignore

    @distributed_trace_async
    async def put_big_decimal(self, number_body: float, **kwargs: Any) -> None:
        """Put big decimal value 2.5976931e+101.

        :param number_body: number body.
        :type number_body: float
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = number_body

        request = build_number_put_big_decimal_request(
            content_type=content_type,
            json=json,
            template_url=self.put_big_decimal.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_big_decimal.metadata = {"url": "/number/big/decimal/2.5976931e+101"}  # type: ignore

    @distributed_trace_async
    async def get_big_decimal(self, **kwargs: Any) -> float:
        """Get big decimal value 2.5976931e+101.

        :return: float
        :rtype: float
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[float]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_big_decimal_request(
            template_url=self.get_big_decimal.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_big_decimal.metadata = {"url": "/number/big/decimal/2.5976931e+101"}  # type: ignore

    @distributed_trace_async
    async def put_big_decimal_positive_decimal(self, **kwargs: Any) -> None:
        """Put big decimal value 99999999.99.

        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        request = build_number_put_big_decimal_positive_decimal_request(
            content_type=content_type,
            template_url=self.put_big_decimal_positive_decimal.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_big_decimal_positive_decimal.metadata = {"url": "/number/big/decimal/99999999.99"}  # type: ignore

    @distributed_trace_async
    async def get_big_decimal_positive_decimal(self, **kwargs: Any) -> float:
        """Get big decimal value 99999999.99.

        :return: float
        :rtype: float
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[float]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_big_decimal_positive_decimal_request(
            template_url=self.get_big_decimal_positive_decimal.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_big_decimal_positive_decimal.metadata = {"url": "/number/big/decimal/99999999.99"}  # type: ignore

    @distributed_trace_async
    async def put_big_decimal_negative_decimal(self, **kwargs: Any) -> None:
        """Put big decimal value -99999999.99.

        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        request = build_number_put_big_decimal_negative_decimal_request(
            content_type=content_type,
            template_url=self.put_big_decimal_negative_decimal.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_big_decimal_negative_decimal.metadata = {"url": "/number/big/decimal/-99999999.99"}  # type: ignore

    @distributed_trace_async
    async def get_big_decimal_negative_decimal(self, **kwargs: Any) -> float:
        """Get big decimal value -99999999.99.

        :return: float
        :rtype: float
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[float]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_big_decimal_negative_decimal_request(
            template_url=self.get_big_decimal_negative_decimal.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_big_decimal_negative_decimal.metadata = {"url": "/number/big/decimal/-99999999.99"}  # type: ignore

    @distributed_trace_async
    async def put_small_float(self, number_body: float, **kwargs: Any) -> None:
        """Put small float value 3.402823e-20.

        :param number_body: number body.
        :type number_body: float
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = number_body

        request = build_number_put_small_float_request(
            content_type=content_type,
            json=json,
            template_url=self.put_small_float.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_small_float.metadata = {"url": "/number/small/float/3.402823e-20"}  # type: ignore

    @distributed_trace_async
    async def get_small_float(self, **kwargs: Any) -> float:
        """Get big double value 3.402823e-20.

        :return: float
        :rtype: float
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[float]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_small_float_request(
            template_url=self.get_small_float.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_small_float.metadata = {"url": "/number/small/float/3.402823e-20"}  # type: ignore

    @distributed_trace_async
    async def put_small_double(self, number_body: float, **kwargs: Any) -> None:
        """Put small double value 2.5976931e-101.

        :param number_body: number body.
        :type number_body: float
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = number_body

        request = build_number_put_small_double_request(
            content_type=content_type,
            json=json,
            template_url=self.put_small_double.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_small_double.metadata = {"url": "/number/small/double/2.5976931e-101"}  # type: ignore

    @distributed_trace_async
    async def get_small_double(self, **kwargs: Any) -> float:
        """Get big double value 2.5976931e-101.

        :return: float
        :rtype: float
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[float]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_small_double_request(
            template_url=self.get_small_double.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_small_double.metadata = {"url": "/number/small/double/2.5976931e-101"}  # type: ignore

    @distributed_trace_async
    async def put_small_decimal(self, number_body: float, **kwargs: Any) -> None:
        """Put small decimal value 2.5976931e-101.

        :param number_body: number body.
        :type number_body: float
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = number_body

        request = build_number_put_small_decimal_request(
            content_type=content_type,
            json=json,
            template_url=self.put_small_decimal.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_small_decimal.metadata = {"url": "/number/small/decimal/2.5976931e-101"}  # type: ignore

    @distributed_trace_async
    async def get_small_decimal(self, **kwargs: Any) -> float:
        """Get small decimal value 2.5976931e-101.

        :return: float
        :rtype: float
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[float]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_number_get_small_decimal_request(
            template_url=self.get_small_decimal.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_small_decimal.metadata = {"url": "/number/small/decimal/2.5976931e-101"}  # type: ignore
