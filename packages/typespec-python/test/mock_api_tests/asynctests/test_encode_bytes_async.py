# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import datetime

import pytest
from encode.bytes.aio import BytesClient
from encode.bytes.models import (
    BytesProperty,
)


@pytest.fixture
async def client():
    async with BytesClient() as client:
        yield client


async def test_query(client: BytesClient):
    await client.query(
        default=bytes("test", "utf-8"),
        base64=bytes("test", "utf-8"),
        base64url=bytes("test", "utf-8"),
        base64_array=[
            bytes("test", "utf-8"),
            bytes("test", "utf-8"),
        ],
    )


async def test_property(client: BytesClient):
    result = await client.property(
        BytesProperty(
            default=bytes("test", "utf-8"),
            base64=bytes("test", "utf-8"),
            base64url=bytes("test", "utf-8"),
            base64_array=[
                bytes("test", "utf-8"),
                bytes("test", "utf-8"),
            ],
        )
    )
    assert result.default == bytes("test", "utf-8")
    assert result.base64 == bytes("test", "utf-8")
    assert result.base64url == bytes("test", "utf-8")
    assert result.base64_array == [
        bytes("test", "utf-8"),
        bytes("test", "utf-8"),
    ]


async def test_header(client: BytesClient):
    await client.header(
        default=bytes("test", "utf-8"),
        base64=bytes("test", "utf-8"),
        base64url=bytes("test", "utf-8"),
        base64_array=[
            bytes("test", "utf-8"),
            bytes("test", "utf-8"),
        ],
    )
