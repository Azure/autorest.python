# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from parameters.spread.aio import SpreadClient
from parameters.spread.models import (
    BodyParameter,
    GeneratedName3,
    GeneratedName2,
    GeneratedName1,
)


@pytest.fixture
async def client():
    async with SpreadClient() as client:
        yield client


@pytest.mark.asyncio
async def test_model_body(client: SpreadClient):
    await client.model.spread_as_request_body(BodyParameter(name="foo"))


@pytest.mark.asyncio
async def test_alias_body(client: SpreadClient):
    await client.alias.spread_as_request_body(GeneratedName1(name="foo"))


@pytest.mark.asyncio
async def test_alias_parameter(client: SpreadClient):
    await client.alias.spread_as_request_parameter(
        "1", GeneratedName2(name="foo"), x_ms_test_header="bar"
    )


@pytest.mark.asyncio
async def test_alias_multiple_parameter(client: SpreadClient):
    await client.alias.spread_with_multiple_parameters(
        "1",
        GeneratedName3(
            prop1="foo1",
            prop2="foo2",
            prop3="foo3",
            prop4="foo4",
            prop5="foo5",
            prop6="foo6",
        ),
        x_ms_test_header="bar",
    )
