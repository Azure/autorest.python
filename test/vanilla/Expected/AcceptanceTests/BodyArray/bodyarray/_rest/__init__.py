# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._request_builders_py3 import build_array_get_null_request
    from ._request_builders_py3 import build_array_get_invalid_request
    from ._request_builders_py3 import build_array_get_empty_request
    from ._request_builders_py3 import build_array_put_empty_request
    from ._request_builders_py3 import build_array_get_boolean_tfft_request
    from ._request_builders_py3 import build_array_put_boolean_tfft_request
    from ._request_builders_py3 import build_array_get_boolean_invalid_null_request
    from ._request_builders_py3 import build_array_get_boolean_invalid_string_request
    from ._request_builders_py3 import build_array_get_integer_valid_request
    from ._request_builders_py3 import build_array_put_integer_valid_request
    from ._request_builders_py3 import build_array_get_int_invalid_null_request
    from ._request_builders_py3 import build_array_get_int_invalid_string_request
    from ._request_builders_py3 import build_array_get_long_valid_request
    from ._request_builders_py3 import build_array_put_long_valid_request
    from ._request_builders_py3 import build_array_get_long_invalid_null_request
    from ._request_builders_py3 import build_array_get_long_invalid_string_request
    from ._request_builders_py3 import build_array_get_float_valid_request
    from ._request_builders_py3 import build_array_put_float_valid_request
    from ._request_builders_py3 import build_array_get_float_invalid_null_request
    from ._request_builders_py3 import build_array_get_float_invalid_string_request
    from ._request_builders_py3 import build_array_get_double_valid_request
    from ._request_builders_py3 import build_array_put_double_valid_request
    from ._request_builders_py3 import build_array_get_double_invalid_null_request
    from ._request_builders_py3 import build_array_get_double_invalid_string_request
    from ._request_builders_py3 import build_array_get_string_valid_request
    from ._request_builders_py3 import build_array_put_string_valid_request
    from ._request_builders_py3 import build_array_get_enum_valid_request
    from ._request_builders_py3 import build_array_put_enum_valid_request
    from ._request_builders_py3 import build_array_get_string_enum_valid_request
    from ._request_builders_py3 import build_array_put_string_enum_valid_request
    from ._request_builders_py3 import build_array_get_string_with_null_request
    from ._request_builders_py3 import build_array_get_string_with_invalid_request
    from ._request_builders_py3 import build_array_get_uuid_valid_request
    from ._request_builders_py3 import build_array_put_uuid_valid_request
    from ._request_builders_py3 import build_array_get_uuid_invalid_chars_request
    from ._request_builders_py3 import build_array_get_date_valid_request
    from ._request_builders_py3 import build_array_put_date_valid_request
    from ._request_builders_py3 import build_array_get_date_invalid_null_request
    from ._request_builders_py3 import build_array_get_date_invalid_chars_request
    from ._request_builders_py3 import build_array_get_date_time_valid_request
    from ._request_builders_py3 import build_array_put_date_time_valid_request
    from ._request_builders_py3 import build_array_get_date_time_invalid_null_request
    from ._request_builders_py3 import build_array_get_date_time_invalid_chars_request
    from ._request_builders_py3 import build_array_get_date_time_rfc1123_valid_request
    from ._request_builders_py3 import build_array_put_date_time_rfc1123_valid_request
    from ._request_builders_py3 import build_array_get_duration_valid_request
    from ._request_builders_py3 import build_array_put_duration_valid_request
    from ._request_builders_py3 import build_array_get_byte_valid_request
    from ._request_builders_py3 import build_array_put_byte_valid_request
    from ._request_builders_py3 import build_array_get_byte_invalid_null_request
    from ._request_builders_py3 import build_array_get_base64_url_request
    from ._request_builders_py3 import build_array_get_complex_null_request
    from ._request_builders_py3 import build_array_get_complex_empty_request
    from ._request_builders_py3 import build_array_get_complex_item_null_request
    from ._request_builders_py3 import build_array_get_complex_item_empty_request
    from ._request_builders_py3 import build_array_get_complex_valid_request
    from ._request_builders_py3 import build_array_put_complex_valid_request
    from ._request_builders_py3 import build_array_get_array_null_request
    from ._request_builders_py3 import build_array_get_array_empty_request
    from ._request_builders_py3 import build_array_get_array_item_null_request
    from ._request_builders_py3 import build_array_get_array_item_empty_request
    from ._request_builders_py3 import build_array_get_array_valid_request
    from ._request_builders_py3 import build_array_put_array_valid_request
    from ._request_builders_py3 import build_array_get_dictionary_null_request
    from ._request_builders_py3 import build_array_get_dictionary_empty_request
    from ._request_builders_py3 import build_array_get_dictionary_item_null_request
    from ._request_builders_py3 import build_array_get_dictionary_item_empty_request
    from ._request_builders_py3 import build_array_get_dictionary_valid_request
    from ._request_builders_py3 import build_array_put_dictionary_valid_request
except (SyntaxError, ImportError):
    from ._request_builders import build_array_get_null_request  # type: ignore
    from ._request_builders import build_array_get_invalid_request  # type: ignore
    from ._request_builders import build_array_get_empty_request  # type: ignore
    from ._request_builders import build_array_put_empty_request  # type: ignore
    from ._request_builders import build_array_get_boolean_tfft_request  # type: ignore
    from ._request_builders import build_array_put_boolean_tfft_request  # type: ignore
    from ._request_builders import build_array_get_boolean_invalid_null_request  # type: ignore
    from ._request_builders import build_array_get_boolean_invalid_string_request  # type: ignore
    from ._request_builders import build_array_get_integer_valid_request  # type: ignore
    from ._request_builders import build_array_put_integer_valid_request  # type: ignore
    from ._request_builders import build_array_get_int_invalid_null_request  # type: ignore
    from ._request_builders import build_array_get_int_invalid_string_request  # type: ignore
    from ._request_builders import build_array_get_long_valid_request  # type: ignore
    from ._request_builders import build_array_put_long_valid_request  # type: ignore
    from ._request_builders import build_array_get_long_invalid_null_request  # type: ignore
    from ._request_builders import build_array_get_long_invalid_string_request  # type: ignore
    from ._request_builders import build_array_get_float_valid_request  # type: ignore
    from ._request_builders import build_array_put_float_valid_request  # type: ignore
    from ._request_builders import build_array_get_float_invalid_null_request  # type: ignore
    from ._request_builders import build_array_get_float_invalid_string_request  # type: ignore
    from ._request_builders import build_array_get_double_valid_request  # type: ignore
    from ._request_builders import build_array_put_double_valid_request  # type: ignore
    from ._request_builders import build_array_get_double_invalid_null_request  # type: ignore
    from ._request_builders import build_array_get_double_invalid_string_request  # type: ignore
    from ._request_builders import build_array_get_string_valid_request  # type: ignore
    from ._request_builders import build_array_put_string_valid_request  # type: ignore
    from ._request_builders import build_array_get_enum_valid_request  # type: ignore
    from ._request_builders import build_array_put_enum_valid_request  # type: ignore
    from ._request_builders import build_array_get_string_enum_valid_request  # type: ignore
    from ._request_builders import build_array_put_string_enum_valid_request  # type: ignore
    from ._request_builders import build_array_get_string_with_null_request  # type: ignore
    from ._request_builders import build_array_get_string_with_invalid_request  # type: ignore
    from ._request_builders import build_array_get_uuid_valid_request  # type: ignore
    from ._request_builders import build_array_put_uuid_valid_request  # type: ignore
    from ._request_builders import build_array_get_uuid_invalid_chars_request  # type: ignore
    from ._request_builders import build_array_get_date_valid_request  # type: ignore
    from ._request_builders import build_array_put_date_valid_request  # type: ignore
    from ._request_builders import build_array_get_date_invalid_null_request  # type: ignore
    from ._request_builders import build_array_get_date_invalid_chars_request  # type: ignore
    from ._request_builders import build_array_get_date_time_valid_request  # type: ignore
    from ._request_builders import build_array_put_date_time_valid_request  # type: ignore
    from ._request_builders import build_array_get_date_time_invalid_null_request  # type: ignore
    from ._request_builders import build_array_get_date_time_invalid_chars_request  # type: ignore
    from ._request_builders import build_array_get_date_time_rfc1123_valid_request  # type: ignore
    from ._request_builders import build_array_put_date_time_rfc1123_valid_request  # type: ignore
    from ._request_builders import build_array_get_duration_valid_request  # type: ignore
    from ._request_builders import build_array_put_duration_valid_request  # type: ignore
    from ._request_builders import build_array_get_byte_valid_request  # type: ignore
    from ._request_builders import build_array_put_byte_valid_request  # type: ignore
    from ._request_builders import build_array_get_byte_invalid_null_request  # type: ignore
    from ._request_builders import build_array_get_base64_url_request  # type: ignore
    from ._request_builders import build_array_get_complex_null_request  # type: ignore
    from ._request_builders import build_array_get_complex_empty_request  # type: ignore
    from ._request_builders import build_array_get_complex_item_null_request  # type: ignore
    from ._request_builders import build_array_get_complex_item_empty_request  # type: ignore
    from ._request_builders import build_array_get_complex_valid_request  # type: ignore
    from ._request_builders import build_array_put_complex_valid_request  # type: ignore
    from ._request_builders import build_array_get_array_null_request  # type: ignore
    from ._request_builders import build_array_get_array_empty_request  # type: ignore
    from ._request_builders import build_array_get_array_item_null_request  # type: ignore
    from ._request_builders import build_array_get_array_item_empty_request  # type: ignore
    from ._request_builders import build_array_get_array_valid_request  # type: ignore
    from ._request_builders import build_array_put_array_valid_request  # type: ignore
    from ._request_builders import build_array_get_dictionary_null_request  # type: ignore
    from ._request_builders import build_array_get_dictionary_empty_request  # type: ignore
    from ._request_builders import build_array_get_dictionary_item_null_request  # type: ignore
    from ._request_builders import build_array_get_dictionary_item_empty_request  # type: ignore
    from ._request_builders import build_array_get_dictionary_valid_request  # type: ignore
    from ._request_builders import build_array_put_dictionary_valid_request  # type: ignore

__all__ = [
    "build_array_get_null_request",
    "build_array_get_invalid_request",
    "build_array_get_empty_request",
    "build_array_put_empty_request",
    "build_array_get_boolean_tfft_request",
    "build_array_put_boolean_tfft_request",
    "build_array_get_boolean_invalid_null_request",
    "build_array_get_boolean_invalid_string_request",
    "build_array_get_integer_valid_request",
    "build_array_put_integer_valid_request",
    "build_array_get_int_invalid_null_request",
    "build_array_get_int_invalid_string_request",
    "build_array_get_long_valid_request",
    "build_array_put_long_valid_request",
    "build_array_get_long_invalid_null_request",
    "build_array_get_long_invalid_string_request",
    "build_array_get_float_valid_request",
    "build_array_put_float_valid_request",
    "build_array_get_float_invalid_null_request",
    "build_array_get_float_invalid_string_request",
    "build_array_get_double_valid_request",
    "build_array_put_double_valid_request",
    "build_array_get_double_invalid_null_request",
    "build_array_get_double_invalid_string_request",
    "build_array_get_string_valid_request",
    "build_array_put_string_valid_request",
    "build_array_get_enum_valid_request",
    "build_array_put_enum_valid_request",
    "build_array_get_string_enum_valid_request",
    "build_array_put_string_enum_valid_request",
    "build_array_get_string_with_null_request",
    "build_array_get_string_with_invalid_request",
    "build_array_get_uuid_valid_request",
    "build_array_put_uuid_valid_request",
    "build_array_get_uuid_invalid_chars_request",
    "build_array_get_date_valid_request",
    "build_array_put_date_valid_request",
    "build_array_get_date_invalid_null_request",
    "build_array_get_date_invalid_chars_request",
    "build_array_get_date_time_valid_request",
    "build_array_put_date_time_valid_request",
    "build_array_get_date_time_invalid_null_request",
    "build_array_get_date_time_invalid_chars_request",
    "build_array_get_date_time_rfc1123_valid_request",
    "build_array_put_date_time_rfc1123_valid_request",
    "build_array_get_duration_valid_request",
    "build_array_put_duration_valid_request",
    "build_array_get_byte_valid_request",
    "build_array_put_byte_valid_request",
    "build_array_get_byte_invalid_null_request",
    "build_array_get_base64_url_request",
    "build_array_get_complex_null_request",
    "build_array_get_complex_empty_request",
    "build_array_get_complex_item_null_request",
    "build_array_get_complex_item_empty_request",
    "build_array_get_complex_valid_request",
    "build_array_put_complex_valid_request",
    "build_array_get_array_null_request",
    "build_array_get_array_empty_request",
    "build_array_get_array_item_null_request",
    "build_array_get_array_item_empty_request",
    "build_array_get_array_valid_request",
    "build_array_put_array_valid_request",
    "build_array_get_dictionary_null_request",
    "build_array_get_dictionary_empty_request",
    "build_array_get_dictionary_item_null_request",
    "build_array_get_dictionary_item_empty_request",
    "build_array_get_dictionary_valid_request",
    "build_array_put_dictionary_valid_request",
]
