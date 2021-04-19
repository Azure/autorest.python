# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import isodate
import json
from datetime import timedelta
from bodydictionary._rest import dictionary
from bodydictionary import AutoRestSwaggerBATDictionaryService
from bodydictionary.models import Widget


import pytest

@pytest.fixture
def client():
    with AutoRestSwaggerBATDictionaryService(base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def make_request(client, base_make_request):
    def _make_request(request):
        return base_make_request(client, request)
    return _make_request

@pytest.fixture
def make_request_json_response(client, base_make_request_json_response):
    def _make_request(request):
        return base_make_request_json_response(client, request)
    return _make_request

@pytest.fixture
def get_deserialized_dict(make_request_json_response):
    def _get_deserialized_dict(request, deserialize_value_callable):
        json_response = make_request_json_response(request)
        return {
            str(idx): deserialize_value_callable(json_response[key]) if json_response[key] else None
            for idx, key in enumerate(json_response.keys())
        }
    return _get_deserialized_dict

@pytest.fixture
def get_serialized_dict():
    def _get_serialized_dict(dict, serialize_value_callable):
        return {
            k: serialize_value_callable(v) for k, v in dict.items()
        }
    return _get_serialized_dict


@pytest.fixture
def test_dict():
    test_product1 = Widget(integer=1, string="2").serialize()
    test_product2 = Widget(integer=3, string="4").serialize()
    test_product3 = Widget(integer=5, string="6").serialize()
    return {"0":test_product1, "1":test_product2, "2":test_product3}

# Primitive types
def test_boolean_tfft(make_request, make_request_json_response):
    tfft = {"0":True, "1":False, "2":False, "3":True}
    request = dictionary.build_get_boolean_tfft_request()
    assert tfft == make_request_json_response(request)

    request = dictionary.build_put_boolean_tfft_request(json=tfft)
    make_request(request)

def test_get_boolean_invalid(make_request_json_response):
    invalid_null_dict = {"0":True, "1":None, "2":False}
    request = dictionary.build_get_boolean_invalid_null_request()
    assert invalid_null_dict ==  make_request_json_response(request)

    request = dictionary.build_get_boolean_invalid_string_request()
    assert {"0": True, "1": "boolean", "2": False} == make_request_json_response(request)

def test_integer_valid(make_request, make_request_json_response):
    int_valid = {"0":1, "1":-1, "2":3, "3":300}
    request = dictionary.build_get_integer_valid_request()
    assert int_valid ==  make_request_json_response(request)

    request = dictionary.build_put_integer_valid_request(json=int_valid)
    make_request(request)

def test_get_int_invalid(make_request_json_response):
    int_null_dict = {"0":1, "1":None, "2":0}
    request = dictionary.build_get_int_invalid_null_request()
    assert int_null_dict ==  make_request_json_response(request)

    request = dictionary.build_get_int_invalid_string_request()
    assert {"0": 1, "1": "integer", "2": 0} == make_request_json_response(request)

def test_long_valid(make_request, make_request_json_response):
    long_valid = {"0":1, "1":-1, "2":3, "3":300}
    request = dictionary.build_get_long_valid_request()
    assert long_valid ==  make_request_json_response(request)

    request = dictionary.build_put_long_valid_request(json=long_valid)
    make_request(request)

def test_get_long_invalid(make_request_json_response):
    long_null_dict = {"0":1, "1":None, "2":0}
    request = dictionary.build_get_long_invalid_null_request()
    assert long_null_dict == make_request_json_response(request)

    request = dictionary.build_get_long_invalid_string_request()
    assert {"0": 1, "1": "integer", "2": 0} == make_request_json_response(request)

def test_float_valid(make_request, make_request_json_response):
    float_valid = {"0":0, "1":-0.01, "2":-1.2e20}
    request = dictionary.build_get_float_valid_request()
    assert float_valid == make_request_json_response(request)

    request = dictionary.build_put_float_valid_request(json=float_valid)
    make_request(request)

def test_get_float_invalid(make_request_json_response):
    float_null_dict = {"0":0.0, "1":None, "2":-1.2e20}
    request = dictionary.build_get_float_invalid_null_request()
    assert float_null_dict == make_request_json_response(request)

    request = dictionary.build_get_float_invalid_string_request()
    assert {"0": 1, "1": "number", "2": 0} == make_request_json_response(request)

def test_double_valid(make_request, make_request_json_response):
    double_valid = {"0":0, "1":-0.01, "2":-1.2e20}
    request = dictionary.build_get_double_valid_request()
    assert double_valid == make_request_json_response(request)

    request = dictionary.build_put_double_valid_request(json=double_valid)
    make_request(request)

def test_get_double_invalid(make_request_json_response):
    double_null_dict = {"0":0.0, "1":None, "2":-1.2e20}
    request = dictionary.build_get_double_invalid_null_request()
    assert double_null_dict == make_request_json_response(request)

    request = dictionary.build_get_double_invalid_string_request()
    assert {"0": 1, "1": "number", "2": 0} == make_request_json_response(request)

def test_string_valid(make_request, make_request_json_response):
    string_valid = {"0":"foo1", "1":"foo2", "2":"foo3"}
    request = dictionary.build_get_string_valid_request()
    assert string_valid == make_request_json_response(request)

    request = dictionary.build_put_string_valid_request(json=string_valid)
    make_request(request)

def test_get_string_with_null_and_invalid(make_request_json_response):
    string_null_dict = {"0":"foo", "1":None, "2":"foo2"}
    string_invalid_dict = {"0":"foo", "1":123, "2":"foo2"}  # in llc, we don't know we should serialize this whole thing as string, so serializes 123 as number
    request = dictionary.build_get_string_with_null_request()
    assert string_null_dict == make_request_json_response(request)
    request = dictionary.build_get_string_with_invalid_request()
    assert string_invalid_dict == make_request_json_response(request)

def test_date_valid(make_request, get_serialized_dict, get_deserialized_dict, msrest_serializer, msrest_deserializer):
    date1 = isodate.parse_date("2000-12-01T00:00:00Z")
    date2 = isodate.parse_date("1980-01-02T00:00:00Z")
    date3 = isodate.parse_date("1492-10-12T00:00:00Z")
    valid_date_dict = {"0":date1, "1":date2, "2":date3}

    request = dictionary.build_get_date_valid_request()
    assert get_deserialized_dict(request, msrest_deserializer.deserialize_date) ==  valid_date_dict

    request = dictionary.build_put_date_valid_request(json=get_serialized_dict(valid_date_dict, msrest_serializer.serialize_date))
    make_request(request)

def test_get_date_invalid(make_request_json_response, msrest_deserializer, get_deserialized_dict):
    date_null_dict = {"0":isodate.parse_date("2012-01-01"),
                        "1":None,
                        "2":isodate.parse_date("1776-07-04")}
    request = dictionary.build_get_date_invalid_null_request()
    assert date_null_dict == get_deserialized_dict(request, msrest_deserializer.deserialize_date)

    request = dictionary.build_get_date_invalid_chars_request()
    assert {"0": "2011-03-22", "1": "date"} == make_request_json_response(request)

def test_date_time_valid(make_request, get_deserialized_dict, get_serialized_dict, msrest_serializer, msrest_deserializer):
    datetime1 = isodate.parse_datetime("2000-12-01T00:00:01Z")
    datetime2 = isodate.parse_datetime("1980-01-02T00:11:35+01:00")
    datetime3 = isodate.parse_datetime("1492-10-12T10:15:01-08:00")
    valid_datetime_dict = {"0":datetime1, "1":datetime2, "2":datetime3}

    request = dictionary.build_get_date_time_valid_request()
    assert valid_datetime_dict == get_deserialized_dict(request, msrest_deserializer.deserialize_iso)

    request = dictionary.build_put_date_time_valid_request(
        json=get_serialized_dict(valid_datetime_dict, msrest_serializer.serialize_iso)
    )
    make_request(request)

def test_get_date_time_invalid(make_request_json_response, msrest_deserializer, get_deserialized_dict):
    datetime_null_dict = {"0":isodate.parse_datetime("2000-12-01T00:00:01Z"), "1":None}
    request = dictionary.build_get_date_time_invalid_null_request()
    assert datetime_null_dict == get_deserialized_dict(request, msrest_deserializer.deserialize_iso)

    request = dictionary.build_get_date_time_invalid_chars_request()
    assert {"0": "2000-12-01t00:00:01z", "1": "date-time"} == make_request_json_response(request)

def test_date_time_rfc1123_valid(make_request, get_deserialized_dict, get_serialized_dict, msrest_serializer, msrest_deserializer):
    rfc_datetime1 = isodate.parse_datetime("2000-12-01T00:00:01Z")
    rfc_datetime2 = isodate.parse_datetime("1980-01-02T00:11:35Z")
    rfc_datetime3 = isodate.parse_datetime("1492-10-12T10:15:01Z")
    valid_rfc_dict = {"0":rfc_datetime1, "1":rfc_datetime2, "2":rfc_datetime3}

    request = dictionary.build_get_date_time_rfc1123_valid_request()
    assert valid_rfc_dict == get_deserialized_dict(request, msrest_deserializer.deserialize_rfc)

    request = dictionary.build_put_date_time_rfc1123_valid_request(json=get_serialized_dict(valid_rfc_dict, msrest_serializer.serialize_rfc))
    make_request(request)

def test_get_duration_valid(make_request, msrest_serializer, msrest_deserializer, get_deserialized_dict, get_serialized_dict):
    duration1 = timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)
    duration2 = timedelta(days=5, hours=1)
    valid_duration_dict = {"0":duration1, "1":duration2}

    request = dictionary.build_get_duration_valid_request()
    assert valid_duration_dict == get_deserialized_dict(request, msrest_deserializer.deserialize_duration)

    request = dictionary.build_put_duration_valid_request(json=get_serialized_dict(valid_duration_dict, msrest_serializer.serialize_duration))
    make_request(request)

def test_bytes_valid(make_request, msrest_serializer, msrest_deserializer, get_serialized_dict, get_deserialized_dict):
    bytes1 = bytearray([0x0FF, 0x0FF, 0x0FF, 0x0FA])
    bytes2 = bytearray([0x01, 0x02, 0x03])
    bytes3 = bytearray([0x025, 0x029, 0x043])
    bytes4 = bytearray([0x0AB, 0x0AC, 0x0AD])

    bytes_valid = {"0":bytes1, "1":bytes2, "2":bytes3}
    request = dictionary.build_put_byte_valid_request(json=get_serialized_dict(bytes_valid, msrest_serializer.serialize_bytearray))
    make_request(request)

    request = dictionary.build_get_byte_valid_request()
    assert bytes_valid == get_deserialized_dict(request, msrest_deserializer.deserialize_bytearray)

def test_get_byte_invalid_null(msrest_deserializer, get_deserialized_dict):
    bytes4 = bytearray([0x0AB, 0x0AC, 0x0AD])
    bytes_null = {"0":bytes4, "1":None}
    request = dictionary.build_get_byte_invalid_null_request()
    assert bytes_null == get_deserialized_dict(request, msrest_deserializer.deserialize_bytearray)
def test_get_base64_url(msrest_deserializer, get_deserialized_dict):
    test_dict = {'0': 'a string that gets encoded with base64url'.encode(),
                    '1': 'test string'.encode(),
                    '2': 'Lorem ipsum'.encode()}
    request = dictionary.build_get_base64_url_request()
    assert test_dict == get_deserialized_dict(request, msrest_deserializer.deserialize_base64)

# Basic dictionary parsing
def test_empty(make_request, make_request_json_response):

    request = dictionary.build_get_empty_request()
    assert {} == make_request_json_response(request)

    request = dictionary.build_put_empty_request(json={})
    make_request(request)

def test_get_null_and_invalid(make_request, make_request_json_response):

    request = dictionary.build_get_null_request()
    assert make_request(request).text == ''

    request = dictionary.build_get_invalid_request()
    with pytest.raises(json.decoder.JSONDecodeError):
        make_request_json_response(request)

def test_get_null_key_and_value(make_request, make_request_json_response):
    # {null:"val1"} is not standard JSON format. C# might work and expects this test to pass,
    # but we fail and we're happy with it.
    request = dictionary.build_get_null_key_request()
    with pytest.raises(json.decoder.JSONDecodeError):
        make_request_json_response(request)

    request = dictionary.build_get_null_value_request()
    assert {"key1":None} == make_request_json_response(request)

def test_get_empty_string_key(make_request_json_response):
    request = dictionary.build_get_empty_string_key_request()
    assert {"":"val1"} == make_request_json_response(request)

def test_complex_valid(make_request, make_request_json_response, test_dict):

    request = dictionary.build_put_complex_valid_request(json=test_dict)
    make_request(request)

    request = dictionary.build_get_complex_valid_request()
    assert test_dict ==  make_request_json_response(request)

def test_array_valid(make_request, make_request_json_response):
    list_dict = {"0":["1","2","3"], "1":["4","5","6"], "2":["7","8","9"]}

    request = dictionary.build_put_array_valid_request(json=list_dict)
    make_request(request)

    request = dictionary.build_get_array_valid_request()
    assert list_dict == make_request_json_response(request)

def test_dictionary_valid(make_request, make_request_json_response):
    dict_dict = {"0":{"1":"one","2":"two","3":"three"},
                    "1":{"4":"four","5":"five","6":"six"},
                    "2":{"7":"seven","8":"eight","9":"nine"}}

    request = dictionary.build_put_dictionary_valid_request(json=dict_dict)
    make_request(request)

    request = dictionary.build_get_dictionary_valid_request()
    assert dict_dict == make_request_json_response(request)

def test_get_complex_null_and_empty(make_request, make_request_json_response):

    request = dictionary.build_get_complex_null_request()
    assert make_request(request).text == ''

    request = dictionary.build_get_complex_empty_request()
    assert {} == make_request_json_response(request)

def test_get_complex_item_null_and_empty(make_request_json_response, test_dict):
    test_dict_null = {"0":test_dict["0"], "1":None, "2":test_dict["2"]}

    request = dictionary.build_get_complex_item_null_request()
    assert test_dict_null == make_request_json_response(request)

    test_dict_empty = {"0":test_dict["0"], "1":Widget().serialize(), "2":test_dict["2"]}

    request = dictionary.build_get_complex_item_empty_request()
    assert make_request_json_response(request) ==  test_dict_empty

def test_get_array_empty(make_request, make_request_json_response):
    request = dictionary.build_get_array_null_request()
    assert make_request(request).text == ''

    request = dictionary.build_get_array_empty_request()
    assert {} == make_request_json_response(request)

def test_get_array_item_null_and_empty(make_request_json_response):
    list_dict = {"0":["1","2","3"], "1":None, "2":["7","8","9"]}
    request = dictionary.build_get_array_item_null_request()
    assert list_dict == make_request_json_response(request)

    # in convenience layer, we deserialize as {[str]}. Since we don't have that in llc, the value for "1" will be None, not an empty list
    list_dict = {"0":["1","2","3"], "1":None, "2":["7","8","9"]}
    assert list_dict == make_request_json_response(request)

def test_get_dictionary_null_and_empty(make_request, make_request_json_response):
    request = dictionary.build_get_dictionary_null_request()
    assert make_request(request).text == ''

    request = dictionary.build_get_dictionary_empty_request()
    assert {} == make_request_json_response(request)

def test_get_dictionary_item_null_and_empty(make_request, make_request_json_response):
    dict_dict = {"0":{"1":"one","2":"two","3":"three"},
                    "1":None,
                    "2":{"7":"seven","8":"eight","9":"nine"}}
    request = dictionary.build_get_dictionary_item_null_request()
    assert dict_dict == make_request_json_response(request)

    dict_dict = {"0":{"1":"one","2":"two","3":"three"},
                    "1":{},
                    "2":{"7":"seven","8":"eight","9":"nine"}}
    request = dictionary.build_get_dictionary_item_empty_request()
    assert dict_dict == make_request_json_response(request)
