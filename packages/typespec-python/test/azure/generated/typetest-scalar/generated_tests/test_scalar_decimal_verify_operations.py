# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ScalarClientTestBase, ScalarPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestScalarDecimalVerifyOperations(ScalarClientTestBase):
    @ScalarPreparer()
    @recorded_by_proxy
    def test_decimal_verify_prepare_verify(self, scalar_endpoint):
        client = self.create_client(endpoint=scalar_endpoint)
        response = client.decimal_verify.prepare_verify()

        # please add some check logic here by yourself
        # ...

    @ScalarPreparer()
    @recorded_by_proxy
    def test_decimal_verify_verify(self, scalar_endpoint):
        client = self.create_client(endpoint=scalar_endpoint)
        response = client.decimal_verify.verify(
            body=0.0,
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
