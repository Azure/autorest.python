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


from bodydatetimerfc1123lowlevel import AutoRestRFC1123DateTimeTestService
from bodydatetimerfc1123lowlevel.rest import datetimerfc1123

import pytest

@pytest.fixture
def client():
    with AutoRestRFC1123DateTimeTestService() as client:
        yield client

@pytest.fixture
def send_request(client, base_send_request):
    def _send_request(request):
        return base_send_request(client, request)
    return _send_request

@pytest.fixture
def send_request_json_response(client, base_send_request_json_response):
    def _send_request(request):
        return base_send_request_json_response(client, request)
    return _send_request

def test_get_null(send_request):
    request = datetimerfc1123.build_get_null_request()
    assert send_request(request).text == ''

def test_get_invalid(send_request_json_response):
    request = datetimerfc1123.build_get_invalid_request()
    assert "Tue, 01 Dec 2000 00:00:0A ABC" == send_request_json_response(request)

def test_get_underflow(send_request_json_response):
    request = datetimerfc1123.build_get_underflow_request()
    assert "Tue, 00 Jan 0000 00:00:00 GMT" == send_request_json_response(request)

def test_get_overflow(send_request_json_response):
    request = datetimerfc1123.build_get_overflow_request()
    assert "Sat, 1 Jan 10000 00:00:00 GMT" == send_request_json_response(request)

def test_utc_max_date_time(send_request, msrest_serializer):
    max_date = isodate.parse_datetime("9999-12-31T23:59:59.999999Z")

    request = datetimerfc1123.build_get_utc_lowercase_max_date_time_request()
    send_request(request)

    request = datetimerfc1123.build_get_utc_uppercase_max_date_time_request()
    send_request(request)

    request = datetimerfc1123.build_put_utc_max_date_time_request(json=msrest_serializer.serialize_rfc(max_date))
    send_request(request)

def test_utc_min_date_time(send_request, msrest_serializer):
    min_date = isodate.parse_datetime("0001-01-01T00:00:00Z")
    request = datetimerfc1123.build_get_utc_min_date_time_request()
    send_request(request)

    request = datetimerfc1123.build_put_utc_min_date_time_request(json=msrest_serializer.serialize_rfc(min_date))
    send_request(request)
