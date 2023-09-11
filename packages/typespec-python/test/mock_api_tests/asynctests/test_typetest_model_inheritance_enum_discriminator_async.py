# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the proasync async def ject root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.model.enumdiscriminator.aio import EnumDiscriminatorClient
from typetest.model.enumdiscriminator import models


@pytest.fixture
async def client():
    async with EnumDiscriminatorClient() as client:
        yield client


@pytest.fixture
async def valid_body():
    return models.Golden(weight=10)

@pytest.fixture
async def valid_fixed_body():
    return models.Cobra(length=10)

@pytest.mark.asyncio
async def test_get_extensible_model(client, valid_body):
    assert await client.get_extensible_model() == valid_body


@pytest.mark.asyncio
async def test_put_extensible_model(client, valid_body):
    await client.put_extensible_model(valid_body)

@pytest.mark.asyncio
async def test_get_extensible_model_missing_discriminator(client):
    assert await client.get_extensible_model_missing_discriminator() == models.Dog(weight=10)

@pytest.mark.asyncio
async def test_get_extensible_model_wrong_discriminator(client):
    assert await client.get_extensible_model_wrong_discriminator() == models.Dog(weight=8, kind="wrongKind")

@pytest.mark.asyncio
async def test_get_fixed_model(client, valid_fixed_body):
    assert await client.get_fixed_model() == valid_fixed_body

@pytest.mark.asyncio
async def test_put_fixed_model(client, valid_fixed_body):
    await client.put_fixed_model(valid_fixed_body)

@pytest.mark.asyncio
async def test_get_fixed_model_missing_discriminator(client):
    assert await client.get_fixed_model_missing_discriminator() == models.Snake(length=10)

@pytest.mark.asyncio
async def test_get_fixed_model_wrong_discriminator(client):
    assert await client.get_fixed_model_wrong_discriminator() == models.Snake(length=8, kind="wrongKind")
