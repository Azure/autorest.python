# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from dictionary import Dictionary, models
from dictionary._model_base import AzureJSONEncoder
import json

@pytest.fixture
def client():
    with Dictionary() as client:
        yield client


@pytest.mark.parametrize(
    "og_name,val", [
        ("int32_value", {"k1": 1, "k2": 2}),
        ("int64_value",  {"k1": 2**53-1, "k2": -(2**53-1)}),
        ("boolean_value", {"k1": True, "k2": False}),
        ("string_value", {"k1": "hello", "k2": ""}),
        ("float32_value", {"k1": 42.42}),
        ("datetime_value",  {"k1": "2022-08-26T18:38:00Z"}),
        ("duration_value", {"k1": "P123DT22H14M12.011S"}),
        ("unknown_value", {"k1": 1, "k2": "hello", "k3": None}),
        ("model_value", {
            "k1": models.InnerModel(property="hello"),
            "k2": models.InnerModel(property="world"),
        }),
        ("recursive_model_value", {
            "k1": models.InnerModel(property="hello", children={}),
            "k2": models.InnerModel(property="world", children={"k2.1": models.InnerModel(property="inner world")}),
        }),
    ]
)
def test_json(client: Dictionary, og_name: str, val: dict):
    og_group = getattr(client, og_name)
    a = json.dumps(og_group.get(), cls=AzureJSONEncoder)
    b = json.dumps(val, cls=AzureJSONEncoder)
    assert json.dumps(og_group.get(), cls=AzureJSONEncoder) == json.dumps(val, cls=AzureJSONEncoder)
    og_group.put(val)



# @pytest.mark.parametrize(
#     "og_name,model,val", [
#         ("boolean", models.BooleanProperty, True),
#         ("string", models.StringProperty, "hello"),
#         ("bytes", models.BytesProperty, b'hello, world!'),
#         ("int", models.IntProperty, 42),
#         ("float", models.FloatProperty, 42.42),
#         ("enum", models.EnumProperty, models.InnerEnum.VALUE_ONE),
#         ("extensible_enum", models.ExtensibleEnumProperty, "UnknownValue"),
#         ("model", models.ModelProperty, models.InnerModel(property="hello")),
#         ("collections_string",
#          models.CollectionsStringProperty, ['hello', 'world']),
#         ("collections_int", models.CollectionsIntProperty, [1, 2]),
#         ("collections_model", models.CollectionsModelProperty,
#          [{'property': 'hello'}, {'property': 'world'}]),
#         ("dictionary_string", models.DictionaryStringProperty,
#          {'k1': 'hello', 'k2': 'world'}),
#     ]
# )
# def test_model(client, og_name, model, val):
#     body = model(property=val)
#     og_group = getattr(client, og_name)
#     assert og_group.get() == body
#     assert og_group.get().property == val
#     og_group.put(body)

