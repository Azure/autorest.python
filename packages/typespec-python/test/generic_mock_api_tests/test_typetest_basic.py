# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import decimal

import pytest
from typetest.basic import BasicClient


@pytest.fixture
def client():
    with BasicClient() as client:
        yield client


@pytest.mark.parametrize(
    "og_name,val",
    [
        ("decimal_type", decimal.Decimal("0.33333")),
        ("decimal128_type", decimal.Decimal("0.33333")),
    ],
)
def test_basic(client: BasicClient, og_name: str, val: dict):
    og_group = getattr(client, og_name)
    assert og_group.response_body() == val
    og_group.request_body(val)
    og_group.request_parameter(value=val)
