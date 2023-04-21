# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from types.union import UnionClient
from types.union.models import ModelWithNamedUnionProperty, ModelWithSimpleUnionProperty, Model1, Model2

@pytest.fixture
def client():
    with UnionClient() as client:
        yield client

def test_send_int(client):
    client.send_int(ModelWithSimpleUnionProperty(simple_union=1))

def test_send_int_array(client):
    client.send_int_array(ModelWithSimpleUnionProperty(simple_union=[1, 2]))

def test_send_first_named_union_value(client):
    client.send_first_named_union_value(ModelWithNamedUnionProperty(named_union=Model1(name="model1", prop1=1)))

def test_send_second_named_union_value(client):
    client.send_second_named_union_value(ModelWithNamedUnionProperty(named_union=Model2(name="model2", prop2=2)))
