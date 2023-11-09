# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azurecore.lro.rpc.aio import RpcClient
from azurecore.lro.rpc import models


@pytest.fixture
async def client():
    async with RpcClient() as client:
        yield client

# cadl-ranch check api-version in poll request which is not supported by azure-core
# @pytest.mark.asyncio
# async def test_long_running_rpc(client: RpcClient):
#     result = await client.begin_long_running_rpc(models.GenerationOptions(prompt="text"))
#     assert (await result.result()) == models.GenerationResult(data="text data")
