# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from headasboolean import aio, models

@pytest.fixture
async def client():
    async with aio.VisibilityClient() as client:
        yield client

@pytest.mark.asyncio
async def test_head(client):
    body = models.VisibilityModel(query_prop=123)
    await client.head_model(body) is None
