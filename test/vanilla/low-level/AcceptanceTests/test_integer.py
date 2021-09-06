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
from bodyintegerlowlevel import AutoRestIntegerTestService
from bodyintegerlowlevel.rest import int as int_rest

import pytest
import calendar
try:
    from datetime import timezone
    TZ_UTC = timezone.utc  # type: ignore
except ImportError:
    TZ_UTC = UTC()  # type: ignore

@pytest.fixture
def client():
    with AutoRestIntegerTestService() as client:
        yield client

@pytest.fixture
def send_request(client, base_send_request):
    def _send_request(request):
        return base_send_request(client, request)
    return _send_request

def test_max_min_32_bit(send_request):
    request = int_rest.build_put_max32_request(json=2147483647) # sys.maxint
    send_request(request)

    request = int_rest.build_put_min32_request(json=-2147483648)
    send_request(request)

def test_max_min_64_bit(send_request):
    request = int_rest.build_put_max64_request(json=9223372036854776000)  # sys.maxsize
    send_request(request)

    request = int_rest.build_put_min64_request(json=-9223372036854776000)
    send_request(request)

def test_get_null_and_invalid(send_request):
    request = int_rest.build_get_null_request()
    send_request(request)

    request = int_rest.build_get_invalid_request()
    assert send_request(request).text() == '123jkl'

def test_get_overflow(send_request):
    # Testserver excepts these to fail, but they won't in Python and it's ok.

    request = int_rest.build_get_overflow_int32_request()
    send_request(request)

    request = int_rest.build_get_overflow_int64_request()
    send_request(request)

def test_get_underflow(send_request):
    request = int_rest.build_get_underflow_int32_request()
    send_request(request)

    request = int_rest.build_get_underflow_int64_request()
    send_request(request)

def test_unix_time_date(send_request):
    unix_date = datetime(year=2016, month=4, day=13)

    input = calendar.timegm(unix_date.utctimetuple())
    request = int_rest.build_put_unix_time_date_request(json=int(input))
    send_request(request)

    request = int_rest.build_get_unix_time_request()
    assert unix_date.utctimetuple() == datetime.fromtimestamp(send_request(request).json(), TZ_UTC).utctimetuple()

def test_get_null_and_invalid_unix_time(send_request):
    request = int_rest.build_get_null_unix_time_request()
    assert send_request(request).text() == ''

    request = int_rest.build_get_invalid_unix_time_request()
    assert send_request(request).text() == '123jkl'
