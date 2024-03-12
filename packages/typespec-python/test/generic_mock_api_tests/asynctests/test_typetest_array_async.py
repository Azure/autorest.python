# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import pytest
import isodate
from typetest.array import models, aio

@pytest.fixture
async def client():
    async with aio.ArrayClient() as client:
        yield client

@pytest.mark.parametrize(
    "og_name,val", [
        ("int32_value", [1, 2]),
        ("int64_value",  [2**53-1, -(2**53-1)]),
        ("boolean_value", [True, False]),
        ("string_value", ["hello", ""]),
        ("float32_value", [43.125]),
        ("datetime_value",  [isodate.parse_datetime("2022-08-26T18:38:00Z")]),
        ("duration_value", [isodate.parse_duration("P123DT22H14M12.011S")]),
        ("unknown_value", [1, "hello", None]),
        ("model_value", [
            models.InnerModel(property="hello"),
            models.InnerModel(property="world"),
        ]),
    ]
)
@pytest.mark.asyncio
async def test_array(client: aio.ArrayClient, og_name: str, val: dict):
    og_group = getattr(client, og_name)
    assert await og_group.get() == val
    await og_group.put(val)
