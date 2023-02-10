# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from _specs_.azure.core.aio import CoreClient


@pytest.fixture
async def client():
    async with CoreClient(api_version="") as client:
        yield client


@pytest.mark.asyncio
async def test_create_or_update(client):
    result = await client.create_or_update(id=1, resource={"name": "Madge"})
    assert result.id == 1
    assert result.name == "Madge"


@pytest.mark.asyncio
async def test_create_or_replace(client):
    result = await client.create_or_replace(id=1, resource={"name": "Madge"})
    assert result.id == 1
    assert result.name == "Madge"


@pytest.mark.asyncio
async def test_get(client):
    result = await client.get(id=1)
    assert result.id == 1
    assert result.name == "Madge"


@pytest.mark.asyncio
async def test_list(client):
    result = client.list()
    result = [item async for item in result]
    assert result[0].id == 1
    assert result[0].name == "Madge"
    assert result[1].id == 2
    assert result[1].name == "John"

@pytest.mark.asyncio
async def test_delete(client):
    await client.delete(id=1)

@pytest.mark.asyncio
async def test_export(client):
    result = await client.export(id=1, format="json")
    assert result.id == 1
    assert result.name == "Madge"
