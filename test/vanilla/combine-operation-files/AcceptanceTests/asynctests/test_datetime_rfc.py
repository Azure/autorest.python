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
import unittest
import subprocess
import sys
import isodate
import tempfile
import json
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

from msrest.exceptions import DeserializationError

from bodydatetimerfc1123combineoperationfiles.aio import AutoRestRFC1123DateTimeTestService

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestRFC1123DateTimeTestService(base_url="http://localhost:3000") as client:
        await yield_(client)

class TestDateTimeRfc(object):

    @pytest.mark.asyncio
    async def test_get_null(self, client):
        assert await client.datetimerfc1123.get_null() is None

    @pytest.mark.asyncio
    async def test_get_invalid(self, client):
        with pytest.raises(DeserializationError):
            await client.datetimerfc1123.get_invalid()

    @pytest.mark.asyncio
    async def test_get_underflow(self, client):
        with pytest.raises(DeserializationError):
            await client.datetimerfc1123.get_underflow()

    @pytest.mark.asyncio
    async def test_get_overflow(self, client):
        with pytest.raises(DeserializationError):
            await client.datetimerfc1123.get_overflow()

    @pytest.mark.asyncio
    async def test_utc_max_date_time(self, client):
        max_date = isodate.parse_datetime("9999-12-31T23:59:59.999999Z")

        await client.datetimerfc1123.get_utc_lowercase_max_date_time()
        await client.datetimerfc1123.get_utc_uppercase_max_date_time()
        await client.datetimerfc1123.put_utc_max_date_time(max_date)

    @pytest.mark.asyncio
    async def test_utc_min_date_time(self, client):
        min_date = isodate.parse_datetime("0001-01-01T00:00:00Z")
        await client.datetimerfc1123.get_utc_min_date_time()
        await client.datetimerfc1123.put_utc_min_date_time(min_date)
