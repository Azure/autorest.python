# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azure.lro.aio import LroClient

@pytest.fixture
async def client():
    async with LroClient() as client:
        yield client

@pytest.mark.asyncio
async def test_lro_basic_put(client):
    result = await (await client.begin_create(polling_interval=0)).result()
    assert result.name == "bob"
