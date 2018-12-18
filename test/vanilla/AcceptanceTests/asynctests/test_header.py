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
sys.path.append(join(tests, "Header"))

from msrest.serialization import Deserializer
from msrest.exceptions import DeserializationError

from header import AutoRestSwaggerBATHeaderService
from header.models.auto_rest_swagger_bat_header_service_enums import GreyscaleColors

import pytest

class TestHeader(object):

    @pytest.mark.asyncio
    async def test_headers(self):
        client = AutoRestSwaggerBATHeaderService(base_url="http://localhost:3000")

        await client.header.param_integer_async("positive", 1)
        await client.header.param_integer_async("negative", -2)

        raw = await client.header.response_integer_async("positive", raw=True)
        assert 1 ==  int(raw.response.headers.get("value"))
        assert 1 ==  raw.headers.get("value")
        raw = await client.header.response_integer_async("negative", raw=True)
        assert -2 ==  raw.headers.get("value")

        await client.header.param_long_async("positive", 105)
        await client.header.param_long_async("negative", -2)

        raw = await client.header.response_long_async("positive", raw=True)
        assert 105 ==  raw.headers.get("value")
        raw = await client.header.response_long_async("negative", raw=True)
        assert -2 ==  raw.headers.get("value")

        await client.header.param_float_async("positive", 0.07)
        await client.header.param_float_async("negative", -3.0)

        raw = await client.header.response_float_async("positive", raw=True)
        assert abs(0.07 - raw.headers.get("value")) < 0.00001
        raw = await client.header.response_float_async("negative", raw=True)
        assert abs(-3.0 - raw.headers.get("value")) < 0.00001

        await client.header.param_double_async("positive", 7e120)
        await client.header.param_double_async("negative", -3.0)

        raw = await client.header.response_double_async("positive", raw=True)
        assert 7e120 ==  raw.headers.get("value")
        raw = await client.header.response_double_async("negative", raw=True)
        assert -3.0 ==  raw.headers.get("value")

        await client.header.param_bool_async("true", True)
        await client.header.param_bool_async("false", False)

        raw = await client.header.response_bool_async("true", raw=True)
        assert True ==  raw.headers.get("value")
        raw = await client.header.response_bool_async("false", raw=True)
        assert False ==  raw.headers.get("value")

        await client.header.param_string_async("valid", "The quick brown fox jumps over the lazy dog")
        await client.header.param_string_async("null", None)
        await client.header.param_string_async("empty", "")

        raw = await client.header.response_string_async("valid", raw=True)
        assert "The quick brown fox jumps over the lazy dog" ==  raw.headers.get("value")
        raw = await client.header.response_string_async("null", raw=True)
        assert None ==  json.loads(raw.headers.get("value"))
        raw = await client.header.response_string_async("empty", raw=True)
        assert "" ==  raw.headers.get("value")

        await client.header.param_enum_async("valid", GreyscaleColors.grey)
        await client.header.param_enum_async("valid", 'GREY')
        await client.header.param_enum_async("null", None)

        raw = await client.header.response_enum_async("valid", raw=True)
        assert GreyscaleColors.grey ==  raw.headers.get("value")

        # We receive an empty string.
        # Starting msrest 0.4.22, we consider that if a string is not in the enum, this not
        # a Deserialization issue and we return the string.
        # Here we now return empty string without failin **on purpose**
        # with pytest.raises(DeserializationError):
        raw = await client.header.response_enum_async("null", raw=True)
        assert "" ==  raw.headers.get("value")

        await client.header.param_date_async("valid", isodate.parse_date("2010-01-01"))
        await client.header.param_date_async("min", datetime.min)

        raw = await client.header.response_date_async("valid", raw=True)
        assert isodate.parse_date("2010-01-01") ==  raw.headers.get("value")
        raw = await client.header.response_date_async("min", raw=True)
        assert isodate.parse_date("0001-01-01") ==  raw.headers.get("value")

        await client.header.param_datetime_async("valid", isodate.parse_datetime("2010-01-01T12:34:56Z"))
        await client.header.param_datetime_async("min", datetime.min)

        raw = await client.header.response_datetime_async("valid", raw=True)
        assert isodate.parse_datetime("2010-01-01T12:34:56Z") ==  raw.headers.get("value")
        raw = await client.header.response_datetime_async("min", raw=True)
        assert isodate.parse_datetime("0001-01-01T00:00:00Z") ==  raw.headers.get("value")

        await client.header.param_datetime_rfc1123_async("valid", isodate.parse_datetime("2010-01-01T12:34:56Z"))
        await client.header.param_datetime_rfc1123_async("min", datetime.min)

        raw = await client.header.response_datetime_rfc1123_async("valid", raw=True)
        assert isodate.parse_datetime("2010-01-01T12:34:56Z") ==  raw.headers.get("value")
        raw = await client.header.response_datetime_rfc1123_async("min", raw=True)
        assert isodate.parse_datetime("0001-01-01T00:00:00Z") ==  raw.headers.get("value")

        await client.header.param_duration_async("valid", timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11))

        raw = await client.header.response_duration_async("valid", raw=True)
        assert timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11) ==  raw.headers.get("value")

        u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
        await client.header.param_byte_async("valid", u_bytes)

        raw = await client.header.response_byte_async("valid", raw=True)
        assert u_bytes ==  raw.headers.get("value")

        await client.header.param_existing_key_async("overwrite")

        raw = await client.header.response_existing_key_async(raw=True)
        assert "overwrite" ==  raw.headers.get('User-Agent')

        # This test is only valid for C#, which content-type can't be override this way
        #await client.header.param_protected_key("text/html")

        # This test has different result compare to C#, which content-type is saved in another place.
        raw = await client.header.response_protected_key_async(raw=True)
        assert "text/html; charset=utf-8", raw.headers.get('Content-Type')

        custom_headers = {"x-ms-client-request-id": "9C4D50EE-2D56-4CD3-8152-34347DC9F2B0"}
        raw = await client.header.custom_request_id_async(custom_headers=custom_headers, raw=True)
        assert raw.response.status_code ==  200
