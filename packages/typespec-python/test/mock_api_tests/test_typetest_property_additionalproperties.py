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
        ("extends_unknown", {'name': 'ExtendsUnknownAddtionalProperties', 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.ExtendsUnknownAddtionalProperties),
        ("is_unknown", {'name': 'IsUnknownAddtionalProperties', 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.IsUnknownAddtionalProperties),
        ("extends_string", {'name': 'ExtendsStringAddtionalProperties', 'prop': 'abc'}, models.ExtendsStringAddtionalProperties),
        ("is_string", {'name': 'IsStringAddtionalProperties', 'prop': 'abc'}, models.IsStringAddtionalProperties),
        ("extends_float", {'id': 42.42, 'prop': 42.42}, models.ExtendsFloatAddtionalProperties),
        ("is_float", {'id': 42.42, 'prop': 42.42}, models.IsFloatAddtionalProperties),
    ]
)
def test_json(client, og_name, val, model_name):
    body = model_name(val)
    og_group = getattr(client, og_name)
    assert og_group.get() == body
    og_group.put(val)

