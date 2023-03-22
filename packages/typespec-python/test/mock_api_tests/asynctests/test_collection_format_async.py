# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from collectionformat.aio import CollectionFormatClient


@pytest.fixture
async def client():
    async with CollectionFormatClient() as client:
        yield client


@pytest.mark.asyncio
async def test_multi(client: CollectionFormatClient):
    await client.test_multi(colors=["blue", "red", "green"])


@pytest.mark.asyncio
async def test_csv(client: CollectionFormatClient):
    await client.test_csv(colors=["blue", "red", "green"])


@pytest.mark.asyncio
async def test_csv_header(client: CollectionFormatClient):
    await client.test_csv_header(colors=["blue", "red", "green"])


@pytest.mark.asyncio
async def test_default_header(client: CollectionFormatClient):
    await client.test_default_header(colors=["blue", "red", "green"])
