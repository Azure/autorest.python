# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import MultipleClientTestBase, MultiplePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestMultiple(MultipleClientTestBase):
    @MultiplePreparer()
    @recorded_by_proxy
    def test_no_operation_params(self, multiple_endpoint):
        client = self.create_client(endpoint=multiple_endpoint)
        response = client.no_operation_params()

        # please add some check logic here by yourself
        # ...

    @MultiplePreparer()
    @recorded_by_proxy
    def test_with_operation_path_param(self, multiple_endpoint):
        client = self.create_client(endpoint=multiple_endpoint)
        response = client.with_operation_path_param(
            keyword="str",
        )

        # please add some check logic here by yourself
        # ...
