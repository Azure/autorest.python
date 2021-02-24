# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Optional, Union

    from azure.core.pipeline.transport import HttpRequest

_SERIALIZER = Serializer()


def _put_no_model_as_string_no_required_two_value_no_default_request(
    input=None,  # type: Optional[Union[str, "_models.NoModelAsStringNoRequiredTwoValueNoDefaultOpEnum"]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringNoRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_no_model_as_string_no_required_two_value_default_request(
    input="value1",  # type: Optional[Union[str, "_models.NoModelAsStringNoRequiredTwoValueDefaultOpEnum"]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringNoRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_no_model_as_string_no_required_one_value_no_default_request(
    input="value1",  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringNoRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_no_model_as_string_no_required_one_value_default_request(
    input="value1",  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringNoRequiredOneValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_no_model_as_string_required_two_value_no_default_request(
    input,  # type: Union[str, "_models.NoModelAsStringRequiredTwoValueNoDefaultOpEnum"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_no_model_as_string_required_two_value_default_request(
    input="value1",  # type: Union[str, "_models.NoModelAsStringRequiredTwoValueDefaultOpEnum"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_no_model_as_string_required_one_value_no_default_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    input = "value1"

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_no_model_as_string_required_one_value_default_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    input = "value1"

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putNoModelAsStringRequiredOneValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_model_as_string_no_required_two_value_no_default_request(
    input=None,  # type: Optional[Union[str, "_models.ModelAsStringNoRequiredTwoValueNoDefaultOpEnum"]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringNoRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_model_as_string_no_required_two_value_default_request(
    input="value1",  # type: Optional[Union[str, "_models.ModelAsStringNoRequiredTwoValueDefaultOpEnum"]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringNoRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_model_as_string_no_required_one_value_no_default_request(
    input=None,  # type: Optional[Union[str, "_models.ModelAsStringNoRequiredOneValueNoDefaultOpEnum"]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringNoRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_model_as_string_no_required_one_value_default_request(
    input="value1",  # type: Optional[Union[str, "_models.ModelAsStringNoRequiredOneValueDefaultOpEnum"]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringNoRequiredOneValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_model_as_string_required_two_value_no_default_request(
    input,  # type: Union[str, "_models.ModelAsStringRequiredTwoValueNoDefaultOpEnum"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredTwoValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_model_as_string_required_two_value_default_request(
    input="value1",  # type: Union[str, "_models.ModelAsStringRequiredTwoValueDefaultOpEnum"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredTwoValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_model_as_string_required_one_value_no_default_request(
    input,  # type: Union[str, "_models.ModelAsStringRequiredOneValueNoDefaultOpEnum"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredOneValueNoDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)


def _put_model_as_string_required_one_value_default_request(
    input="value1",  # type: Union[str, "_models.ModelAsStringRequiredOneValueDefaultOpEnum"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/constants/putModelAsStringRequiredOneValueDefault")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return self._client.put(url, query_parameters, header_parameters)
