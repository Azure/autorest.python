# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import decimal

import pytest
import datetime
from typetest.property.valuetypes import ValueTypesClient, models


@pytest.fixture
def client():
    with ValueTypesClient() as client:
        yield client


@pytest.mark.parametrize(
    "og_name,val", [
        ("boolean", True),
        ("string", "hello"),
        ("bytes", "aGVsbG8sIHdvcmxkIQ=="),
        ("int_operations", 42),
        ("float", 42.42),
        ("decimal", decimal.Decimal("0.33333")),
        ("decimal128", decimal.Decimal("0.33333")),
        ("datetime", '2022-08-26T18:38:00Z'),
        ("duration", "P123DT22H14M12.011S"),
        ("enum", "ValueOne"),
        ("extensible_enum", "UnknownValue"),
        ("model", {'property': 'hello'}),
        ("collections_string", ['hello', 'world']),
        ("collections_int", [1, 2]),
        ("collections_model", [{'property': 'hello'}, {'property': 'world'}]),
        ("dictionary_string", {'k1': 'hello', 'k2': 'world'}),
        ("unknown_string", "hello"),
        ("unknown_int", 42),
        ("unknown_dict", {'k1': 'hello', 'k2': 42}),
        ("unknown_array", ['hello', 'world']),
        ("boolean_literal", True),
        ("int_literal", 42),
        ("string_literal", "hello"),
        ("float_literal", 42.42),
        ("union_string_literal", "world"),
        ("union_float_literal", 43.43),
        ("union_int_literal", 42),
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
        ("bytes", models.BytesProperty, b'hello, world!'),
        ("int_operations", models.IntProperty, 42),
        ("float", models.FloatProperty, 42.42),
        ("decimal", models.DecimalProperty, decimal.Decimal("0.33333")),
        ("decimal128", models.Decimal128Property, decimal.Decimal("0.33333")),
        ("enum", models.EnumProperty, models.InnerEnum.VALUE_ONE),
        ("extensible_enum", models.ExtensibleEnumProperty, "UnknownValue"),
        ("model", models.ModelProperty, models.InnerModel(property="hello")),
        ("collections_string",
         models.CollectionsStringProperty, ['hello', 'world']),
        ("collections_int", models.CollectionsIntProperty, [1, 2]),
        ("collections_model", models.CollectionsModelProperty,
         [{'property': 'hello'}, {'property': 'world'}]),
        ("dictionary_string", models.DictionaryStringProperty,
         {'k1': 'hello', 'k2': 'world'}),
        ("unknown_string", models.UnknownStringProperty, "hello"),
        ("unknown_int", models.UnknownIntProperty, 42),
        ("unknown_dict", models.UnknownDictProperty, {'k1': 'hello', 'k2': 42}),
        ("unknown_array", models.UnknownArrayProperty, ['hello', 'world']),
        ("boolean_literal", models.BooleanLiteralProperty, True),
        ("int_literal", models.IntLiteralProperty, 42),
        ("string_literal", models.StringLiteralProperty, "hello"),
        ("float_literal", models.FloatLiteralProperty, 42.42),
        ("union_string_literal", models.UnionStringLiteralProperty, "world"),
        ("union_float_literal", models.UnionFloatLiteralProperty, 43.43),
        ("union_int_literal", models.UnionIntLiteralProperty, 42),
    ]
)
def test_model(client, og_name, model, val):
    body = model(property=val)
    og_group = getattr(client, og_name)
    assert og_group.get() == body
    assert og_group.get().property == val
    og_group.put(body)


def test_datetime_model(client):
    received_body = client.datetime.get()
    assert received_body == {"property": '2022-08-26T18:38:00Z'}
    assert received_body.property.year == 2022
    assert received_body.property.month == 8
    assert received_body.property.day == 26
    assert received_body.property.hour == 18
    assert received_body.property.minute == 38
    client.datetime.put(models.DatetimeProperty(
        property=datetime.datetime(2022, 8, 26, hour=18, minute=38)))


def test_never_model(client: ValueTypesClient):
    assert client.never.get() == models.NeverProperty()
    client.never.put(models.NeverProperty())


def test_model_deserialization(client: ValueTypesClient):
    body = models.ModelProperty(property={"property": "hello"})
    assert body.property.property == body["property"]["property"]
    resp = client.model.get()
    assert resp.property.property == resp["property"]["property"]

    body = models.CollectionsModelProperty(property=[{'property': 'hello'}, {'property': 'world'}])
    assert body.property[0].property == body["property"][0]["property"]
    resp = client.collections_model.get()
    assert resp.property[1].property == resp["property"][1]["property"]


def test_enum_property():
    string_type = models.EnumProperty(property="ValueOne")
    assert isinstance(string_type.property, models.FixedInnerEnum)
    assert isinstance(string_type["property"], str)

    string_type = models.EnumProperty(property=models.FixedInnerEnum.VALUE_ONE)
    assert isinstance(string_type.property, models.FixedInnerEnum)
    assert isinstance(string_type["property"], models.FixedInnerEnum)
