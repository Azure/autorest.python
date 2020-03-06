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

from async_generator import yield_, async_generator
import unittest
import subprocess
import sys
import isodate
import tempfile
import json
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

from msrest.exceptions import DeserializationError

from header.aio import AutoRestSwaggerBATHeaderService
from header.models import GreyscaleColors

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestSwaggerBATHeaderService(base_url="http://localhost:3000") as client:
        await yield_(client)

@pytest.fixture
@async_generator
def value_header():
    def _value_header(response, _, headers):
        return headers.get("value")
    return _value_header

class TestHeader(object):

    @pytest.mark.asyncio
    async def test_integer(self, client, value_header):
        await client.header.param_integer("positive", 1)
        await client.header.param_integer("negative", -2)

        response = await client.header.response_integer("positive", cls=value_header)
        assert response == 1

        response = await client.header.response_integer("negative", cls=value_header)
        assert response == -2

    @pytest.mark.asyncio
    async def test_long(self, client, value_header):
        await client.header.param_long("positive", 105)
        await client.header.param_long("negative", -2)

        response = await client.header.response_long("positive", cls=value_header)
        assert response == 105
        response = await client.header.response_long("negative", cls=value_header)
        assert response == -2

    @pytest.mark.asyncio
    async def test_float(self, client, value_header):
        await client.header.param_float("positive", 0.07)
        await client.header.param_float("negative", -3.0)

        response = await client.header.response_float("positive", cls=value_header)
        assert abs(0.07 - response) < 0.00001
        response = await client.header.response_float("negative", cls=value_header)
        assert abs(-3.0 - response) < 0.00001

    @pytest.mark.asyncio
    async def test_double(self, client, value_header):
        await client.header.param_double("positive", 7e120)
        await client.header.param_double("negative", -3.0)

        response = await client.header.response_double("positive", cls=value_header)
        assert response == 7e120
        response = await client.header.response_double("negative", cls=value_header)
        assert response == -3.0

    @pytest.mark.asyncio
    async def test_bool(self, client, value_header):
        await client.header.param_bool("true", True)
        await client.header.param_bool("false", False)

        response = await client.header.response_bool("true", cls=value_header)
        assert response == True
        response = await client.header.response_bool("false", cls=value_header)
        assert response == False

    @pytest.mark.asyncio
    async def test_string(self, client, value_header):
        await client.header.param_string("valid", "The quick brown fox jumps over the lazy dog")
        await client.header.param_string("null", None)
        await client.header.param_string("empty", "")

        response = await client.header.response_string("valid", cls=value_header)
        assert response == "The quick brown fox jumps over the lazy dog"
        response = await client.header.response_string("null", cls=value_header)
        assert response == "null"  # TODO This should be None
        response = await client.header.response_string("empty", cls=value_header)
        assert response == ""

    @pytest.mark.asyncio
    async def test_enum(self, client, value_header):
        await client.header.param_enum("valid", GreyscaleColors.grey)
        await client.header.param_enum("valid", 'GREY')
        await client.header.param_enum("null", None)

        response = await client.header.response_enum("valid", cls=value_header)
        assert response == GreyscaleColors.grey

        # We receive an empty string.
        # Starting msrest 0.4.22, we consider that if a string is not in the enum, this not
        # a Deserialization issue and we return the string.
        # Here we now return empty string without failin **on purpose**
        # with pytest.raises(DeserializationError):
        response = await client.header.response_enum("null", cls=value_header)
        assert response == ""

    @pytest.mark.asyncio
    async def test_date(self, client, value_header):
        await client.header.param_date("valid", isodate.parse_date("2010-01-01"))
        await client.header.param_date("min", datetime.min)

        response = await client.header.response_date("valid", cls=value_header)
        assert response == isodate.parse_date("2010-01-01")
        response = await client.header.response_date("min", cls=value_header)
        assert response == isodate.parse_date("0001-01-01")

    @pytest.mark.asyncio
    async def test_datetime(self, client, value_header):
        await client.header.param_datetime("valid", isodate.parse_datetime("2010-01-01T12:34:56Z"))
        await client.header.param_datetime("min", datetime.min)

        response = await client.header.response_datetime("valid", cls=value_header)
        assert response == isodate.parse_datetime("2010-01-01T12:34:56Z")
        response = await client.header.response_datetime("min", cls=value_header)
        assert response == isodate.parse_datetime("0001-01-01T00:00:00Z")

    @pytest.mark.asyncio
    async def test_datetime_rfc(self, client, value_header):
        await client.header.param_datetime_rfc1123("valid", isodate.parse_datetime("2010-01-01T12:34:56Z"))
        await client.header.param_datetime_rfc1123("min", datetime.min)

        response = await client.header.response_datetime_rfc1123("valid", cls=value_header)
        assert response == isodate.parse_datetime("2010-01-01T12:34:56Z")
        response = await client.header.response_datetime_rfc1123("min", cls=value_header)
        assert response == isodate.parse_datetime("0001-01-01T00:00:00Z")

    @pytest.mark.asyncio
    async def test_duration(self, client, value_header):
        await client.header.param_duration("valid", timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11))

        response = await client.header.response_duration("valid", cls=value_header)
        assert response == timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)

    @pytest.mark.asyncio
    async def test_byte(self, client, value_header):
        u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
        await client.header.param_byte("valid", u_bytes)

        response = await client.header.response_byte("valid", cls=value_header)
        assert response == u_bytes

        await client.header.param_existing_key("overwrite")

    @pytest.mark.asyncio
    async def test_response_existing_key(self, client):
        def useragent_header(response, _, headers):
            return headers.get('User-Agent')
        response = await client.header.response_existing_key(cls=useragent_header)
        assert response == "overwrite"

    @pytest.mark.asyncio
    async def test_response_protected_key(self, client):
        # This test is only valid for C#, which content-type can't be override this way
        #await client.header.param_protected_key("text/html")

        # This test has different result compare to C#, which content-type is saved in another place.
        def content_header(response, _, headers):
            return headers.get('Content-Type')
        response = await client.header.response_protected_key(cls=content_header)
        assert response == "text/html; charset=utf-8"

    @pytest.mark.asyncio
    async def test_custom_request_id(self, client):
        def status_code(pipeline_response, _, headers):
            return pipeline_response.http_response.status_code
        custom_headers = {"x-ms-client-request-id": "9C4D50EE-2D56-4CD3-8152-34347DC9F2B0"}
        response = await client.header.custom_request_id(headers=custom_headers, cls=status_code)
        assert response == 200
