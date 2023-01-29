# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from server.parameterized.aio import ParameterizedClient


@pytest.fixture
async def client():
    async with ParameterizedClient() as client:
        yield client


@pytest.mark.asyncio
async def test_my_op(client):
    assert await client.my_op() is True
