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
from async_generator import yield_, async_generator
import isodate

from bodydurationlowlevel.aio import AutoRestDurationTestService
from bodydurationlowlevel.rest import duration

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestDurationTestService(endpoint="http://localhost:3000") as client:
        await yield_(client)

@pytest.fixture
def send_request(client, base_send_request):
    async def _send_request(request):
        return await base_send_request(client, request)
    return _send_request

@pytest.fixture
def send_request_json_response(client, base_send_request_json_response):
    async def _send_request(request):
        return await base_send_request_json_response(client, request)
    return _send_request

@pytest.mark.asyncio
async def test_get_null_and_invalid(send_request, send_request_json_response):
    request = duration.build_get_null_request()
    assert (await send_request(request)).text == ''

    request = duration.build_get_invalid_request()
    with pytest.raises(isodate.ISO8601Error):
        isodate.parse_duration(await send_request_json_response(request))

@pytest.mark.asyncio
async def test_positive_duration(send_request, send_request_json_response):
    request = duration.build_get_positive_duration_request()
    assert isodate.duration.Duration(4, 45005, 0, years=3, months=6) == isodate.parse_duration(await send_request_json_response(request))

    request = duration.build_put_positive_duration_request(json=isodate.duration_isoformat(timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)))
    await send_request(request)
