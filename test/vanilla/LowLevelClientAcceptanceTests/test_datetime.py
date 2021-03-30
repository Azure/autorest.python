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

from msrest.exceptions import DeserializationError, SerializationError

from bodydatetime import AutoRestDateTimeTestService
from bodydatetime._rest import *

import pytest

@pytest.fixture
def client():
    with AutoRestDateTimeTestService(base_url="http://localhost:3000") as client:
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
def get_deserialized_iso(make_request_json_response, msrest_deserializer):
    def _get_deserialized_iso(request):
        return msrest_deserializer.deserialize_iso(make_request_json_response(request))
    return _get_deserialized_iso

@pytest.fixture
def get_serialized_iso(msrest_serializer):
    def _get_serialized_iso(date):
        return msrest_serializer.serialize_iso(date)
    return _get_serialized_iso


def test_utc_max_date_time(make_request, get_serialized_iso, get_deserialized_iso):
    max_date = isodate.parse_datetime("9999-12-31T23:59:59.999Z")
    request = build_datetime_get_utc_lowercase_max_date_time_request()
    assert max_date ==  get_deserialized_iso(request)

    request = build_datetime_get_utc_uppercase_max_date_time_request()
    assert get_deserialized_iso(request) ==  max_date

    request = build_datetime_put_utc_max_date_time_request(json=get_serialized_iso(max_date))
    make_request(request)

def test_utc_max_date_time_7digits(make_request, get_serialized_iso, get_deserialized_iso):
    max_date = isodate.parse_datetime("9999-12-31T23:59:59.999999Z")
    request = build_datetime_get_utc_uppercase_max_date_time7_digits_request()
    assert get_deserialized_iso(request) == max_date

    request = build_datetime_put_utc_max_date_time7_digits_request(json=get_serialized_iso(max_date))
    with pytest.raises(Exception):
        # Python doesn't support 7 digits
        make_request(request)

def test_get_utc_min_date_time(make_request, get_serialized_iso, get_deserialized_iso):
    min_date = isodate.parse_datetime("0001-01-01T00:00:00Z")
    request = build_datetime_get_utc_min_date_time_request()
    assert get_deserialized_iso(request) ==  min_date

    request = build_datetime_put_utc_min_date_time_request(json=get_serialized_iso(min_date))
    make_request(request)

def test_get_local_negative_offset_min_date_time(make_request, make_request_json_response, get_serialized_iso):
    request = build_datetime_get_local_negative_offset_min_date_time_request()
    assert '0001-01-01T00:00:00-14:00' == make_request_json_response(request)

    request = build_datetime_put_local_negative_offset_min_date_time_request(json=get_serialized_iso(isodate.parse_datetime("0001-01-01T00:00:00-14:00")))
    make_request(request)

def test_get_local_no_offset_min_date_time(get_deserialized_iso):
    local_no_offset_min_date_time = isodate.parse_datetime("0001-01-01T00:00:00")
    request = build_datetime_get_local_no_offset_min_date_time_request()
    assert get_deserialized_iso(request) == local_no_offset_min_date_time

def test_get_local_negative_offset_lowercase_max_date_time(make_request_json_response):
    request = build_datetime_get_local_negative_offset_lowercase_max_date_time_request()
    assert make_request_json_response(request) == "9999-12-31t23:59:59.999-14:00"

def test_get_local_negative_offset_uppercase_max_date_time(make_request_json_response):
    request = build_datetime_get_local_negative_offset_uppercase_max_date_time_request()
    assert make_request_json_response(request) == "9999-12-31T23:59:59.999-14:00"

def test_local_positive_offset_min_date_time(make_request_json_response, get_serialized_iso):
    request = build_datetime_get_local_positive_offset_min_date_time_request()
    assert make_request_json_response(request) == "0001-01-01T00:00:00+14:00"

    with pytest.raises(SerializationError):
        build_datetime_put_local_positive_offset_min_date_time_request(json=get_serialized_iso(isodate.parse_datetime("0001-01-01T00:00:00+14:00")))


def test_local_positive_offset_max_date_time(make_request_json_response, make_request, get_serialized_iso):
    request = build_datetime_get_local_positive_offset_lowercase_max_date_time_request()
    assert make_request_json_response(request) == "9999-12-31t23:59:59.999+14:00"

    request = build_datetime_get_local_positive_offset_uppercase_max_date_time_request()
    assert make_request_json_response(request) == "9999-12-31T23:59:59.999+14:00"

    request = build_datetime_put_local_positive_offset_max_date_time_request(json=get_serialized_iso(isodate.parse_datetime("9999-12-31T23:59:59.999999+14:00")))
    make_request(request)

def test_get_null(make_request, get_serialized_iso, get_deserialized_iso):
    request = build_datetime_get_null_request()
    assert make_request(request).text == ''

def test_get_overflow(make_request_json_response):
    request = build_datetime_get_overflow_request()
    assert make_request_json_response(request) == "9999-12-31T23:59:59.999-14:00"

def test_get_invalid(make_request_json_response):
    request = build_datetime_get_invalid_request()
    assert make_request_json_response(request) == "201O-18-90D00:89:56.9AX"

def test_get_underflow(make_request_json_response):
    request = build_datetime_get_underflow_request()
    assert make_request_json_response(request) == "0000-00-00T00:00:00.000+00:00"

def test_put_local_negative_offset_max_date_time(get_serialized_iso):
    with pytest.raises(SerializationError):
        build_datetime_put_local_negative_offset_max_date_time_request(json=get_serialized_iso(isodate.parse_datetime("9999-12-31T23:59:59.999999-14:00")))
