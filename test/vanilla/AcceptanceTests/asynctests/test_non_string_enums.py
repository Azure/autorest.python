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
from nonstringenums.aio import NonStringEnumsClient
from nonstringenums.models import IntEnum, FloatEnum

import pytest
import json

@pytest.fixture
@async_generator
async def client():
    async with NonStringEnumsClient(base_url="http://localhost:3000") as client:
        await yield_(client)


class TestNonStringEnums(object):

    @pytest.mark.asyncio
    async def test_put_int_enum(self, client):
        result = await client.int.put(IntEnum.two_hundred)
        assert result == "Nice job posting an int enum"

    @pytest.mark.asyncio
    async def test_get_int_enum(self, client):
        result = await client.int.get()
        assert result == IntEnum.four_hundred_twenty_nine.value

    @pytest.mark.asyncio
    async def test_put_float_enum(self, client):
        result = await client.float.put(FloatEnum.two_hundred4)
        assert result == "Nice job posting a float enum"

    @pytest.mark.asyncio
    async def test_get_float_enum(self, client):
        result = await client.float.get()
        assert result == FloatEnum.four_hundred_twenty_nine1.value
