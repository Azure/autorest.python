# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any
import pytest
from types.property.nullable.aio import NullableClient
from types.property.nullable import models\


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
        # (
        #     "collections_model",
        #     models.CollectionsModelProperty,
        #     [
        #         models.InnerModel(property="hello"),
        #         models.InnerModel(property="world"),
        #     ],
        # ),
    ],
)
@pytest.mark.asyncio
async def test(client, og_name, model, val):
    og_group = getattr(client, og_name)
    non_null_model = model(required_property="foo", nullable_property=val)
    # non_model = model(required_property="foo", nullable_property=NULL)
    assert await og_group.get_non_null() == non_null_model
    assert (await og_group.get_null())["nullableProperty"] is None
    await og_group.patch_non_null(body=non_null_model)
    # await og_group.patch_null(body=non_model)
