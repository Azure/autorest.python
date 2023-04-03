# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azure.lro.core import CoreClient
from azure.lro.core.models import User, ExportedUser

@pytest.fixture
def client():
    with CoreClient() as client:
        yield client

def test_lro_core_put(client):
    user = User({"name": "madge", "role": "contributor"})
    result = client.begin_create_or_replace(name=user.name, resource=user, polling_interval=0).result()
    assert result == user

def test_lro_core_delete(client):
    client.begin_delete(name="madge", polling_interval=0).result()

def test_lro_core_export(client):
    export_user = ExportedUser({ "name": "madge", "resourceUri": "/users/madge" })
    result = client.begin_export(name="madge", format="json", polling_interval=0).result()
    print(result)
    assert result == export_user
