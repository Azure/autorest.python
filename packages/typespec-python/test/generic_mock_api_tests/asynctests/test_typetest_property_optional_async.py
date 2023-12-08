# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.property.optional import models
from typetest.property.optional.aio import OptionalClient

@pytest.fixture
async def client():
    async with OptionalClient() as client:
        yield client

@pytest.mark.parametrize(
"og_name,val", [
    ("string", "hello"),
    ("bytes", "aGVsbG8sIHdvcmxkIQ=="),
    ("datetime", "2022-08-26T18:38:00Z"),
    ("duration", "P123DT22H14M12.011S"),
    ("collections_byte", ["aGVsbG8sIHdvcmxkIQ==", "aGVsbG8sIHdvcmxkIQ=="]),
    ("collections_model", [{'property': 'hello'}, {'property': 'world'}]),
    ("string_literal", "hello"),
    ("int_literal", 1),
    ("float_literal", 1.2),
    ("boolean_literal", True),
    ("union_string_literal", "world"),
    ("union_int_literal", 2),
    ("union_float_literal", 2.3),
]
)
@pytest.mark.asyncio
async def test_json(client, og_name, val):
    body = {"property": val}
    og_group = getattr(client, og_name)
    assert await og_group.get_all() == body
    assert await og_group.get_default() == {}
    await og_group.put_all(body)
    await og_group.put_default({})

@pytest.mark.parametrize(
"og_name,model,val", [
    ("string", models.StringProperty, "hello"),
    ("bytes", models.BytesProperty, "aGVsbG8sIHdvcmxkIQ=="),
    ("datetime", models.DatetimeProperty, "2022-08-26T18:38:00Z"),
    ("duration", models.DurationProperty, "P123DT22H14M12.011S"),
    ("collections_byte", models.CollectionsByteProperty, ["aGVsbG8sIHdvcmxkIQ==", "aGVsbG8sIHdvcmxkIQ=="]),
    ("collections_model", models.CollectionsModelProperty, [models.StringProperty(property="hello"), models.StringProperty(property="world")]),
    ("string_literal", models.StringLiteralProperty, "hello"),
    ("int_literal", models.IntLiteralProperty, 1),
    ("float_literal", models.FloatLiteralProperty, 1.2),
    ("boolean_literal", models.BooleanLiteralProperty, True),
    ("union_string_literal", models.UnionStringLiteralProperty, "world"),
    ("union_int_literal", models.UnionIntLiteralProperty, 2),
    ("union_float_literal", models.UnionFloatLiteralProperty, 2.3),
]
)
@pytest.mark.asyncio
async def test_model(client, og_name, model, val):
    body = model(property=val)
    og_group = getattr(client, og_name)
    assert await og_group.get_all() == body
    assert await og_group.get_default() == {} == model()
    await og_group.put_all(body)
    await og_group.put_default(model())

@pytest.mark.asyncio
async def test_required_and_optional(client):
    all_body = {
        "optionalProperty": "hello",
        "requiredProperty": 42,
    }
    required_only_body = {
        "requiredProperty": 42,
    }
    assert await client.required_and_optional.get_all() == all_body
    assert await client.required_and_optional.get_required_only() == required_only_body
    await client.required_and_optional.put_all(all_body)
    await client.required_and_optional.put_required_only(required_only_body)
