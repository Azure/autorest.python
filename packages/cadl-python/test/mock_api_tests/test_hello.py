# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from hello import Hello

@pytest.fixture
def client():
    with Hello() as client:
        yield client

def test_get(client):
    assert client.world() == "Hello World!"
