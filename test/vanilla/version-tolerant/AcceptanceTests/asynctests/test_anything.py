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
from anythingversiontolerant.aio import AnythingClient

@pytest.fixture
@async_generator
async def client():
    async with AnythingClient(endpoint="http://localhost:3000") as client:
        await yield_(client)

@pytest.mark.asyncio
async def test_get_string(client):
    assert await client.get_string() == 'anything'

@pytest.mark.asyncio
async def test_put_string(client):
    await client.put_string(input="anything")

@pytest.mark.asyncio
async def test_get_object(client):
    assert await client.get_object() == {"message": "An object was successfully returned"}

@pytest.mark.asyncio
async def test_put_object(client):
    await client.put_object({'foo': 'bar'})

@pytest.mark.asyncio
async def test_get_array(client):
    assert await client.get_array() == ['foo', 'bar']

@pytest.mark.asyncio
async def test_put_array(client):
    await client.put_array(['foo', 'bar'])
