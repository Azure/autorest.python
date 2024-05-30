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
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import _model_base, models as _models
from .._serialization import Serializer
from .._vendor import prepare_multipart_form_data

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
_Unset: Any = object()
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_form_data_basic_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/multipart/form-data/mixed-parts"

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_form_data_complex_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/multipart/form-data/complex-parts"

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_form_data_json_part_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/multipart/form-data/json-part"

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_form_data_binary_array_parts_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/multipart/form-data/binary-array-parts"

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_form_data_json_array_parts_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/multipart/form-data/json-array-parts"

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_form_data_multi_binary_parts_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/multipart/form-data/multi-binary-parts"

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_form_data_check_file_name_and_content_type_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/multipart/form-data/check-filename-and-content-type"

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_form_data_anonymous_model_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/multipart/form-data/anonymous-model"

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class FormDataOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~payload.multipart.MultiPartClient`'s
        :attr:`form_data` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def basic(  # pylint: disable=inconsistent-return-statements
        self, body: _models.MultiPartRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: ~payload.multipart.models.MultiPartRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "id": "str",  # Required.
                    "profileImage": filetype
                }
        """

    @overload
    def basic(self, body: JSON, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def basic(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.MultiPartRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Is either a MultiPartRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.MultiPartRequest or JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "id": "str",  # Required.
                    "profileImage": filetype
                }
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
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def complex(  # pylint: disable=inconsistent-return-statements
        self, body: _models.ComplexPartsRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for mixed scenarios.

        :param body: Required.
        :type body: ~payload.multipart.models.ComplexPartsRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "address": {
                        "city": "str"  # Required.
                    },
                    "id": "str",  # Required.
                    "pictures": [filetype],
                    "previousAddresses": [
                        {
                            "city": "str"  # Required.
                        }
                    ],
                    "profileImage": filetype
                }
        """

    @overload
    def complex(self, body: JSON, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Test content-type: multipart/form-data for mixed scenarios.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def complex(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.ComplexPartsRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for mixed scenarios.

        :param body: Is either a ComplexPartsRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.ComplexPartsRequest or JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "address": {
                        "city": "str"  # Required.
                    },
                    "id": "str",  # Required.
                    "pictures": [filetype],
                    "previousAddresses": [
                        {
                            "city": "str"  # Required.
                        }
                    ],
                    "profileImage": filetype
                }
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

        _request = build_form_data_complex_request(
            files=_files,
            data=_data,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def json_part(  # pylint: disable=inconsistent-return-statements
        self, body: _models.JsonPartRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains json part and binary part.

        :param body: Required.
        :type body: ~payload.multipart.models.JsonPartRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "address": {
                        "city": "str"  # Required.
                    },
                    "profileImage": filetype
                }
        """

    @overload
    def json_part(self, body: JSON, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Test content-type: multipart/form-data for scenario contains json part and binary part.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def json_part(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.JsonPartRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains json part and binary part.

        :param body: Is either a JsonPartRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.JsonPartRequest or JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "address": {
                        "city": "str"  # Required.
                    },
                    "profileImage": filetype
                }
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
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def binary_array_parts(  # pylint: disable=inconsistent-return-statements
        self, body: _models.BinaryArrayPartsRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Required.
        :type body: ~payload.multipart.models.BinaryArrayPartsRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "id": "str",  # Required.
                    "pictures": [filetype]
                }
        """

    @overload
    def binary_array_parts(self, body: JSON, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def binary_array_parts(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.BinaryArrayPartsRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Is either a BinaryArrayPartsRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.BinaryArrayPartsRequest or JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "id": "str",  # Required.
                    "pictures": [filetype]
                }
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
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def json_array_parts(  # pylint: disable=inconsistent-return-statements
        self, body: _models.JsonArrayPartsRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi json parts.

        :param body: Required.
        :type body: ~payload.multipart.models.JsonArrayPartsRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "previousAddresses": [
                        {
                            "city": "str"  # Required.
                        }
                    ],
                    "profileImage": filetype
                }
        """

    @overload
    def json_array_parts(self, body: JSON, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Test content-type: multipart/form-data for scenario contains multi json parts.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def json_array_parts(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.JsonArrayPartsRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi json parts.

        :param body: Is either a JsonArrayPartsRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.JsonArrayPartsRequest or JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "previousAddresses": [
                        {
                            "city": "str"  # Required.
                        }
                    ],
                    "profileImage": filetype
                }
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
        _data_fields: List[str] = ["previousAddresses"]
        _files, _data = prepare_multipart_form_data(_body, _file_fields, _data_fields)

        _request = build_form_data_json_array_parts_request(
            files=_files,
            data=_data,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def multi_binary_parts(  # pylint: disable=inconsistent-return-statements
        self, body: _models.MultiBinaryPartsRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Required.
        :type body: ~payload.multipart.models.MultiBinaryPartsRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "profileImage": filetype,
                    "picture": filetype
                }
        """

    @overload
    def multi_binary_parts(self, body: JSON, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def multi_binary_parts(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.MultiBinaryPartsRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Is either a MultiBinaryPartsRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.MultiBinaryPartsRequest or JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "profileImage": filetype,
                    "picture": filetype
                }
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
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def check_file_name_and_content_type(  # pylint: disable=inconsistent-return-statements
        self, body: _models.MultiPartRequest, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: ~payload.multipart.models.MultiPartRequest
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "id": "str",  # Required.
                    "profileImage": filetype
                }
        """

    @overload
    def check_file_name_and_content_type(  # pylint: disable=inconsistent-return-statements
        self, body: JSON, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def check_file_name_and_content_type(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.MultiPartRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Is either a MultiPartRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.MultiPartRequest or JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "id": "str",  # Required.
                    "profileImage": filetype
                }
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
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def anonymous_model(self, body: JSON, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "profileImage": filetype
                }
        """

    @overload
    def anonymous_model(  # pylint: disable=inconsistent-return-statements
        self, *, profile_image: bytes, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :keyword profile_image: Required.
        :paramtype profile_image: bytes
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def anonymous_model(  # pylint: disable=inconsistent-return-statements
        self, body: JSON = _Unset, *, profile_image: bytes = _Unset, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Is one of the following types: JSON Required.
        :type body: JSON
        :keyword profile_image: Required.
        :paramtype profile_image: bytes
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "profileImage": filetype
                }
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
            body = {"profileimage": profile_image}
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
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
