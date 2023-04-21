# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from types.dictionary import DictionaryClient, models
import isodate
@pytest.fixture
def client():
    with DictionaryClient() as client:
        yield client

@pytest.mark.parametrize(
    "og_name,val", [
        ("int32_value", {"k1": 1, "k2": 2}),
        ("int64_value",  {"k1": 2**53-1, "k2": -(2**53-1)}),
        ("boolean_value", {"k1": True, "k2": False}),
        ("string_value", {"k1": "hello", "k2": ""}),
        ("float32_value", {"k1": 42.42}),
        ("datetime_value",  {"k1": isodate.parse_datetime("2022-08-26T18:38:00Z")}),
        ("duration_value", {"k1": isodate.parse_duration("P123DT22H14M12.011S")}),
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
def test_dictionary(client: DictionaryClient, og_name: str, val: dict):
    og_group = getattr(client, og_name)
    assert og_group.get() == val
    og_group.put(val)
