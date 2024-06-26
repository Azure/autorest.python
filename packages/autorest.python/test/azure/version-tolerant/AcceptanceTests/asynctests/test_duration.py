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
import isodate
from async_generator import yield_, async_generator
from datetime import timedelta
from serializer import serialize_duration, deserialize_duration

from bodydurationversiontolerant.aio import AutoRestDurationTestService

import pytest


@pytest.fixture
@async_generator
async def client():
    async with AutoRestDurationTestService() as client:
        await yield_(client)


@pytest.mark.asyncio
async def test_get_null_and_invalid(client):
    assert await client.duration.get_null() is None

    with pytest.raises(isodate.ISO8601Error):
        deserialize_duration(await client.duration.get_invalid())


@pytest.mark.asyncio
async def test_positive_duration(client):
    await client.duration.get_positive_duration()
    delta = timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)
    await client.duration.put_positive_duration(serialize_duration(delta))
