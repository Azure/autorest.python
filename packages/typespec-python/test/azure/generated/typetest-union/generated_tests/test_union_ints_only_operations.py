# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import UnionClientTestBase, UnionPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUnionIntsOnlyOperations(UnionClientTestBase):
    @UnionPreparer()
    @recorded_by_proxy
    def test_ints_only_get(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.ints_only.get()

        # please add some check logic here by yourself
        # ...

    @UnionPreparer()
    @recorded_by_proxy
    def test_ints_only_send(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.ints_only.send(
            body={"prop": 1},
            prop=1,
        )

        # please add some check logic here by yourself
        # ...
