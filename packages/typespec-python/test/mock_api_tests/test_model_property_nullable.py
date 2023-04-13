# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import json
from typing import Any
import pytest
from models.property.nullable import NullableClient, models
from azure.core.serialization import NULL
from models.property.nullable._model_base import (  # pylint: disable=protected-access
    AzureJSONEncoder,
)


@pytest.fixture
def client():
    with NullableClient() as client:
        yield client


@pytest.mark.parametrize(
    "og_name,model,val",
    [
        ("string", models.StringProperty, "hello"),
        ("bytes", models.BytesProperty, "aGVsbG8sIHdvcmxkIQ=="),
        ("datetime", models.DatetimeProperty, "2022-08-26T18:38:00Z"),
        ("duration", models.DurationProperty, "P123DT22H14M12.011S"),
        (
            "collections_byte",
            models.CollectionsByteProperty,
            ["aGVsbG8sIHdvcmxkIQ==", "aGVsbG8sIHdvcmxkIQ=="],
        ),
        (
            "collections_model",
            models.CollectionsModelProperty,
            [
                models.InnerModel(property="hello"),
                models.InnerModel(property="world"),
            ],
        ),
    ],
)
def test(client, og_name, model, val):
    og_group = getattr(client, og_name)
    non_null_model = model(required_property="foo", nullable_property=val)
    non_model = model(required_property="foo", nullable_property=NULL)
    assert '{"requiredProperty": "foo", "nullableProperty": null}' == json.dumps(
        non_model, cls=AzureJSONEncoder
    )
    assert og_group.get_non_null() == non_null_model
    assert og_group.get_null()["nullableProperty"] is None
    og_group.patch_non_null(body=non_null_model)
    og_group.patch_null(body=non_model)
