# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any
import pytest
from models.property.types import ModelsPropertyTypes, models

@pytest.fixture
def client():
    with ModelsPropertyTypes() as client:
        yield client

@pytest.mark.parametrize(
"og_name,val", [
    ("boolean", True),
    ("string", "hello"),
    ("bytes", "aGVsbG8sIHdvcmxkIQ=="),
    ("int", 42),
    ("float", 42.42),
    ("datetime", "2022-08-26T18:38:00Z"),
    ("duration", "P123DT22H14M12.011S"),
    ("enum", "ValueOne"),
    ("extensible_enum", "UnknownValue"),
    ("model", {'property': 'hello'}),
    ("collections_string", ['hello', 'world']),
    ("collections_int", [1, 2]),
    ("collections_model", [{'property': 'hello'}, {'property': 'world'}]),
]
)
def test_json(client, og_name, val):
    body = {"property": val}
    og_group = getattr(client, og_name)
    assert og_group.get() == body
    og_group.put(body)

@pytest.mark.parametrize(
"og_name,model,val", [
    ("boolean", models.BooleanProperty, True),
    ("string", models.StringProperty, "hello"),
    ("bytes", models.BytesProperty, "aGVsbG8sIHdvcmxkIQ=="),
    ("int", models.IntProperty, 42),
    ("float", models.FloatProperty, 42.42),
    ("datetime", models.DatetimeProperty, "2022-08-26T18:38:00Z"),
    ("duration", models.DurationProperty, "P123DT22H14M12.011S"),
    ("enum", models.EnumProperty, "ValueOne"),
    ("extensible_enum", models.ExtensibleEnumProperty, "UnknownValue"),
    ("model", models.ModelProperty, {'property': 'hello'}),
    ("collections_string", models.CollectionsStringProperty, ['hello', 'world']),
    ("collections_int", models.CollectionsIntProperty, [1, 2]),
    ("collections_model", models.CollectionsModelProperty, [{'property': 'hello'}, {'property': 'world'}]),
]
)
def test_model(client, og_name, model, val):
    body = model(property=val)
    og_group = getattr(client, og_name)
    assert og_group.get() == body
    og_group.put(body)
