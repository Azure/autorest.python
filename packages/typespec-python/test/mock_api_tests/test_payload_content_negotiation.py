# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Iterator
import base64
import pytest
from pathlib import Path
from payload.contentnegotiation import ContentNegotiationClient
from payload.contentnegotiation.models import PngImageAsJson


FILE_FOLDER = Path(__file__).parent

@pytest.fixture
def client():
    with ContentNegotiationClient(endpoint="http://localhost:3000") as client:
        yield client

@pytest.fixture
def png_data() -> bytes:
    with open(str(FILE_FOLDER / "data/image.png"), "rb") as file_in:
        return file_in.read()

@pytest.fixture
def jpg_data() -> bytes:
    with open(str(FILE_FOLDER / "data/image.jpg"), "rb") as file_in:
        return file_in.read()

def iter_bytes_to_bytes(data: Iterator[bytes]) -> bytes:
    return b"".join(list(data))

def test_get_avatar_as_png(client: ContentNegotiationClient, png_data: bytes):
    result = client.same_body.get_avatar_as_png(stream=True)
    assert iter_bytes_to_bytes(result) == png_data

def test_get_avatar_as_jpeg(client: ContentNegotiationClient, jpg_data: bytes):
    result = client.same_body.get_avatar_as_jpeg(stream=True)
    assert iter_bytes_to_bytes(result) == jpg_data

def test_different_body_get_avatar_as_png(client: ContentNegotiationClient, png_data: bytes):
    result = client.different_body.get_avatar_as_png(stream=True)
    assert iter_bytes_to_bytes(result) == png_data

def test_different_body_get_avatar_as_json(client: ContentNegotiationClient, png_data: bytes):
    result = client.different_body.get_avatar_as_json()
    expected = PngImageAsJson(content=base64.b64encode(png_data).decode())
    assert result == expected
