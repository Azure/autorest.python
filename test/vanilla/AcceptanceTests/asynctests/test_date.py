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

from bodydate.aio import AutoRestDateTestService

import pytest

@pytest.fixture
async def client():
    async with AutoRestDateTestService(base_url="http://localhost:3000") as client:
        yield client

class TestDate(object):

    @pytest.mark.asyncio
    async def test_model_get_and_put_max_date(self, client):
        max_date = isodate.parse_date("9999-12-31T23:59:59.999999Z")
        await client.date.put_max_date(max_date)
        assert max_date ==  (await client.date.get_max_date())

    @pytest.mark.asyncio
    async def test_model_get_and_put_min_date(self, client):
        min_date = isodate.parse_date("0001-01-01T00:00:00Z")
        await client.date.put_min_date(min_date)
        assert min_date ==  (await client.date.get_min_date())

    @pytest.mark.asyncio
    async def test_model_get_null(self, client):
        assert await client.date.get_null() is None

    @pytest.mark.asyncio
    async def test_model_get_invalid_date(self, client):
        with pytest.raises(DeserializationError):
            await client.date.get_invalid_date()

    @pytest.mark.asyncio
    async def test_model_get_overflow_date(self, client):
        with pytest.raises(DeserializationError):
            await client.date.get_overflow_date()

    @pytest.mark.asyncio
    async def test_model_get_underflow_date(self, client):
        with pytest.raises(DeserializationError):
            await client.date.get_underflow_date()
