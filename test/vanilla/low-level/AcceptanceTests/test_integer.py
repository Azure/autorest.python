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

from datetime import datetime
from bodyinteger import AutoRestIntegerTestService
from bodyinteger.rest import int

import pytest
import calendar
try:
    from datetime import timezone
    TZ_UTC = timezone.utc  # type: ignore
except ImportError:
    TZ_UTC = UTC()  # type: ignore

@pytest.fixture
def client():
    with AutoRestIntegerTestService(base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def make_request(client, base_make_request):
    def _make_request(request):
        return base_make_request(client, request)
    return _make_request

def test_max_min_32_bit(make_request):
    request = int.build_put_max32_request(json=2147483647) # sys.maxint
    make_request(request)

    request = int.build_put_min32_request(json=-2147483648)
    make_request(request)

def test_max_min_64_bit(make_request):
    request = int.build_put_max64_request(json=9223372036854776000)  # sys.maxsize
    make_request(request)

    request = int.build_put_min64_request(json=-9223372036854776000)
    make_request(request)

def test_get_null_and_invalid(make_request):
    request = int.build_get_null_request()
    make_request(request)

    request = int.build_get_invalid_request()
    assert make_request(request).text == '123jkl'

def test_get_overflow(make_request):
    # Testserver excepts these to fail, but they won't in Python and it's ok.

    request = int.build_get_overflow_int32_request()
    make_request(request)

    request = int.build_get_overflow_int64_request()
    make_request(request)

def test_get_underflow(make_request):
    request = int.build_get_underflow_int32_request()
    make_request(request)

    request = int.build_get_underflow_int64_request()
    make_request(request)

def test_unix_time_date(make_request):
    unix_date = datetime(year=2016, month=4, day=13)
    request = int.build_put_unix_time_date_request(json=int(calendar.timegm(unix_date.utctimetuple())))
    make_request(request)

    request = int.build_get_unix_time_request()
    assert unix_date.utctimetuple() == datetime.fromtimestamp(make_request(request).json(), TZ_UTC).utctimetuple()

def test_get_null_and_invalid_unix_time(make_request):
    request = int.build_get_null_unix_time_request()
    assert make_request(request).text == ''

    request = int.build_get_invalid_unix_time_request()
    assert make_request(request).text == '123jkl'
