# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.union import UnionClient
from typetest.union import models

@pytest.fixture
def client():
    with UnionClient() as client:
        yield client

# def test_send_int(client):
#     client.send_int(models.ModelWithSimpleUnionProperty(simple_union=1))

# def test_send_int_array(client):
#     client.send_int_array(models.ModelWithSimpleUnionProperty(simple_union=[1, 2]))

# def test_send_first_named_union_value(client):
#     client.send_first_named_union_value(models.ModelWithNamedUnionProperty(named_union=models.Model1(name="model1", prop1=1)))

# def test_send_second_named_union_value(client):
#     client.send_second_named_union_value(models.ModelWithNamedUnionProperty(named_union=models.Model2(name="model2", prop2=2)))

# def test_receive_string(client):
#     assert client.receive_string() == models.ModelWithSimpleUnionPropertyInResponse(simple_union="string")

# def test_receive_int_array(client):
#     assert client.receive_int_array() == models.ModelWithSimpleUnionPropertyInResponse(simple_union=[1, 2])

# def test_receive_first_named_union_value(client):
#     assert client.receive_first_named_union_value() == models.ModelWithNamedUnionPropertyInResponse(named_union=models.Model1(name="model1", prop1=1))

# def test_receive_second_named_union_value(client):
#     assert client.receive_second_named_union_value() == models.ModelWithNamedUnionPropertyInResponse(named_union=models.Model2(name="model2", prop2=2))
