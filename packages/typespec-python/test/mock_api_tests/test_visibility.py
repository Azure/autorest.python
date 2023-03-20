# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from models.visibility.automatic import AutomaticClient, models

@pytest.fixture
def client():
    with AutomaticClient() as client:
        yield client

def test_read(client):
    body = models.VisibilityModel(query_prop=123)
    assert client.get_model(body).read_prop == "abc"

def test_head(client):
    body = models.VisibilityModel(query_prop=123)
    client.head_model(body)

def test_put(client):
    body = models.VisibilityModel(
        create_prop= ["foo", "bar"],
        update_prop= [1, 2],
    )
    client.put_model(body)

def test_patch(client):
    body = models.VisibilityModel(
        update_prop=[1, 2],
    )
    client.patch_model(body)

def test_post(client):
    body = models.VisibilityModel(
        create_prop=["foo", "bar"],
    )
    client.post_model(body)

def test_delete(client):
    body = models.VisibilityModel(
        delete_prop=True,
    )
    client.delete_model(body)
