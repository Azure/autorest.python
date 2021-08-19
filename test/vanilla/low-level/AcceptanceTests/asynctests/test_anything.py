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
import pytest
from async_generator import yield_, async_generator
from anythinglowlevel.aio import AnythingClient
from anythinglowlevel import rest

@pytest.fixture
@async_generator
async def client():
    async with AnythingClient(endpoint="http://localhost:3000") as client:
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
async def test_get_string(send_request_json_response):
    request = rest.build_get_string_request()
    assert await send_request_json_response(request) == 'anything'

@pytest.mark.asyncio
async def test_put_string(send_request):
    request = rest.build_put_string_request(json="anything")
    await send_request(request)

@pytest.mark.asyncio
async def test_get_object(send_request_json_response):
    request = rest.build_get_object_request()
    assert await send_request_json_response(request) == {"message": "An object was successfully returned"}

@pytest.mark.asyncio
async def test_put_object(send_request):
    request = rest.build_put_object_request(json={'foo': 'bar'})
    await send_request(request)

@pytest.mark.asyncio
async def test_get_array(send_request_json_response):
    request = rest.build_get_array_request()
    assert await send_request_json_response(request) == ['foo', 'bar']

@pytest.mark.asyncio
async def test_put_array(send_request):
    request = rest.build_put_array_request(json=['foo', 'bar'])
    await send_request(request)

