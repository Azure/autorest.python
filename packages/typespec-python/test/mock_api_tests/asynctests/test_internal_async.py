# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from internal.aio import InternalClient


@pytest.fixture
async def client():
    async with InternalClient() as client:
        yield client


async def test_get(client: InternalClient):
    result = await client._get_internal(name="test")
    assert result.name == "test"
