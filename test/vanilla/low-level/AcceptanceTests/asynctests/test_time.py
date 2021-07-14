# coding=utf-8
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

import datetime
from async_generator import yield_, async_generator

from bodytimelowlevel.aio import AutoRestTimeTestService
from bodytimelowlevel.rest import time
import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestTimeTestService(base_url="http://localhost:3000") as client:
        await yield_(client)

@pytest.mark.asyncio
async def test_get(client):
    request = time.build_get_request()
    response = await client.send_request(request)
    response.raise_for_status()
    assert datetime.datetime.strptime(response.json(), '%H:%M:%S').time() == datetime.time(11, 34, 56)


@pytest.mark.asyncio
async def test_put(client):
    request = time.build_put_request(json=datetime.time(8, 7, 56).strftime("%H:%M:%S"))
    response = await client.send_request(request)
    response.raise_for_status()
    assert response.json() == "Nice job posting time"
