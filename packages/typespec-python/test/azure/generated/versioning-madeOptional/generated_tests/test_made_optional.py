# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import MadeOptionalClientTestBase, MadeOptionalPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestMadeOptional(MadeOptionalClientTestBase):
    @MadeOptionalPreparer()
    @recorded_by_proxy
    def test_test(self, madeoptional_endpoint):
        client = self.create_client(endpoint=madeoptional_endpoint)
        response = client.test(
            body={"prop": "str", "changedProp": "str"},
        )

        # please add some check logic here by yourself
        # ...
