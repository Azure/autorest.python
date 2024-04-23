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
        ("extends_float", {'id': 43.125, 'prop': 43.125}, models.ExtendsFloatAdditionalProperties),
        ("is_float", {'id': 43.125, 'prop': 43.125}, models.IsFloatAdditionalProperties),
        ("extends_model", {'knownProp': {'state': 'ok'}, 'prop': {'state': 'ok'}}, models.ExtendsModelAdditionalProperties),
        ("is_model", {'knownProp': {'state': 'ok'}, 'prop': {'state': 'ok'}}, models.IsModelAdditionalProperties),
        ("extends_model_array", {'knownProp': [{'state': 'ok'}, {'state': 'ok'}], 'prop': [{'state': 'ok'}, {'state': 'ok'}]}, models.ExtendsModelArrayAdditionalProperties),
        ("is_model_array", {'knownProp': [{'state': 'ok'}, {'state': 'ok'}], 'prop': [{'state': 'ok'}, {'state': 'ok'}]}, models.IsModelArrayAdditionalProperties),
        ("spread_string", {'name': 'SpreadSpringRecord', 'prop': 'abc'}, dict),
        ("spread_float", {'id': 43.125, 'prop': 43.125}, dict),
        ("spread_model", {'knownProp': {'state': 'ok'}, 'prop': {'state': 'ok'}}, dict),
        ("spread_model_array", {'knownProp': [{'state': 'ok'}, {'state': 'ok'}], 'prop': [{'state': 'ok'}, {'state': 'ok'}]}, dict),
        ("spread_different_string", {'id': 43.125, 'prop': 'abc'}, dict),
        ("spread_different_float", {'name': 'abc', 'prop': 43.125}, dict),
        ("spread_different_model", {'knownProp': 'abc', 'prop': {'state': 'ok'}}, dict),
        ("spread_different_model_array", {'knownProp': 'abc', 'prop': [{'state': 'ok'}, {'state': 'ok'}]}, dict),
        ("extends_different_spread_string", {'id': 43.125, 'prop': 'abc', 'derivedProp': 'abc'}, models.DifferentSpreadStringDerived),
        ("extends_different_spread_float", {'name': 'abc', 'prop': 43.125, 'derivedProp': 43.125}, models.DifferentSpreadFloatDerived),
        ("extends_different_spread_model", {'knownProp': 'abc', 'prop': {'state': 'ok'}, 'derivedProp': {'state': 'ok'}}, models.DifferentSpreadModelDerived),
        ("extends_different_spread_model_array", {'knownProp': 'abc', 'prop': [{'state': 'ok'}, {'state': 'ok'}], 'derivedProp': [{'state': 'ok'}, {'state': 'ok'}]}, models.DifferentSpreadModelArrayDerived),
        ("multiple_spread", {'flag': True, 'prop1': 'abc', 'prop2': 43.125}, dict),
        ("spread_record_discriminated_union", {'name': 'abc', 'prop1': {'fooProp': 'abc', 'kind': 'kind0'}, 'prop2': {'end': '2021-01-02T00:00:00Z', 'kind': 'kind1', 'start': '2021-01-01T00:00:00Z'}}, dict),
        ("spread_record_non_discriminated_union", {'name': 'abc', 'prop1': {'kind': 'kind0', 'fooProp': 'abc'}, 'prop2': {'kind': 'kind1', 'start': '2021-01-01T00:00:00Z', 'end': '2021-01-02T00:00:00Z'}}, dict),
        ("spread_record_non_discriminated_union2", {'name': 'abc', 'prop1': {'kind': 'kind1', 'start': '2021-01-01T00:00:00Z'}, 'prop2': {'kind': 'kind1', 'start': '2021-01-01T00:00:00Z', 'end': '2021-01-02T00:00:00Z'}}, dict),
        ("spread_record_non_discriminated_union3", {'name': 'abc', 'prop1': [{'kind': 'kind1', 'start': '2021-01-01T00:00:00Z'}, {'kind': 'kind1', 'start': '2021-01-01T00:00:00Z'}], 'prop2': {'kind': 'kind1', 'start': '2021-01-01T00:00:00Z', 'end': '2021-01-02T00:00:00Z'}}, dict),
    ]
)
@pytest.mark.asyncio
async def test_json(client, og_name, val, model_name):
    body = model_name(val)
    og_group = getattr(client, og_name)
    assert await og_group.get() == body
    await og_group.put(body)
