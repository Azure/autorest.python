# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import datetime

import pytest
from encode.bytes.aio import BytesClient
from encode.bytes.models import (
    DefaultBytesProperty,
    Base64urlBytesProperty,
    Base64BytesProperty,
    Base64urlArrayBytesProperty,
)


@pytest.fixture
async def client():
    async with BytesClient() as client:
        yield client


@pytest.mark.asyncio
async def test_query(client: BytesClient):
    await client.query.default(
        value=bytes("test", "utf-8"),
    )
    await client.query.base64(
        value=bytes("test", "utf-8"),
    )
    await client.query.base64url(
        value=bytes("test", "utf-8"),
    )
    await client.query.base64url_array(
        value=[
            bytes("test", "utf-8"),
            bytes("test", "utf-8"),
        ],
    )


@pytest.mark.asyncio
async def test_property(client: BytesClient):
    result = await client.property.default(
        DefaultBytesProperty(
            value=bytes("test", "utf-8"),
        )
    )
    assert result.value == bytes("test", "utf-8")

    result = await client.property.base64(
        Base64BytesProperty(
            value=bytes("test", "utf-8"),
        )
    )
    assert result.value == bytes("test", "utf-8")

    result = await client.property.base64url(
        Base64urlBytesProperty(
            value=bytes("test", "utf-8"),
        )
    )
    assert result.value == bytes("test", "utf-8")

    result = await client.property.base64url_array(
        Base64urlArrayBytesProperty(
            value=[
                bytes("test", "utf-8"),
                bytes("test", "utf-8"),
            ],
        )
    )
    assert result.value == [
        bytes("test", "utf-8"),
        bytes("test", "utf-8"),
    ]


@pytest.mark.asyncio
async def test_header(client: BytesClient):
    await client.header.default(
        value=bytes("test", "utf-8"),
    )
    await client.header.base64(
        value=bytes("test", "utf-8"),
    )
    await client.header.base64url(
        value=bytes("test", "utf-8"),
    )
    await client.header.base64url_array(
        value=[
            bytes("test", "utf-8"),
            bytes("test", "utf-8"),
        ],
    )
