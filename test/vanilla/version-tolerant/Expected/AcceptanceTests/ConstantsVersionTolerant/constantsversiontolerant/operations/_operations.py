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
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from .._vendor import _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_contants_put_no_model_as_string_no_required_two_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putNoModelAsStringNoRequiredTwoValueNoDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_no_model_as_string_no_required_two_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putNoModelAsStringNoRequiredTwoValueDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_no_model_as_string_no_required_one_value_no_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putNoModelAsStringNoRequiredOneValueNoDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_no_model_as_string_no_required_one_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putNoModelAsStringNoRequiredOneValueDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_no_model_as_string_required_two_value_no_default_request(
    *, input: str, **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putNoModelAsStringRequiredTwoValueNoDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_no_model_as_string_required_two_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putNoModelAsStringRequiredTwoValueDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_no_model_as_string_required_one_value_no_default_request(**kwargs: Any) -> HttpRequest:
    input = kwargs.pop("input", "value1")  # type: str

    # Construct URL
    _url = "/constants/putNoModelAsStringRequiredOneValueNoDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_no_model_as_string_required_one_value_default_request(**kwargs: Any) -> HttpRequest:
    input = kwargs.pop("input", "value1")  # type: str

    # Construct URL
    _url = "/constants/putNoModelAsStringRequiredOneValueDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_model_as_string_no_required_two_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putModelAsStringNoRequiredTwoValueNoDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_model_as_string_no_required_two_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putModelAsStringNoRequiredTwoValueDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_model_as_string_no_required_one_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putModelAsStringNoRequiredOneValueNoDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_model_as_string_no_required_one_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putModelAsStringNoRequiredOneValueDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_model_as_string_required_two_value_no_default_request(
    *, input: str, **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putModelAsStringRequiredTwoValueNoDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_model_as_string_required_two_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putModelAsStringRequiredTwoValueDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_model_as_string_required_one_value_no_default_request(
    *, input: str, **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putModelAsStringRequiredOneValueNoDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_model_as_string_required_one_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    # Construct URL
    _url = "/constants/putModelAsStringRequiredOneValueDefault"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, **kwargs)


def build_contants_put_client_constants_request(**kwargs: Any) -> HttpRequest:
    header_constant = kwargs.pop("header_constant", True)  # type: bool
    query_constant = kwargs.pop("query_constant", 100)  # type: int
    path_constant = kwargs.pop("path_constant", "path")  # type: str

    # Construct URL
    _url = "/constants/clientConstants/{path-constant}"
    path_format_arguments = {
        "path-constant": _SERIALIZER.url("path_constant", path_constant, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["query-constant"] = _SERIALIZER.query("query_constant", query_constant, "int")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["header-constant"] = _SERIALIZER.header("header_constant", header_constant, "bool")

    return HttpRequest(method="PUT", url=_url, params=_query_parameters, headers=_header_parameters, **kwargs)


class ContantsOperations(object):
    """ContantsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def put_no_model_as_string_no_required_two_value_no_default(
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_no_required_two_value_default(
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_no_required_one_value_no_default(
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_no_required_one_value_default(
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_required_two_value_no_default(self, *, input: str, **kwargs: Any) -> None:
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_required_two_value_default(self, *, input: str = "value1", **kwargs: Any) -> None:
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_required_one_value_no_default(self, **kwargs: Any) -> None:
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_no_model_as_string_required_one_value_default(self, **kwargs: Any) -> None:
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_no_required_two_value_no_default(
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_no_required_two_value_default(
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_no_required_one_value_no_default(
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_no_required_one_value_default(
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_required_two_value_no_default(self, *, input: str, **kwargs: Any) -> None:
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_required_two_value_default(self, *, input: str = "value1", **kwargs: Any) -> None:
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_required_one_value_no_default(self, *, input: str, **kwargs: Any) -> None:
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_model_as_string_required_one_value_default(self, *, input: str = "value1", **kwargs: Any) -> None:
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def put_client_constants(self, **kwargs: Any) -> None:
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

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
