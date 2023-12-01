# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import decimal
from functools import reduce

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
def test_scalar(client: ScalarClient, og_name: str, val):
    og_group = getattr(client, og_name)
    assert og_group.get() == val
    og_group.put(val)


@pytest.mark.parametrize(
    "og_name,val",
    [
        ("decimal_type", decimal.Decimal("0.33333")),
        ("decimal128_type", decimal.Decimal("0.33333")),
    ],
)
def test_type(client: ScalarClient, og_name: str, val):
    og_group = getattr(client, og_name)
    assert og_group.response_body() == val
    og_group.request_body(val)
    og_group.request_parameter(value=val)


@pytest.mark.parametrize(
    "og_name",
    [
        "decimal_verify",
        "decimal128_verify",
    ],
)
def test_verify(client: ScalarClient, og_name: str):
    og_group = getattr(client, og_name)
    prepare = og_group.prepare_verify()
    og_group.verify(reduce(lambda x, y: x + y, prepare))
