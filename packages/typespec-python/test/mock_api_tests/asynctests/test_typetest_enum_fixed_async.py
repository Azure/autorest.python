# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azure.core.exceptions import HttpResponseError
from typetest.enum.fixed import aio, models

@pytest.fixture
async def client():
    async with aio.FixedClient() as client:
        yield client

@pytest.mark.asyncio
async def test_known_value(client):
    assert await client.get_known_value() == models.DaysOfWeekEnum.MONDAY
    await client.put_known_value(models.DaysOfWeekEnum.MONDAY)

@pytest.mark.asyncio
async def test_unknown_value(client):
    try:
        await client.put_unknown_value("Weekend")
    except HttpResponseError as err:
        assert err.status_code == 500
