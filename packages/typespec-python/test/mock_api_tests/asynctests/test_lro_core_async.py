# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azure.lro.core.aio import CoreClient
from azure.lro.core.models import User

@pytest.fixture
async def client():
    async with CoreClient() as client:
        yield client

@pytest.mark.asyncio
async def test_lro_core_put(client):
    user = User({"name": "madge", "role": "contributor"})
    result = await (await client.begin_create_or_replace(name=user.name, resource=user, polling_interval=0)).result()
    assert result == user

@pytest.mark.asyncio
async def test_lro_core_delete(client):
    await (await client.begin_delete(name="madge", polling_interval=0)).result()

@pytest.mark.asyncio
async def test_lro_core_delete(client):
    export_user = { "name": "madge", "resourceUri": "/users/madge" }
    result = await (await client.begin_export(name="madge", polling_interval=0)).result()
    assert result == export_user
