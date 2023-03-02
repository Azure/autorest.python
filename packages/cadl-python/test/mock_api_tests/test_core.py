# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from _specs_.azure.core import CoreClient

@pytest.fixture
def client():
    with CoreClient() as client:
        yield client

def test_create_or_update(client):
    result = client.create_or_update(id=1, resource={"name": "Madge"})
    assert result.id == 1
    assert result.name == "Madge"
    
def test_create_or_replace(client):
    result = client.create_or_replace(id=1, resource={"name": "Madge"})
    assert result.id == 1
    assert result.name == "Madge"
    
def test_get(client):
    result = client.get(id=1)
    assert result.id == 1
    assert result.name == "Madge"

def test_list(client):
    result = list(client.list())
    assert result[0].id == 1
    assert result[0].name == "Madge"
    assert result[1].id == 2
    assert result[1].name == "John"

def test_delete(client):
    client.delete(id=1)

def test_export(client):
    result = client.export(id=1, format="json")
    assert result.id == 1
    assert result.name == "Madge"
