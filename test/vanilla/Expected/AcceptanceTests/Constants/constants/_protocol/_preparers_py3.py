# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional, Union

from azure.core.protocol import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def prepare_contants_put_no_model_as_string_no_required_two_value_no_default_request(
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

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_no_model_as_string_no_required_two_value_default_request(
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

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_no_model_as_string_no_required_one_value_no_default_request(
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

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_no_model_as_string_no_required_one_value_default_request(
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

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_no_model_as_string_required_two_value_no_default_request(
    input: Union[str, "_models.NoModelAsStringRequiredTwoValueNoDefaultOpEnum"], **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_no_model_as_string_required_two_value_default_request(
    input: Union[str, "_models.NoModelAsStringRequiredTwoValueDefaultOpEnum"] = "value1", **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_no_model_as_string_required_one_value_no_default_request(**kwargs) -> HttpRequest:
    input = "value1"

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_no_model_as_string_required_one_value_default_request(**kwargs) -> HttpRequest:
    input = "value1"

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredOneValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_model_as_string_no_required_two_value_no_default_request(
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

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_model_as_string_no_required_two_value_default_request(
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

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_model_as_string_no_required_one_value_no_default_request(
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

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_model_as_string_no_required_one_value_default_request(
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

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_model_as_string_required_two_value_no_default_request(
    input: Union[str, "_models.ModelAsStringRequiredTwoValueNoDefaultOpEnum"], **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_model_as_string_required_two_value_default_request(
    input: Union[str, "_models.ModelAsStringRequiredTwoValueDefaultOpEnum"] = "value1", **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_model_as_string_required_one_value_no_default_request(
    input: Union[str, "_models.ModelAsStringRequiredOneValueNoDefaultOpEnum"], **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )


def prepare_contants_put_model_as_string_required_one_value_default_request(
    input: Union[str, "_models.ModelAsStringRequiredOneValueDefaultOpEnum"] = "value1", **kwargs
) -> HttpRequest:

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredOneValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
    )
