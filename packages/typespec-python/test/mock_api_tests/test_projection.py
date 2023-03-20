# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from projectedname import ProjectedNameClient
from projectedname.models import Project

@pytest.fixture
def client():
    with ProjectedNameClient() as client:
        yield client

def test_json_projection(client):
    client.json_projection(Project(produced_by="DPG"))

def test_client_projection(client):
    client.client_projection(Project(created_by="DPG"))

def test_language_projection(client):
    client.language_projection(Project(made_for_python="customers"))
