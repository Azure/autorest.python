# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import FlattenClientTestBase, FlattenPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestFlatten(FlattenClientTestBase):
    @FlattenPreparer()
    @recorded_by_proxy
    def test_put_flatten_model(self, flatten_endpoint):
        client = self.create_client(endpoint=flatten_endpoint)
        response = client.put_flatten_model(
            input={"name": "str", "properties": {"age": 0, "description": "str"}},
        )

        # please add some check logic here by yourself

    @FlattenPreparer()
    @recorded_by_proxy
    def test_put_nested_flatten_model(self, flatten_endpoint):
        client = self.create_client(endpoint=flatten_endpoint)
        response = client.put_nested_flatten_model(
            input={"name": "str", "properties": {"properties": {"age": 0, "description": "str"}, "summary": "str"}},
        )

        # please add some check logic here by yourself
