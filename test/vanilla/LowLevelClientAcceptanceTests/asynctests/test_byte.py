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
from bodybyte.aio import AutoRestSwaggerBATByteService
from bodybyte.rest import byte
from async_generator import yield_, async_generator
from base64 import b64encode

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestSwaggerBATByteService(base_url="http://localhost:3000") as client:
        await yield_(client)

@pytest.fixture
def make_request(client, base_make_request):
    async def _make_request(request):
        return await base_make_request(client, request)
    return _make_request

@pytest.mark.asyncio
async def test_non_ascii(make_request):
    tests = bytearray([0x0FF, 0x0FE, 0x0FD, 0x0FC, 0x0FB, 0x0FA, 0x0F9, 0x0F8, 0x0F7, 0x0F6])
    request = byte.build_put_non_ascii_request(json=b64encode(tests).decode())
    await make_request(request)

    request = byte.build_get_non_ascii_request()
    response = await make_request(request)

@pytest.mark.asyncio
async def test_get_null(make_request):
    request = byte.build_get_null_request()
    assert (await make_request(request)).text == ''

@pytest.mark.asyncio
async def test_get_empty(make_request):
    request = byte.build_get_empty_request()
    assert b'""' == (await make_request(request)).content  # in convenience layer, we deserialize as bytearray specif

@pytest.mark.asyncio
async def test_get_invalid(make_request):
    request = byte.build_get_invalid_request()
    assert (await make_request(request)).content == b'"::::SWAGGER::::"'
