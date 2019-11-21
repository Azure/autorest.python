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
from datetime import date, datetime, timedelta, tzinfo
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "BodyInteger"))

from msrest.serialization import Deserializer
from azure.core.exceptions import DecodeError

from bodyinteger import AutoRestIntegerTestService

import pytest

@pytest.fixture
def client():
    return AutoRestIntegerTestService(base_url="http://localhost:3000")

class TestInteger(object):

    def test_max_min_32_bit(self, client):
        client.int_model.put_max32(2147483647) # sys.maxint
        client.int_model.put_min32(-2147483648)

    def test_max_min_64_bit(self, client):
        client.int_model.put_max64(9223372036854776000)  # sys.maxsize
        client.int_model.put_min64(-9223372036854776000)

    def test_get_null_and_invalid(self, client):
        client.int_model.get_null()

        with pytest.raises(DecodeError):
            client.int_model.get_invalid()

    def test_get_overflow(self, client):
        # Testserver excepts these to fail, but they won't in Python and it's ok.
        client.int_model.get_overflow_int32()
        client.int_model.get_overflow_int64()

    def test_get_underflow(self, client):
        client.int_model.get_underflow_int32()
        client.int_model.get_underflow_int64()

    def test_unix_time_date(self, client):
        unix_date = datetime(year=2016, month=4, day=13)
        client.int_model.put_unix_time_date(unix_date)
        assert unix_date.utctimetuple() ==  client.int_model.get_unix_time().utctimetuple()

    def test_get_null_and_invalid_unix_time(self, client):
        assert client.int_model.get_null_unix_time() is None

        with pytest.raises(DecodeError):
            client.int_model.get_invalid_unix_time()
