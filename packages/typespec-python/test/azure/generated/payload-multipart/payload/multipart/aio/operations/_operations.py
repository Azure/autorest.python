# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union, overload

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

from ... import _model_base, models as _models
from ..._vendor import FileType, prepare_multipart_form_data
from ...operations._operations import (
    build_form_data_anonymous_model_request,
    build_form_data_basic_request,
    build_form_data_binary_array_parts_request,
    build_form_data_check_file_name_and_content_type_request,
    build_form_data_complex_request,
    build_form_data_complex_with_http_part_request,
    build_form_data_file_with_http_part_optional_content_type_request,
    build_form_data_file_with_http_part_required_content_type_request,
    build_form_data_file_with_http_part_specific_content_type_request,
    build_form_data_json_part_request,
    build_form_data_multi_binary_parts_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
_Unset: Any = object()
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class FormDataOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~payload.multipart.aio.MultiPartClient`'s
        :attr:`form_data` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def basic(  # pylint: disable=inconsistent-return-statements
        self, body: _models.MultiPartRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: ~payload.multipart.models.MultiPartRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def basic(self, body: JSON, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def basic(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.MultiPartRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Is either a MultiPartRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.MultiPartRequest or JSON
        :return: None
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

        _body = body.as_dict() if isinstance(body, _model_base.Model) else body
        _file_fields: List[str] = ["profileImage"]
        _data_fields: List[str] = ["id"]
        _files, _data = prepare_multipart_form_data(_body, _file_fields, _data_fields)

        _request = build_form_data_basic_request(
            files=_files,
            data=_data,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def complex(  # pylint: disable=inconsistent-return-statements
        self, body: _models.ComplexPartsRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for mixed scenarios.

        :param body: Required.
        :type body: ~payload.multipart.models.ComplexPartsRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def complex(self, body: JSON, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Test content-type: multipart/form-data for mixed scenarios.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def complex(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.ComplexPartsRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for mixed scenarios.

        :param body: Is either a ComplexPartsRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.ComplexPartsRequest or JSON
        :return: None
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

        _body = body.as_dict() if isinstance(body, _model_base.Model) else body
        _file_fields: List[str] = ["profileImage", "pictures"]
        _data_fields: List[str] = ["id", "address"]
        _files, _data = prepare_multipart_form_data(_body, _file_fields, _data_fields)

        _request = build_form_data_complex_request(
            files=_files,
            data=_data,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def json_part(  # pylint: disable=inconsistent-return-statements
        self, body: _models.JsonPartRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains json part and binary part.

        :param body: Required.
        :type body: ~payload.multipart.models.JsonPartRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def json_part(self, body: JSON, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Test content-type: multipart/form-data for scenario contains json part and binary part.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def json_part(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.JsonPartRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains json part and binary part.

        :param body: Is either a JsonPartRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.JsonPartRequest or JSON
        :return: None
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

        _body = body.as_dict() if isinstance(body, _model_base.Model) else body
        _file_fields: List[str] = ["profileImage"]
        _data_fields: List[str] = ["address"]
        _files, _data = prepare_multipart_form_data(_body, _file_fields, _data_fields)

        _request = build_form_data_json_part_request(
            files=_files,
            data=_data,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def binary_array_parts(  # pylint: disable=inconsistent-return-statements
        self, body: _models.BinaryArrayPartsRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Required.
        :type body: ~payload.multipart.models.BinaryArrayPartsRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def binary_array_parts(  # pylint: disable=inconsistent-return-statements
        self, body: JSON, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def binary_array_parts(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.BinaryArrayPartsRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Is either a BinaryArrayPartsRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.BinaryArrayPartsRequest or JSON
        :return: None
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

        _body = body.as_dict() if isinstance(body, _model_base.Model) else body
        _file_fields: List[str] = ["pictures"]
        _data_fields: List[str] = ["id"]
        _files, _data = prepare_multipart_form_data(_body, _file_fields, _data_fields)

        _request = build_form_data_binary_array_parts_request(
            files=_files,
            data=_data,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def multi_binary_parts(  # pylint: disable=inconsistent-return-statements
        self, body: _models.MultiBinaryPartsRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Required.
        :type body: ~payload.multipart.models.MultiBinaryPartsRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def multi_binary_parts(  # pylint: disable=inconsistent-return-statements
        self, body: JSON, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def multi_binary_parts(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.MultiBinaryPartsRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Is either a MultiBinaryPartsRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.MultiBinaryPartsRequest or JSON
        :return: None
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

        _body = body.as_dict() if isinstance(body, _model_base.Model) else body
        _file_fields: List[str] = ["profileImage", "picture"]
        _data_fields: List[str] = []
        _files, _data = prepare_multipart_form_data(_body, _file_fields, _data_fields)

        _request = build_form_data_multi_binary_parts_request(
            files=_files,
            data=_data,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def check_file_name_and_content_type(  # pylint: disable=inconsistent-return-statements
        self, body: _models.MultiPartRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: ~payload.multipart.models.MultiPartRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def check_file_name_and_content_type(  # pylint: disable=inconsistent-return-statements
        self, body: JSON, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def check_file_name_and_content_type(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.MultiPartRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Is either a MultiPartRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.MultiPartRequest or JSON
        :return: None
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

        _body = body.as_dict() if isinstance(body, _model_base.Model) else body
        _file_fields: List[str] = ["profileImage"]
        _data_fields: List[str] = ["id"]
        _files, _data = prepare_multipart_form_data(_body, _file_fields, _data_fields)

        _request = build_form_data_check_file_name_and_content_type_request(
            files=_files,
            data=_data,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def anonymous_model(  # pylint: disable=inconsistent-return-statements
        self, body: JSON, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def anonymous_model(  # pylint: disable=inconsistent-return-statements
        self, *, profile_image: FileType, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :keyword profile_image: Required.
        :paramtype profile_image: ~payload.multipart._vendor.FileType
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def anonymous_model(  # pylint: disable=inconsistent-return-statements
        self, body: JSON = _Unset, *, profile_image: FileType = _Unset, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Is one of the following types: JSON Required.
        :type body: JSON
        :keyword profile_image: Required.
        :paramtype profile_image: ~payload.multipart._vendor.FileType
        :return: None
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

        if body is _Unset:
            if profile_image is _Unset:
                raise TypeError("missing required argument: profile_image")
            body = {"profileImage": profile_image}
            body = {k: v for k, v in body.items() if v is not None}
        _body = body.as_dict() if isinstance(body, _model_base.Model) else body
        _file_fields: List[str] = ["profileImage"]
        _data_fields: List[str] = []
        _files, _data = prepare_multipart_form_data(_body, _file_fields, _data_fields)

        _request = build_form_data_anonymous_model_request(
            files=_files,
            data=_data,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def file_with_http_part_specific_content_type(  # pylint: disable=inconsistent-return-statements,name-too-long
        self, body: _models.FileWithHttpPartSpecificContentTypeRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: ~payload.multipart.models.FileWithHttpPartSpecificContentTypeRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def file_with_http_part_specific_content_type(  # pylint: disable=inconsistent-return-statements,name-too-long
        self, body: JSON, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def file_with_http_part_specific_content_type(  # pylint: disable=inconsistent-return-statements,name-too-long
        self, body: Union[_models.FileWithHttpPartSpecificContentTypeRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Is either a FileWithHttpPartSpecificContentTypeRequest type or a JSON type.
         Required.
        :type body: ~payload.multipart.models.FileWithHttpPartSpecificContentTypeRequest or JSON
        :return: None
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

        _body = body.as_dict() if isinstance(body, _model_base.Model) else body
        _file_fields: List[str] = ["profileImage"]
        _data_fields: List[str] = []
        _files, _data = prepare_multipart_form_data(_body, _file_fields, _data_fields)

        _request = build_form_data_file_with_http_part_specific_content_type_request(
            files=_files,
            data=_data,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def file_with_http_part_required_content_type(  # pylint: disable=inconsistent-return-statements,name-too-long
        self, body: _models.FileWithHttpPartRequiredContentTypeRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: ~payload.multipart.models.FileWithHttpPartRequiredContentTypeRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def file_with_http_part_required_content_type(  # pylint: disable=inconsistent-return-statements,name-too-long
        self, body: JSON, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def file_with_http_part_required_content_type(  # pylint: disable=inconsistent-return-statements,name-too-long
        self, body: Union[_models.FileWithHttpPartRequiredContentTypeRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Is either a FileWithHttpPartRequiredContentTypeRequest type or a JSON type.
         Required.
        :type body: ~payload.multipart.models.FileWithHttpPartRequiredContentTypeRequest or JSON
        :return: None
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

        _body = body.as_dict() if isinstance(body, _model_base.Model) else body
        _file_fields: List[str] = ["profileImage"]
        _data_fields: List[str] = []
        _files, _data = prepare_multipart_form_data(_body, _file_fields, _data_fields)

        _request = build_form_data_file_with_http_part_required_content_type_request(
            files=_files,
            data=_data,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def file_with_http_part_optional_content_type(  # pylint: disable=inconsistent-return-statements,name-too-long
        self, body: _models.FileWithHttpPartOptionalContentTypeRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for optional content type.

        :param body: Required.
        :type body: ~payload.multipart.models.FileWithHttpPartOptionalContentTypeRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def file_with_http_part_optional_content_type(  # pylint: disable=inconsistent-return-statements,name-too-long
        self, body: JSON, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for optional content type.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def file_with_http_part_optional_content_type(  # pylint: disable=inconsistent-return-statements,name-too-long
        self, body: Union[_models.FileWithHttpPartOptionalContentTypeRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for optional content type.

        :param body: Is either a FileWithHttpPartOptionalContentTypeRequest type or a JSON type.
         Required.
        :type body: ~payload.multipart.models.FileWithHttpPartOptionalContentTypeRequest or JSON
        :return: None
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

        _body = body.as_dict() if isinstance(body, _model_base.Model) else body
        _file_fields: List[str] = ["profileImage"]
        _data_fields: List[str] = []
        _files, _data = prepare_multipart_form_data(_body, _file_fields, _data_fields)

        _request = build_form_data_file_with_http_part_optional_content_type_request(
            files=_files,
            data=_data,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def complex_with_http_part(  # pylint: disable=inconsistent-return-statements
        self, body: _models.ComplexHttpPartsModelRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for mixed scenarios.

        :param body: Required.
        :type body: ~payload.multipart.models.ComplexHttpPartsModelRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def complex_with_http_part(  # pylint: disable=inconsistent-return-statements
        self, body: JSON, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for mixed scenarios.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def complex_with_http_part(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.ComplexHttpPartsModelRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for mixed scenarios.

        :param body: Is either a ComplexHttpPartsModelRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.ComplexHttpPartsModelRequest or JSON
        :return: None
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

        _body = body.as_dict() if isinstance(body, _model_base.Model) else body
        _file_fields: List[str] = ["profileImage", "pictures"]
        _data_fields: List[str] = ["id", "address", "previousAddresses"]
        _files, _data = prepare_multipart_form_data(_body, _file_fields, _data_fields)

        _request = build_form_data_complex_with_http_part_request(
            files=_files,
            data=_data,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
