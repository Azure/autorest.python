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

import isodate
from async_generator import yield_, async_generator

from msrest.exceptions import DeserializationError, SerializationError

from bodydatetime.aio import AutoRestDateTimeTestService
from bodydatetime.rest import datetime

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestDateTimeTestService(base_url="http://localhost:3000") as client:
        await yield_(client)
@pytest.fixture
def make_request(client, base_make_request):
    async def _make_request(request):
        return await base_make_request(client, request)
    return _make_request

@pytest.fixture
def make_request_json_response(client, base_make_request_json_response):
    async def _make_request(request):
        return await base_make_request_json_response(client, request)
    return _make_request

@pytest.fixture
def get_deserialized_iso(make_request_json_response, msrest_deserializer):
    async def _get_deserialized_iso(request):
        return msrest_deserializer.deserialize_iso(await make_request_json_response(request))
    return _get_deserialized_iso

@pytest.fixture
def get_serialized_iso(msrest_serializer):
    def _get_serialized_iso(date):
        return msrest_serializer.serialize_iso(date)
    return _get_serialized_iso

@pytest.mark.asyncio
async def test_utc_max_date_time(make_request, get_serialized_iso, get_deserialized_iso):
    max_date = isodate.parse_datetime("9999-12-31T23:59:59.999Z")
    request = datetime.build_get_utc_lowercase_max_date_time_request()
    assert max_date ==  await get_deserialized_iso(request)

    request = datetime.build_get_utc_uppercase_max_date_time_request()
    assert await get_deserialized_iso(request) ==  max_date

    request = datetime.build_put_utc_max_date_time_request(json=get_serialized_iso(max_date))
    await make_request(request)

@pytest.mark.asyncio
async def test_utc_max_date_time_7digits(make_request, get_serialized_iso, get_deserialized_iso):
    max_date = isodate.parse_datetime("9999-12-31T23:59:59.999999Z")
    request = datetime.build_get_utc_uppercase_max_date_time7_digits_request()
    assert await get_deserialized_iso(request) == max_date

    request = datetime.build_put_utc_max_date_time7_digits_request(json=get_serialized_iso(max_date))
    with pytest.raises(Exception):
        # Python doesn't support 7 digits
        await make_request(request)

@pytest.mark.asyncio
async def test_get_utc_min_date_time(make_request, get_serialized_iso, get_deserialized_iso):
    min_date = isodate.parse_datetime("0001-01-01T00:00:00Z")
    request = datetime.build_get_utc_min_date_time_request()
    assert await get_deserialized_iso(request) ==  min_date

    request = datetime.build_put_utc_min_date_time_request(json=get_serialized_iso(min_date))
    await make_request(request)

@pytest.mark.asyncio
async def test_get_local_negative_offset_min_date_time(make_request, make_request_json_response, get_serialized_iso):
    request = datetime.build_get_local_negative_offset_min_date_time_request()
    assert '0001-01-01T00:00:00-14:00' == await make_request_json_response(request)

    request = datetime.build_put_local_negative_offset_min_date_time_request(json=get_serialized_iso(isodate.parse_datetime("0001-01-01T00:00:00-14:00")))
    await make_request(request)

@pytest.mark.asyncio
async def test_get_local_no_offset_min_date_time(get_deserialized_iso):
    local_no_offset_min_date_time = isodate.parse_datetime("0001-01-01T00:00:00")
    request = datetime.build_get_local_no_offset_min_date_time_request()
    assert await get_deserialized_iso(request) == local_no_offset_min_date_time

@pytest.mark.asyncio
async def test_get_local_negative_offset_lowercase_max_date_time(make_request_json_response):
    request = datetime.build_get_local_negative_offset_lowercase_max_date_time_request()
    assert await make_request_json_response(request) == "9999-12-31t23:59:59.999-14:00"

@pytest.mark.asyncio
async def test_get_local_negative_offset_uppercase_max_date_time(make_request_json_response):
    request = datetime.build_get_local_negative_offset_uppercase_max_date_time_request()
    assert await make_request_json_response(request) == "9999-12-31T23:59:59.999-14:00"

@pytest.mark.asyncio
async def test_local_positive_offset_min_date_time(make_request_json_response, get_serialized_iso):
    request = datetime.build_get_local_positive_offset_min_date_time_request()
    assert await make_request_json_response(request) == "0001-01-01T00:00:00+14:00"

    with pytest.raises(SerializationError):
        datetime.build_put_local_positive_offset_min_date_time_request(json=get_serialized_iso(isodate.parse_datetime("0001-01-01T00:00:00+14:00")))


@pytest.mark.asyncio
async def test_local_positive_offset_max_date_time(make_request_json_response, make_request, get_serialized_iso):
    request = datetime.build_get_local_positive_offset_lowercase_max_date_time_request()
    assert await make_request_json_response(request) == "9999-12-31t23:59:59.999+14:00"

    request = datetime.build_get_local_positive_offset_uppercase_max_date_time_request()
    assert await make_request_json_response(request) == "9999-12-31T23:59:59.999+14:00"

    request = datetime.build_put_local_positive_offset_max_date_time_request(json=get_serialized_iso(isodate.parse_datetime("9999-12-31T23:59:59.999999+14:00")))
    await make_request(request)

@pytest.mark.asyncio
async def test_get_null(make_request, get_serialized_iso, get_deserialized_iso):
    request = datetime.build_get_null_request()
    assert (await make_request(request)).text == ''

@pytest.mark.asyncio
async def test_get_overflow(make_request_json_response):
    request = datetime.build_get_overflow_request()
    assert await make_request_json_response(request) == "9999-12-31T23:59:59.999-14:00"

@pytest.mark.asyncio
async def test_get_invalid(make_request_json_response):
    request = datetime.build_get_invalid_request()
    assert await make_request_json_response(request) == "201O-18-90D00:89:56.9AX"

@pytest.mark.asyncio
async def test_get_underflow(make_request_json_response):
    request = datetime.build_get_underflow_request()
    assert await make_request_json_response(request) == "0000-00-00T00:00:00.000+00:00"

@pytest.mark.asyncio
async def test_put_local_negative_offset_max_date_time(get_serialized_iso):
    with pytest.raises(SerializationError):
        datetime.build_put_local_negative_offset_max_date_time_request(json=get_serialized_iso(isodate.parse_datetime("9999-12-31T23:59:59.999999-14:00")))
