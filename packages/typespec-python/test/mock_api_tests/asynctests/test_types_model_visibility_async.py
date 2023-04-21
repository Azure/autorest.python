# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from types.model.visibility import aio, models

@pytest.fixture
async def client():
    async with aio.VisibilityClient() as client:
        yield client

@pytest.mark.asyncio
async def test_read(client):
    body = models.VisibilityModel(query_prop=123)
    assert (await client.get_model(body)).read_prop == "abc"

@pytest.mark.asyncio
async def test_head(client):
    body = models.VisibilityModel(query_prop=123)
    await client.head_model(body)

@pytest.mark.asyncio
async def test_put(client):
    body = models.VisibilityModel(
        create_prop= ["foo", "bar"],
        update_prop= [1, 2],
    )
    await client.put_model(body)

@pytest.mark.asyncio
async def test_patch(client):
    body = models.VisibilityModel(
        update_prop=[1, 2],
    )
    await client.patch_model(body)

@pytest.mark.asyncio
async def test_post(client):
    body = models.VisibilityModel(
        create_prop=["foo", "bar"],
    )
    await client.post_model(body)

@pytest.mark.asyncio
async def test_delete(client):
    body = models.VisibilityModel(
        delete_prop=True,
    )
    await client.delete_model(body)
