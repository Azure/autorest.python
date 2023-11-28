# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import decimal
from functools import reduce

import pytest
from typetest.scalar.aio import ScalarClient


@pytest.fixture
async def client():
    async with ScalarClient() as client:
        yield client


@pytest.mark.parametrize(
    "og_name,val",
    [
        ("string", "test"),
        ("boolean", True),
        ("unknown", "test"),
    ],
)
@pytest.mark.asyncio
async def test_scalar(client: ScalarClient, og_name: str, val: dict):
    og_group = getattr(client, og_name)
    assert await og_group.get() == val
    await og_group.put(val)


@pytest.mark.parametrize(
    "og_name,val",
    [
        ("decimal_type", decimal.Decimal("0.33333")),
        ("decimal128_type", decimal.Decimal("0.33333")),
    ],
)
@pytest.mark.asyncio
async def test_type(client: ScalarClient, og_name: str, val):
    og_group = getattr(client, og_name)
    assert await og_group.response_body() == val
    await og_group.request_body(val)
    await og_group.request_parameter(value=val)


@pytest.mark.parametrize(
    "og_name",
    [
        "decimal_verify",
        "decimal128_verify",
    ],
)
@pytest.mark.asyncio
async def test_verify(client: ScalarClient, og_name: str):
    og_group = getattr(client, og_name)
    prepare = await og_group.prepare_verify()
    await og_group.verify(reduce(lambda x, y: x + y, prepare))
