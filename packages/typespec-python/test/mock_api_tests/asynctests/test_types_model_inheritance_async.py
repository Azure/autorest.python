# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from types.model.inheritance.aio import InheritanceClient
from types.model.inheritance import models

@pytest.fixture
async def client():
    async with InheritanceClient() as client:
        yield client

@pytest.fixture
async def valid_body():
    return models.Siamese({ "name": "abc", "age": 32, "smart": True })

@pytest.mark.asyncio
async def test_get_valid(client, valid_body):
    assert await client.get_valid() == valid_body

@pytest.mark.asyncio
async def test_post_valid(client, valid_body):
    await client.post_valid(valid_body)

@pytest.mark.asyncio
async def test_put_valid(client, valid_body):
    assert await client.put_valid(valid_body) == valid_body

@pytest.fixture
def polymorphic_body():
    return models.GoblinShark({"age": 1})

@pytest.mark.asyncio
async def test_polymorhic_put_model(client, polymorphic_body):
    await client.put_model(polymorphic_body)

@pytest.mark.asyncio
async def test_polymorhic_get_model(client, polymorphic_body):
    assert await client.get_model() == polymorphic_body


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

@pytest.mark.asyncio
async def test_put_recursive_body(client, recursive_body):
    await client.put_recursive_model(recursive_body)

@pytest.mark.asyncio
async def test_get_recursive_body(client, recursive_body):
    assert await client.get_recursive_model() == recursive_body

@pytest.mark.asyncio
async def test_get_missing_discriminator(client):
    assert await client.get_missing_discriminator() == models.Fish(age=1)

@pytest.mark.asyncio
async def test_get_wrong_discriminator(client):
    assert await client.get_wrong_discriminator() == models.Fish(age=1, kind="wrongKind")
