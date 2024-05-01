# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import pytest
import isodate
from typetest.array.aio import ArrayClient
from typetest.array import models


@pytest.fixture
async def client():
    async with ArrayClient() as client:
        yield client

@pytest.mark.asyncio
async def test_boolean_value(client: ArrayClient):
    assert await client.boolean_value.get() == [True, False]
    client.boolean_value.put([True, False])

@pytest.mark.asyncio
async def test_datetime_value(client: ArrayClient):
    assert await client.datetime_value.get() == [isodate.parse_datetime("2022-08-26T18:38:00Z")]
    client.datetime_value.put([isodate.parse_datetime("2022-08-26T18:38:00Z")])

@pytest.mark.asyncio
async def test_duration_value(client: ArrayClient):
    assert await client.duration_value.get() == [isodate.parse_duration("P123DT22H14M12.011S")]
    client.duration_value.put([isodate.parse_duration("P123DT22H14M12.011S")])

@pytest.mark.asyncio
async def test_float32_value(client: ArrayClient):
    assert await client.float32_value.get() == [43.125]
    client.float32_value.put([43.125])

@pytest.mark.asyncio
async def test_int32_value(client: ArrayClient):
    assert await client.int32_value.get() == [1, 2]
    client.int32_value.put([1, 2])    

@pytest.mark.asyncio
async def test_int64_value(client: ArrayClient):
    assert await client.int64_value.get() == [2**53 - 1, -(2**53 - 1)]
    client.int64_value.put([2**53 - 1, -(2**53 - 1)])

@pytest.mark.asyncio
async def test_model_value(client: ArrayClient):
    assert await client.model_value.get() == [
        models.InnerModel(property="hello"),
        models.InnerModel(property="world"),
    ]
    client.model_value.put([
        models.InnerModel(property="hello"),
        models.InnerModel(property="world"),
    ])

@pytest.mark.asyncio
async def test_nullable_float_value(client: ArrayClient):
    assert await client.nullable_float_value.get() == [1.25, None, 3.0]
    client.nullable_float_value.put([1.25, None, 3.0])

@pytest.mark.asyncio
async def test_string_value(client: ArrayClient):
    assert await client.string_value.get() == ["hello", ""]
    client.string_value.put(["hello", ""])

@pytest.mark.asyncio
async def test_unknown_value(client: ArrayClient):
    assert await client.unknown_value.get() == [1, "hello", None]
    client.unknown_value.put([1, "hello", None])

