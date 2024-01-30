# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from projection.clientnameandencodedname import ClientNameAndEncodedNameClient, models

@pytest.fixture
def client():
    with ClientNameAndEncodedNameClient() as client:
        yield client

def test_property_json(client: ClientNameAndEncodedNameClient):
    client.property.json(models.JsonAndClientClientNameAndEncodedNameModel(client_name=True))

def test_property_client(client: ClientNameAndEncodedNameClient):
    client.property.client(models.ClientClientNameAndEncodedNameModel(client_name=True))

def test_property_language(client: ClientNameAndEncodedNameClient):
    client.property.language(models.LanguageClientNameAndEncodedNameModel(python_name=True))

def test_property_json_and_client(client: ClientNameAndEncodedNameClient):
    client.property.json_and_client(models.JsonAndClientClientNameAndEncodedNameModel(client_name=True))

def test_operation(client: ClientNameAndEncodedNameClient):
    # test that projected client name for operation is client_name
    client.client_name()

def test_parameter(client: ClientNameAndEncodedNameClient):
    client.parameter(client_name="true")

def test_model_client(client: ClientNameAndEncodedNameClient):
    client.model.client(models.ClientModel(default_name=True))

def test_model_language(client: ClientNameAndEncodedNameClient):
    client.model.language(models.PythonModel(default_name=True))
