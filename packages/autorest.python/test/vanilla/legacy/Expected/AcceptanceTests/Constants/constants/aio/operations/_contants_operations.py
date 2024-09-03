# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Literal, Optional, Type, TypeVar, Union

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
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ...operations._contants_operations import (
    build_put_client_constants_request,
    build_put_model_as_string_no_required_one_value_default_request,
    build_put_model_as_string_no_required_one_value_no_default_request,
    build_put_model_as_string_no_required_two_value_default_request,
    build_put_model_as_string_no_required_two_value_no_default_request,
    build_put_model_as_string_required_one_value_default_request,
    build_put_model_as_string_required_one_value_no_default_request,
    build_put_model_as_string_required_two_value_default_request,
    build_put_model_as_string_required_two_value_no_default_request,
    build_put_no_model_as_string_no_required_one_value_default_request,
    build_put_no_model_as_string_no_required_one_value_no_default_request,
    build_put_no_model_as_string_no_required_two_value_default_request,
    build_put_no_model_as_string_no_required_two_value_no_default_request,
    build_put_no_model_as_string_required_one_value_default_request,
    build_put_no_model_as_string_required_one_value_no_default_request,
    build_put_no_model_as_string_required_two_value_default_request,
    build_put_no_model_as_string_required_two_value_no_default_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ContantsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~constants.aio.AutoRestSwaggerConstantService`'s
        :attr:`contants` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def put_no_model_as_string_no_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self,
        input: Optional[Union[str, _models.NoModelAsStringNoRequiredTwoValueNoDefaultOpEnum]] = None,
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: Known values are: "value1" and "value2". Default value is None.
        :type input: str or ~constants.models.NoModelAsStringNoRequiredTwoValueNoDefaultOpEnum
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_no_model_as_string_no_required_two_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_no_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, _models.NoModelAsStringNoRequiredTwoValueDefaultOpEnum] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: Known values are: "value1" and "value2". Default value is "value1".
        :type input: str or ~constants.models.NoModelAsStringNoRequiredTwoValueDefaultOpEnum
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_no_model_as_string_no_required_two_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_no_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, input: Literal["value1"] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: Known values are "value1" and None. Default value is "value1".
        :type input: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_no_model_as_string_no_required_one_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_no_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, input: Literal["value1"] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: Known values are "value1" and None. Default value is "value1".
        :type input: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_no_model_as_string_no_required_one_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, _models.NoModelAsStringRequiredTwoValueNoDefaultOpEnum], **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: Known values are: "value1" and "value2". Required.
        :type input: str or ~constants.models.NoModelAsStringRequiredTwoValueNoDefaultOpEnum
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_no_model_as_string_required_two_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, _models.NoModelAsStringRequiredTwoValueDefaultOpEnum] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: Known values are: "value1" and "value2". Default value is "value1".
        :type input: str or ~constants.models.NoModelAsStringRequiredTwoValueDefaultOpEnum
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_no_model_as_string_required_two_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        input: Literal["value1"] = kwargs.pop("input", _params.pop("input", "value1"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_no_model_as_string_required_one_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        input: Literal["value1"] = kwargs.pop("input", _params.pop("input", "value1"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_no_model_as_string_required_one_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_no_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, input: Optional[Union[str, _models.ModelAsStringNoRequiredTwoValueNoDefaultOpEnum]] = None, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: Known values are: "value1" and "value2". Default value is None.
        :type input: str or ~constants.models.ModelAsStringNoRequiredTwoValueNoDefaultOpEnum
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_model_as_string_no_required_two_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_no_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, _models.ModelAsStringNoRequiredTwoValueDefaultOpEnum] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: Known values are: "value1" and "value2". Default value is "value1".
        :type input: str or ~constants.models.ModelAsStringNoRequiredTwoValueDefaultOpEnum
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_model_as_string_no_required_two_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_no_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, input: Optional[Union[str, _models.ModelAsStringNoRequiredOneValueNoDefaultOpEnum]] = None, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: "value1" Default value is None.
        :type input: str or ~constants.models.ModelAsStringNoRequiredOneValueNoDefaultOpEnum
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_model_as_string_no_required_one_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_no_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, _models.ModelAsStringNoRequiredOneValueDefaultOpEnum] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: "value1" Default value is "value1".
        :type input: str or ~constants.models.ModelAsStringNoRequiredOneValueDefaultOpEnum
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_model_as_string_no_required_one_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, _models.ModelAsStringRequiredTwoValueNoDefaultOpEnum], **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: Known values are: "value1" and "value2". Required.
        :type input: str or ~constants.models.ModelAsStringRequiredTwoValueNoDefaultOpEnum
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_model_as_string_required_two_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, _models.ModelAsStringRequiredTwoValueDefaultOpEnum] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: Known values are: "value1" and "value2". Default value is "value1".
        :type input: str or ~constants.models.ModelAsStringRequiredTwoValueDefaultOpEnum
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_model_as_string_required_two_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, _models.ModelAsStringRequiredOneValueNoDefaultOpEnum], **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: "value1" Required.
        :type input: str or ~constants.models.ModelAsStringRequiredOneValueNoDefaultOpEnum
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_model_as_string_required_one_value_no_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, _models.ModelAsStringRequiredOneValueDefaultOpEnum] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: "value1" Default value is "value1".
        :type input: str or ~constants.models.ModelAsStringRequiredOneValueDefaultOpEnum
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_model_as_string_required_one_value_default_request(
            input=input,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def put_client_constants(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Pass constants from the client to this function. Will pass in constant path, query, and header
        parameters.

        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_put_client_constants_request(
            header_constant=self._config.header_constant,
            query_constant=self._config.query_constant,
            path_constant=self._config.path_constant,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

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
