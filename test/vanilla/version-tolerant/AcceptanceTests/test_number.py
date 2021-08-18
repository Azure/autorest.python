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

from azure.core.exceptions import DecodeError

from bodynumberversiontolerant import AutoRestNumberTestService

import pytest

@pytest.fixture
def client():
    with AutoRestNumberTestService(endpoint="http://localhost:3000") as client:
        yield client

def test_big_float(client):
    client.number.put_big_float(3.402823e+20)
    assert client.number.get_big_float() ==  3.402823e+20

def test_small_float(client):
    client.number.put_small_float(3.402823e-20)
    assert client.number.get_small_float() ==  3.402823e-20

def test_big_double(client):
    client.number.put_big_double(2.5976931e+101)
    assert client.number.get_big_double() ==  2.5976931e+101

def test_small_double(client):
    client.number.put_small_double(2.5976931e-101)
    assert client.number.get_small_double() ==  2.5976931e-101

def test_big_double_negative_decimal(client):
    client.number.put_big_double_negative_decimal()
    assert client.number.get_big_double_negative_decimal() ==  -99999999.99

def test_big_double_positive_decimal(client):
    client.number.put_big_double_positive_decimal()
    assert client.number.get_big_double_positive_decimal() ==  99999999.99

def test_big_decimal(client):
    client.number.put_big_decimal(2.5976931e+101)
    assert client.number.get_big_decimal() ==  2.5976931e+101

def test_small_decimal(client):
    client.number.put_small_decimal(2.5976931e-101)
    assert client.number.get_small_decimal() ==  2.5976931e-101

def test_get_big_decimal_negative_decimal(client):
    client.number.put_big_decimal_positive_decimal()
    assert client.number.get_big_decimal_negative_decimal() ==  -99999999.99

def test_get_big_decimal_positive_decimal(client):
    client.number.put_big_decimal_negative_decimal()
    assert client.number.get_big_decimal_positive_decimal() ==  99999999.99

def test_get_null(client):
    client.number.get_null()

def test_get_invalid_decimal(client):
    with pytest.raises(DecodeError):
        client.number.get_invalid_decimal()

def test_get_invalid_double(client):
    with pytest.raises(DecodeError):
        client.number.get_invalid_double()

def test_get_invalid_float(client):
    with pytest.raises(DecodeError):
        client.number.get_invalid_float()
