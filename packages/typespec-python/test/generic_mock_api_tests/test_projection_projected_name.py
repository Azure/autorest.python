# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from projection.projectedname import ProjectedNameClient, models

@pytest.fixture
def client():
    with ProjectedNameClient() as client:
        yield client

def test_property_json(client: ProjectedNameClient):
    client.property.json(models.JsonAndClientProjectedNameModel(client_name=True))

def test_property_client(client: ProjectedNameClient):
    client.property.client(models.ClientProjectedNameModel(client_name=True))

def test_property_language(client: ProjectedNameClient):
    client.property.language(models.LanguageProjectedNameModel(python_name=True))

def test_property_json_and_client(client: ProjectedNameClient):
    client.property.json_and_client(models.JsonAndClientProjectedNameModel(client_name=True))

def test_operation(client: ProjectedNameClient):
    # test that projected client name for operation is client_name
    client.client_name()

def test_parameter(client: ProjectedNameClient):
    client.parameter(client_name="true")

def test_model_client(client: ProjectedNameClient):
    client.model.client(models.ClientModel(default_name=True))

def test_model_language(client: ProjectedNameClient):
    client.model.language(models.PythonModel(default_name=True))
