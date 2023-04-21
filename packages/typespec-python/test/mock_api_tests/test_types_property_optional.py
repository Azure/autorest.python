# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any
import pytest
from types.property.optional import OptionalClient, models

@pytest.fixture
def client():
    with OptionalClient() as client:
        yield client

@pytest.mark.parametrize(
"og_name,val", [
    ("string", "hello"),
    ("bytes", "aGVsbG8sIHdvcmxkIQ=="),
    ("datetime", "2022-08-26T18:38:00Z"),
    ("duration", "P123DT22H14M12.011S"),
    ("collections_byte", ["aGVsbG8sIHdvcmxkIQ==", "aGVsbG8sIHdvcmxkIQ=="]),
    ("collections_model", [{'property': 'hello'}, {'property': 'world'}]),
]
)
def test_json(client, og_name, val):
    body = {"property": val}
    og_group = getattr(client, og_name)
    assert og_group.get_all() == body
    assert og_group.get_default() == {}
    og_group.put_all(body)
    og_group.put_default({})

@pytest.mark.parametrize(
"og_name,model,val", [
    ("string", models.StringProperty, "hello"),
    ("bytes", models.BytesProperty, "aGVsbG8sIHdvcmxkIQ=="),
    ("datetime", models.DatetimeProperty, "2022-08-26T18:38:00Z"),
    ("duration", models.DurationProperty, "P123DT22H14M12.011S"),
    ("collections_byte", models.CollectionsByteProperty, ["aGVsbG8sIHdvcmxkIQ==", "aGVsbG8sIHdvcmxkIQ=="]),
    ("collections_model", models.CollectionsModelProperty, [models.StringProperty(property="hello"), models.StringProperty(property="world")]),
]
)
def test_model(client, og_name, model, val):
    body = model(property=val)
    og_group = getattr(client, og_name)
    assert og_group.get_all() == body
    assert og_group.get_default() == {} == model()
    og_group.put_all(body)
    og_group.put_default(model())

def test_required_and_optional(client):
    all_body = {
        "optionalProperty": "hello",
        "requiredProperty": 42,
    }
    required_only_body = {
        "requiredProperty": 42,
    }
    assert client.required_and_optional.get_all() == all_body
    assert client.required_and_optional.get_required_only() == required_only_body
    client.required_and_optional.put_all(all_body)
    client.required_and_optional.put_required_only(required_only_body)
