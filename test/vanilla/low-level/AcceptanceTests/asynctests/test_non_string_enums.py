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
from nonstringenumslowlevel.aio import NonStringEnumsClient
from nonstringenumslowlevel.rest import int, float
from async_generator import yield_, async_generator

import pytest

@pytest.fixture
@async_generator
async def client():
    async with NonStringEnumsClient(base_url="http://localhost:3000") as client:
        await yield_(client)

@pytest.fixture
def make_request_json_response(client, base_make_request_json_response):
    def _make_request(request):
        return base_make_request_json_response(client, request)
    return _make_request

@pytest.mark.asyncio
async def test_put_int_enum(make_request_json_response):
    request = int.build_put_request(json=200)
    assert await make_request_json_response(request) == "Nice job posting an int enum"

@pytest.mark.asyncio
async def test_get_int_enum(make_request_json_response):
    request = int.build_get_request()
    assert await make_request_json_response(request) == 429

@pytest.mark.asyncio
async def test_put_float_enum(make_request_json_response):
    request = float.build_put_request(json=200.4)
    assert await make_request_json_response(request) == "Nice job posting a float enum"

@pytest.mark.asyncio
async def test_get_float_enum(make_request_json_response):
    request = float.build_get_request()
    assert await make_request_json_response(request) == 429.1
