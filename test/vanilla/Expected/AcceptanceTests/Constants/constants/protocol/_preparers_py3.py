# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional, Union

from azure.core.pipeline.transport import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()

import xml.etree.ElementTree as ET


def _request(
    method,
    url,
    params=None,
    headers=None,
    content=None,
    form_content=None,
    stream_content=None,
):
    request = HttpRequest(method, url, headers=headers)

    if params:
        request.format_parameters(params)

    if content is not None:
        content_type = request.headers.get("Content-Type")
        if isinstance(content, ET.Element):
            request.set_xml_body(content)
        # https://github.com/Azure/azure-sdk-for-python/issues/12137
        # A string is valid JSON, make the difference between text
        # and a plain JSON string.
        # Content-Type is a good indicator of intent from user
        elif content_type and content_type.startswith("text/"):
            request.set_text_body(content)
        else:
            try:
                request.set_json_body(content)
            except TypeError:
                request.data = content

    if form_content:
        request.set_formdata_body(form_content)
    elif stream_content:
        request.set_streamed_data_body(stream_content)

    return request


def _prepare_contants_put_no_model_as_string_no_required_two_value_no_default_request(
    input: Optional[Union[str, "_models.NoModelAsStringNoRequiredTwoValueNoDefaultOpEnum"]] = None, **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringNoRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_no_model_as_string_no_required_two_value_default_request(
    input: Optional[Union[str, "_models.NoModelAsStringNoRequiredTwoValueDefaultOpEnum"]] = "value1", **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringNoRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_no_model_as_string_no_required_one_value_no_default_request(
    input: Optional[str] = "value1", **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringNoRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_no_model_as_string_no_required_one_value_default_request(
    input: Optional[str] = "value1", **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringNoRequiredOneValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_no_model_as_string_required_two_value_no_default_request(
    input: Union[str, "_models.NoModelAsStringRequiredTwoValueNoDefaultOpEnum"], **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_no_model_as_string_required_two_value_default_request(
    input: Union[str, "_models.NoModelAsStringRequiredTwoValueDefaultOpEnum"] = "value1", **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_no_model_as_string_required_one_value_no_default_request(**kwargs) -> HttpRequest:
    input = "value1"

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_no_model_as_string_required_one_value_default_request(**kwargs) -> HttpRequest:
    input = "value1"

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredOneValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_model_as_string_no_required_two_value_no_default_request(
    input: Optional[Union[str, "_models.ModelAsStringNoRequiredTwoValueNoDefaultOpEnum"]] = None, **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringNoRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_model_as_string_no_required_two_value_default_request(
    input: Optional[Union[str, "_models.ModelAsStringNoRequiredTwoValueDefaultOpEnum"]] = "value1", **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringNoRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_model_as_string_no_required_one_value_no_default_request(
    input: Optional[Union[str, "_models.ModelAsStringNoRequiredOneValueNoDefaultOpEnum"]] = None, **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringNoRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_model_as_string_no_required_one_value_default_request(
    input: Optional[Union[str, "_models.ModelAsStringNoRequiredOneValueDefaultOpEnum"]] = "value1", **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringNoRequiredOneValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_model_as_string_required_two_value_no_default_request(
    input: Union[str, "_models.ModelAsStringRequiredTwoValueNoDefaultOpEnum"], **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_model_as_string_required_two_value_default_request(
    input: Union[str, "_models.ModelAsStringRequiredTwoValueDefaultOpEnum"] = "value1", **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_model_as_string_required_one_value_no_default_request(
    input: Union[str, "_models.ModelAsStringRequiredOneValueNoDefaultOpEnum"], **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)


def _prepare_contants_put_model_as_string_required_one_value_default_request(
    input: Union[str, "_models.ModelAsStringRequiredOneValueDefaultOpEnum"] = "value1", **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredOneValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return _request("PUT", url, query_parameters, header_parameters)
