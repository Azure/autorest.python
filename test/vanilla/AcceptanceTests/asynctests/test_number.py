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
from decimal import Decimal
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "BodyNumber"))

from msrest.serialization import Deserializer
from azure.core.exceptions import DecodeError

from bodynumber.aio import AutoRestNumberTestService

import pytest

@pytest.fixture
def client():
    return AutoRestNumberTestService(base_url="http://localhost:3000")

class TestNumber(object):

    @pytest.mark.asyncio
    async def test_big_float(self, client):
        await client.number.put_big_float(3.402823e+20)
        assert (await client.number.get_big_float()) ==  3.402823e+20

    @pytest.mark.asyncio
    async def test_small_float(self, client):
        await client.number.put_small_float(3.402823e-20)
        assert (await client.number.get_small_float()) ==  3.402823e-20

    @pytest.mark.asyncio
    async def test_big_double(self, client):
        await client.number.put_big_double(2.5976931e+101)
        assert (await client.number.get_big_double()) ==  2.5976931e+101

    @pytest.mark.asyncio
    async def test_small_double(self, client):
        await client.number.put_small_double(2.5976931e-101)
        assert (await client.number.get_small_double()) ==  2.5976931e-101

    @pytest.mark.asyncio
    async def test_big_double_negative_decimal(self, client):
        await client.number.put_big_double_negative_decimal()
        assert (await client.number.get_big_double_negative_decimal()) ==  -99999999.99

    @pytest.mark.asyncio
    async def test_big_double_positive_decimal(self, client):
        await client.number.put_big_double_positive_decimal()
        assert (await client.number.get_big_double_positive_decimal()) ==  99999999.99

    @pytest.mark.asyncio
    async def test_big_decimal(self, client):
        await client.number.put_big_decimal(Decimal(2.5976931e+101))
        assert (await client.number.get_big_decimal()) ==  2.5976931e+101

    @pytest.mark.asyncio
    async def test_small_decimal(self, client):
        await client.number.put_small_decimal(Decimal(2.5976931e-101))
        assert (await client.number.get_small_decimal()) ==  2.5976931e-101

    @pytest.mark.asyncio
    async def test_get_big_decimal_negative_decimal(self, client):
        # await client.number.put_big_decimal_positive_decimal()
        assert (await client.number.get_big_decimal_negative_decimal()) ==  -99999999.99

    @pytest.mark.asyncio
    async def test_get_big_decimal_positive_decimal(self, client):
        # await client.number.put_big_decimal_negative_decimal()
        assert (await client.number.get_big_decimal_positive_decimal()) ==  99999999.99

    @pytest.mark.asyncio
    async def test_get_null(self, client):
        await client.number.get_null()

    @pytest.mark.asyncio
    async def test_get_invalid_decimal(self, client):
        with pytest.raises(DecodeError):
            await client.number.get_invalid_decimal()

    @pytest.mark.asyncio
    async def test_get_invalid_double(self, client):
        with pytest.raises(DecodeError):
            await client.number.get_invalid_double()

    @pytest.mark.asyncio
    async def test_get_invalid_float(self, client):
        with pytest.raises(DecodeError):
            await client.number.get_invalid_float()
