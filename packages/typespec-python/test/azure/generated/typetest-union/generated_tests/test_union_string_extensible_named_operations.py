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
class TestUnionStringExtensibleNamedOperations(UnionClientTestBase):
    @UnionPreparer()
    @recorded_by_proxy
    def test_get(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.string_extensible_named.get()

        # please add some check logic here by yourself

    @UnionPreparer()
    @recorded_by_proxy
    def test_send(self, union_endpoint):
        client = self.create_client(endpoint=union_endpoint)
        response = client.string_extensible_named.send(
            body={"prop": "str"},
            prop="str",
        )

        # please add some check logic here by yourself
