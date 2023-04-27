# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from _specs_.azure.clientgenerator.core.internal.aio import InternalClient


@pytest.fixture
async def client():
    async with InternalClient() as client:
        yield client


@pytest.mark.asyncio
async def test_public_only(client: InternalClient):
    result = await client.public_only(name="test")
    assert result.name == "test"


@pytest.mark.asyncio
async def test_internal_only(client: InternalClient):
    result = await client._internal_only(name="test")
    assert result.name == "test"


@pytest.mark.asyncio
async def test_shared_public(client: InternalClient):
    result = await client.shared.public(name="test")
    assert result.name == "test"


@pytest.mark.asyncio
async def test_shared_internal(client: InternalClient):
    result = await client.shared._internal(name="test")
    assert result.name == "test"


@pytest.mark.asyncio
async def test_visibility(client: InternalClient):
    from _specs_.azure.clientgenerator.core.internal.models import (
        PublicModel,
        SharedModel,
    )

    with pytest.raises(ImportError):
        from _specs_.azure.clientgenerator.core.internal.models import InternalModel

    with pytest.raises(AttributeError):
        client.internal_only(name="test")

    with pytest.raises(AttributeError):
        client.shared.internal(name="test")
