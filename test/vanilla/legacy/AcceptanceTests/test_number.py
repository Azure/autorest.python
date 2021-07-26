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
from decimal import Decimal
from datetime import date, datetime, timedelta
import os
import pytest
from os.path import dirname, pardir, join, realpath

from azure.core.exceptions import DecodeError

from bodynumber import AutoRestNumberTestService

import pytest

@pytest.fixture
def client():
    with AutoRestNumberTestService(base_url="http://localhost:3000") as client:
        yield client

class TestNumber(object):

    def test_big_float(self, client):
        client.number.put_big_float(3.402823e+20)
        assert client.number.get_big_float() ==  3.402823e+20

    def test_small_float(self, client):
        client.number.put_small_float(3.402823e-20)
        assert client.number.get_small_float() ==  3.402823e-20

    def test_big_double(self, client):
        client.number.put_big_double(2.5976931e+101)
        assert client.number.get_big_double() ==  2.5976931e+101

    def test_small_double(self, client):
        client.number.put_small_double(2.5976931e-101)
        assert client.number.get_small_double() ==  2.5976931e-101

    def test_big_double_negative_decimal(self, client):
        client.number.put_big_double_negative_decimal()
        assert client.number.get_big_double_negative_decimal() ==  -99999999.99

    def test_big_double_positive_decimal(self, client):
        client.number.put_big_double_positive_decimal()
        assert client.number.get_big_double_positive_decimal() ==  99999999.99

    def test_big_decimal(self, client):
        client.number.put_big_decimal(Decimal(2.5976931e+101))
        assert client.number.get_big_decimal() ==  2.5976931e+101

    def test_small_decimal(self, client):
        client.number.put_small_decimal(Decimal(2.5976931e-101))
        assert client.number.get_small_decimal() ==  2.5976931e-101

    def test_get_big_decimal_negative_decimal(self, client):
        client.number.put_big_decimal_positive_decimal()
        assert client.number.get_big_decimal_negative_decimal() ==  -99999999.99

    def test_get_big_decimal_positive_decimal(self, client):
        client.number.put_big_decimal_negative_decimal()
        assert client.number.get_big_decimal_positive_decimal() ==  99999999.99

    def test_get_null(self, client):
        client.number.get_null()

    def test_get_invalid_decimal(self, client):
        with pytest.raises(DecodeError):
            client.number.get_invalid_decimal()

    def test_get_invalid_double(self, client):
        with pytest.raises(DecodeError):
            client.number.get_invalid_double()

    def test_get_invalid_float(self, client):
        with pytest.raises(DecodeError):
            client.number.get_invalid_float()

    def test_models(self):
        from bodynumber.models import Error

        if sys.version_info >= (3,5):
            from bodynumber.models._models_py3 import Error as ErrorPy3
            assert Error == ErrorPy3
        else:
            from bodynumber.models._models import Error as ErrorPy2
            assert Error == ErrorPy2

    def test_operation_groups(self):
        from bodynumber.operations import NumberOperations

        if sys.version_info >= (3, 5):
            from bodynumber.operations._number_operations_py3 import NumberOperations as NumberOperationsPy3
            assert NumberOperations == NumberOperationsPy3
        else:
            from bodynumber.operations._number_operations import NumberOperations as NumberOperationsPy2
            assert NumberOperations == NumberOperationsPy2
