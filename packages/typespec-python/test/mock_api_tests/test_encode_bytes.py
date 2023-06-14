# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import datetime

import pytest
from encode.bytes import BytesClient
from encode.bytes.models import (
    BytesProperty,
)


@pytest.fixture
def client():
    with BytesClient() as client:
        yield client


def test_query(client: BytesClient):
    client.query.get(
        default=bytes("test", "utf-8"),
        base64=bytes("test", "utf-8"),
        base64url=bytes("test", "utf-8"),
        base64url_array=[
            bytes("test", "utf-8"),
            bytes("test", "utf-8"),
        ],
    )


def test_property(client: BytesClient):
    result = client.property.post(
        BytesProperty(
            default=bytes("test", "utf-8"),
            base64=bytes("test", "utf-8"),
            base64url=bytes("test", "utf-8"),
            base64url_array=[
                bytes("test", "utf-8"),
                bytes("test", "utf-8"),
            ],
        )
    )
    assert result.default == bytes("test", "utf-8")
    assert result.base64 == bytes("test", "utf-8")
    assert result.base64url == bytes("test", "utf-8")
    assert result.base64url_array == [
        bytes("test", "utf-8"),
        bytes("test", "utf-8"),
    ]


def test_header(client: BytesClient):
    client.header.get(
        default=bytes("test", "utf-8"),
        base64=bytes("test", "utf-8"),
        base64url=bytes("test", "utf-8"),
        base64url_array=[
            bytes("test", "utf-8"),
            bytes("test", "utf-8"),
        ],
    )
