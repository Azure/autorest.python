# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from apitest.limit.aio import LimitClient
from azure.core.exceptions import ResourceNotFoundError

@pytest.fixture
async def client():
    async with LimitClient() as client:
        yield client

# actually SDK does not validate the length of the name
@pytest.mark.asyncio
async def test_limit_length(client: LimitClient):
    with pytest.raises(ResourceNotFoundError):
        await client.length(name="ok")
