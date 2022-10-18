# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from telnetlib import SE
import pytest
from clients.multiple import MainClient, SecondaryClient, models

@pytest.fixture
def main_client():
    with MainClient(endpoint="") as client:
        yield client

@pytest.fixture
def secondary_client():
    with SecondaryClient(endpoint="") as client:
        yield client

def test_main_get(main_client: MainClient):
    assert main_client.get() == models.Model(id="hello")

def test_secondary_get(secondary_client: SecondaryClient):
    assert secondary_client.get() == "hello, world!"
