# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.scalar import ScalarClient


@pytest.fixture
def client():
    with ScalarClient() as client:
        yield client


@pytest.mark.parametrize(
    "og_name,val",
    [
        ("string", "test"),
        ("boolean", True),
        ("unknown", "test"),
    ],
)
def test_scalar(client: ScalarClient, og_name: str, val: dict):
    og_group = getattr(client, og_name)
    assert og_group.get() == val
    og_group.put(val)
