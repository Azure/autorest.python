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

import unittest
import subprocess
import sys
import isodate
import os
from datetime import date, datetime, timedelta
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "BodyDictionary"))

from azure.core.exceptions import DecodeError
from msrest.exceptions import DeserializationError

<<<<<<< HEAD
from bodydictionary.aio import AutoRestSwaggerBATdictionaryService
from bodydictionary.models import Widget
=======
from bodydictionary.aio import AutoRestSwaggerBATDictionaryService
from bodydictionary.models import Widget, ErrorException
>>>>>>> aa990ad77f6dee34ee63b4f51a9a98a76ffe8d88

import pytest

@pytest.fixture
async def client():
    async with AutoRestSwaggerBATDictionaryService(base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def test_dict():
    test_product1 = Widget(integer=1, string="2")
    test_product2 = Widget(integer=3, string="4")
    test_product3 = Widget(integer=5, string="6")
    return {"0":test_product1, "1":test_product2, "2":test_product3}

class TestDictionary(object):

    # Primitive types

    @pytest.mark.asyncio
    async def test_boolean_tfft(self, client):
        tfft = {"0":True, "1":False, "2":False, "3":True}
        assert tfft ==  (await client.dictionary.get_boolean_tfft())

        await client.dictionary.put_boolean_tfft(tfft)

    @pytest.mark.asyncio
    async def test_get_boolean_invalid(self, client):
        invalid_null_dict = {"0":True, "1":None, "2":False}
        assert invalid_null_dict ==  (await client.dictionary.get_boolean_invalid_null())

        with pytest.raises(DeserializationError):
            await client.dictionary.get_boolean_invalid_string()

    @pytest.mark.asyncio
    async def test_integer_valid(self, client):
        int_valid = {"0":1, "1":-1, "2":3, "3":300}
        assert int_valid ==  (await client.dictionary.get_integer_valid())

        await client.dictionary.put_integer_valid(int_valid)

    @pytest.mark.asyncio
    async def test_get_int_invalid(self, client):
        int_null_dict = {"0":1, "1":None, "2":0}
        assert int_null_dict ==  (await client.dictionary.get_int_invalid_null())

        with pytest.raises(DeserializationError):
            await client.dictionary.get_int_invalid_string()

    @pytest.mark.asyncio
    async def test_long_valid(self, client):
        long_valid = {"0":1, "1":-1, "2":3, "3":300}
        assert long_valid ==  (await client.dictionary.get_long_valid())

        await client.dictionary.put_long_valid(long_valid)

    @pytest.mark.asyncio
    async def test_get_long_invalid(self, client):
        long_null_dict = {"0":1, "1":None, "2":0}
        assert long_null_dict ==  (await client.dictionary.get_long_invalid_null())

        with pytest.raises(DeserializationError):
            await client.dictionary.get_long_invalid_string()

    @pytest.mark.asyncio
    async def test_float_valid(self, client):
        float_valid = {"0":0, "1":-0.01, "2":-1.2e20}
        assert float_valid ==  (await client.dictionary.get_float_valid())

        await client.dictionary.put_float_valid(float_valid)

    @pytest.mark.asyncio
    async def test_get_float_invalid(self, client):
        float_null_dict = {"0":0.0, "1":None, "2":-1.2e20}
        assert float_null_dict ==  (await client.dictionary.get_float_invalid_null())

        with pytest.raises(DeserializationError):
            await client.dictionary.get_float_invalid_string()

    @pytest.mark.asyncio
    async def test_double_valid(self, client):
        double_valid = {"0":0, "1":-0.01, "2":-1.2e20}
        assert double_valid ==  (await client.dictionary.get_double_valid())

        await client.dictionary.put_double_valid(double_valid)

    @pytest.mark.asyncio
    async def test_get_double_invalid(self, client):
        double_null_dict = {"0":0.0, "1":None, "2":-1.2e20}
        assert double_null_dict ==  (await client.dictionary.get_double_invalid_null())

        with pytest.raises(DeserializationError):
            await client.dictionary.get_double_invalid_string()

    @pytest.mark.asyncio
    async def test_string_valid(self, client):
        string_valid = {"0":"foo1", "1":"foo2", "2":"foo3"}
        assert string_valid ==  (await client.dictionary.get_string_valid())

        await client.dictionary.put_string_valid(string_valid)

    @pytest.mark.asyncio
    async def test_get_string_with_null_and_invalid(self, client):
        string_null_dict = {"0":"foo", "1":None, "2":"foo2"}
        string_invalid_dict = {"0":"foo", "1":"123", "2":"foo2"}
        assert string_null_dict ==  (await client.dictionary.get_string_with_null())
        assert string_invalid_dict ==  (await client.dictionary.get_string_with_invalid())

    @pytest.mark.asyncio
    async def test_date_valid(self, client):
        date1 = isodate.parse_date("2000-12-01T00:00:00Z")
        date2 = isodate.parse_date("1980-01-02T00:00:00Z")
        date3 = isodate.parse_date("1492-10-12T00:00:00Z")
        valid_date_dict = {"0":date1, "1":date2, "2":date3}

        date_dictionary = await client.dictionary.get_date_valid()
        assert date_dictionary ==  valid_date_dict

        await client.dictionary.put_date_valid(valid_date_dict)

    @pytest.mark.asyncio
    async def test_get_date_invalid(self, client):
        date_null_dict = {"0":isodate.parse_date("2012-01-01"),
                          "1":None,
                          "2":isodate.parse_date("1776-07-04")}
        assert date_null_dict ==  await (client.dictionary.get_date_invalid_null())

        with pytest.raises(DeserializationError):
            await client.dictionary.get_date_invalid_chars()

    @pytest.mark.asyncio
    async def test_date_time_valid(self, client):
        datetime1 = isodate.parse_datetime("2000-12-01T00:00:01Z")
        datetime2 = isodate.parse_datetime("1980-01-02T00:11:35+01:00")
        datetime3 = isodate.parse_datetime("1492-10-12T10:15:01-08:00")
        valid_datetime_dict = {"0":datetime1, "1":datetime2, "2":datetime3}

        assert valid_datetime_dict ==  (await client.dictionary.get_date_time_valid())

        await client.dictionary.put_date_time_valid(valid_datetime_dict)

    @pytest.mark.asyncio
    async def test_get_date_time_invalid(self, client):
        datetime_null_dict = {"0":isodate.parse_datetime("2000-12-01T00:00:01Z"), "1":None}
        assert datetime_null_dict ==  (await client.dictionary.get_date_time_invalid_null())

        with pytest.raises(DeserializationError):
            await client.dictionary.get_date_time_invalid_chars()

    @pytest.mark.asyncio
    async def test_date_time_rfc1123_valid(self, client):
        rfc_datetime1 = isodate.parse_datetime("2000-12-01T00:00:01Z")
        rfc_datetime2 = isodate.parse_datetime("1980-01-02T00:11:35Z")
        rfc_datetime3 = isodate.parse_datetime("1492-10-12T10:15:01Z")
        valid_rfc_dict = {"0":rfc_datetime1, "1":rfc_datetime2, "2":rfc_datetime3}

        assert valid_rfc_dict ==  (await client.dictionary.get_date_time_rfc1123_valid())

        await client.dictionary.put_date_time_rfc1123_valid(valid_rfc_dict)

    @pytest.mark.asyncio
    async def test_get_duration_valid(self, client):
        duration1 = timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)
        duration2 = timedelta(days=5, hours=1)
        valid_duration_dict = {"0":duration1, "1":duration2}

        assert valid_duration_dict ==  (await client.dictionary.get_duration_valid())

        await client.dictionary.put_duration_valid(valid_duration_dict)

    @pytest.mark.asyncio
    async def test_bytes_valid(self, client):
        bytes1 = bytearray([0x0FF, 0x0FF, 0x0FF, 0x0FA])
        bytes2 = bytearray([0x01, 0x02, 0x03])
        bytes3 = bytearray([0x025, 0x029, 0x043])
        bytes4 = bytearray([0x0AB, 0x0AC, 0x0AD])

        bytes_valid = {"0":bytes1, "1":bytes2, "2":bytes3}
        await client.dictionary.put_byte_valid(bytes_valid)

        bytes_result = await client.dictionary.get_byte_valid()
        assert bytes_valid ==  bytes_result

    @pytest.mark.asyncio
    async def test_get_byte_invalid_null(self, client):
        bytes4 = bytearray([0x0AB, 0x0AC, 0x0AD])
        bytes_null = {"0":bytes4, "1":None}
        bytes_result = await client.dictionary.get_byte_invalid_null()
        assert bytes_null ==  bytes_result

    @pytest.mark.asyncio
    async def test_get_base64_url(self, client):
        test_dict = {'0': 'a string that gets encoded with base64url'.encode(),
                     '1': 'test string'.encode(),
                     '2': 'Lorem ipsum'.encode()}
        assert (await client.dictionary.get_base64_url())==  test_dict

    # Basic dictionary parsing

    @pytest.mark.asyncio
    async def test_empty(self, client):

        assert {} ==  (await client.dictionary.get_empty())

        await client.dictionary.put_empty({})

    @pytest.mark.asyncio
    async def test_get_null_and_invalid(self, client):
        assert await client.dictionary.get_null() is None

        with pytest.raises(DecodeError):
            await client.dictionary.get_invalid()

    @pytest.mark.asyncio
    async def test_get_null_key_and_value(self, client):
        # {null:"val1"} is not standard JSON format. C# might work and expects this test to pass,
        # but we fail and we're happy with it.
        with pytest.raises(DecodeError):
            await client.dictionary.get_null_key()
        assert {"key1":None} ==  (await client.dictionary.get_null_value())

    @pytest.mark.asyncio
    async def test_get_empty_string_key(self, client):
        assert {"":"val1"} ==  (await client.dictionary.get_empty_string_key())

    # Dictionary composed types

    @pytest.mark.asyncio
    async def test_get_complex_null_and_empty(self, client):
        assert await client.dictionary.get_complex_null() is None
        assert {} ==  (await client.dictionary.get_complex_empty())

    @pytest.mark.asyncio
    async def test_complex_valid(self, client, test_dict):

        await client.dictionary.put_complex_valid(test_dict)
        complex_result = await client.dictionary.get_complex_valid()
        assert test_dict ==  complex_result

    @pytest.mark.asyncio
    async def test_array_valid(self, client):
        list_dict = {"0":["1","2","3"], "1":["4","5","6"], "2":["7","8","9"]}
        await client.dictionary.put_array_valid(list_dict)

        array_result = await client.dictionary.get_array_valid()
        assert list_dict ==  array_result

    @pytest.mark.asyncio
    async def test_dictionary_valid(self, client):
        dict_dict = {"0":{"1":"one","2":"two","3":"three"},
                     "1":{"4":"four","5":"five","6":"six"},
                     "2":{"7":"seven","8":"eight","9":"nine"}}
        await client.dictionary.put_dictionary_valid(dict_dict)

        dict_result = await client.dictionary.get_dictionary_valid()
        assert dict_dict ==  dict_result

    @pytest.mark.asyncio
    async def test_get_complex_null_and_empty(self, client):
        assert await client.dictionary.get_complex_null() is None
        assert {} ==  (await client.dictionary.get_complex_empty())

    @pytest.mark.asyncio
    async def test_get_complex_item_null_and_empty(self, client, test_dict):
        test_dict_null = {"0":test_dict["0"], "1":None, "2":test_dict["2"]}
        complex_result = await client.dictionary.get_complex_item_null()
        assert complex_result ==  test_dict_null

        test_dict_empty = {"0":test_dict["0"], "1":Widget(), "2":test_dict["2"]}
        complex_result = await client.dictionary.get_complex_item_empty()
        assert complex_result ==  test_dict_empty

    @pytest.mark.asyncio
    async def test_get_array_empty(self, client):
        assert await client.dictionary.get_array_null() is None
        assert {} ==  (await client.dictionary.get_array_empty())

    @pytest.mark.asyncio
    async def test_get_array_item_null_and_empty(self, client):
        list_dict = {"0":["1","2","3"], "1":None, "2":["7","8","9"]}
        array_result = await client.dictionary.get_array_item_null()
        assert list_dict ==  array_result

        list_dict = {"0":["1","2","3"], "1":[], "2":["7","8","9"]}
        array_result = await client.dictionary.get_array_item_empty()
        assert list_dict ==  array_result

    @pytest.mark.asyncio
    async def test_get_dictionary_null_and_empty(self, client):
        assert await client.dictionary.get_dictionary_null() is None
        assert {} ==  (await client.dictionary.get_dictionary_empty())

    @pytest.mark.asyncio
    async def test_get_dictionary_item_null_and_empty(self, client):
        dict_dict = {"0":{"1":"one","2":"two","3":"three"},
                     "1":None,
                     "2":{"7":"seven","8":"eight","9":"nine"}}
        dict_result = await client.dictionary.get_dictionary_item_null()
        assert dict_dict ==  dict_result

        dict_dict = {"0":{"1":"one","2":"two","3":"three"},
                     "1":{},
                     "2":{"7":"seven","8":"eight","9":"nine"}}
        dict_result = await client.dictionary.get_dictionary_item_empty()
        assert dict_dict ==  dict_result
