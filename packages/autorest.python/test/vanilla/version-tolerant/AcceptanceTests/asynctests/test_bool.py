﻿# --------------------------------------------------------------------------
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
from azure.core.exceptions import DecodeError

from bodybooleanversiontolerant.aio import AutoRestBoolTestService

import pytest


@pytest.fixture
@async_generator
async def client():
    async with AutoRestBoolTestService() as client:
        await yield_(client)


@pytest.mark.asyncio
async def test_model_get_true(client):
    assert await client.bool.get_true()


@pytest.mark.asyncio
async def test_model_get_false(client):
    assert not (await client.bool.get_false())


@pytest.mark.asyncio
async def test_model_get_null(client):
    await client.bool.get_null()


@pytest.mark.asyncio
async def test_model_put_false(client):
    await client.bool.put_false()


@pytest.mark.asyncio
async def test_model_put_true(client):
    await client.bool.put_true()


@pytest.mark.asyncio
async def test_model_get_invalid(client):
    with pytest.raises(DecodeError):
        await client.bool.get_invalid()
