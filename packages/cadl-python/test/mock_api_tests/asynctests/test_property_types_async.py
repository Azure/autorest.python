# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import datetime
import pytest
from models.property.types import models
from models.property.types.aio import TypesClient

@pytest.fixture
async def client():
    async with TypesClient() as client:
        yield client

@pytest.mark.asyncio
@pytest.mark.parametrize(
"og_name,val", [
    ("boolean", True),
    ("string", "hello"),
    ("bytes", "aGVsbG8sIHdvcmxkIQ=="),
    ("int", 42),
    ("float", 42.42),
    ("datetime", "2022-08-26T18:38:00.000Z"),
    ("duration", "P123DT22H14M12.011S"),
    ("enum", "ValueOne"),
    ("extensible_enum", "UnknownValue"),
    ("model", {'property': 'hello'}),
    ("collections_string", ['hello', 'world']),
    ("collections_int", [1, 2]),
    ("collections_model", [{'property': 'hello'}, {'property': 'world'}]),
]
)
async def test(client, og_name, val):
    body = {"property": val}
    og_group = getattr(client, og_name)
    assert await og_group.get() == body
    await og_group.put(body)

@pytest.mark.parametrize(
"og_name,model,val", [
    ("boolean", models.BooleanProperty, True),
    ("string", models.StringProperty, "hello"),
    ("bytes", models.BytesProperty, b'hello, world!'),
    ("int", models.IntProperty, 42),
    ("float", models.FloatProperty, 42.42),
    ("enum", models.EnumProperty, models.InnerEnum.VALUE_ONE),
    ("extensible_enum", models.ExtensibleEnumProperty, "UnknownValue"),
    ("model", models.ModelProperty, models.InnerModel(property="hello")),
    ("collections_string", models.CollectionsStringProperty, ['hello', 'world']),
    ("collections_int", models.CollectionsIntProperty, [1, 2]),
    ("collections_model", models.CollectionsModelProperty, [{'property': 'hello'}, {'property': 'world'}]),
]
)
@pytest.mark.asyncio
async def test_model(client, og_name, model, val):
    body = model(property=val)
    og_group = getattr(client, og_name)
    assert await og_group.get() == body
    assert (await og_group.get()).property == val
    await og_group.put(body)

@pytest.mark.asyncio
async def test_datetime_model(client):
    received_body = await client.datetime.get()
    assert received_body == {"property": '2022-08-26T18:38:00.000Z'}
    assert received_body.property.year == 2022
    assert received_body.property.month == 8
    assert received_body.property.day == 26
    assert received_body.property.hour == 18
    assert received_body.property.minute == 38
    await client.datetime.put(models.DatetimeProperty(property=datetime.datetime(2022, 8, 26, hour=18, minute=38)))

# def test_duration_model(client):
#     received_body = client.duration.get()
#     assert received_body == {"property": "P123DT22H14M12.011S"}
#     assert received_body.property.days == 123
#     assert received_body.property.seconds == 80052
#     assert received_body.property.microseconds == 11000
#     client.duration.put(models.DurationProperty(property=datetime.timedelta(days=123, seconds=80052, microseconds=11000)))
