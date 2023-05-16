# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import datetime

import pytest
from encode.duration.aio import DurationClient
from encode.duration.models import (
    Int32SecondsDurationProperty,
    ISO8601DurationProperty,
    FloatSecondsDurationProperty,
    DefaultDurationProperty,
)


@pytest.fixture
async def client():
    async with DurationClient() as client:
        yield client


@pytest.mark.asyncio
async def test_query(client: DurationClient):
    await client.query.default(input=datetime.timedelta(days=40))
    await client.query.iso8601(input=datetime.timedelta(days=40))
    await client.query.int32_seconds(input=36)
    await client.query.float_seconds(input=35.621)


@pytest.mark.asyncio
async def test_property(client: DurationClient):
    result = await client.property.default(
        DefaultDurationProperty(value=datetime.timedelta(days=40))
    )
    assert result.value == datetime.timedelta(days=40)
    result = await client.property.default(DefaultDurationProperty(value="P40D"))
    assert result.value == datetime.timedelta(days=40)
    result = await client.property.iso8601(
        ISO8601DurationProperty(value=datetime.timedelta(days=40))
    )
    assert result.value == datetime.timedelta(days=40)
    result = await client.property.iso8601(ISO8601DurationProperty(value="P40D"))
    assert result.value == datetime.timedelta(days=40)
    result = await client.property.int32_seconds(Int32SecondsDurationProperty(value=36))
    assert result.value == 36
    result = await client.property.float_seconds(
        FloatSecondsDurationProperty(value=35.621)
    )
    assert abs(result.value - 35.621) < 0.0001
