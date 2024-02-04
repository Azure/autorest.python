# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from type.model.flatten import FlattenClient
from type.model.flatten.models import FlattenModel, ChildModel, NestedFlattenModel, ChildFlattenModel


@pytest.fixture
def client():
    with FlattenClient() as client:
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
def test_flatten(client: FlattenClient, op_name, reqs, reses):
    for req in reqs:
        for res in reses:
            assert getattr(client, op_name)(req) == res


# ============test for compatibility ============
def test_dpg_model_common():
    flatten_model = FlattenModel(name="hello", properties=ChildModel(age=0, description="test"))
    assert flatten_model.name == "hello"
    assert flatten_model.properties.age == 0
    assert flatten_model.properties.description == "test"


def test_dpg_model_none():
    flatten_model = FlattenModel()
    assert flatten_model.name is None
    assert flatten_model.properties is None
    assert flatten_model.age is None
    assert flatten_model.description is None


def test_dpg_model_compatility():
    flatten_model = FlattenModel(description="test", age=0)
    assert flatten_model.description == "test"
    assert flatten_model.age == 0
    assert flatten_model.properties.description == "test"
    assert flatten_model.properties.age == 0


def test_dpg_model_setattr():
    flatten_model = FlattenModel()

    flatten_model.age = 0
    assert flatten_model.properties.age == 0
    flatten_model.description = "test"
    assert flatten_model.properties.description == "test"

    flatten_model.properties.age = 1
    assert flatten_model.age == 1
    flatten_model.properties.description = "test2"
    assert flatten_model.description == "test2"


def test_dpg_model_exception():
    with pytest.raises(AttributeError):
        FlattenModel().no_prop
