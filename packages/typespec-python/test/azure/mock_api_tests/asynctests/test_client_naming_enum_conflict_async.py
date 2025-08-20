# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from client.naming.enumconflict.aio import EnumConflictClient
from client.naming.enumconflict import models


@pytest.fixture
async def client():
    async with EnumConflictClient() as client:
        yield client


@pytest.mark.asyncio
async def test_first_operations_first_async(client: EnumConflictClient):
    """Test enum with same name in different namespace - first namespace (async)."""
    body = models.FirstModel(status=models.Status.ACTIVE, name="test")

    response = await client.first_operations.first(body=body)

    assert response.status == "active"
    assert response.name == "test"


@pytest.mark.asyncio
async def test_second_operations_second_async(client: EnumConflictClient):
    """Test enum with same name in different namespace - second namespace (async)."""
    body = models.SecondModel(status=models.SecondStatus.RUNNING, description="test description")

    response = await client.second_operations.second(body=body)

    assert response.status == "running"
    assert response.description == "test description"
