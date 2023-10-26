# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from projection.projectedname import aio, models

@pytest.fixture
async def client():
    async with aio.ProjectedNameClient() as client:
        yield client

@pytest.mark.asyncio
async def test_property_json(client: aio.ProjectedNameClient):
    await client.property.json(models.JsonAndClientProjectedNameModel(client_name=True))

@pytest.mark.asyncio
async def test_property_client(client: aio.ProjectedNameClient):
    await client.property.client(models.ClientProjectedNameModel(client_name=True))

@pytest.mark.asyncio
async def test_property_language(client: aio.ProjectedNameClient):
    await client.property.language(models.LanguageProjectedNameModel(python_name=True))

@pytest.mark.asyncio
async def test_property_json_and_client(client: aio.ProjectedNameClient):
    await client.property.json_and_client(models.JsonAndClientProjectedNameModel(client_name=True))

@pytest.mark.asyncio
async def test_operation(client: aio.ProjectedNameClient):
    # test that projected client name for operation is client_name
    await client.client_name()

@pytest.mark.asyncio
async def test_parameter(client: aio.ProjectedNameClient):
    await client.parameter(client_name="true")
