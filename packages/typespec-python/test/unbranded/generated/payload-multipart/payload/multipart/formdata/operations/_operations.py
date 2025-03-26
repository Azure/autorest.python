# coding=utf-8

import sys
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from ... import _model_base, models as _models2
from ..._configuration import MultiPartClientConfiguration
from ..._serialization import Deserializer, Serializer
from ..._vendor import FileType, prepare_multipart_form_data
from ..httpparts.operations._operations import FormDataHttpPartsOperations

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
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


def build_form_data_file_array_and_basic_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
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
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: MultiPartClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

        self.http_parts = FormDataHttpPartsOperations(self._client, self._config, self._serialize, self._deserialize)

    @overload
    def basic(self, body: _models2.MultiPartRequest, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: ~payload.multipart.models.MultiPartRequest
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def basic(self, body: JSON, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def basic(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models2.MultiPartRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Is either a MultiPartRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.MultiPartRequest or JSON
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
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
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def file_array_and_basic(self, body: _models2.ComplexPartsRequest, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data for mixed scenarios.

        :param body: Required.
        :type body: ~payload.multipart.models.ComplexPartsRequest
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def file_array_and_basic(self, body: JSON, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data for mixed scenarios.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def file_array_and_basic(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models2.ComplexPartsRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for mixed scenarios.

        :param body: Is either a ComplexPartsRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.ComplexPartsRequest or JSON
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
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

        _request = build_form_data_file_array_and_basic_request(
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
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def json_part(self, body: _models2.JsonPartRequest, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data for scenario contains json part and binary part.

        :param body: Required.
        :type body: ~payload.multipart.models.JsonPartRequest
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def json_part(self, body: JSON, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data for scenario contains json part and binary part.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def json_part(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models2.JsonPartRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains json part and binary part.

        :param body: Is either a JsonPartRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.JsonPartRequest or JSON
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
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
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def binary_array_parts(self, body: _models2.BinaryArrayPartsRequest, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Required.
        :type body: ~payload.multipart.models.BinaryArrayPartsRequest
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def binary_array_parts(self, body: JSON, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def binary_array_parts(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models2.BinaryArrayPartsRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Is either a BinaryArrayPartsRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.BinaryArrayPartsRequest or JSON
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
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
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def multi_binary_parts(self, body: _models2.MultiBinaryPartsRequest, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Required.
        :type body: ~payload.multipart.models.MultiBinaryPartsRequest
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def multi_binary_parts(self, body: JSON, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def multi_binary_parts(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models2.MultiBinaryPartsRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data for scenario contains multi binary parts.

        :param body: Is either a MultiBinaryPartsRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.MultiBinaryPartsRequest or JSON
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
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
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def check_file_name_and_content_type(self, body: _models2.MultiPartRequest, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: ~payload.multipart.models.MultiPartRequest
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def check_file_name_and_content_type(self, body: JSON, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def check_file_name_and_content_type(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models2.MultiPartRequest, JSON], **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Is either a MultiPartRequest type or a JSON type. Required.
        :type body: ~payload.multipart.models.MultiPartRequest or JSON
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
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
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def anonymous_model(self, *, profile_image: FileType, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data.

        :keyword profile_image: Required.
        :paramtype profile_image: ~payload.multipart._vendor.FileType
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def anonymous_model(self, body: JSON, **kwargs: Any) -> None:
        """Test content-type: multipart/form-data.

        :param body: Required.
        :type body: JSON
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def anonymous_model(  # pylint: disable=inconsistent-return-statements
        self, body: JSON = _Unset, *, profile_image: FileType = _Unset, **kwargs: Any
    ) -> None:
        """Test content-type: multipart/form-data.

        :param body: Is one of the following types: JSON Required.
        :type body: JSON
        :keyword profile_image: Required.
        :paramtype profile_image: ~payload.multipart._vendor.FileType
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
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
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
