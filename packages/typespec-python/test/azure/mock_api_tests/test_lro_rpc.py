# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azurecore.lro.rpc import RpcClient
from azurecore.lro.rpc.models import GenerationOptions, GenerationResult

@pytest.fixture
def client():
    with RpcClient() as client:
        yield client

def test_lro_rpc_long_running_rpc(client):
    result = client.begin_long_running_rpc(GenerationOptions(prompt="text"), polling_interval=0).result()
    assert result == GenerationResult(data="text data")
