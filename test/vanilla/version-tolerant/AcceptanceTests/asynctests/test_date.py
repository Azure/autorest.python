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
from async_generator import yield_, async_generator
import datetime
from ..serializer import deserialize_date
from bodydateversiontolerant.aio import AutoRestDateTestService

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestDateTestService(base_url="http://localhost:3000") as client:
        await yield_(client)

@pytest.mark.asyncio
async def test_model_get_and_put_max_date(client):
    max_date = deserialize_date("9999-12-31T23:59:59.999999Z")
    await client.date.put_max_date(str(max_date))
    assert max_date == deserialize_date(await client.date.get_max_date())

@pytest.mark.asyncio
async def test_model_get_and_put_min_date(client):
    min_date = deserialize_date("0001-01-01T00:00:00Z")
    await client.date.put_min_date(str(min_date))
    assert min_date == deserialize_date(await client.date.get_min_date())

@pytest.mark.asyncio
async def test_model_get_null(client):
    assert await client.date.get_null() is None

@pytest.mark.asyncio
async def test_model_get_invalid_date(client):
    assert deserialize_date(await client.date.get_invalid_date()) == datetime.date(2001, 1, 1)

@pytest.mark.asyncio
async def test_model_get_overflow_date(client):
    with pytest.raises(ValueError) as ex:
        deserialize_date(await client.date.get_overflow_date())
    assert "day is out of range for month" in str(ex.value)

@pytest.mark.asyncio
async def test_model_get_underflow_date(client):
    with pytest.raises(ValueError) as ex:
        deserialize_date(await client.date.get_underflow_date())
    assert "year 0 is out of range" in str(ex.value)
