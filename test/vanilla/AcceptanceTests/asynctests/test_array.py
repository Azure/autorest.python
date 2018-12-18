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
import tempfile
import json
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "BodyArray"))

from msrest.serialization import Deserializer
from msrest.exceptions import DeserializationError

from bodyarray import AutoRestSwaggerBATArrayService
from bodyarray.models import Product

import pytest


class TestArray(object):

    @pytest.mark.asyncio
    async def test_array(self):
        client = AutoRestSwaggerBATArrayService(base_url="http://localhost:3000")

        assert [] ==  await client.array.get_empty_async()
        assert await client.array.get_null_async() is None

        await client.array.put_empty_async([])
        assert [True, False, False, True] ==  await client.array.get_boolean_tfft_async()
        await client.array.put_boolean_tfft_async([True, False, False, True])

        assert [1, -1, 3, 300] ==  await client.array.get_integer_valid_async()
        await client.array.put_integer_valid_async([1, -1, 3, 300])

        assert [1, -1, 3, 300] ==  await client.array.get_long_valid_async()
        await client.array.put_long_valid_async([1, -1, 3, 300])

        assert [0, -0.01, -1.2e20] ==  await client.array.get_float_valid_async()
        await client.array.put_float_valid_async([0, -0.01, -1.2e20])

        assert [0, -0.01, -1.2e20] ==  await client.array.get_double_valid_async()
        await client.array.put_double_valid_async([0, -0.01, -1.2e20])

        assert ["foo1", "foo2", "foo3"] ==  await client.array.get_string_valid_async()
        await client.array.put_string_valid_async(["foo1", "foo2", "foo3"])
        assert ["foo", None, "foo2"] ==  await client.array.get_string_with_null_async()
        assert ["foo", "123", "foo2"] ==  await client.array.get_string_with_invalid_async()

        assert ["6dcc7237-45fe-45c4-8a6b-3a8a3f625652", "d1399005-30f7-40d6-8da6-dd7c89ad34db",
                          "f42f6aa1-a5bc-4ddf-907e-5f915de43205"] == await client.array.get_uuid_valid_async()
        await client.array.put_uuid_valid_async(["6dcc7237-45fe-45c4-8a6b-3a8a3f625652", "d1399005-30f7-40d6-8da6-dd7c89ad34db",
                          "f42f6aa1-a5bc-4ddf-907e-5f915de43205"])
        #Handles invalid characters without error because of no guid class
        assert ["6dcc7237-45fe-45c4-8a6b-3a8a3f625652", "foo"] ==  await client.array.get_uuid_invalid_chars_async()

        date1 = isodate.parse_date("2000-12-01")
        date2 = isodate.parse_date("1980-01-02")
        date3 = isodate.parse_date("1492-10-12")
        datetime1 = isodate.parse_datetime("2000-12-01T00:00:01Z")
        datetime2 = isodate.parse_datetime("1980-01-02T00:11:35Z")
        datetime3 = isodate.parse_datetime("1492-10-12T10:15:01Z")
        duration1 = timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)
        duration2 = timedelta(days=5, hours=1)

        date_array = await client.array.get_date_valid_async()
        assert date_array, [date1, date2 ==  date3]
        await client.array.put_date_valid_async([date1, date2, date3])

        dt_array = await client.array.get_date_time_valid_async()
        assert dt_array, [datetime1, datetime2 ==  datetime3]
        await client.array.put_date_time_valid_async([datetime1, datetime2, datetime3])

        dt_array = await client.array.get_date_time_rfc1123_valid_async()
        assert dt_array, [datetime1, datetime2 ==  datetime3]
        await client.array.put_date_time_rfc1123_valid_async([datetime1, datetime2, datetime3])

        dur_array = await client.array.get_duration_valid_async()
        assert dur_array, [duration1 ==  duration2]
        await client.array.put_duration_valid_async([duration1, duration2])

        bytes1 = bytearray([0x0FF, 0x0FF, 0x0FF, 0x0FA])
        bytes2 = bytearray([0x01, 0x02, 0x03])
        bytes3 = bytearray([0x025, 0x029, 0x043])
        bytes4 = bytearray([0x0AB, 0x0AC, 0x0AD])

        await client.array.put_byte_valid_async([bytes1, bytes2, bytes3])
        bytes_array = await client.array.get_byte_valid_async()
        assert bytes_array, [bytes1, bytes2 ==  bytes3]

        bytes_array = await client.array.get_byte_invalid_null_async()
        assert bytes_array, [bytes4 ==  None]

        prod1 = Product(integer=1, string="2")
        prod2 = Product(integer=3, string="4")
        prod3 = Product(integer=5, string="6")
        products = [prod1, prod2, prod3]

        assert await client.array.get_complex_null_async() is None
        assert [] ==  await client.array.get_complex_empty_async()
        await client.array.put_complex_valid_async(products)
        assert products ==  await client.array.get_complex_valid_async()

        listlist = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        await client.array.put_array_valid_async(listlist)
        assert listlist ==  await client.array.get_array_valid_async()

        listdict = [{"1": "one", "2": "two", "3": "three"}, 
                    {"4": "four", "5": "five", "6": "six"}, 
                    {"7": "seven", "8": "eight", "9": "nine"}]
        await client.array.put_dictionary_valid_async(listdict)
        assert listdict ==  await client.array.get_dictionary_valid_async()

        products2 = [prod1, None, prod3]
        assert products2 ==  await client.array.get_complex_item_null_async()

        products3 = [prod1, Product(), prod3]
        assert products3 ==  await client.array.get_complex_item_empty_async()

        assert await client.array.get_array_null_async() is None
        assert [] ==  await client.array.get_array_empty_async()

        listlist2 = [["1", "2", "3"], None, ["7", "8", "9"]]
        assert listlist2 ==  await client.array.get_array_item_null_async()

        listlist3 = [["1", "2", "3"], [], ["7", "8", "9"]]
        assert listlist3 ==  await client.array.get_array_item_empty_async()

        assert await client.array.get_dictionary_null_async() is None
        assert [] ==  await client.array.get_dictionary_empty_async()

        listdict[1] = None
        assert listdict ==  await client.array.get_dictionary_item_null_async()

        listdict[1] = {}
        assert listdict ==  await client.array.get_dictionary_item_empty_async()

        with pytest.raises(DeserializationError):
            await client.array.get_invalid_async()

        assert await client.array.get_boolean_invalid_null_async(), [True, None ==  False]

        with pytest.raises(DeserializationError):
            await client.array.get_boolean_invalid_string_async()

        assert await client.array.get_int_invalid_null_async(), [1, None ==  0]

        with pytest.raises(DeserializationError):
            await client.array.get_int_invalid_string_async()

        assert await client.array.get_long_invalid_null_async(), [1, None ==  0]

        with pytest.raises(DeserializationError):
            await client.array.get_long_invalid_string_async()

        assert await client.array.get_float_invalid_null_async(), [0.0, None ==  -1.2e20]

        with pytest.raises(DeserializationError):
            await client.array.get_float_invalid_string_async()

        assert await client.array.get_double_invalid_null_async(), [0.0, None ==  -1.2e20]

        with pytest.raises(DeserializationError):
            await client.array.get_double_invalid_string_async()

        assert await client.array.get_string_with_invalid_async(), ["foo", "123" ==  "foo2"]

        d_array = await client.array.get_date_invalid_null_async()
        assert d_array, [isodate.parse_date("2012-01-01"), None ==  isodate.parse_date("1776-07-04")]

        with pytest.raises(DeserializationError):
            await client.array.get_date_invalid_chars_async()

        dt_array = await client.array.get_date_time_invalid_null_async()
        assert dt_array, [isodate.parse_datetime("2000-12-01T00:00:01Z") ==  None]

        with pytest.raises(DeserializationError):
            await client.array.get_date_time_invalid_chars_async()

        test_array = ['a string that gets encoded with base64url'.encode(),
                      'test string'.encode(),
                      'Lorem ipsum'.encode()]
        assert await client.array.get_base64_url_async() ==  test_array
