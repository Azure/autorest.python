# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Type
import pytest
from typetest.union import UnionClient
from typetest.union import models


@pytest.fixture
def client():
    with UnionClient() as client:
        yield client


@pytest.mark.parametrize(
    "og_name,value,res_model_type",
    [
        ("strings_only", "b", models.GetResponse),
        ("string_extensible", "custom", models.GetResponse1),
        ("string_extensible_named", "custom", models.GetResponse2),
        ("ints_only", 2, models.GetResponse3),
        ("floats_only", 2.2, models.GetResponse4),
        ("models_only", models.Cat(name="test"), models.GetResponse5),
        (
            "enums_only",
            models.EnumsOnlyCases(lr=models.EnumsOnlyCasesLr.RIGHT, ud=models.EnumsOnlyCasesLr.UP),
            models.GetResponse6,
        ),
        (
            "string_and_array",
            models.StringAndArrayCases(string="test", array=["test1", "test2"]),
            models.GetResponse7,
        ),
        (
            "mixed_literals",
            models.MixedLiteralsCases(
                string_literal="a",
                int_literal=2,
                float_literal=3.3,
                boolean_literal=True,
            ),
            models.GetResponse8,
        ),
        (
            "mixed_types",
            models.MixedTypesCases(
                model=models.Cat(name="test"), literal="a", int_property=2, boolean=True
            ),
            models.GetResponse9,
        ),
    ],
)
def test_union(client: UnionClient, og_name: str, value: Any, res_model_type: Type):
    og_group = getattr(client, og_name)
    assert og_group.get() == res_model_type(prop=value)
    og_group.send(prop=value)
    og_group.send({"prop": value})
