# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from unions.aio import UnionsClient
from unions.models import ModelWithNamedUnionProperty, ModelWithSimpleUnionProperty, Model1, Model2

@pytest.fixture
async def client():
    async with UnionsClient() as client:
        yield client

@pytest.mark.asyncio
async def test_send_int(client):
    await client.send_int(ModelWithSimpleUnionProperty(simple_union=1))

@pytest.mark.asyncio
async def test_send_int_array(client):
    await client.send_int_array(ModelWithSimpleUnionProperty(simple_union=[1, 2]))

@pytest.mark.asyncio
async def test_send_first_named_union_value(client):
    await client.send_first_named_union_value(ModelWithNamedUnionProperty(named_union=Model1(name="model1", prop1=1)))

@pytest.mark.asyncio
async def test_send_second_named_union_value(client):
    await client.send_second_named_union_value(ModelWithNamedUnionProperty(named_union=Model2(name="model2", prop2=2)))
