# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.property.additionalproperties.aio import AdditionalPropertiesClient
from typetest.property.additionalproperties import models


@pytest.fixture
async def client():
    async with AdditionalPropertiesClient() as client:
        yield client


@pytest.mark.parametrize(
    "og_name,val, model_name", [
        ("extends_unknown", {'name': 'ExtendsUnknownAdditionalProperties', 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.ExtendsUnknownAdditionalProperties),
        ("extends_unknown_derived", {'name': 'ExtendsUnknownAdditionalProperties', 'index': 314, 'age': 2.71828, 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.ExtendsUnknownAdditionalPropertiesDerived),
        ("extends_unknown_discriminated", {'kind': 'derived', 'name': 'Derived', 'index': 314, 'age': 2.71828, 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.ExtendsUnknownAdditionalPropertiesDiscriminatedDerived),
        ("is_unknown", {'name': 'IsUnknownAdditionalProperties', 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.IsUnknownAdditionalProperties),
        ("is_unknown_derived", {'name': 'IsUnknownAdditionalProperties', 'index': 314, 'age': 2.71828, 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.IsUnknownAdditionalPropertiesDerived),
        ("is_unknown_discriminated", {'kind': 'derived', 'name': 'Derived', 'index': 314, 'age': 2.71828, 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.IsUnknownAdditionalPropertiesDiscriminatedDerived),
        ("extends_string", {'name': 'ExtendsStringAdditionalProperties', 'prop': 'abc'}, models.ExtendsStringAdditionalProperties),
        ("is_string", {'name': 'IsStringAdditionalProperties', 'prop': 'abc'}, models.IsStringAdditionalProperties),
        ("extends_float", {'id': 42.42, 'prop': 42.42}, models.ExtendsFloatAdditionalProperties),
        ("is_float", {'id': 42.42, 'prop': 42.42}, models.IsFloatAdditionalProperties),
        ("extends_model", {'prop': { 'state': 'ok' }}, models.ExtendsModelAdditionalProperties),
        ("is_model", {'prop': { 'state': 'ok' }}, models.IsModelAdditionalProperties),
        ("extends_model_array", {'prop': [{ 'state': 'ok' }, { 'state': 'ok' }]}, models.ExtendsModelArrayAdditionalProperties),
        ("is_model_array", {'prop': [{ 'state': 'ok' }, { 'state': 'ok' }]}, models.IsModelArrayAdditionalProperties),
    ]
)
@pytest.mark.asyncio
async def test_json(client, og_name, val, model_name):
    body = model_name(val)
    og_group = getattr(client, og_name)
    assert await og_group.get() == body
    await og_group.put(body)
