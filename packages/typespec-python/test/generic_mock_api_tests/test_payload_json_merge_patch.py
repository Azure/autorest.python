# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from payload.jsonmergepatch import JsonMergePatchClient
from payload.jsonmergepatch.models import InnerModel, Resource, ResourcePatch

try:
    from azure.core.serialization import NULL as CoreNull
except ImportError:
    from corehttp.serialization import NULL as CoreNull


@pytest.fixture
def client():
    with JsonMergePatchClient(endpoint="http://localhost:3000") as client:
        yield client


INNER_MADGE = InnerModel(name="InnerMadge", description="innerDesc")
CREATE_RESOURCE = Resource(
    name="Madge",
    description="desc",
    map={"key": INNER_MADGE},
    array=[INNER_MADGE],
    int_value=1,
    float_value=1.1,
    inner_model=INNER_MADGE,
    int_array=[1, 2, 3],
)
UPDATE_RESOURCE_REQ = ResourcePatch(
    description=CoreNull,
    map={"key": InnerModel(description=CoreNull), "key2": CoreNull},
    array=CoreNull,
    int_value=CoreNull,
    float_value=CoreNull,
    inner_model=CoreNull,
    int_array=CoreNull,
)
UPDATE_RESOURCE_RAW_REQ = {
    "description": None,
    "map": {"key": {"description": None}, "key2": None},
    "array": None,
    "intValue": None,
    "floatValue": None,
    "innerModel": None,
    "intArray": None,
}
UPDATE_RESOURCE_EXPECTED = Resource(
    name="Madge",
    map={"key": InnerModel(name="InnerMadge")},
)


@pytest.mark.parametrize(
    "op,req,expected",
    [
        ("create_resource", CREATE_RESOURCE, CREATE_RESOURCE),
        (
            "update_resource",
            UPDATE_RESOURCE_REQ,
            UPDATE_RESOURCE_EXPECTED,
        ),
        (
            "update_resource",
            UPDATE_RESOURCE_RAW_REQ,
            UPDATE_RESOURCE_EXPECTED,
        ),
        (
            "update_optional_resource",
            UPDATE_RESOURCE_REQ,
            UPDATE_RESOURCE_EXPECTED,
        ),
        (
            "update_optional_resource",
            UPDATE_RESOURCE_RAW_REQ,
            UPDATE_RESOURCE_EXPECTED,
        ),
    ],
)
def test_json_merge_patch(client: JsonMergePatchClient, op, req, expected):
    response = getattr(client, op)(req)
    assert response == expected
