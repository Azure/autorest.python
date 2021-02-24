# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Optional, Union

from azure.core.pipeline.transport import HttpRequest


def _param_existing_key_request(self, user_agent_parameter: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/existingkey")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["User-Agent"] = self._serialize.header("user_agent_parameter", user_agent_parameter, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_existing_key_request(self, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/existingkey")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _param_protected_key_request(self, content_type: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/protectedkey")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_protected_key_request(self, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/protectedkey")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _param_integer_request(self, scenario: str, value: int, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/integer")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["value"] = self._serialize.header("value", value, "int")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_integer_request(self, scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/integer")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _param_long_request(self, scenario: str, value: int, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/long")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["value"] = self._serialize.header("value", value, "long")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_long_request(self, scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/long")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _param_float_request(self, scenario: str, value: float, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/float")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["value"] = self._serialize.header("value", value, "float")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_float_request(self, scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/float")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _param_double_request(self, scenario: str, value: float, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/double")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["value"] = self._serialize.header("value", value, "float")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_double_request(self, scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/double")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _param_bool_request(self, scenario: str, value: bool, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/bool")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["value"] = self._serialize.header("value", value, "bool")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_bool_request(self, scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/bool")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _param_string_request(self, scenario: str, value: Optional[str] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/string")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    if value is not None:
        header_parameters["value"] = self._serialize.header("value", value, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_string_request(self, scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/string")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _param_date_request(self, scenario: str, value: datetime.date, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/date")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["value"] = self._serialize.header("value", value, "date")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_date_request(self, scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/date")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _param_datetime_request(self, scenario: str, value: datetime.datetime, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/datetime")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["value"] = self._serialize.header("value", value, "iso-8601")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_datetime_request(self, scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/datetime")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _param_datetime_rfc1123_request(
    self, scenario: str, value: Optional[datetime.datetime] = None, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/datetimerfc1123")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    if value is not None:
        header_parameters["value"] = self._serialize.header("value", value, "rfc-1123")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_datetime_rfc1123_request(self, scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/datetimerfc1123")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _param_duration_request(self, scenario: str, value: datetime.timedelta, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/duration")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["value"] = self._serialize.header("value", value, "duration")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_duration_request(self, scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/duration")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _param_byte_request(self, scenario: str, value: bytearray, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/byte")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["value"] = self._serialize.header("value", value, "bytearray")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_byte_request(self, scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/byte")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _param_enum_request(
    self, scenario: str, value: Optional[Union[str, "_models.GreyscaleColors"]] = None, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/enum")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    if value is not None:
        header_parameters["value"] = self._serialize.header("value", value, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _response_enum_request(self, scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/enum")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = self._serialize.header("scenario", scenario, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _custom_request_id_request(self, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/custom/x-ms-client-request-id/9C4D50EE-2D56-4CD3-8152-34347DC9F2B0")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)
