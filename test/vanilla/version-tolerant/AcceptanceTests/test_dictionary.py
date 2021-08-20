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
from datetime import timedelta
from azure.core.exceptions import DecodeError
from .serializer import (
    deserialize_base64,
    deserialize_bytearray,
    deserialize_iso,
    serialize_bytearray,
    deserialize_date,
    serialize_date,
    deserialize_duration,
    deserialize_datetime,
    serialize_duration,
    deserialize_rfc,
    serialize_iso,
    serialize_rfc,
)

from bodydictionaryversiontolerant import AutoRestSwaggerBATDictionaryService

import pytest

@pytest.fixture
def client():
    with AutoRestSwaggerBATDictionaryService() as client:
        yield client

@pytest.fixture
def test_dict():
    test_product1 = {"integer": 1, "string": "2"}
    test_product2 = {"integer": 3, "string": "4"}
    test_product3 = {"integer": 5, "string": "6"}
    return {"0":test_product1, "1":test_product2, "2":test_product3}

def get_deserialized_dict(response, deserializer):
    return {
        str(idx): deserializer(response[key]) if response[key] else None
        for idx, key in enumerate(response.keys())
    }

def get_serialized_dict(dict, serializer):
    return {
        k: serializer(v) for k, v in dict.items()
    }

# Primitive types
def test_boolean_tfft(client):
    tfft = {"0":True, "1":False, "2":False, "3":True}
    assert tfft ==  client.dictionary.get_boolean_tfft()

    client.dictionary.put_boolean_tfft(tfft)

def test_get_boolean_invalid(client):
    invalid_null_dict = {"0":True, "1":None, "2":False}
    assert invalid_null_dict ==  client.dictionary.get_boolean_invalid_null()

    assert {"0": True, "1": "boolean", "2": False} == client.dictionary.get_boolean_invalid_string()

def test_integer_valid(client):
    int_valid = {"0":1, "1":-1, "2":3, "3":300}
    assert int_valid ==  client.dictionary.get_integer_valid()

    client.dictionary.put_integer_valid(int_valid)

def test_get_int_invalid(client):
    int_null_dict = {"0":1, "1":None, "2":0}
    assert int_null_dict ==  client.dictionary.get_int_invalid_null()

    assert {"0": 1, "1": "integer", "2": 0} == client.dictionary.get_int_invalid_string()

def test_long_valid(client):
    long_valid = {"0":1, "1":-1, "2":3, "3":300}
    assert long_valid ==  client.dictionary.get_long_valid()

    client.dictionary.put_long_valid(long_valid)

def test_get_long_invalid(client):
    long_null_dict = {"0":1, "1":None, "2":0}
    assert long_null_dict ==  client.dictionary.get_long_invalid_null()

    assert {"0": 1, "1": "integer", "2": 0} == client.dictionary.get_long_invalid_string()

def test_float_valid(client):
    float_valid = {"0":0, "1":-0.01, "2":-1.2e20}
    assert float_valid ==  client.dictionary.get_float_valid()

    client.dictionary.put_float_valid(float_valid)

def test_get_float_invalid(client):
    float_null_dict = {"0":0.0, "1":None, "2":-1.2e20}
    assert float_null_dict ==  client.dictionary.get_float_invalid_null()

    assert {"0": 1, "1": "number", "2": 0} == client.dictionary.get_float_invalid_string()

def test_double_valid(client):
    double_valid = {"0":0, "1":-0.01, "2":-1.2e20}
    assert double_valid ==  client.dictionary.get_double_valid()

    client.dictionary.put_double_valid(double_valid)

def test_get_double_invalid(client):
    double_null_dict = {"0":0.0, "1":None, "2":-1.2e20}
    assert double_null_dict ==  client.dictionary.get_double_invalid_null()

    assert {"0": 1, "1": "number", "2": 0} == client.dictionary.get_double_invalid_string()

def test_string_valid(client):
    string_valid = {"0":"foo1", "1":"foo2", "2":"foo3"}
    assert string_valid ==  client.dictionary.get_string_valid()

    client.dictionary.put_string_valid(string_valid)

def test_get_string_with_null_and_invalid(client):
    string_null_dict = {"0":"foo", "1":None, "2":"foo2"}
    string_invalid_dict = {"0":"foo", "1":123, "2":"foo2"}  # in version-tolerant, we don't know we should serialize this whole thing as string, so serializes 123 as number
    assert string_null_dict ==  client.dictionary.get_string_with_null()
    assert string_invalid_dict ==  client.dictionary.get_string_with_invalid()

def test_date_valid(client):
    date1 = deserialize_date("2000-12-01T00:00:00Z")
    date2 = deserialize_date("1980-01-02T00:00:00Z")
    date3 = deserialize_date("1492-10-12T00:00:00Z")
    valid_date_dict = {"0":date1, "1":date2, "2":date3}

    date_dictionary = client.dictionary.get_date_valid()
    assert get_deserialized_dict(date_dictionary, deserialize_date) == valid_date_dict

    client.dictionary.put_date_valid(get_serialized_dict(valid_date_dict, serialize_date))

def test_get_date_invalid(client):
    date_null_dict = {"0":deserialize_date("2012-01-01"),
                        "1":None,
                        "2":deserialize_date("1776-07-04")}
    assert date_null_dict == get_deserialized_dict(client.dictionary.get_date_invalid_null(), deserialize_date)

    assert {"0": "2011-03-22", "1": "date"} == client.dictionary.get_date_invalid_chars()

def test_date_time_valid(client):
    datetime1 = deserialize_datetime("2000-12-01T00:00:01Z")
    datetime2 = deserialize_datetime("1980-01-02T00:11:35+01:00")
    datetime3 = deserialize_datetime("1492-10-12T10:15:01-08:00")
    valid_datetime_dict = {"0":datetime1, "1":datetime2, "2":datetime3}

    assert valid_datetime_dict == get_deserialized_dict(client.dictionary.get_date_time_valid(), deserialize_iso)

    client.dictionary.put_date_time_valid(get_serialized_dict(valid_datetime_dict, serialize_iso))

def test_get_date_time_invalid(client):
    datetime_null_dict = {"0":deserialize_datetime("2000-12-01T00:00:01Z"), "1":None}
    assert datetime_null_dict == get_deserialized_dict(client.dictionary.get_date_time_invalid_null(), deserialize_iso)

    assert {"0": "2000-12-01t00:00:01z", "1": "date-time"} == client.dictionary.get_date_time_invalid_chars()

def test_date_time_rfc1123_valid(client):
    rfc_datetime1 = deserialize_datetime("2000-12-01T00:00:01Z")
    rfc_datetime2 = deserialize_datetime("1980-01-02T00:11:35Z")
    rfc_datetime3 = deserialize_datetime("1492-10-12T10:15:01Z")
    valid_rfc_dict = {"0":rfc_datetime1, "1":rfc_datetime2, "2":rfc_datetime3}

    assert valid_rfc_dict == get_deserialized_dict(client.dictionary.get_date_time_rfc1123_valid(), deserialize_rfc)

    client.dictionary.put_date_time_rfc1123_valid(get_serialized_dict(valid_rfc_dict, serialize_rfc))

def test_get_duration_valid(client):
    duration1 = timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)
    duration2 = timedelta(days=5, hours=1)
    valid_duration_dict = {"0":duration1, "1":duration2}

    assert valid_duration_dict == get_deserialized_dict(client.dictionary.get_duration_valid(), deserialize_duration)

    client.dictionary.put_duration_valid(get_serialized_dict(valid_duration_dict, serialize_duration))

def test_bytes_valid(client):
    bytes1 = bytearray([0x0FF, 0x0FF, 0x0FF, 0x0FA])
    bytes2 = bytearray([0x01, 0x02, 0x03])
    bytes3 = bytearray([0x025, 0x029, 0x043])
    bytes4 = bytearray([0x0AB, 0x0AC, 0x0AD])

    bytes_valid = {"0":bytes1, "1":bytes2, "2":bytes3}
    client.dictionary.put_byte_valid(get_serialized_dict(bytes_valid, serialize_bytearray))

    bytes_result = client.dictionary.get_byte_valid()
    assert bytes_valid == get_deserialized_dict(bytes_result, deserialize_bytearray)

def test_get_byte_invalid_null(client):
    bytes4 = bytearray([0x0AB, 0x0AC, 0x0AD])
    bytes_null = {"0":bytes4, "1":None}
    bytes_result = get_deserialized_dict(client.dictionary.get_byte_invalid_null(), deserialize_bytearray)
    assert bytes_null ==  bytes_result

def test_get_base64_url(client):
    test_dict = {'0': 'a string that gets encoded with base64url'.encode(),
                    '1': 'test string'.encode(),
                    '2': 'Lorem ipsum'.encode()}
    assert get_deserialized_dict(client.dictionary.get_base64_url(), deserialize_base64) ==  test_dict

# Basic dictionary parsing
def test_empty(client):

    assert {} ==  client.dictionary.get_empty()

    client.dictionary.put_empty({})

def test_get_null_and_invalid(client):
    assert client.dictionary.get_null() is None

    with pytest.raises(DecodeError):
        client.dictionary.get_invalid()

def test_get_null_key_and_value(client):
    # {null:"val1"} is not standard JSON format. C# might work and expects this test to pass,
    # but we fail and we're happy with it.
    with pytest.raises(DecodeError):
        client.dictionary.get_null_key()
    assert {"key1":None} ==  client.dictionary.get_null_value()

def test_get_empty_string_key(client):
    assert {"":"val1"} ==  client.dictionary.get_empty_string_key()

# Dictionary composed types
def test_get_complex_null_and_empty(client):
    assert client.dictionary.get_complex_null() is None
    assert {} ==  client.dictionary.get_complex_empty()

def test_complex_valid(client, test_dict):

    client.dictionary.put_complex_valid(test_dict)
    complex_result = client.dictionary.get_complex_valid()
    assert test_dict ==  complex_result

def test_array_valid(client):
    list_dict = {"0":["1","2","3"], "1":["4","5","6"], "2":["7","8","9"]}
    client.dictionary.put_array_valid(list_dict)

    array_result = client.dictionary.get_array_valid()
    assert list_dict ==  array_result

def test_dictionary_valid(client):
    dict_dict = {"0":{"1":"one","2":"two","3":"three"},
                    "1":{"4":"four","5":"five","6":"six"},
                    "2":{"7":"seven","8":"eight","9":"nine"}}
    client.dictionary.put_dictionary_valid(dict_dict)

    dict_result = client.dictionary.get_dictionary_valid()
    assert dict_dict ==  dict_result

def test_get_complex_null_and_empty(client):
    assert client.dictionary.get_complex_null() is None
    assert {} ==  client.dictionary.get_complex_empty()

def test_get_complex_item_null_and_empty(client, test_dict):
    test_dict_null = {"0":test_dict["0"], "1":None, "2":test_dict["2"]}
    complex_result = client.dictionary.get_complex_item_null()
    assert complex_result ==  test_dict_null

    test_dict_empty = {"0":test_dict["0"], "1": {}, "2":test_dict["2"]}
    complex_result = client.dictionary.get_complex_item_empty()
    assert complex_result ==  test_dict_empty

def test_get_array_empty(client):
    assert client.dictionary.get_array_null() is None
    assert {} ==  client.dictionary.get_array_empty()

def test_get_array_item_null_and_empty(client):
    list_dict = {"0":["1","2","3"], "1":None, "2":["7","8","9"]}
    array_result = client.dictionary.get_array_item_null()
    assert list_dict ==  array_result

    list_dict = {"0":["1","2","3"], "1":[], "2":["7","8","9"]}
    array_result = client.dictionary.get_array_item_empty()
    assert list_dict ==  array_result

def test_get_dictionary_null_and_empty(client):
    assert client.dictionary.get_dictionary_null() is None
    assert {} ==  client.dictionary.get_dictionary_empty()

def test_get_dictionary_item_null_and_empty(client):
    dict_dict = {"0":{"1":"one","2":"two","3":"three"},
                    "1":None,
                    "2":{"7":"seven","8":"eight","9":"nine"}}
    dict_result = client.dictionary.get_dictionary_item_null()
    assert dict_dict ==  dict_result

    dict_dict = {"0":{"1":"one","2":"two","3":"three"},
                    "1":{},
                    "2":{"7":"seven","8":"eight","9":"nine"}}
    dict_result = client.dictionary.get_dictionary_item_empty()
    assert dict_dict ==  dict_result
