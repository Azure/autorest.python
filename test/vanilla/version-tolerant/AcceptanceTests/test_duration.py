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
from datetime import timedelta
import isodate

from bodydurationversiontolerant import AutoRestDurationTestService
from .serializer import deserialize_duration, serialize_duration

import pytest

@pytest.fixture
def client():
    with AutoRestDurationTestService(base_url="http://localhost:3000") as client:
        yield client

def test_get_null_and_invalid(client):
    assert client.duration.get_null() is None

    with pytest.raises(isodate.ISO8601Error):
        deserialize_duration(client.duration.get_invalid())

def test_positive_duration(client):
    assert isodate.Duration(4, 45005, 0, years=3, months=6) == deserialize_duration(client.duration.get_positive_duration())
    client.duration.put_positive_duration(serialize_duration(timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)))
