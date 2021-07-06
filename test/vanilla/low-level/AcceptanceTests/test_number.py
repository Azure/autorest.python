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
def make_request(client, base_make_request):
    def _make_request(request):
        return base_make_request(client, request)
    return _make_request

@pytest.fixture
def make_request_json_response(client, base_make_request_json_response):
    def _make_request(request):
        return base_make_request_json_response(client, request)
    return _make_request

def test_big_float(make_request, make_request_json_response):
    request = number.build_put_big_float_request(json=3.402823e+20)
    make_request(request)

    request = number.build_get_big_float_request()
    assert make_request_json_response(request) ==  3.402823e+20

def test_small_float(make_request, make_request_json_response):
    request = number.build_put_small_float_request(json=3.402823e-20)
    make_request(request)

    request = number.build_get_small_float_request()
    assert make_request_json_response(request) ==  3.402823e-20

def test_big_double(make_request, make_request_json_response):
    request = number.build_put_big_double_request(json=2.5976931e+101)
    make_request(request)

    request = number.build_get_big_double_request()
    assert make_request_json_response(request) ==  2.5976931e+101

def test_small_double(make_request, make_request_json_response):
    request = number.build_put_small_double_request(json=2.5976931e-101)
    make_request(request)

    request = number.build_get_small_double_request()
    assert make_request_json_response(request) ==  2.5976931e-101

def test_big_double_negative_decimal(make_request, make_request_json_response):
    request = number.build_get_big_double_negative_decimal_request(json=-99999999.99)
    make_request(request)

    request = number.build_get_big_double_negative_decimal_request()
    assert make_request_json_response(request) ==  -99999999.99

def test_big_double_positive_decimal(make_request, make_request_json_response):
    request = number.build_put_big_double_positive_decimal_request(json=99999999.99)
    make_request(request)

    request = number.build_get_big_double_positive_decimal_request()
    assert make_request_json_response(request) ==  99999999.99

def test_big_decimal(make_request, make_request_json_response):
    request = number.build_put_big_decimal_request(json=2.5976931e+101)
    make_request(request)

    request = number.build_get_big_decimal_request()
    assert make_request_json_response(request) ==  2.5976931e+101

def test_small_decimal(make_request, make_request_json_response):
    request = number.build_put_small_decimal_request(json=2.5976931e-101)
    make_request(request)

    request = number.build_get_small_decimal_request()
    assert make_request_json_response(request) ==  2.5976931e-101

def test_get_big_decimal_negative_decimal(make_request, make_request_json_response):
    request = number.build_put_big_decimal_negative_decimal_request(json=-99999999.99)

    request = number.build_get_big_decimal_negative_decimal_request()
    assert make_request_json_response(request) ==  -99999999.99

def test_get_big_decimal_positive_decimal(make_request, make_request_json_response):
    request = number.build_put_big_decimal_positive_decimal_request(json=99999999.99)
    make_request(request)

    request = number.build_get_big_decimal_positive_decimal_request()
    assert make_request_json_response(request) ==  99999999.99

def test_get_null(make_request):
    request = number.build_get_null_request()
    assert make_request(request).text == ''

def test_get_invalid_decimal(make_request):
    request = number.build_get_invalid_decimal_request()
    assert make_request(request).text == '9223372036854775910.980089k'

def test_get_invalid_double(make_request):
    request = number.build_get_invalid_double_request()
    assert make_request(request).text == '9223372036854775910.980089k'

def test_get_invalid_float(make_request):
    request = number.build_get_invalid_float_request()
    assert make_request(request).text == '2147483656.090096789909j'
