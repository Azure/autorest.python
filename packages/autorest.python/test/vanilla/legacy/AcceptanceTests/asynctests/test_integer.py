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
import unittest
import subprocess
import sys
import isodate
import tempfile
import json
from datetime import date, datetime, timedelta, tzinfo
import os
from os.path import dirname, pardir, join, realpath

from azure.core.exceptions import DecodeError

from bodyinteger.aio import AutoRestIntegerTestService

import pytest


@pytest.fixture
@async_generator
async def client():
    async with AutoRestIntegerTestService(base_url="http://localhost:3000") as client:
        await yield_(client)


class TestInteger(object):
    @pytest.mark.asyncio
    async def test_max_min_32_bit(self, client):
        await client.int_operations.put_max32(2147483647)  # sys.maxint
        await client.int_operations.put_min32(-2147483648)

    @pytest.mark.asyncio
    async def test_max_min_64_bit(self, client):
        await client.int_operations.put_max64(9223372036854776000)  # sys.maxsize
        await client.int_operations.put_min64(-9223372036854776000)

    @pytest.mark.asyncio
    async def test_get_null_and_invalid(self, client):
        await client.int_operations.get_null()

        with pytest.raises(DecodeError):
            await client.int_operations.get_invalid()

    @pytest.mark.asyncio
    async def test_get_overflow(self, client):
        # Testserver excepts these to fail, but they won't in Python and it's ok.
        await client.int_operations.get_overflow_int32()
        await client.int_operations.get_overflow_int64()

    @pytest.mark.asyncio
    async def test_get_underflow(self, client):
        await client.int_operations.get_underflow_int32()
        await client.int_operations.get_underflow_int64()

    @pytest.mark.asyncio
    async def test_unix_time_date(self, client):
        unix_date = datetime(year=2016, month=4, day=13)
        await client.int_operations.put_unix_time_date(unix_date)
        assert unix_date.utctimetuple() == (await client.int_operations.get_unix_time()).utctimetuple()

    @pytest.mark.asyncio
    async def test_get_null_and_invalid_unix_time(self, client):
        assert await client.int_operations.get_null_unix_time() is None

        with pytest.raises(DecodeError):
            await client.int_operations.get_invalid_unix_time()
