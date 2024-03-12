# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from type.model.flatten.aio import FlattenClient
from type.model.flatten.models import FlattenModel, ChildModel, NestedFlattenModel, ChildFlattenModel


@pytest.fixture
async def client():
    async with FlattenClient() as client:
        yield client


# ========== test for cadl-ranch ==========


@pytest.mark.parametrize(
    "op_name,reqs,reses",
    [
        (
            "put_flatten_model",
            [
                FlattenModel(name="foo", properties=ChildModel(age=10, description="bar")),
                FlattenModel(name="foo", age=10, description="bar"),
            ],
            [
                FlattenModel(name="test", properties=ChildModel(age=1, description="test")),
                FlattenModel(name="test", age=1, description="test"),
            ],
        ),
        # python doesn't support nested flatten model
        (
            "put_nested_flatten_model",
            [
                NestedFlattenModel(
                    name="foo",
                    properties=ChildFlattenModel(summary="bar", properties=ChildModel(age=10, description="test")),
                ),
            ],
            [
                NestedFlattenModel(
                    name="test",
                    properties=ChildFlattenModel(summary="test", properties=ChildModel(age=1, description="foo")),
                ),
            ],
        ),
    ],
)
@pytest.mark.asyncio
async def test_flatten(client: FlattenClient, op_name, reqs, reses):
    for req in reqs:
        for res in reses:
            assert await getattr(client, op_name)(req) == res
