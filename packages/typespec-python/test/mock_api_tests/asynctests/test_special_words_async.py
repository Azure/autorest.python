# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from specialwords import models
from specialwords.aio import SpecialWordsClient

@pytest.fixture
async def client():
    async with SpecialWordsClient() as client:
        yield client

@pytest.mark.asyncio
async def test_operation_for(client: SpecialWordsClient):
    await client.operation.for_method()

@pytest.mark.asyncio
async def test_parameter_if(client: SpecialWordsClient):
    await client.parameter.get_with_if(if_parameter="weekend")

@pytest.mark.asyncio
async def test_parameter_filter(client: SpecialWordsClient):
    await client.parameter.get_with_filter(filter="abc*.")

@pytest.mark.asyncio
async def test_model_get(client: SpecialWordsClient):
    assert await client.model.get() == models.DerivedModel(derived_name="my.name", for_property="value")

@pytest.mark.asyncio
async def test_model_put(client: SpecialWordsClient):
    await client.model.put(models.DerivedModel(derived_name="my.name", for_property="value"))