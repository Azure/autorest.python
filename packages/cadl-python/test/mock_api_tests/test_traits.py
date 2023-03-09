# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from datetime import datetime

import pytest
from _specs_.azure.traits import TraitsClient


@pytest.fixture
def client():
    with TraitsClient() as client:
        yield client


def test_get(client: TraitsClient):
    result, header = client.get(
        id=1,
        foo="123",
        if_match="valid",
        if_none_match="invalid",
        if_unmodified_since=datetime(
            year=2022, month=8, day=26, hour=14, minute=38, second=0
        ),
        if_modified_since=datetime(
            year=2021, month=8, day=26, hour=14, minute=38, second=0
        ),
        client_request_id="test-id",
        cls=lambda x, y, z: (y, z),
    )
    assert result.id == 1
    assert result.name == "Madge"
    assert header["ETag"] == "11bdc430-65e8-45ad-81d9-8ffa60d55b59"
    assert header["bar"] == "456"
    assert header["x-ms-client-request-id"] == "test-id"


def test_delete(client: TraitsClient):
    header = client.delete(id=1, client_request_id="test-id", cls=lambda x, y, z: z)
    assert header["x-ms-client-request-id"] == "test-id"
    assert header["Repeatability-Result"] == "Accepted"
