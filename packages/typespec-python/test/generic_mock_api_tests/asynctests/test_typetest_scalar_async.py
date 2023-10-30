# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
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
