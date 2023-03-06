# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from overload.aio import OverloadClient
from overload.models import Data

@pytest.fixture
async def client():
    async with OverloadClient() as client:
        yield client

@pytest.mark.asyncio
async def test_upload_bytes_or_string(client):
    await client.upload_bytes_or_string("hello world")
    await client.upload_bytes_or_string(b"hello world")


@pytest.mark.asyncio
async def test_upload_json_or_string(client):
    await client.upload_json_or_string({"hello": "world"})
    await client.upload_json_or_string(Data(hello="world"))
    await client.upload_json_or_string("hello world")
