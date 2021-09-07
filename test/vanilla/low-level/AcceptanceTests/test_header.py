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
from datetime import datetime, timedelta
from base64 import b64decode

from headerlowlevel import AutoRestSwaggerBATHeaderService
from headerlowlevel.rest import header

import pytest

@pytest.fixture
def client():
    with AutoRestSwaggerBATHeaderService() as client:
        yield client

@pytest.fixture
def send_request(client, base_send_request):
    def _send_request(request):
        return base_send_request(client, request)
    return _send_request

@pytest.fixture
def send_request_value_response_header(client, base_send_request):
    def _send_request(request):
        return base_send_request(client, request).headers['value']
    return _send_request

# NOTE: in llc, we don't know to deserialize response headers as int / datetime etc. So you'll see they'll just be strings, not ints etc
def test_integer(send_request, send_request_value_response_header):

    request = header.build_param_integer_request(scenario="positive", value=1)
    send_request(request)
    request = header.build_param_integer_request(scenario="negative", value=-2)
    send_request(request)

    request = header.build_response_integer_request(scenario="positive")
    assert send_request_value_response_header(request) == "1"

    request = header.build_response_integer_request(scenario="negative")
    assert send_request_value_response_header(request) == "-2"

def test_long(send_request, send_request_value_response_header):
    request = header.build_param_long_request(scenario="positive", value=105)
    send_request(request)
    request = header.build_param_long_request(scenario="negative", value=-2)
    send_request(request)

    request = header.build_response_long_request(scenario="positive")
    assert send_request_value_response_header(request) == "105"

    request = header.build_response_long_request(scenario="negative")
    assert send_request_value_response_header(request) == "-2"

def test_float(send_request, send_request_value_response_header):
    request = header.build_param_float_request(scenario="positive", value=0.07)
    send_request(request)

    request = header.build_param_float_request(scenario="negative", value=-3.0)
    send_request(request)

    request = header.build_response_float_request(scenario="positive")
    assert abs(0.07 - float(send_request_value_response_header(request))) < 0.00001

    request = header.build_response_float_request(scenario="negative")
    assert abs(-3.0 - float(send_request_value_response_header(request))) < 0.00001

def test_double(send_request, send_request_value_response_header):
    request = header.build_param_double_request(scenario="positive", value=7e120)
    send_request(request)

    request = header.build_param_double_request(scenario="negative", value=-3.0)
    send_request(request)

    request = header.build_response_double_request(scenario="positive")
    assert send_request_value_response_header(request) == "7e+120"

    request = header.build_response_double_request(scenario="negative")
    assert send_request_value_response_header(request) == "-3"

def test_bool(send_request, send_request_value_response_header):
    request = header.build_param_bool_request(scenario="true", value=True)
    send_request(request)
    request = header.build_param_bool_request(scenario="false", value=False)
    send_request(request)

    request = header.build_response_bool_request(scenario="true")
    assert send_request_value_response_header(request) == 'true'

    request = header.build_response_bool_request(scenario="false")
    assert send_request_value_response_header(request) == 'false'

def test_string(send_request, send_request_value_response_header):
    request = header.build_param_string_request(scenario="valid", value="The quick brown fox jumps over the lazy dog")
    send_request(request)

    request = header.build_param_string_request(scenario="null", value=None)
    send_request(request)

    request = header.build_param_string_request(scenario="empty", value="")
    send_request(request)

    request = header.build_response_string_request(scenario="valid")
    assert send_request_value_response_header(request) == "The quick brown fox jumps over the lazy dog"

    request = header.build_response_string_request(scenario="null")
    assert send_request_value_response_header(request) == "null"  # TODO This should be None

    request = header.build_response_string_request(scenario="empty")
    assert send_request_value_response_header(request) == ""

def test_enum(send_request, send_request_value_response_header):
    request = header.build_param_enum_request(scenario="valid", value="GREY")
    send_request(request)

    request = header.build_param_enum_request(scenario="valid", value="GREY")
    send_request(request)

    request = header.build_param_enum_request(scenario="null", value=None)
    send_request(request)


    request = header.build_response_enum_request(scenario="valid")
    assert send_request_value_response_header(request) == "GREY"

    # We receive an empty string.
    # Starting msrest 0.4.22, we consider that if a string is not in the enum, this not
    # a Deserialization issue and we return the string.
    # Here we now return empty string without failin **on purpose**
    # with pytest.raises(DeserializationError):
    request = header.build_response_enum_request(scenario="null")
    assert send_request_value_response_header(request) == ""

def test_date(send_request, send_request_value_response_header):
    request = header.build_param_date_request(scenario="valid", value=isodate.parse_date("2010-01-01"))
    send_request(request)
    request = header.build_param_date_request(scenario="min", value=datetime.min)
    send_request(request)

    request = header.build_response_date_request(scenario="valid")
    assert send_request_value_response_header(request) == str(isodate.parse_date("2010-01-01"))

    request = header.build_response_date_request(scenario="min")
    assert send_request_value_response_header(request) == str(isodate.parse_date("0001-01-01"))

def test_datetime(send_request, send_request_value_response_header):
    request = header.build_param_datetime_request(scenario="valid", value=isodate.parse_datetime("2010-01-01T12:34:56Z"))
    send_request(request)
    request = header.build_param_datetime_request(scenario="min", value=datetime.min)
    send_request(request)

    request = header.build_response_datetime_request(scenario="valid")
    assert send_request_value_response_header(request) == '2010-01-01T12:34:56Z'

    request = header.build_response_datetime_request(scenario="min")
    assert send_request_value_response_header(request) == '0001-01-01T00:00:00Z'

def test_datetime_rfc(send_request, send_request_value_response_header):
    request = header.build_param_datetime_rfc1123_request(scenario="valid", value=isodate.parse_datetime("2010-01-01T12:34:56Z"))
    send_request(request)

    request = header.build_param_datetime_rfc1123_request(scenario="min", value=datetime.min)
    send_request(request)

    request = header.build_response_datetime_rfc1123_request(scenario="valid")
    assert send_request_value_response_header(request) == "Fri, 01 Jan 2010 12:34:56 GMT"

    # we are not using the min date of year 1 because of the latest msrest update
    # with msrest update, minimal year we can parse is 100, instead of 1
    request = header.build_response_datetime_rfc1123_request(scenario="min")
    assert send_request_value_response_header(request) == "Mon, 01 Jan 0001 00:00:00 GMT"

def test_duration(send_request, send_request_value_response_header):
    request = header.build_param_duration_request(scenario="valid", value=timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11))
    send_request(request)

    request = header.build_response_duration_request(scenario="valid")
    assert send_request_value_response_header(request) == 'P123DT22H14M12.011S'  # raw str of the above timedelta

def test_byte(send_request, send_request_value_response_header):
    u_bytes = bytearray(u"\u554A\u9F44\u4E02\u72DB\u72DC\uF9F1\uF92C\uF9F1\uFA0C\uFA29", encoding='utf-8')
    request = header.build_param_byte_request(scenario="valid", value=u_bytes)
    send_request(request)

    request = header.build_response_byte_request(scenario="valid")
    assert bytearray(b64decode(send_request_value_response_header(request))) == u_bytes

def test_response_existing_key(send_request):

    request = header.build_param_existing_key_request(user_agent_parameter="overwrite")
    send_request(request)
    request = header.build_response_existing_key_request()
    assert send_request(request).headers['User-Agent'] == "overwrite"

def test_response_protected_key(send_request):
    # This test is only valid for C#, which content-type can't be override this way
    #client.header.param_protected_key("text/html")

    # This test has different result compare to C#, which content-type is saved in another place.
    request = header.build_response_protected_key_request()
    assert send_request(request).headers['Content-Type'] == "text/html; charset=utf-8"

def test_custom_request_id(send_request):
    custom_headers = {"x-ms-client-request-id": "9C4D50EE-2D56-4CD3-8152-34347DC9F2B0"}
    request = header.build_custom_request_id_request(headers=custom_headers)
    send_request(request)
