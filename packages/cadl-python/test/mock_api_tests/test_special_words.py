# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from specialwords import SpecialWordsClient,  models

@pytest.fixture
def client():
    with SpecialWordsClient() as client:
        yield client

def test_operation_for(client: SpecialWordsClient):
    client.operation.for_method()

def test_parameter_if(client: SpecialWordsClient):
    client.parameter.get_with_if(if_parameter="weekend")

def test_parameter_filter(client: SpecialWordsClient):
    client.parameter.get_with_filter(filter="abc*.")

def test_model_get(client: SpecialWordsClient):
    assert client.model.get() == models.DerivedModel(derived_name="my.name", for_property="value")

def test_model_put(client: SpecialWordsClient):
    client.model.put(models.DerivedModel(derived_name="my.name", for_property="value"))