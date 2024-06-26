# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import RepeatabilityClientTestBase, RepeatabilityPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRepeatability(RepeatabilityClientTestBase):
    @RepeatabilityPreparer()
    @recorded_by_proxy
    def test_immediate_success(self, repeatability_endpoint):
        client = self.create_client(endpoint=repeatability_endpoint)
        response = client.immediate_success()

        # please add some check logic here by yourself
        # ...
