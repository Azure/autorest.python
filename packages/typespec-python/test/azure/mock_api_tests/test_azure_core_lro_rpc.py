# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azurecore.lro.rpc import RpcClient, models


@pytest.fixture
def client():
    with RpcClient() as client:
        yield client

# cadl-ranch check api-version in poll request which is not supported by azure-core
# def test_long_running_rpc(client: RpcClient):
#     result = client.begin_long_running_rpc(models.GenerationOptions(prompt="text")).result()
#     assert result == models.GenerationResult(data="text data")
