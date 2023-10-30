# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import json
import pytest
from typetest.property.nullable.aio import NullableClient
from typetest.property.nullable import models
from typetest.property.nullable._model_base import (  # pylint: disable=protected-access
    AzureJSONEncoder,
)


@pytest.fixture
async def client():
    async with NullableClient() as client:
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
@pytest.mark.asyncio
async def test(client, og_name, model, val, core_library):
    og_group = getattr(client, og_name)
    non_null_model = model(required_property="foo", nullable_property=val)
    non_model = model(required_property="foo", nullable_property=core_library.serialization.NULL)
    assert '{"requiredProperty": "foo", "nullableProperty": null}' == json.dumps(
        non_model, cls=AzureJSONEncoder
    )
    assert await og_group.get_non_null() == non_null_model
    assert (await og_group.get_null())["nullableProperty"] is None
    await og_group.patch_non_null(body=non_null_model)
    await og_group.patch_null(body=non_model)
