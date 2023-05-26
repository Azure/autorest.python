# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.property.additionalproperties import models
from typetest.property.additionalproperties.aio import AdditionalPropertiesClient


@pytest.fixture
async def client():
    async with AdditionalPropertiesClient() as client:
        yield client


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "og_name,val, model_name", [
        ("extends_unknown", {'name': 'ExtendsUnknownAddtionalProperties', 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.ExtendsUnknownAddtionalProperties),
        ("is_unknown", {'name': 'IsUnknownAddtionalProperties', 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.IsUnknownAddtionalProperties),
        ("extends_string", {'name': 'ExtendsStringAddtionalProperties', 'prop': 'abc'}, models.ExtendsStringAddtionalProperties),
        ("is_string", {'name': 'IsStringAddtionalProperties', 'prop': 'abc'}, models.IsStringAddtionalProperties),
        ("extends_float", {'id': 42.42, 'prop': 42.42}, models.ExtendsFloatAddtionalProperties),
        ("is_float", {'id': 42.42, 'prop': 42.42}, models.IsFloatAddtionalProperties),
    ]
)
async def test_json(client, og_name, val, model_name):
    body = model_name(val)
    og_group = getattr(client, og_name)
    assert await og_group.get() == val
    await og_group.put(val)

