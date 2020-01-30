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

from azure.core.exceptions import DecodeError

from bodyboolean.aio import AutoRestBoolTestService
from bodyboolean.models import ErrorException

import pytest

@pytest.fixture
async def client():
    async with AutoRestBoolTestService(base_url="http://localhost:3000") as client:
        yield client

class TestBool(object):

    @pytest.mark.asyncio
    async def test_model_get_true(self, client):
        assert (await client.bool_model.get_true())

    @pytest.mark.asyncio
    async def test_model_get_false(self, client):
        assert not (await client.bool_model.get_false())

    @pytest.mark.asyncio
    async def test_model_get_null(self, client):
        await client.bool_model.get_null()

    @pytest.mark.asyncio
    async def test_model_put_false(self, client):
        await client.bool_model.put_false()

    @pytest.mark.asyncio
    async def test_model_put_true(self, client):
        await client.bool_model.put_true()

    @pytest.mark.asyncio
    async def test_model_get_invalid(self, client):
        with pytest.raises(DecodeError):
            await client.bool_model.get_invalid()
