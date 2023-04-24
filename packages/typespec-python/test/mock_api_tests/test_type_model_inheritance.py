# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from type.model.inheritance import InheritanceClient, models

@pytest.fixture
def client():
    with InheritanceClient() as client:
        yield client

@pytest.fixture
def valid_body():
    return models.Siamese({ "name": "abc", "age": 32, "smart": True })

def test_get_valid(client, valid_body):
    assert client.get_valid() == valid_body

def test_post_valid(client, valid_body):
    client.post_valid(valid_body)

def test_put_valid(client, valid_body):
    assert client.put_valid(valid_body) == valid_body

@pytest.fixture
def polymorphic_body():
    return models.GoblinShark({"age": 1})

def test_polymorhic_put_model(client, polymorphic_body):
    client.put_model(polymorphic_body)

def test_polymorhic_get_model(client, polymorphic_body):
    assert client.get_model() == polymorphic_body


@pytest.fixture
def recursive_body():
    return models.Salmon({
        "age": 1,
        "kind": "salmon",
        "partner": {
            "age": 2,
            "kind": "shark",
            "sharktype": "saw",
        },
        "friends": [
            {
            "age": 2,
            "kind": "salmon",
            "partner": {
                "age": 3,
                "kind": "salmon",
            },
            "hate": {
                "key1": {
                "age": 4,
                "kind": "salmon",
                },
                "key2": {
                "age": 2,
                "kind": "shark",
                "sharktype": "goblin",
                },
            },
            },
            {
            "age": 3,
            "kind": "shark",
            "sharktype": "goblin",
            },
        ],
        "hate": {
            "key3": {
            "age": 3,
            "kind": "shark",
            "sharktype": "saw",
            },
            "key4": {
            "age": 2,
            "kind": "salmon",
            "friends": [
                {
                "age": 1,
                "kind": "salmon",
                },
                {
                "age": 4,
                "kind": "shark",
                "sharktype": "goblin",
                },
            ],
            },
        },
})

def test_put_recursive_body(client, recursive_body):
    client.put_recursive_model(recursive_body)

def test_get_recursive_body(client, recursive_body):
    assert client.get_recursive_model() == recursive_body

def test_get_missing_discriminator(client):
    assert client.get_missing_discriminator() == models.Fish(age=1)

def test_get_wrong_discriminator(client):
    assert client.get_wrong_discriminator() == models.Fish(age=1, kind="wrongKind")
