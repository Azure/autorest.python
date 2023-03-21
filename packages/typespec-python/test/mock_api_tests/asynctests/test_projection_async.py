# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from projectedname.aio import ProjectedNameClient
from projectedname.models import Project

@pytest.fixture
async def client():
    async with ProjectedNameClient() as client:
        yield client

@pytest.mark.asyncio
async def test_json_projection(client):
    await client.json_projection(Project(produced_by="DPG"))

@pytest.mark.asyncio
async def test_client_projection(client):
    await client.client_projection(Project(created_by="DPG"))

@pytest.mark.asyncio
async def test_language_projection(client):
    await client.language_projection(Project(made_for_python="customers"))
