# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

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
    build_contants_put_client_constants_request,
    build_contants_put_model_as_string_no_required_one_value_default_request,
    build_contants_put_model_as_string_no_required_one_value_no_default_request,
    build_contants_put_model_as_string_no_required_two_value_default_request,
    build_contants_put_model_as_string_no_required_two_value_no_default_request,
    build_contants_put_model_as_string_required_one_value_default_request,
    build_contants_put_model_as_string_required_one_value_no_default_request,
    build_contants_put_model_as_string_required_two_value_default_request,
    build_contants_put_model_as_string_required_two_value_no_default_request,
    build_contants_put_no_model_as_string_no_required_one_value_default_request,
    build_contants_put_no_model_as_string_no_required_one_value_no_default_request,
    build_contants_put_no_model_as_string_no_required_two_value_default_request,
    build_contants_put_no_model_as_string_no_required_two_value_no_default_request,
    build_contants_put_no_model_as_string_required_one_value_default_request,
    build_contants_put_no_model_as_string_required_one_value_no_default_request,
    build_contants_put_no_model_as_string_required_two_value_default_request,
    build_contants_put_no_model_as_string_required_two_value_no_default_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ContantsOperations:
    """ContantsOperations async operations.

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
    async def put_no_model_as_string_no_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_no_required_two_value_no_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_no_model_as_string_no_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: Optional[str] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_no_required_two_value_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_no_model_as_string_no_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: Optional[str] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: The default value is "value1".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_no_required_one_value_no_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_no_model_as_string_no_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: Optional[str] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: The default value is "value1".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_no_required_one_value_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_no_model_as_string_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_required_two_value_no_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_no_model_as_string_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_no_model_as_string_required_two_value_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_no_model_as_string_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: The default value is "value1". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        input = kwargs.pop("input", "value1")  # type: str

        request = build_contants_put_no_model_as_string_required_one_value_no_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_no_model_as_string_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: The default value is "value1". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        input = kwargs.pop("input", "value1")  # type: str

        request = build_contants_put_no_model_as_string_required_one_value_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_model_as_string_no_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_no_required_two_value_no_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_model_as_string_no_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: Optional[str] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_no_required_two_value_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_model_as_string_no_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: "value1"
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_no_required_one_value_no_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_model_as_string_no_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: Optional[str] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: "value1"
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_no_required_one_value_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_model_as_string_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_required_two_value_no_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_model_as_string_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: Possible values are: "value1" or "value2".
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_required_two_value_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_model_as_string_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: "value1"
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_required_one_value_no_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_model_as_string_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, *, input: str = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input: "value1"
        :paramtype input: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_model_as_string_required_one_value_default_request(
            input=input,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def put_client_constants(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Pass constants from the client to this function. Will pass in constant path, query, and header
        parameters.

        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_contants_put_client_constants_request(
            header_constant=self._config.header_constant,
            query_constant=self._config.query_constant,
            path_constant=self._config.path_constant,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
