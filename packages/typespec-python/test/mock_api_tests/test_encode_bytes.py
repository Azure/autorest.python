# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import datetime

import pytest
from encode.bytes import BytesClient
from encode.bytes.models import (
    DefaultBytesProperty,
    Base64urlBytesProperty,
    Base64BytesProperty,
    Base64urlArrayBytesProperty,
)


@pytest.fixture
def client():
    with BytesClient() as client:
        yield client


def test_query(client: BytesClient):
    client.query.default(
        value=bytes("test", "utf-8"),
    )
    client.query.base64(
        value=bytes("test", "utf-8"),
    )
    client.query.base64url(
        value=bytes("test", "utf-8"),
    )
    client.query.base64url_array(
        value=[
            bytes("test", "utf-8"),
            bytes("test", "utf-8"),
        ],
    )


def test_property(client: BytesClient):
    result = client.property.default(
        DefaultBytesProperty(
            value=bytes("test", "utf-8"),
        )
    )
    assert result.value == bytes("test", "utf-8")

    result = client.property.base64(
        Base64BytesProperty(
            value=bytes("test", "utf-8"),
        )
    )
    assert result.value == bytes("test", "utf-8")

    result = client.property.base64url(
        Base64urlBytesProperty(
            value=bytes("test", "utf-8"),
        )
    )
    assert result.value == bytes("test", "utf-8")

    result = client.property.base64url_array(
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


def test_header(client: BytesClient):
    client.header.default(
        value=bytes("test", "utf-8"),
    )
    client.header.base64(
        value=bytes("test", "utf-8"),
    )
    client.header.base64url(
        value=bytes("test", "utf-8"),
    )
    client.header.base64url_array(
        value=[
            bytes("test", "utf-8"),
            bytes("test", "utf-8"),
        ],
    )
