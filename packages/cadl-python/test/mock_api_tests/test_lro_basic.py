# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azure.lro import AzureLro

@pytest.fixture
def client():
    with AzureLro() as client:
        yield client

def test_lro_basic_put(client):
    result = client.polling_success.begin_create(polling_interval=0).result()
    assert result == "Test for polling succeed"
