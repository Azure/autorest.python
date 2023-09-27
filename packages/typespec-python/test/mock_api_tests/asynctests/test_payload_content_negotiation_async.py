# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Iterator
import base64
import pytest
from pathlib import Path
from payload.contentnegotiation.aio import ContentNegotiationClient
from payload.contentnegotiation.models import PngImageAsJson
from ..utils.validation import iter_bytes_to_bytes_async

FILE_FOLDER = Path(__file__).parent.parent

@pytest.fixture
async def client():
    async with ContentNegotiationClient(endpoint="http://localhost:3000") as client:
        yield client

@pytest.fixture
def png_data() -> bytes:
    with open(str(FILE_FOLDER / "data/image.png"), "rb") as file_in:
        return file_in.read()

@pytest.fixture
def jpg_data() -> bytes:
    with open(str(FILE_FOLDER / "data/image.jpg"), "rb") as file_in:
        return file_in.read()

@pytest.mark.asyncio
async def test_get_avatar_as_png(client: ContentNegotiationClient, png_data: bytes):
    result = await client.same_body.get_avatar_as_png(stream=True)
    assert await iter_bytes_to_bytes_async(result) == png_data

@pytest.mark.asyncio
async def test_get_avatar_as_jpeg(client: ContentNegotiationClient, jpg_data: bytes):
    result = await client.same_body.get_avatar_as_jpeg(stream=True)
    assert await iter_bytes_to_bytes_async(result) == jpg_data

@pytest.mark.asyncio
async def test_different_body_get_avatar_as_png(client: ContentNegotiationClient, png_data: bytes):
    result = await client.different_body.get_avatar_as_png(stream=True)
    assert await iter_bytes_to_bytes_async(result) == png_data

@pytest.mark.asyncio
async def test_different_body_get_avatar_as_json(client: ContentNegotiationClient, png_data: bytes):
    result = await client.different_body.get_avatar_as_json()
    expected = PngImageAsJson(content=base64.b64encode(png_data).decode())
    assert result == expected
