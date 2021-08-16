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

from decimal import Decimal
import pytest

from bodynumberlowlevel import AutoRestNumberTestService
from bodynumberlowlevel.rest import number

import pytest

@pytest.fixture
def client():
    with AutoRestNumberTestService(base_url="http://localhost:3000") as client:
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

def test_big_float(send_request, send_request_json_response):
    request = number.build_put_big_float_request(json=3.402823e+20)
    send_request(request)

    request = number.build_get_big_float_request()
    assert send_request_json_response(request) ==  3.402823e+20

def test_small_float(send_request, send_request_json_response):
    request = number.build_put_small_float_request(json=3.402823e-20)
    send_request(request)

    request = number.build_get_small_float_request()
    assert send_request_json_response(request) ==  3.402823e-20

def test_big_double(send_request, send_request_json_response):
    request = number.build_put_big_double_request(json=2.5976931e+101)
    send_request(request)

    request = number.build_get_big_double_request()
    assert send_request_json_response(request) ==  2.5976931e+101

def test_small_double(send_request, send_request_json_response):
    request = number.build_put_small_double_request(json=2.5976931e-101)
    send_request(request)

    request = number.build_get_small_double_request()
    assert send_request_json_response(request) ==  2.5976931e-101

def test_big_double_negative_decimal(send_request, send_request_json_response):
    request = number.build_get_big_double_negative_decimal_request(json=-99999999.99)
    send_request(request)

    request = number.build_get_big_double_negative_decimal_request()
    assert send_request_json_response(request) ==  -99999999.99

def test_big_double_positive_decimal(send_request, send_request_json_response):
    request = number.build_put_big_double_positive_decimal_request()
    send_request(request)

    request = number.build_get_big_double_positive_decimal_request()
    assert send_request_json_response(request) ==  99999999.99

def test_big_decimal(send_request, send_request_json_response):
    request = number.build_put_big_decimal_request(json=2.5976931e+101)
    send_request(request)

    request = number.build_get_big_decimal_request()
    assert send_request_json_response(request) ==  2.5976931e+101

def test_small_decimal(send_request, send_request_json_response):
    request = number.build_put_small_decimal_request(json=2.5976931e-101)
    send_request(request)

    request = number.build_get_small_decimal_request()
    assert send_request_json_response(request) ==  2.5976931e-101

def test_get_big_decimal_negative_decimal(send_request, send_request_json_response):
    request = number.build_put_big_decimal_negative_decimal_request()

    request = number.build_get_big_decimal_negative_decimal_request()
    assert send_request_json_response(request) ==  -99999999.99

def test_get_big_decimal_positive_decimal(send_request, send_request_json_response):
    request = number.build_put_big_decimal_positive_decimal_request()
    send_request(request)

    request = number.build_get_big_decimal_positive_decimal_request()
    assert send_request_json_response(request) ==  99999999.99

def test_get_null(send_request):
    request = number.build_get_null_request()
    assert send_request(request).text == ''

def test_get_invalid_decimal(send_request):
    request = number.build_get_invalid_decimal_request()
    assert send_request(request).text == '9223372036854775910.980089k'

def test_get_invalid_double(send_request):
    request = number.build_get_invalid_double_request()
    assert send_request(request).text == '9223372036854775910.980089k'

def test_get_invalid_float(send_request):
    request = number.build_get_invalid_float_request()
    assert send_request(request).text == '2147483656.090096789909j'
