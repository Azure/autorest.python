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

from msrest.exceptions import DeserializationError

from headercombineoperationfiles import AutoRestSwaggerBATHeaderService
from headercombineoperationfiles.models import GreyscaleColors

import pytest

@pytest.fixture
def client():
    with AutoRestSwaggerBATHeaderService(base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def value_header():
    def _value_header(response, _, headers):
        return headers.get("value")
    return _value_header

class TestHeader(object):

    def test_integer(self, client, value_header):
        client.header.param_integer("positive", 1)
        client.header.param_integer("negative", -2)

        response = client.header.response_integer("positive", cls=value_header)
        assert response == 1

        response = client.header.response_integer("negative", cls=value_header)
        assert response == -2

    def test_long(self, client, value_header):
        client.header.param_long("positive", 105)
        client.header.param_long("negative", -2)

        response = client.header.response_long("positive", cls=value_header)
        assert response == 105
        response = client.header.response_long("negative", cls=value_header)
        assert response == -2

    def test_float(self, client, value_header):
        client.header.param_float("positive", 0.07)
        client.header.param_float("negative", -3.0)

        response = client.header.response_float("positive", cls=value_header)
        assert abs(0.07 - response) < 0.00001
        response = client.header.response_float("negative", cls=value_header)
        assert abs(-3.0 - response) < 0.00001

    def test_double(self, client, value_header):
        client.header.param_double("positive", 7e120)
        client.header.param_double("negative", -3.0)

        response = client.header.response_double("positive", cls=value_header)
        assert response == 7e120
        response = client.header.response_double("negative", cls=value_header)
        assert response == -3.0

    def test_bool(self, client, value_header):
        client.header.param_bool("true", True)
        client.header.param_bool("false", False)

        response = client.header.response_bool("true", cls=value_header)
        assert response == True
        response = client.header.response_bool("false", cls=value_header)
        assert response == False

    def test_string(self, client, value_header):
        client.header.param_string("valid", "The quick brown fox jumps over the lazy dog")
        client.header.param_string("null", None)
        client.header.param_string("empty", "")

        response = client.header.response_string("valid", cls=value_header)
        assert response == "The quick brown fox jumps over the lazy dog"
        response = client.header.response_string("null", cls=value_header)
        assert response == "null"  # TODO This should be None
        response = client.header.response_string("empty", cls=value_header)
        assert response == ""

    def test_enum(self, client, value_header):
        client.header.param_enum("valid", GreyscaleColors.grey)
        client.header.param_enum("valid", 'GREY')
        client.header.param_enum("null", None)

        response = client.header.response_enum("valid", cls=value_header)
        assert response == GreyscaleColors.grey

        # We receive an empty string.
        # Starting msrest 0.4.22, we consider that if a string is not in the enum, this not
        # a Deserialization issue and we return the string.
        # Here we now return empty string without failin **on purpose**
        # with pytest.raises(DeserializationError):
        response = client.header.response_enum("null", cls=value_header)
        assert response == ""

    def test_date(self, client, value_header):
        client.header.param_date("valid", isodate.parse_date("2010-01-01"))
        client.header.param_date("min", datetime.min)

        response = client.header.response_date("valid", cls=value_header)
        assert response == isodate.parse_date("2010-01-01")
        response = client.header.response_date("min", cls=value_header)
        assert response == isodate.parse_date("0001-01-01")

    def test_datetime(self, client, value_header):
        client.header.param_datetime("valid", isodate.parse_datetime("2010-01-01T12:34:56Z"))
        client.header.param_datetime("min", datetime.min)

        response = client.header.response_datetime("valid", cls=value_header)
        assert response == isodate.parse_datetime("2010-01-01T12:34:56Z")
        response = client.header.response_datetime("min", cls=value_header)
        assert response == isodate.parse_datetime("0001-01-01T00:00:00Z")

    def test_datetime_rfc(self, client, value_header):
        client.header.param_datetime_rfc1123("valid", isodate.parse_datetime("2010-01-01T12:34:56Z"))
        client.header.param_datetime_rfc1123("min", datetime.min)

        response = client.header.response_datetime_rfc1123("valid", cls=value_header)
        assert response == isodate.parse_datetime("2010-01-01T12:34:56Z")

        # we are not using the min date of year 1 because of the latest msrest update
        # with msrest update, minimal year we can parse is 100, instead of 1
        response = client.header.response_datetime_rfc1123("min", cls=value_header)
        assert response == isodate.parse_datetime("2001-01-01T00:00:00Z")

    def test_duration(self, client, value_header):
        client.header.param_duration("valid", timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11))

        response = client.header.response_duration("valid", cls=value_header)
        assert response == timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)

    def test_byte(self, client, value_header):
        u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
        client.header.param_byte("valid", u_bytes)

        response = client.header.response_byte("valid", cls=value_header)
        assert response == u_bytes

        client.header.param_existing_key("overwrite")

    def test_response_existing_key(self, client):
        def useragent_header(response, _, headers):
            return headers.get('User-Agent')
        response = client.header.response_existing_key(cls=useragent_header)
        assert response == "overwrite"

    def test_response_protected_key(self, client):
        # This test is only valid for C#, which content-type can't be override this way
        #client.header.param_protected_key("text/html")

        # This test has different result compare to C#, which content-type is saved in another place.
        def content_header(response, _, headers):
            return headers.get('Content-Type')
        response = client.header.response_protected_key(cls=content_header)
        assert response == "text/html; charset=utf-8"

    def test_custom_request_id(self, client):
        def status_code(pipeline_response, _, headers):
            return pipeline_response.http_response.status_code
        custom_headers = {"x-ms-client-request-id": "9C4D50EE-2D56-4CD3-8152-34347DC9F2B0"}
        response = client.header.custom_request_id(headers=custom_headers, cls=status_code)
        assert response == 200

    def test_models(self):
        from headercombineoperationfiles.models import Error

        if sys.version_info >= (3,5):
            from headercombineoperationfiles.models._models_py3 import Error as ErrorPy3
            assert Error == ErrorPy3
        else:
            from headercombineoperationfiles.models._models import Error as ErrorPy2
            assert Error == ErrorPy2

    def test_operation_groups(self):
        from headercombineoperationfiles.operations import HeaderOperations

        with pytest.raises(ImportError):
            from headercombineoperationfiles.operations import _combine_operations_py3

        from headercombineoperationfiles.operations._combine_operations import HeaderOperations as HeaderOperationsPy2
        assert HeaderOperations == HeaderOperationsPy2
