# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azure.lro.basic import LroClient

@pytest.fixture
def client():
    with LroClient() as client:
        yield client

def test_lro_basic_put(client):
    result = client.begin_create(polling_interval=0).result()
    assert result.name == "bob"
