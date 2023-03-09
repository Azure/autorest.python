# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from _specs_.azure.core.aio import CoreClient


@pytest.fixture
async def client():
    async with CoreClient() as client:
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
    result = client.list(
        top=5,
        skip=10,
        orderby=["id"],
        filter="id lt 10",
        select=["id", "orders", "etag"],
        expand=["orders"],
    )
    result = [item async for item in result]
    assert len(result) == 2
    assert result[0].id == 1
    assert result[0].name == "Madge"
    assert result[0].etag == "11bdc430-65e8-45ad-81d9-8ffa60d55b59"
    assert result[0].orders[0].id == 1
    assert result[0].orders[0].user_id == 1
    assert result[0].orders[0].detail == "a recorder"
    assert result[1].id == 2
    assert result[1].name == "John"
    assert result[1].etag == "11bdc430-65e8-45ad-81d9-8ffa60d55b5a"
    assert result[1].orders[0].id == 2
    assert result[1].orders[0].user_id == 2
    assert result[1].orders[0].detail == "a TV"


@pytest.mark.asyncio
async def test_list_with_page(client):
    result = client.list_with_page()
    result = [item async for item in result]
    assert len(result) == 1
    assert result[0].id == 1
    assert result[0].name == "Madge"
    assert result[0].etag == "11bdc430-65e8-45ad-81d9-8ffa60d55b59"
    assert result[0].orders is None


@pytest.mark.asyncio
async def test_delete(client):
    await client.delete(id=1)


@pytest.mark.asyncio
async def test_export(client):
    result = await client.export(id=1, format="json")
    assert result.id == 1
    assert result.name == "Madge"
