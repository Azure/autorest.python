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
import datetime
from async_generator import yield_, async_generator

from bodydatelowlevel.aio import AutoRestDateTestService
from bodydatelowlevel.rest import date

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestDateTestService() as client:
        await yield_(client)

@pytest.fixture
def send_request(client, base_send_request):
    async def _send_request(request):
        return await base_send_request(client, request)
    return _send_request

@pytest.fixture
def send_request_json_response(client, base_send_request_json_response):
    async def _send_request(request):
        return await base_send_request_json_response(client, request)
    return _send_request

@pytest.mark.asyncio
async def test_model_get_and_put_max_date(send_request, send_request_json_response):
    max_date = isodate.parse_date("9999-12-31T23:59:59.999999Z")
    request = date.build_put_max_date_request(json=str(max_date))
    await send_request(request)

    request = date.build_get_max_date_request()
    assert max_date == isodate.parse_date(await send_request_json_response(request))

@pytest.mark.asyncio
async def test_model_get_and_put_min_date(send_request, send_request_json_response):
    min_date = isodate.parse_date("0001-01-01T00:00:00Z")
    request = date.build_put_min_date_request(json=str(min_date))
    await send_request(request)

    request = date.build_get_min_date_request()
    assert min_date == isodate.parse_date(await send_request_json_response(request))

@pytest.mark.asyncio
async def test_model_get_null(send_request):
    request = date.build_get_null_request()
    assert (await send_request(request)).text == ''

@pytest.mark.asyncio
async def test_model_get_invalid_date(send_request_json_response):
    request = date.build_get_invalid_date_request()
    assert datetime.date(2001, 1, 1) == isodate.parse_date(await send_request_json_response(request))

@pytest.mark.asyncio
async def test_model_get_overflow_date(send_request_json_response):
    request = date.build_get_overflow_date_request()
    with pytest.raises(ValueError) as ex:
        isodate.parse_date(await send_request_json_response(request))
    assert "day is out of range for month" in str(ex.value)

@pytest.mark.asyncio
async def test_model_get_underflow_date(send_request_json_response):
    request = date.build_get_underflow_date_request()
    with pytest.raises(ValueError) as ex:
        isodate.parse_date(await send_request_json_response(request))
    assert "year 0 is out of range" in str(ex.value)
