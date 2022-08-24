# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from hello.aio import HelloClient

@pytest.fixture
async def client():
    async with HelloClient() as client:
        yield client

@pytest.mark.asyncio
async def test_get(client):
    assert await client.world() == "Hello World!"
