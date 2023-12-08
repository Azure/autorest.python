# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.property.additionalproperties import AdditionalPropertiesClient, models


@pytest.fixture
def client():
    with AdditionalPropertiesClient() as client:
        yield client


@pytest.mark.parametrize(
    "og_name,val, model_name", [
        ("extends_unknown", {'name': 'ExtendsUnknownAdditionalProperties', 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.ExtendsUnknownAdditionalProperties),
        ("is_unknown", {'name': 'IsUnknownAdditionalProperties', 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.IsUnknownAdditionalProperties),
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
def test_json(client, og_name, val, model_name):
    body = model_name(val)
    og_group = getattr(client, og_name)
    assert og_group.get() == body
    og_group.put(val)
