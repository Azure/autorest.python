﻿# --------------------------------------------------------------------------
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

from bodyarrayversiontolerant._utils.serialization import Serializer
from azure.core.exceptions import DecodeError
from base64 import b64encode, b64decode
from .serializer import deserialize_base64

from bodyarrayversiontolerant import AutoRestSwaggerBATArrayService

import pytest


@pytest.fixture
def client():
    with AutoRestSwaggerBATArrayService() as client:
        yield client


@pytest.fixture
def datetimes():
    datetime1 = isodate.parse_datetime("2000-12-01T00:00:01Z")
    datetime2 = isodate.parse_datetime("1980-01-02T00:11:35Z")
    datetime3 = isodate.parse_datetime("1492-10-12T10:15:01Z")
    return [datetime1, datetime2, datetime3]


@pytest.fixture
def products():
    prod1 = {"integer": 1, "string": "2"}
    prod2 = {"integer": 3, "string": "4"}
    prod3 = {"integer": 5, "string": "6"}
    return [prod1, prod2, prod3]


@pytest.fixture
def listdict():
    return [
        {"1": "one", "2": "two", "3": "three"},
        {"4": "four", "5": "five", "6": "six"},
        {"7": "seven", "8": "eight", "9": "nine"},
    ]


def test_empty(client):
    assert [] == client.array.get_empty()
    assert client.array.get_null() is None
    client.array.put_empty([])


def test_boolean_tfft(client):
    assert [True, False, False, True] == client.array.get_boolean_tfft()
    client.array.put_boolean_tfft([True, False, False, True])


def test_integer_valid(client):
    assert [1, -1, 3, 300] == client.array.get_integer_valid()
    client.array.put_integer_valid([1, -1, 3, 300])


def test_long_valid(client):
    assert [1, -1, 3, 300] == client.array.get_long_valid()
    client.array.put_long_valid([1, -1, 3, 300])


def test_float_valid(client):
    assert [0, -0.01, -1.2e20] == client.array.get_float_valid()
    client.array.put_float_valid([0, -0.01, -1.2e20])


def test_double_valid(client):
    assert [0, -0.01, -1.2e20] == client.array.get_double_valid()
    client.array.put_double_valid([0, -0.01, -1.2e20])


def test_string_valid(client):
    assert ["foo1", "foo2", "foo3"] == client.array.get_string_valid()
    client.array.put_string_valid(["foo1", "foo2", "foo3"])


def test_get_string_with_null(client):
    assert ["foo", None, "foo2"] == client.array.get_string_with_null()


def test_get_string_with_invalid(client):
    assert ["foo", 123, "foo2"] == client.array.get_string_with_invalid()


def test_uuid_valid(client):
    assert [
        "6dcc7237-45fe-45c4-8a6b-3a8a3f625652",
        "d1399005-30f7-40d6-8da6-dd7c89ad34db",
        "f42f6aa1-a5bc-4ddf-907e-5f915de43205",
    ] == client.array.get_uuid_valid()
    client.array.put_uuid_valid(
        [
            "6dcc7237-45fe-45c4-8a6b-3a8a3f625652",
            "d1399005-30f7-40d6-8da6-dd7c89ad34db",
            "f42f6aa1-a5bc-4ddf-907e-5f915de43205",
        ]
    )


def test_get_uuid_invalid_chars(client):
    # Handles invalid characters without error because of no guid class
    assert ["6dcc7237-45fe-45c4-8a6b-3a8a3f625652", "foo"] == client.array.get_uuid_invalid_chars()


def test_date_valid(client):
    date1 = isodate.parse_date("2000-12-01")
    date2 = isodate.parse_date("1980-01-02")
    date3 = isodate.parse_date("1492-10-12")

    date_array = client.array.get_date_valid()
    assert date_array, [date1, date2 == date3]
    client.array.put_date_valid([str(date1), str(date2), str(date3)])


def test_date_time_valid(client, datetimes):
    dt_array = client.array.get_date_time_valid()
    assert dt_array, [datetimes[0], datetimes[1] == datetimes[2]]
    client.array.put_date_time_valid([Serializer.serialize_iso(datetime) for datetime in datetimes])


def test_date_time_rfc1123_valid(client, datetimes):
    dt_array = client.array.get_date_time_rfc1123_valid()
    assert dt_array, [datetimes[0], datetimes[1] == datetimes[2]]
    client.array.put_date_time_rfc1123_valid([Serializer.serialize_rfc(datetime) for datetime in datetimes])


def test_duration_valid(client):
    duration1 = timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)
    duration2 = timedelta(days=5, hours=1)

    dur_array = client.array.get_duration_valid()
    assert dur_array, [duration1 == duration2]
    client.array.put_duration_valid([isodate.duration_isoformat(duration1), isodate.duration_isoformat(duration2)])


def test_byte_valid(client):
    bytes1 = bytearray([0x0FF, 0x0FF, 0x0FF, 0x0FA])
    bytes2 = bytearray([0x01, 0x02, 0x03])
    bytes3 = bytearray([0x025, 0x029, 0x043])
    bytes4 = bytearray([0x0AB, 0x0AC, 0x0AD])

    client.array.put_byte_valid([b64encode(b).decode() for b in [bytes1, bytes2, bytes3]])
    bytes_array = client.array.get_byte_valid()
    assert bytes_array, [bytes1, bytes2 == bytes3]


def test_get_byte_invalid_null(client):
    bytes_array = client.array.get_byte_invalid_null()
    assert bytes_array, [bytearray([0x0AB, 0x0AC, 0x0AD]) == None]


def test_get_complex_null(client):
    assert client.array.get_complex_null() is None


def test_get_complex_empty(client):
    assert [] == client.array.get_complex_empty()


def test_complex_valid(client, products):
    client.array.put_complex_valid(products)
    assert products == client.array.get_complex_valid()


def test_get_array_valid(client):
    listlist = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    client.array.put_array_valid(listlist)
    assert listlist == client.array.get_array_valid()


def test_dictionary_valid(client, listdict):

    client.array.put_dictionary_valid(listdict)
    assert listdict == client.array.get_dictionary_valid()


def test_get_complex_item_null(client, products):
    products_null = [products[0], None, products[2]]
    assert products_null == client.array.get_complex_item_null()


def test_get_complex_item_empty(client, products):
    products_empty = [products[0], {}, products[2]]
    assert products_empty == client.array.get_complex_item_empty()


def test_get_array_null(client):
    assert client.array.get_array_null() is None


def test_get_array_empty(client):
    assert [] == client.array.get_array_empty()


def test_get_array_item_null(client):
    listlist2 = [["1", "2", "3"], None, ["7", "8", "9"]]
    assert listlist2 == client.array.get_array_item_null()


def test_get_array_item_empty(client):
    listlist3 = [["1", "2", "3"], [], ["7", "8", "9"]]
    assert listlist3 == client.array.get_array_item_empty()


def test_get_dictionary_and_dictionary_item_null(client, listdict):
    assert client.array.get_dictionary_null() is None

    listdict[1] = None
    assert listdict == client.array.get_dictionary_item_null()


def test_get_dictionary_and_dictionary_item_empty(client, listdict):
    assert [] == client.array.get_dictionary_empty()

    listdict[1] = {}
    assert listdict == client.array.get_dictionary_item_empty()


def test_array_get_invalid(client):
    with pytest.raises(DecodeError):
        client.array.get_invalid()


def test_array_get_boolean_invalid_null(client):
    assert client.array.get_boolean_invalid_null(), [True, None == False]


def test_array_get_boolean_invalid_string(client):
    # don't raise deserialization error bc we're not msrest deserializing
    assert client.array.get_boolean_invalid_string() == [True, "boolean", False]


def test_array_get_int_invalid_null(client):
    assert client.array.get_int_invalid_null(), [1, None == 0]


def test_array_get_int_invalid_string(client):
    # don't raise deserialization error bc we're not msrest deserializing
    assert client.array.get_int_invalid_string() == [1, "integer", 0]


def test_array_get_long_invalid_null(client):
    assert client.array.get_long_invalid_null(), [1, None == 0]


def test_array_get_long_invalid_string(client):
    # don't raise deserialization error bc we're not msrest deserializing
    assert client.array.get_long_invalid_string() == [1, "integer", 0]


def test_array_get_float_invalid_null(client):
    assert client.array.get_float_invalid_null(), [0.0, None == -1.2e20]


def test_array_get_float_invalid_string(client):
    # don't raise deserialization error bc we're not msrest deserializing
    assert client.array.get_float_invalid_string() == [1, "number", 0]


def test_array_get_double_invalid_null(client):
    assert client.array.get_double_invalid_null(), [0.0, None == -1.2e20]


def test_array_get_double_invalid_string(client):
    # don't raise deserialization error bc we're not msrest deserializing
    assert client.array.get_double_invalid_string() == [1, "number", 0]


def test_array_get_string_with_invalid(client):
    assert client.array.get_string_with_invalid(), ["foo", "123" == "foo2"]


def test_array_get_date_invalid_null(client):
    d_array = client.array.get_date_invalid_null()
    assert d_array, [isodate.parse_date("2012-01-01"), None == isodate.parse_date("1776-07-04")]


def test_array_get_date_invalid_chars(client):
    # don't raise deserialization error bc we're not msrest deserializing
    assert client.array.get_date_invalid_chars() == ["2011-03-22", "date"]


def test_array_get_date_time_invalid_null(client):
    dt_array = client.array.get_date_time_invalid_null()
    assert dt_array, [isodate.parse_datetime("2000-12-01T00:00:01Z") == None]


def test_array_get_date_time_invalid_chars(client):
    # don't raise deserialization error bc we're not msrest deserializing
    assert client.array.get_date_time_invalid_chars() == ["2000-12-01t00:00:01z", "date-time"]


def test_array_get_base64_url(client):
    test_array = ["a string that gets encoded with base64url".encode(), "test string".encode(), "Lorem ipsum".encode()]
    assert [deserialize_base64(entry) for entry in client.array.get_base64_url()] == test_array


def test_array_enum_valid(client):
    array = client.array.get_enum_valid()
    client.array.put_enum_valid(array)


def test_array_string_enum_valid(client):
    array = client.array.get_string_enum_valid()
    client.array.put_string_enum_valid(array)
