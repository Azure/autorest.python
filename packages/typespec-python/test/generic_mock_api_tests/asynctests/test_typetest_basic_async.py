# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import decimal

import pytest
from typetest.basic import aio


@pytest.fixture
async def client():
    async with aio.BasicClient() as client:
        yield client


@pytest.mark.parametrize(
    "og_name,val",
    [
        ("decimal_type", decimal.Decimal("0.33333")),
        ("decimal128_type", decimal.Decimal("0.33333")),
    ],
)
@pytest.mark.asyncio
async def test_array(client: aio.BasicClient, og_name: str, val: dict):
    og_group = getattr(client, og_name)
    assert await og_group.response_body() == val
    await og_group.request_body(val)
    await og_group.request_parameter(value=val)
